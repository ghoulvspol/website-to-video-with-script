#!/usr/bin/env python3
"""
Combine TTS audio with video using FFmpeg

Usage:
  python3 combine_audio_video.py --video video.mp4 --audio ./audio --output final.mp4

Requirements:
  - FFmpeg installed
  - Audio files named slide1.mp3, slide2.mp3, etc.
"""

import subprocess
import argparse
import json
from pathlib import Path


def get_video_duration(video_file: str) -> float:
    """Get video duration in seconds"""
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", video_file],
        capture_output=True, text=True
    )
    return float(result.stdout.strip())


def parse_timings(timings_str: str) -> list:
    """Parse timings string like '0:5,5:10,15:10,...' to list of dicts"""
    timings = []
    parts = timings_str.split(",")
    current_time = 0

    for i, part in enumerate(parts):
        if ":" in part:
            start, duration = part.split(":")
            timings.append({
                "id": i + 1,
                "start": float(start),
                "duration": float(duration)
            })
        else:
            timings.append({
                "id": i + 1,
                "start": current_time,
                "duration": float(part)
            })
            current_time += float(part)

    return timings


def combine_audio_video(video_file: str, audio_dir: str, output_file: str, timings: list):
    """Combine audio with video using FFmpeg"""

    audio_path = Path(audio_dir)

    # Build FFmpeg command
    inputs = ["-i", video_file]
    filter_parts = []

    audio_count = 0
    for timing in timings:
        audio_file = audio_path / f"slide{timing['id']}.mp3"
        if audio_file.exists():
            inputs.extend(["-i", str(audio_file)])
            delay_ms = timing["start"] * 1000
            filter_parts.append(f"[{audio_count + 1}:a]adelay={delay_ms}|{delay_ms}[a{audio_count}]")
            audio_count += 1

    if not filter_parts:
        print("No audio files found")
        return False

    # Create filter complex
    filter_complex = ";".join(filter_parts)
    mix_inputs = "".join(f"[a{i}]" for i in range(audio_count))
    filter_complex += f";{mix_inputs}amix=inputs={audio_count}:duration=longest[mixed]"

    cmd = [
        "ffmpeg", "-y",
        *inputs,
        "-filter_complex", filter_complex,
        "-map", "0:v",
        "-map", "[mixed]",
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        output_file
    ]

    print("Running FFmpeg...")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode == 0:
        print(f"✓ Saved to: {output_file}")
        return True
    else:
        print(f"✗ Error: {result.stderr}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Combine audio with video")
    parser.add_argument("--video", required=True, help="Input video file")
    parser.add_argument("--audio", required=True, help="Audio directory")
    parser.add_argument("--output", required=True, help="Output video file")
    parser.add_argument("--timings", help="Timings string like '0:5,5:10,15:10,...'")

    args = parser.parse_args()

    # Get video duration
    duration = get_video_duration(args.video)
    print(f"Video duration: {duration}s")

    # Parse timings or auto-generate
    if args.timings:
        timings = parse_timings(args.timings)
    else:
        # Auto-generate timings based on audio files
        audio_path = Path(args.audio)
        audio_files = sorted(audio_path.glob("slide*.mp3"))
        if not audio_files:
            print("No audio files found")
            return

        # Assume 10 seconds per slide (except first which is 5)
        timings = []
        current_time = 0
        for i, f in enumerate(audio_files):
            slide_duration = 5 if i == 0 else 10
            timings.append({
                "id": i + 1,
                "start": current_time,
                "duration": slide_duration
            })
            current_time += slide_duration

    print(f"Timings: {len(timings)} slides")

    # Combine
    combine_audio_video(args.video, args.audio, args.output, timings)


if __name__ == "__main__":
    main()

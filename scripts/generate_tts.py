#!/usr/bin/env python3
"""
Generate TTS audio for each slide using edge-tts

Usage:
  python3 generate_tts.py --script script.md --output ./audio --voice zh-CN-XiaoyiNeural

Requirements:
  pip3 install edge-tts
"""

import asyncio
import argparse
import re
from pathlib import Path

try:
    import edge_tts
except ImportError:
    print("Installing edge-tts...")
    import subprocess
    subprocess.run(["pip3", "install", "edge-tts"], check=True)
    import edge_tts


def parse_script(script_file: str) -> list:
    """Parse script.md to extract slide narrations"""
    with open(script_file, 'r', encoding='utf-8') as f:
        content = f.read()

    slides = []
    pattern = r'## P(\d+) - .+?\n\*\*时间\*\*: .+?\n\*\*文案\*\*: (.+?)(?=\n\n|\n##|\Z)'
    matches = re.findall(pattern, content, re.DOTALL)

    for match in matches:
        slide_id = int(match[0])
        text = match[1].strip()
        slides.append({"id": slide_id, "text": text})

    return slides


async def generate_tts(text: str, output_file: str, voice: str, speed: float):
    """Generate TTS audio for a single text"""
    rate = f"+{int((speed - 1) * 100)}%" if speed >= 1 else f"{int((speed - 1) * 100)}%"
    communicate = edge_tts.Communicate(text, voice, rate=rate)
    await communicate.save(output_file)


async def main():
    parser = argparse.ArgumentParser(description="Generate TTS audio from script")
    parser.add_argument("--script", required=True, help="Path to script.md")
    parser.add_argument("--output", default="./audio", help="Output directory")
    parser.add_argument("--voice", default="zh-CN-XiaoyiNeural", help="TTS voice ID")
    parser.add_argument("--speed", type=float, default=1.0, help="Speech speed (0.5-2.0)")

    args = parser.parse_args()

    # Parse script
    slides = parse_script(args.script)
    if not slides:
        print("Error: No slides found in script")
        return

    # Create output directory
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Generate audio for each slide
    print(f"Generating TTS audio with voice: {args.voice}")
    print(f"Speed: {args.speed}x")
    print(f"Output: {output_dir}")
    print()

    for slide in slides:
        slide_id = slide["id"]
        text = slide["text"]
        output_file = output_dir / f"slide{slide_id}.mp3"

        print(f"[{slide_id}/{len(slides)}] Generating...")

        try:
            await generate_tts(text, str(output_file), args.voice, args.speed)
            print(f"  ✓ Saved: {output_file.name}")
        except Exception as e:
            print(f"  ✗ Error: {e}")
            return

    print(f"\n✓ All {len(slides)} audio files generated in {output_dir}")


if __name__ == "__main__":
    asyncio.run(main())

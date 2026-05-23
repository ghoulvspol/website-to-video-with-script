# Website to Video with Script

> 🎬 将网站转换为带讲解音频 + 字幕的专业视频。每张幻灯片自动生成旁白文案，支持 TTS 语音合成，视频中同步显示字幕和播放讲解音频。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code Skill](https://img.shields.io/badge/Claude%20Code-Skill-blue.svg)](https://claude.ai/code)

---

## ✨ 功能特性

| 功能 | 说明 |
|------|------|
| 🌐 自动抓取 | 智能提取网站内容和结构 |
| 📝 文案生成 | 每张幻灯片自动生成旁白文案 |
| 🎤 TTS 讲解 | 使用 edge-tts 生成高质量中文/英文语音 |
| 🎬 字幕显示 | 视频中同步显示字幕 |
| 🎨 多种风格 | 4 种文案风格可选 |
| 🔊 多种语音 | 14 种中文语音 + 多种英文语音 |
| ⚡ 参数灵活 | 自定义语速、字幕位置、字号等 |

---

## 🚀 快速开始

### 基础用法

```bash
# 带讲解音频 + 字幕的完整视频
/website-to-video-with-script https://example.com

# 禁用讲解音频，只显示字幕
/website-to-video-with-script https://example.com --no-audio

# 切换为男声
/website-to-video-with-script https://example.com --tts-voice zh-CN-YunjianNeural

# 只生成文案，不渲染视频
/website-to-video-with-script https://example.com --script-only
```

### 完整示例

```bash
# 知识图谱网站 → 带讲解的演示视频
/website-to-video-with-script https://ghoulvspol.github.io/bank-knowledge-graph/

# AI 投资网站 → 口语化风格 + 年轻男声
/website-to-video-with-script https://ghoulvspol.github.io/ai-stocks-site/ \
  --script-style casual \
  --tts-voice zh-CN-YunxiNeural

# 微信文章 → 故事化风格 + 1.2倍速
/website-to-video-with-script https://mp.weixin.qq.com/s/xxx \
  --script-style storytelling \
  --tts-speed 1.2
```

---

## 📖 与 website-to-ppt-video 的区别

| 特性 | website-to-ppt-video | website-to-video-with-script |
|------|---------------------|------------------------------|
| HTML PPT | ✅ | ✅ |
| MP4 视频 | ✅ | ✅ |
| 文案生成 | ❌ | ✅ 自动为每页生成旁白 |
| 字幕显示 | ❌ | ✅ 视频中显示字幕 |
| 讲解音频 | ❌ | ✅ TTS 语音合成 |
| 文案文件 | ❌ | ✅ 输出 script.md |
| 音频文件 | ❌ | ✅ 输出 audio/*.mp3 |

---

## 🎤 TTS 语音选项

### 🇨🇳 中文语音（推荐）

| Voice ID | 性别 | 特点 | 适用场景 |
|----------|------|------|----------|
| `zh-CN-XiaoyiNeural` | 👩 女声 | 温柔亲切，柔和自然 | **知识讲解、教程（默认）** |
| `zh-CN-XiaoxiaoNeural` | 👩 女声 | 标准清晰，自然流畅 | 通用场景、正式内容 |
| `zh-CN-YunjianNeural` | 👨 男声 | 稳重大气，专业感强 | 商务汇报、正式演讲 |
| `zh-CN-YunxiNeural` | 👨 男声 | 年轻活力，阳光自然 | 轻松内容、社交媒体 |
| `zh-CN-YunxiaNeural` | 👨 男声 | 少年清新，自然亲切 | 年轻化内容、趣味视频 |
| `zh-CN-YunyangNeural` | 👨 男声 | 新闻播报风格，专业 | 新闻、正式报告 |
| `zh-CN-liaoning-XiaobeiNeural` | 👩 女声 | 东北口音，有趣亲切 | 趣味内容、地方特色 |
| `zh-CN-shaanxi-XiaoniNeural` | 👩 女声 | 陕西口音，地方特色 | 地方文化内容 |

### 🇭🇰 粤语语音

| Voice ID | 性别 | 特点 |
|----------|------|------|
| `zh-HK-HiuGaaiNeural` | 👩 女声 | 粤语女声，香港口音 |
| `zh-HK-HiuMaanNeural` | 👩 女声 | 粤语女声，香港口音 |
| `zh-HK-WanLungNeural` | 👨 男声 | 粤语男声，香港口音 |

### 🇹🇼 台湾语音

| Voice ID | 性别 | 特点 |
|----------|------|------|
| `zh-TW-HsiaoChenNeural` | 👩 女声 | 温柔甜美，台湾腔 |
| `zh-TW-YunJheNeural` | 👨 男声 | 温和有礼，台湾腔 |
| `zh-TW-HsiaoYuNeural` | 👩 女声 | 活泼可爱，台湾腔 |

### 🇺🇸 英文语音

| Voice ID | 性别 | 特点 | 口音 |
|----------|------|------|------|
| `en-US-JennyNeural` | 👩 女声 | 专业清晰 | 美式 |
| `en-US-GuyNeural` | 👨 男声 | 稳重可靠 | 美式 |
| `en-US-AriaNeural` | 👩 女声 | 自然流畅 | 美式 |
| `en-US-DavisNeural` | 👨 男声 | 友好亲切 | 美式 |
| `en-GB-SoniaNeural` | 👩 女声 | 优雅端庄 | 英式 |
| `en-GB-RyanNeural` | 👨 男声 | 绅士风格 | 英式 |
| `en-AU-NatashaNeural` | 👩 女声 | 轻松活泼 | 澳式 |
| `en-AU-WilliamNeural` | 👨 男声 | 随和自然 | 澳式 |

### 推荐搭配

| 场景 | 推荐语音 | 原因 |
|------|----------|------|
| 知识讲解 | `zh-CN-XiaoyiNeural` | 温柔亲切，适合长时间聆听 |
| 商务汇报 | `zh-CN-YunjianNeural` | 稳重大气，专业感强 |
| 社交媒体 | `zh-CN-YunxiNeural` | 年轻活力，吸引注意力 |
| 正式报告 | `zh-CN-YunyangNeural` | 新闻播报风格，权威感 |
| 英文内容 | `en-US-JennyNeural` | 专业清晰，美式发音 |
| 趣味内容 | `zh-CN-liaoning-XiaobeiNeural` | 东北口音，有趣亲切 |

---

## 🎯 文案风格

| 风格 | 说明 | 适用场景 | 示例 |
|------|------|----------|------|
| `professional` | 专业正式 | 商务汇报、产品介绍 | "欢迎观看本期内容，今天我们将深入探讨..." |
| `casual` | 轻松口语 | 社交媒体、知识分享 | "嘿！今天来聊聊一个超火的话题..." |
| `storytelling` | 故事化 | 品牌宣传、案例分享 | "在 AI 时代，有一个故事正在上演..." |
| `educational` | 教育科普 | 教程、培训材料 | "本节课程将讲解..." |

---

## 📍 字幕位置

| 位置 | 说明 |
|------|------|
| `bottom` | 底部居中（默认） |
| `top` | 顶部居中 |
| `overlay` | 半透明覆盖层 |

---

## 📁 输出结构

```
{output-dir}/
├── source.md              # 网站内容
├── script.md              # 文案脚本（可独立使用）
├── presentation.html      # HTML PPT（可独立使用）
├── generate_tts.py        # TTS 生成脚本
├── combine_audio_video.py # 音视频合并脚本
├── audio/
│   ├── slide1.mp3         # 第1页讲解音频
│   ├── slide2.mp3         # 第2页讲解音频
│   └── ...                # 每页一个音频文件
├── video-project/
│   ├── index.html         # 视频合成文件（含字幕）
│   └── output.mp4         # 原始视频（无音频）
└── output-final.mp4       # 最终视频（带讲解音频 + 字幕）✅
```

---

## 📝 文案脚本格式

```markdown
# 视频文案脚本

## P1 - 封面
**时间**: 0-5秒
**文案**: 欢迎来到保险业务体系知识库，带你构建保险行业的全景认知框架。

## P2 - 概览
**时间**: 5-15秒
**文案**: 本知识库涵盖 20 个核心概念、15 个保险产品、10 家公司档案...

## P3 - 核心概念
**时间**: 15-25秒
**文案**: 首先来看核心概念。精算学是保险的数学基础，偿付能力决定公司稳健性...
```

---

## 🔧 参数选项

### 基础参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--output` | 输出目录名 | 基于网站标题 |
| `--slides` | 幻灯片数量 | 8-12 |
| `--duration` | 每张幻灯片时长 | 10秒 |
| `--cover-duration` | 封面时长 | 5秒 |

### 文案参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--script-style` | 文案风格 | professional |
| `--script-only` | 只生成文案 | false |

### 字幕参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--subtitle-position` | 字幕位置 | bottom |
| `--subtitle-font-size` | 字幕字号 | 24px |
| `--no-subtitle` | 不显示字幕 | false |

### TTS 参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--tts-voice` | TTS 语音 ID | zh-CN-XiaoyiNeural |
| `--tts-speed` | 语速（0.5-2.0） | 1.0 |
| `--no-audio` | 禁用讲解音频 | false |
| `--audio-only` | 只生成音频 | false |

### 视觉参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--style` | 视觉风格 | default |
| `--theme` | 配色主题 | blue |

---

## 📚 工作流程

```
网站 URL
    ↓
[Step 1] 抓取网站内容（baoyu-fetch / WebFetch）
    ↓
[Step 2] 生成 HTML PPT + 文案脚本
    ↓
[Step 3] 生成 TTS 讲解音频（edge-tts）
    ↓
[Step 4] 合成带字幕 + 讲解音频的视频
    ↓
MP4 文件 + script.md + audio/
```

---

## 📝 示例

### 示例 1: 知识图谱网站

```bash
/website-to-video-with-script https://ghoulvspol.github.io/bank-knowledge-graph/
```

输出：
- 12 张幻灯片 + 12 段文案 + 12 个音频文件
- 带讲解音频和字幕的视频

### 示例 2: AI 投资网站

```bash
/website-to-video-with-script https://ghoulvspol.github.io/ai-stocks-site/ \
  --script-style casual \
  --tts-voice zh-CN-YunxiNeural
```

输出：
- 9 张幻灯片 + 9 段口语化文案
- 年轻男声讲解的视频

### 示例 3: 微信文章

```bash
/website-to-video-with-script https://mp.weixin.qq.com/s/xxx \
  --script-style storytelling \
  --tts-speed 1.2
```

输出：
- 故事化文案 + 1.2倍速讲解
- 叙事风格视频

### 示例 4: 保险知识图谱

```bash
/website-to-video-with-script https://ghoulvspol.github.io/insurance-knowledge-graph/ \
  --tts-voice zh-CN-XiaoyiNeural \
  --subtitle-position bottom
```

输出：
- 9 张幻灯片 + 9 段专业文案
- 温柔女声讲解 + 底部字幕

---

## 🛠️ 技术栈

| 技术 | 版本 | 用途 |
|------|------|------|
| Reveal.js | 5.1.0 | HTML 幻灯片框架 |
| GSAP | 3.14.2 | 动画库 |
| Hyperframes | latest | 视频渲染引擎 |
| edge-tts | latest | TTS 语音合成 |
| FFmpeg | latest | 音视频处理 |
| Google Fonts | - | 字体服务 |

---

## 🔧 依赖安装

### 必需依赖

```bash
# Node.js (>= 22)
brew install node

# FFmpeg
brew install ffmpeg

# Hyperframes
npm install -g hyperframes

# bun (用于网站抓取)
curl -fsSL https://bun.sh/install | bash
```

### TTS 依赖

```bash
# edge-tts (Python)
pip3 install edge-tts
```

### 检查依赖

```bash
# 检查所有依赖
which bun && which ffmpeg && npx hyperframes --help && python3 -c "import edge_tts"
```

---

## ❓ 常见问题

### Q: 文案太长怎么办？

A: 使用 `--script-style casual` 生成更简洁的文案，或手动编辑 `script.md`。

### Q: 字幕遮挡内容？

A: 使用 `--subtitle-position top` 将字幕移到顶部，或调整 `--subtitle-font-size`。

### Q: 如何自定义文案？

A: 编辑 `script.md` 文件后重新渲染视频。

### Q: 支持 TTS 语音吗？

A: 支持！默认使用 `edge-tts` 生成中文女声讲解音频。可通过 `--tts-voice` 参数切换语音。

### Q: 如何切换 TTS 语音？

A: 使用 `--tts-voice` 参数指定语音 ID，例如：
```bash
/website-to-video-with-script https://example.com --tts-voice zh-CN-YunxiNeural
```

### Q: 讲解音频和字幕不同步？

A: 音频通过 FFmpeg `adelay` 滤镜精确同步到每张幻灯片的时间点。如果仍有偏差，可手动调整 `combine_audio_video.py` 中的时间戳。

### Q: 视频渲染失败？

A: 运行 `npx hyperframes doctor` 检查依赖，或清理缓存 `rm -rf ~/.cache/puppeteer`。

### Q: 字体显示异常？

A: 在 HTML 中添加本地字体声明，或使用 Google Fonts（默认）。

---

## 📊 性能参考

| 内容类型 | 幻灯片数 | 生成时间 | 文件大小 |
|----------|----------|----------|----------|
| 知识图谱网站 | 12 页 | ~2 分钟 | ~5 MB |
| AI 投资网站 | 9 页 | ~1.5 分钟 | ~4 MB |
| 微信文章 | 8 页 | ~1.5 分钟 | ~4 MB |

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

---

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE)

---

## 🙏 致谢

- [website-to-ppt-video](https://github.com/ghoulvspol/website-to-ppt-video) - 基础版 skill
- [Reveal.js](https://revealjs.com/) - HTML 幻灯片框架
- [Hyperframes](https://github.com/heygen-com/hyperframes) - 视频渲染引擎
- [edge-tts](https://github.com/rany2/edge-tts) - TTS 语音合成
- [GSAP](https://greensock.com/gsap/) - 动画库

---

## 📧 联系方式

- GitHub: [@ghoulvspol](https://github.com/ghoulvspol)
- 项目链接: [https://github.com/ghoulvspol/website-to-video-with-script](https://github.com/ghoulvspol/website-to-video-with-script)

---

⭐ 如果觉得有用，请给个 Star！

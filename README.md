# Website to Video with Script

> 🎬 将网站转换为带文案旁白的专业视频，每页自动生成字幕

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code Skill](https://img.shields.io/badge/Claude%20Code-Skill-blue.svg)](https://claude.ai/code)

## ✨ 功能特性

- 🌐 **自动抓取** - 智能提取网站内容
- 📝 **文案生成** - 每张幻灯片自动生成旁白文案
- 🎬 **字幕显示** - 视频中同步显示字幕
- 🎨 **多种风格** - 4 种文案风格可选
- ⚡ **参数灵活** - 自定义字幕位置、字号等

## 🚀 快速开始

```bash
# 在 Claude Code 中使用
/website-to-video-with-script https://example.com

# 指定文案风格
/website-to-video-with-script https://example.com --script-style casual

# 只生成文案
/website-to-video-with-script https://example.com --script-only
```

## 📖 与 website-to-ppt-video 的区别

| 特性 | website-to-ppt-video | website-to-video-with-script |
|------|---------------------|------------------------------|
| HTML PPT | ✅ | ✅ |
| MP4 视频 | ✅ | ✅ |
| 文案生成 | ❌ | ✅ 自动为每页生成旁白 |
| 字幕显示 | ❌ | ✅ 视频中显示字幕 |
| 文案文件 | ❌ | ✅ 输出 script.md |

## 🎯 文案风格

| 风格 | 说明 | 适用场景 | 示例 |
|------|------|----------|------|
| `professional` | 专业正式 | 商务汇报、产品介绍 | "欢迎观看本期内容，今天我们将深入探讨..." |
| `casual` | 轻松口语 | 社交媒体、知识分享 | "嘿！今天来聊聊一个超火的话题..." |
| `storytelling` | 故事化 | 品牌宣传、案例分享 | "在 AI 时代，有一个故事正在上演..." |
| `educational` | 教育科普 | 教程、培训材料 | "本节课程将讲解..." |

## 📍 字幕位置

| 位置 | 说明 |
|------|------|
| `bottom` | 底部居中（默认） |
| `top` | 顶部居中 |
| `overlay` | 半透明覆盖层 |

## 📁 输出结构

```
{output-dir}/
├── source.md              # 网站内容
├── script.md              # 文案脚本（可独立使用）
├── presentation.html      # HTML PPT
└── video-project/
    ├── index.html         # 视频合成文件（含字幕）
    └── output.mp4         # 最终视频
```

## 📝 文案脚本格式

```markdown
# 视频文案脚本

## P1 - 封面
**时间**: 0-5秒
**文案**: GitHub 最流行的十大 Skill，带你了解 Claude Code 生态全景。

## P2 - 概览
**时间**: 5-15秒
**文案**: 目前 SkillsMP 已有超过 70 万技能，最高安装量达 41.8 万。

## P3 - Top 1-3
**时间**: 15-25秒
**文案**: 排名前三的是 Anthropic 官方技能集合、Vercel 的技能搜索引擎...
```

## 🔧 参数选项

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--output` | 输出目录名 | 基于网站标题 |
| `--slides` | 幻灯片数量 | 8-12 |
| `--duration` | 每张幻灯片时长 | 10秒 |
| `--cover-duration` | 封面时长 | 5秒 |
| `--script-style` | 文案风格 | professional |
| `--subtitle-position` | 字幕位置 | bottom |
| `--subtitle-font-size` | 字幕字号 | 24px |
| `--script-only` | 只生成文案 | false |
| `--no-subtitle` | 不显示字幕 | false |

## 📚 工作流程

```
网站 URL
    ↓
[Step 1] 抓取网站内容
    ↓
[Step 2] 生成 HTML PPT + 文案脚本
    ↓
[Step 3] 合成带字幕的视频
    ↓
MP4 文件 + script.md
```

## 📝 示例

### 示例 1: 知识图谱网站

```bash
/website-to-video-with-script https://ghoulvspol.github.io/bank-knowledge-graph/
```

输出：12 张幻灯片 + 12 段文案 + 带字幕视频

### 示例 2: AI 投资网站

```bash
/website-to-video-with-script https://ghoulvspol.github.io/ai-stocks-site/ --script-style casual
```

输出：9 张幻灯片 + 9 段口语化文案 + 轻松风格视频

### 示例 3: 微信文章

```bash
/website-to-video-with-script https://mp.weixin.qq.com/s/xxx --script-style storytelling
```

输出：故事化文案 + 叙事风格视频

## 🛠️ 技术栈

| 技术 | 版本 | 用途 |
|------|------|------|
| Reveal.js | 5.1.0 | HTML 幻灯片框架 |
| GSAP | 3.14.2 | 动画库 |
| Hyperframes | latest | 视频渲染引擎 |
| Google Fonts | - | 字体服务 |

## ❓ 常见问题

### Q: 文案太长怎么办？

A: 使用 `--script-style casual` 生成更简洁的文案，或手动编辑 `script.md`。

### Q: 字幕遮挡内容？

A: 使用 `--subtitle-position top` 将字幕移到顶部，或调整 `--subtitle-font-size`。

### Q: 如何自定义文案？

A: 编辑 `script.md` 文件后重新渲染视频。

### Q: 支持 TTS 语音吗？

A: 当前版本仅支持字幕显示，TTS 功能开发中。

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE)

## 🙏 致谢

- [website-to-ppt-video](https://github.com/ghoulvspol/website-to-ppt-video) - 基础版 skill
- [Reveal.js](https://revealjs.com/) - HTML 幻灯片框架
- [Hyperframes](https://github.com/heygen-com/hyperframes) - 视频渲染引擎

## 📧 联系方式

- GitHub: [@ghoulvspol](https://github.com/ghoulvspol)

---

⭐ 如果觉得有用，请给个 Star！

# Scientific Animation｜科研算法动画制作

[English](README.md) · **简体中文** · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md)

本仓库**同时维护两个独立的 ChatGPT Skill**，用于将论文、科研报告、算法、源码和工程材料制作成科学原理动画。两种模式共用科学准确性与视觉规范，但沟通和工作流程严格分开。

## 两种模式有什么区别？

| | **完整托管（Autopilot）** | **交互确认（Dialogue）** |
|---|---|---|
| 对应目录 | [scientific-animation-autopilot](skills/scientific-animation-autopilot/SKILL.md) | [scientific-animation-dialogue](skills/scientific-animation-dialogue/SKILL.md) |
| 使用场景 | 直接提供资料，希望尽快拿到成片 | 科研边界复杂，希望在关键环节确认 |
| 制作期间是否询问 | **不提出确认问题**；自主决定并自我检查 | **允许少量关键询问**；不重复已明确的条件 |
| 样片及反馈 | 不等待样片批准 | 可展示真实可播放样片并根据反馈修改 |
| 核心目标 | 无需打断的端到端制作 | 尽量少的沟通与 Token，减少返工 |
| 成果形式 | 可播放 MP4；无法渲染时明确说明并交付可播放 HTML/GIF | 同左 |

**注意：两个 Skill 是不同目录的独立技能，不是一个 Skill 的模式开关。** 可以只安装其中一个，也可以分别安装两个；不要将整仓库一次性作为单个 Skill 上传。

## 安装

下载或克隆仓库后运行：

```bash
python tools/build_skill_zips.py
```

生成两个独立压缩包：`dist/autopilot/skill.zip` 和 `dist/dialogue/skill.zip`。在 ChatGPT 的 Skill 导入界面中，分别上传你需要的 ZIP（具体入口取决于客户端及工作区权限）。

## 调用示例

完整托管：

> 使用「科研动画制作 · 完整托管」，阅读我的论文与源码，自行完成设计、渲染、检查；不要中途询问，直接交付实际可播放的动画。

交互确认：

> 使用「科研动画制作 · 交互确认」，根据材料制作算法动画；只询问会影响科学准确性或导致重大返工的问题，可以先展示关键镜头的可播放样片。

## 共同规范

- 科学准确性优先，不能编造实验数据或把未实现功能说成已实现。
- 极简二维/适量 2.5D；白黑灰为主，少量有明确含义的强调色，避免蓝紫霓虹 AI 风。
- 公式与机器人轨迹、矩阵、事件时间轴、实体动作建立直接对应。
- **保留可读的解说字幕**，不要误把“删除冗余小字”理解为“无字幕”。优先使用有授权的微软雅黑 Bold，部分标签使用华文中宋。
- 成片必须实际可播放并接受检验；工具无能力时说明限制，不得把脚本或分镜冒充成片。
- 飞梯机器人、底部缓存、AMR 可从架下穿行等规则仅属于对应 RMFS 案例，不能强加给其他课题。

## 目录

```text
skills/
  scientific-animation-autopilot/
    SKILL.md
    agents/openai.yaml
    references/
    scripts/
    assets/starter/film.html
  scientific-animation-dialogue/
    SKILL.md
    agents/openai.yaml
    references/
    scripts/
    assets/starter/film.html
tools/build_skill_zips.py
```

每个文件夹可以独立安装与维护。项目不捆绑专有字体、账户凭据或原始科研机密。尚未选择仓库代码许可证，请勿默认所有内容已按 MIT 授权。

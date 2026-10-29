# Scientific Animation｜科研演算法動畫製作

[English](README.md) · [简体中文](README.zh-CN.md) · **繁體中文** · [日本語](README.ja.md)

本倉庫在**同一個 GitHub 專案內管理兩個可獨立安裝的 ChatGPT Skills**：完整託管與互動確認。它們共用動畫的科學準確性及視覺標準，但工作流程互不混用。

| | **完整託管 Autopilot** | **互動確認 Dialogue** |
|---|---|---|
| Skill | [autopilot](skills/scientific-animation-autopilot/SKILL.md) | [dialogue](skills/scientific-animation-dialogue/SKILL.md) |
| 製作中提問 | **不提問，AI 自主決策** | **只針對重要邊界適量提問** |
| 樣片回饋 | 自主檢查，不等待批准 | 可提供可播放樣片並根據回饋修正 |
| 適用 | 快速獲得完成的動畫 | 需要確認研究假設、降低返工 |
| 交付 | 已驗證的 MP4，或明確標示的可播放 HTML/GIF 替代品 | 同左 |

## 安裝

下載或克隆倉庫後執行 `python tools/build_skill_zips.py`，產生 `dist/autopilot/skill.zip` 及 `dist/dialogue/skill.zip`。**請分別匯入每個 ZIP，不要把整個倉庫當成一個 Skill 匯入。**

## 使用範例

**完整託管：**「使用科研動畫製作・完整託管，根據附上的論文與程式碼製作動畫，全程自主完成，不要中途向我提問，直接交付成片。」

**互動確認：**「使用科研動畫製作・互動確認，只在會影響結果的問題上詢問我，先提供必要的可播放樣片，再製作最後成片。」

兩者皆注重白黑灰極簡 2D、場景融合數學視覺化、預設可見的旁白字幕、可重現程式碼及完成檔案檢查。實際輸出受可用工具與環境限制；不得把提示詞或未執行的程式稱為動畫成品。

原始碼位於 `skills/`，各 Skill 的 `SKILL.md` 與參考資料都在自己的目錄中。本專案尚未選擇程式碼授權條款，亦不包含專有字型。

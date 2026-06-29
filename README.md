# 跑鞋对比 Skill for Codex

结构化跑鞋数据管理与 Markdown 对比报告生成。

## 功能

- 📊 跑鞋 JSON 数据管理（品牌、型号、重量、落差、缓震、价格等）
- 📝 一键生成 Markdown 对比表格
- 🔍 支持按类别、品牌、型号筛选排序
- 🇨🇳 中文字段标签，CJK 宽度对齐
- 🎯 18 款热门跑鞋示例数据预置（Nike / Adidas / ASICS / Hoka / 李宁 / 特步 / Brooks / New Balance）

## 安装

在 Codex 中安装：

```
$skill-installer install https://github.com/cc-Change/running-shoe-compare
```

或手动复制到 `$CODEX_HOME/skills/running-shoe-compare/`。

## 使用

在 Codex 对话中直接说：

- "帮我对比一下竞速跑鞋"
- "按重量排序所有跑鞋"
- "只比较 Nike Vaporfly 3 和 李宁飞电4 Ultra"

## 目录结构

```
running-shoe-compare/
├── SKILL.md                 # Skill 核心指令
├── agents/openai.yaml       # UI 元数据
├── scripts/compare.py       # 对比脚本
├── references/shoe-schema.md # 字段说明
└── assets/sample-shoes.json  # 示例数据
```

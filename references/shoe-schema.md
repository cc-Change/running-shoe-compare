# 跑鞋数据字段说明

## JSON 结构

```json
{
  "shoes": [
    {
      "brand": "品牌名",
      "model": "型号名",
      "weight_g": 280,
      "drop_mm": 10,
      "stack_height_mm": 33,
      "category": "日常训练",
      "cushioning": "中",
      "stability": "中性",
      "pace_range": "4:30-6:30/km",
      "price_cny": 899,
      "notes": "自由备注"
    }
  ]
}
```

## 字段说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| brand | string | 是 | 品牌名，如 Nike、Adidas、ASICS、李宁 |
| model | string | 是 | 具体型号，用于精确匹配 |
| weight_g | number | 否 | 单只鞋重量(克)，常见范围 150-350 |
| drop_mm | number | 否 | 前后掌落差(毫米)，常见 0-12 |
| stack_height_mm | number | 否 | 中底厚度(毫米) |
| category | string | 否 | 用途分类 |
| cushioning | string | 否 | 缓震级别 |
| stability | string | 否 | 稳定类型 |
| pace_range | string | 否 | 适用配速区间 |
| price_cny | number | 否 | 参考价格(人民币) |
| notes | string | 否 | 个人备注或补充信息 |

## 分类参考值

**category（用途）**：`竞速`、`速度训练`、`日常训练`、`越野`、`恢复跑`

**cushioning（缓震）**：`低`、`中`、`中高`、`高`、`极致`

**stability（稳定类型）**：`中性`、`稳定支撑`、`运动控制`

## 自定义字段

可在 JSON 中自由添加额外字段，脚本会自动检测并展示所有有值的列。

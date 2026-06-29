---
name: running-shoe-compare
description: Compare and analyze running shoes with structured data and Markdown comparison tables. Use when the user wants to compare running shoes, track running shoe data, generate shoe comparison reports, create a running shoe database, or analyze shoe specs (weight, drop, stack height, cushioning, stability, pace range, price). Triggers on keywords like "跑鞋", "running shoes", "对比", "compare shoes", "shoe rotation", or when the user asks about which running shoes to buy or how shoes differ.
---

# Running Shoe Compare

Compare running shoes by generating structured Markdown tables from JSON data.

## Quick Start

1. Locate or create shoe data: `assets/sample-shoes.json` provides 18 popular models as a starting point
2. Run the comparison script
3. Review the Markdown output

## Core Workflow

### 1. Understand the Data Schema

Read `references/shoe-schema.md` to understand the JSON structure and field definitions.

### 2. Prepare Shoe Data

- **Add new shoes**: Edit an existing JSON file (or create a new one) following the schema in `references/shoe-schema.md`
- **Use the sample data**: `assets/sample-shoes.json` contains 18 popular running shoes across major brands
- **Multiple files are supported**: Use `--data file1.json file2.json` to combine sources

### 3. Run Comparisons

Run `scripts/compare.py` with the desired options:

```bash
# Compare all shoes
python scripts/compare.py --data assets/sample-shoes.json

# Sort by weight (lightest first)
python scripts/compare.py --data assets/sample-shoes.json --sort weight_g

# Show only racing shoes
python scripts/compare.py --data assets/sample-shoes.json --filter category=竞速

# Compare specific models
python scripts/compare.py --data assets/sample-shoes.json --models "Vaporfly 3,Adios Pro 3,飞电4 Ultra"

# Show only key columns
python scripts/compare.py --data assets/sample-shoes.json --columns brand,model,weight_g,price_cny

# Save to file
python scripts/compare.py --data assets/sample-shoes.json -o 跑鞋对比.md --title "2024 竞速跑鞋对比"
```

### 4. Read and Interpret Results

The script outputs a Markdown table. Present the table to the user, then offer analysis:

- **Lightest shoes** for race day
- **Best value** by price-to-performance ratio
- **Category breakdown**: racing vs training vs recovery
- **Stability needs**: neutral vs support shoes

### 5. Help User Build Their Rotation

When the user asks for advice:
1. Ask about their running goals (race distance, target pace, weekly mileage)
2. Ask about their foot type (neutral, low arch/flat feet)
3. Compare relevant shoes using filters
4. Recommend a rotation with reasoning

## Tips

- **Chinese-friendly**: All column labels are in Chinese by default; the script handles CJK character width correctly
- **Custom fields**: Add any extra JSON fields (e.g., `forefoot_width`, `upper_material`) — the script auto-detects non-empty columns
- **Data accuracy**: Verify specs from official sources before adding; the sample data reflects 2024 market info
- **Currency**: Prices default to CNY (¥)

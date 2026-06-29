#!/usr/bin/env python3
"""
Running Shoe Compare - Generate Markdown comparison tables from JSON shoe data.

Usage:
    python compare.py --data shoes.json                     # Compare all shoes
    python compare.py --data shoes.json --sort weight_g      # Sort by weight
    python compare.py --data shoes.json --filter category=竞速  # Filter by category
    python compare.py --data shoes.json --models "Vaporfly 3,Adios Pro 3"  # Compare specific models
    python compare.py --data shoes.json --output report.md   # Write to file
"""

import argparse
import json
import sys
from pathlib import Path

COLUMNS = [
    ("brand",      "品牌"),
    ("model",      "型号"),
    ("weight_g",   "重量(g)"),
    ("drop_mm",    "落差(mm)"),
    ("stack_height_mm", "中底厚度(mm)"),
    ("category",   "用途"),
    ("cushioning", "缓震"),
    ("stability",  "稳定类型"),
    ("pace_range", "适用配速"),
    ("price_cny",  "价格(¥)"),
    ("notes",      "备注"),
]


def load_shoes(data_paths):
    shoes = []
    for dp in data_paths:
        path = Path(dp)
        if not path.exists():
            print(f"[WARN] File not found: {dp}", file=sys.stderr)
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        items = data if isinstance(data, list) else data.get("shoes", [])
        for shoe in items:
            shoe["_source"] = str(path)
        shoes.extend(items)
    return shoes


def filter_shoes(shoes, filters):
    result = shoes
    for f in filters:
        if "=" not in f:
            continue
        key, val = f.split("=", 1)
        result = [s for s in result if str(s.get(key, "")).lower() == val.lower()]
    return result


def pick_columns(shoes, columns=None):
    """Return only the columns that have at least one non-empty value across all shoes."""
    if columns:
        return [(k, l) for k, l in COLUMNS if k in columns]
    active = []
    for key, label in COLUMNS:
        if any(s.get(key) not in (None, "", []) for s in shoes):
            active.append((key, label))
    return active


def render_markdown(shoes, columns, sort_by=None, title="跑鞋对比"):
    if not shoes:
        return f"# {title}\n\n暂无匹配的跑鞋数据。\n"

    if sort_by:
        shoes = sorted(shoes, key=lambda s: s.get(sort_by, "") if isinstance(s.get(sort_by), (int, float)) else str(s.get(sort_by, "")))

    keys = [c[0] for c in columns]
    labels = [c[1] for c in columns]

    # Calculate column widths (Chinese chars count as 2)
    def display_width(s):
        w = 0
        for ch in str(s):
            w += 2 if '\u4e00' <= ch <= '\u9fff' or '\u3000' <= ch <= '\u303f' or '\uff00' <= ch <= '\uffef' else 1
        return w

    widths = [display_width(l) for l in labels]
    for shoe in shoes:
        for i, k in enumerate(keys):
            widths[i] = max(widths[i], display_width(str(shoe.get(k, ""))))

    lines = [f"# {title}\n"]

    # Header
    header = "| " + " | ".join(labels) + " |"
    lines.append(header)
    sep = "|" + "|".join("-" * (w + 2) for w in widths) + "|"
    lines.append(sep)

    # Rows
    for shoe in shoes:
        cells = []
        for i, k in enumerate(keys):
            val = str(shoe.get(k, ""))
            cells.append(val)
        row = "| " + " | ".join(cells) + " |"
        lines.append(row)

    lines.append("")
    lines.append(f"*共 {len(shoes)} 款跑鞋*")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Generate running shoe comparison tables in Markdown")
    parser.add_argument("--data", nargs="+", required=True, help="JSON data file(s)")
    parser.add_argument("--sort", help="Sort by field (e.g., weight_g, price_cny)")
    parser.add_argument("--filter", nargs="+", default=[], help="Filter in key=value format")
    parser.add_argument("--models", help="Comma-separated model names to compare")
    parser.add_argument("--columns", help="Comma-separated column keys to include")
    parser.add_argument("--output", "-o", help="Output file (default: stdout)")
    parser.add_argument("--title", default="跑鞋对比", help="Report title")
    args = parser.parse_args()

    shoes = load_shoes(args.data)
    if not shoes:
        print("[ERROR] No shoe data loaded.", file=sys.stderr)
        sys.exit(1)

    if args.filter:
        shoes = filter_shoes(shoes, args.filter)

    if args.models:
        model_names = [m.strip() for m in args.models.split(",")]
        shoes = [s for s in shoes if s.get("model", "") in model_names]

    columns = args.columns.split(",") if args.columns else None
    active_columns = pick_columns(shoes, columns)

    sort_by = args.sort
    md = render_markdown(shoes, active_columns, sort_by, args.title)

    if args.output:
        Path(args.output).write_text(md, encoding="utf-8")
        print(f"[OK] Report saved to {args.output}")
    else:
        print(md)


if __name__ == "__main__":
    main()

# World News Summary — 20 November 2026

This repository contains an entry for the make.fun bounty **news-image-20261120**: a single image that sums up the world news of Friday 20 November 2026.

## Entry Description

The image (`entry.png`) presents 8 consequential news stories from 20 November 2026, spanning different regions and topics:

1. **Oil Tanker Damaged in Strait of Hormuz** (Middle East) — Conflict/Economy
2. **Saudi Airstrikes on Houthi Targets in Yemen** (Middle East) — Conflict
3. **Russian Missile Hits Poland Near NATO Exercise** (Europe) — Conflict/Geopolitics
4. **Nigeria Boat Capsizes: 30 Dead, ~300 Missing** (Africa) — Disaster
5. **Italy General Strike Paralyzes Transport** (Europe) — Politics/Economy
6. **Anthropic Claims Riemann Hypothesis Proof via AI** (Global) — Science/Technology
7. **UK–EU Deal on Food, Emissions, Youth Mobility** (Europe) — Politics/Economy
8. **Iraq PM Reaches Deal with Kata'ib Hezbollah** (Middle East) — Politics

Each story is represented with a hand-drawn icon, a concise headline, and a region tag.

### Image Specifications
- **Dimensions:** 1024 × 1024 pixels
- **Format:** PNG
- **File size:** ~64 KiB (well under 1 MiB limit)
- **Fonts:** Helvetica Neue (system font on macOS)

## How to Run

```sh
python3 main.py
```

This copies `entry.png` (located next to `main.py`) to `/output/entry.png`, creating the `/output` directory if needed. The script uses only the Python standard library and requires no network access.

### Requirements
- Python 3.8+
- Pillow (for generating the image — only needed for `draw.py`)

To generate the image from scratch:
```sh
pip install pillow
python3 draw.py
```

## Files

- `draw.py` — Generates `entry.png` with the news summary visualization
- `main.py` — Entry point that copies `entry.png` to `/output/entry.png`
- `entry.png` — The generated news summary image (1024×1024 PNG)
- `NEWS.md` — Source news stories with citations
- `LICENSE` — MIT License
- `README.md` — This file

## License

MIT License — see [LICENSE](LICENSE) for details.

SPDX-License-Identifier: MIT
Copyright 2026 Guanzhi1024
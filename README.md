# ⚛️ Ag–Mg Interactive Binary Phase Diagram

A browser-based tool for exploring the **Silver–Magnesium (Ag–Mg)** binary phase diagram with real-time phase analysis, lever rule calculations, and microstructure visualization.

**Built during Packathon 2026** · Zero dependencies · Single HTML file

[![Live Demo](https://img.shields.io/badge/Live_Demo-Vercel-000?style=flat-square&logo=vercel)](https://ag-mg-phase-diagram.vercel.app)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](./LICENSE)

![Ag-Mg Phase Diagram](Ag%20Mg%20phase%20diagram.png)

---

## Features

- **Interactive Phase Diagram** — Full Ag–Mg diagram (100–1000 °C, 0–100 wt.% Mg) rendered on HTML5 Canvas with color-coded phase regions
- **Real-Time Controls** — Temperature & composition sliders with instant updates
- **Lever Rule** — Automatic phase fraction calculation for two-phase regions with animated bar chart
- **Microstructure Visualization** — Algorithmically generated microstructures for 6 types: uniform grains, precipitates, dendrites, lamellar eutectic, intermetallic, and liquid
- **Composition Sweep** — Animated sweep across all phases at adjustable speed
- **Hover Tooltips** — Mouse over any point for phase info
- **PDF Export** — One-click analysis report generation

---

## Tech Stack

- **Frontend**: Vanilla HTML5 + CSS3 + JavaScript (no frameworks, no dependencies)
- **Rendering**: HTML5 Canvas 2D API (two canvases — diagram + microstructure)
- **Data Processing**: Python 3 scripts for CSV parsing and RDP curve simplification
- **Deployment**: Vercel (static site)
- **Typography**: Inter + JetBrains Mono via Google Fonts

---

## How It Works

**Phase Detection** — Given a temperature and composition, the engine checks which region the point falls in by interpolating piecewise boundary curves. No pixel-color detection.

**Lever Rule** — For composition C₀ in a two-phase field [C₁, C₂]:
```
f₁ = (C₂ − C₀) / (C₂ − C₁)
f₂ = (C₀ − C₁) / (C₂ − C₁)
```

**Data Pipeline** — 9,986 experimental CSV data points → Ramer-Douglas-Peucker simplification → 276 points embedded as JS arrays.

---

## Project Structure

```
├── index.html                 # Main app (all-in-one, ~80 KB)
├── Final Website.html         # Polished final version
├── Liquidus Dataset.csv       # Raw liquidus data (9,986 points)
├── alpha solidus.csv          # Raw α-solidus data (930 points)
├── process_liquidus.py        # CSV → JS array (RDP simplification)
├── process_alpha_solidus.py   # CSV → JS array (RDP simplification)
├── generate_report.py         # Auto-generates Word report
├── isotherm.py                # Isotherm analysis utility
├── Ag Mg phase diagram.png    # Reference diagram image
├── REPORT.md                  # Technical methodology report
├── package.json               # Project metadata
└── vercel.json                # Deployment config
```

---

## Getting Started

No install required — just open `index.html` in any modern browser.

```bash
# Or serve locally
npx serve . -p 3000
python -m http.server 3000
```

---

## Data Sources

Phase boundary data sourced from:
- **Liquidus & Solidus**: Experimental CSV datasets, RDP-simplified
- **Other boundaries**: Digitized from ASM Handbook Vol. 3 (Massalski, 1990)

Key invariant reactions: Eutectic E1 (760 °C), Peritectic P (492 °C), Eutectic E2 (472 °C).

---

## License

MIT — see [LICENSE](./LICENSE)

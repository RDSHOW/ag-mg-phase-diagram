# ⚛️ Ag–Mg Interactive Binary Phase Diagram

**A browser-based scientific visualization tool for exploring the Silver–Magnesium binary alloy system in real time**

[![Live Demo](https://img.shields.io/badge/Live_Demo-Vercel-000?style=for-the-badge&logo=vercel)](https://ag-mg-phase-diagram.vercel.app)
[![License: MIT](https://img.shields.io/badge/License-MIT-8b5cf6?style=for-the-badge)](./LICENSE)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero-14b8a6?style=for-the-badge)]()
[![HTML5 Canvas](https://img.shields.io/badge/Rendered_with-HTML5_Canvas-e34f26?style=for-the-badge&logo=html5&logoColor=white)]()

![Ag-Mg Phase Diagram Preview](Ag%20Mg%20phase%20diagram.png)

*Interactive phase diagram with real-time lever rule, microstructure visualization, and PDF export — all in a single HTML file.*

---

## 📌 Overview

The **Ag–Mg Interactive Phase Diagram** is a zero-dependency, fully client-side scientific tool that allows users to explore the Silver–Magnesium binary alloy system. Built during **Packathon 2026**, it bridges the gap between heavyweight CALPHAD software and static textbook diagrams by providing:

- 🔬 **Real-time phase identification** at any (T, C₀) coordinate
- ⚖️ **Automatic lever rule calculations** with visual fraction bars
- 🧬 **Algorithmically generated microstructures** for each phase state
- 📊 **Interactive Canvas-rendered diagram** with 276+ data points from experimental CSV data
- 📄 **One-click PDF export** of analysis reports

> **No server, no build step, no dependencies.** Open `index.html` in any modern browser and start exploring.

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 📊 **Interactive Phase Diagram** | Full Ag–Mg diagram (100–1000 °C, 0–100 wt.% Mg) with color-coded regions, piecewise boundary curves, and hover tooltips |
| 🎛️ **Real-Time Sliders** | Temperature and composition controls with instant diagram/microstructure updates |
| ⚖️ **Lever Rule Engine** | Automatic phase fraction calculation for two-phase regions with animated segmented bar chart |
| 🔬 **Microstructure Visualization** | Canvas-based rendering of 6 distinct microstructure types: uniform grains, precipitates, dendrites, lamellar eutectic, intermetallic, and liquid |
| ▶️ **Composition Sweep** | Animated marker sweep across the diagram at adjustable speed with ping-pong mode |
| 🥧 **Phase Fraction Pie Chart** | Real-time pie chart showing proportional phase distribution |
| 🏷️ **Hover Tooltips** | Mouse-over any diagram point to see phase info, temperature, and composition |
| ⬇️ **PDF Export** | Browser-native print dialog for generating analysis reports |
| 🌙 **Dark Mode UI** | Premium dark-mode design with glassmorphism cards and gradient accents |
| 📱 **Responsive Layout** | CSS Grid layout that adapts from desktop to tablet |

---

## 🏗️ Architecture

### Phase Detection Algorithm

The core engine uses a **boundary-comparison approach** rather than pixel-based detection:

```
Input: (Temperature T, Composition C₀)
  │
  ├─ T ≥ Liquidus(C₀) → LIQUID
  │
  ├─ Check Ag-rich side (C < 10 wt.%)
  │   ├─ T ≥ α-Solidus → L + α (lever rule applied)
  │   └─ T < E1 → α or α + β' (solvus check)
  │
  ├─ Check β' region (10 ≤ C ≤ betaRight)
  │   ├─ Above solidus → L + β'
  │   └─ Below solidus → β' single phase
  │
  ├─ Check γ strip (40–44 wt.%)
  ├─ Check middle region (44–88 wt.%)
  └─ Check Mg-rich side (C ≥ 88 wt.%)
```

### Lever Rule

For composition C₀ in a two-phase field bounded by C₁ and C₂:

```
f₁ = (C₂ − C₀) / (C₂ − C₁)     ← fraction of phase 1
f₂ = (C₀ − C₁) / (C₂ − C₁)     ← fraction of phase 2
```

### Data Pipeline

```
Raw CSV Data (9,986 points)
    │
    ├─ process_liquidus.py ──→ RDP Simplification ──→ 276 points
    │
    ├─ process_alpha_solidus.py ──→ RDP ──→ 18 points
    │
    └─ Manual digitization from ASM Handbook
                                    │
                                    ▼
                            Embedded as JS arrays in HTML
```

### Microstructure Rendering Engine

| Phase State | Visual Pattern | Technique |
|------------|----------------|-----------|
| Liquid | Swirling atoms and convection | Radial gradient + scattered circles |
| α (FCC Ag-rich) | Equiaxed grains | Voronoi-like polygons with grain boundaries |
| β' (AgMg B2) | Ordered blocks | Rectangular tiles with superlattice lines |
| α + β' | Precipitate dispersion | Matrix grains + scattered particles |
| Eutectic (E1, E2) | Alternating lamellae | Waviness-modulated stripe pattern |
| L + solid | Dendritic solidification | Recursive branching algorithm |

All patterns use a **seeded PRNG** (mulberry32) for deterministic, reproducible results.

---

## 🛠️ Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Structure** | HTML5 | Single-file application |
| **Styling** | CSS3 Custom Properties | Dark-mode design system with responsive grid |
| **Logic** | Vanilla ES2020 JavaScript | Phase detection, lever rule, animation |
| **Rendering** | HTML5 Canvas 2D API | Phase diagram + microstructure visualization |
| **Typography** | Google Fonts (Inter + JetBrains Mono) | Professional scientific UI |
| **Data Processing** | Python 3 (offline) | CSV parsing + RDP curve simplification |
| **Hosting** | Vercel | Static CDN deployment |

**Total bundle: ~80 KB** — zero runtime dependencies.

---

## 📦 Project Structure

```
ag-mg-phase-diagram/
├── index.html                    # Main application (deployed to Vercel)
├── Final Website.html            # Final polished version
├── Liquidus Dataset.csv          # Raw liquidus data (9,986 experimental points)
├── alpha solidus.csv             # Raw α-solidus boundary data (930 points)
├── Ag Mg phase diagram.png       # Reference phase diagram image
├── process_liquidus.py           # Liquidus CSV → RDP-simplified JS array
├── process_alpha_solidus.py      # α-solidus CSV → RDP-simplified JS array
├── generate_report.py            # Auto-generates Word document report
├── isotherm.py                   # Isotherm analysis utility
├── liquidus_js.txt               # Processed JS array output (276 points)
├── alpha_solidus_js.txt          # Processed JS array output (18 points)
├── REPORT.md                     # Technical methodology report
├── README.md                     # This file
├── CONTRIBUTING.md               # Contribution guidelines
├── LICENSE                       # MIT License
├── package.json                  # npm/Vercel project metadata
├── vercel.json                   # Vercel deployment config
└── .gitignore                    # Git ignore rules
```

---

## 🚀 Getting Started

### Quick Start (No Install Required)

```bash
# Just open in your browser
start index.html          # Windows
open index.html           # macOS
xdg-open index.html       # Linux
```

### Local Development Server

```bash
# Option 1: npx serve
npx serve . -p 3000

# Option 2: Python
python -m http.server 3000
```

Then visit `http://localhost:3000`

### Regenerate Boundary Data (Optional)

```bash
python process_liquidus.py          # → liquidus_js.txt (276 points)
python process_alpha_solidus.py     # → alpha_solidus_js.txt (18 points)
```

---

## 🌐 Deployment

Deployed on Vercel as a static site:

1. Push to GitHub
2. Import at [vercel.com/new](https://vercel.com/new)
3. Deploy — auto-detected via `vercel.json`

---

## 📋 Phase Diagram Data Sources

| Boundary | Points | Source |
|----------|--------|--------|
| Liquidus | 276 (from 9,986 raw) | Experimental CSV + RDP simplification |
| α-Solidus | 18 (from 930 raw) | Experimental CSV + RDP simplification |
| α-Solvus | 8 | Digitized from ASM Handbook Vol. 3 |
| β' Solidus (L/R) | 6 + 11 | Digitized from reference diagram |
| γ boundaries | 2 + 2 | Vertical limits from literature |
| δ Solidus/Solvus | 6 + 7 | Digitized from reference diagram |

### Invariant Reactions

| Reaction | Temperature | Composition | Type |
|----------|-------------|-------------|------|
| E1: L ↔ α + β' | 760 °C | ~10 wt.% Mg | Eutectic |
| P: L + β' → γ | 492 °C | ~32 wt.% Mg | Peritectic |
| E2: L ↔ γ + δ | 472 °C | ~50 wt.% Mg | Eutectic |

---

## 🧪 Assumptions and Limitations

- Phase boundaries are **piecewise-linear** approximations (not full CALPHAD polynomials)
- Assumes **thermodynamic equilibrium** only — no kinetic effects
- Accuracy: approximately **±10 °C** and **±2 wt.%** vs. reference diagrams
- **Metastable phases** excluded
- Microstructure images are **schematic/algorithmic** — representative, not simulation-accurate
- Composition axis uses **wt.% Mg** throughout

---

## 📚 References

1. Massalski, T. B. (Ed.). (1990). *Binary Alloy Phase Diagrams* (2nd ed.). ASM International.
2. ASM International. (1992). *ASM Handbook Volume 3: Alloy Phase Diagrams*. ASM International.
3. CALPHAD methodology — general thermodynamic modeling reference.
4. [HTML5 Canvas 2D API — MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API)

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](./LICENSE) file for details.

---

**Built with ❤️ during Packathon 2026** — HTML5 Canvas · Vanilla JavaScript · Zero Dependencies

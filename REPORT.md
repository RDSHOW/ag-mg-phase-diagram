# Ag–Mg Interactive Binary Phase Diagram
## Technical Report — Methodology, Assumptions & Lever Rule

---

## 1. Introduction

The Ag–Mg system features:
- Eutectic at **472 °C** / **~30 at.% Mg**
- Peritectic near **820 °C** / **~48 at.% Mg**
- Intermetallics: AgMg (β, B2-ordered), AgMg₃ (ε)
- Ag mp = 961.8 °C; Mg mp = 650 °C

## 2. Digitisation Methodology

Phase boundaries approximated from ASM Handbook Vol.3 and CALPHAD estimates as piecewise linear arrays of `[at.% Mg, T °C]` points. Interpolation: linear between adjacent points.

## 3. Lever Rule

For C₀ in a two-phase field [C₁, C₂]:

- f₁ = (C₂ − C₀) / (C₂ − C₁)
- f₂ = (C₀ − C₁) / (C₂ − C₁)

Example — 400°C, C₀=30, C₁=22(α), C₂=42(β): f_α=60%, f_β=40%

## 4. Assumptions

- Piecewise linear boundaries (not full CALPHAD)
- Equilibrium only; no kinetic effects
- ±10°C, ±2 at.% accuracy
- Metastable phases excluded

## 5. References

1. Massalski, Binary Alloy Phase Diagrams, ASM 1990
2. ASM Handbook Vol. 3, 1992

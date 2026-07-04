<![CDATA[# Contributing to Ag–Mg Phase Diagram

Thank you for your interest in contributing! This project welcomes improvements to phase boundary data, UI enhancements, and new features.

## How to Contribute

1. **Fork** the repository
2. **Create a branch** for your feature (`git checkout -b feature/my-feature`)
3. **Commit** your changes (`git commit -m 'Add some feature'`)
4. **Push** to the branch (`git push origin feature/my-feature`)
5. **Open a Pull Request**

## Development Setup

No build tools required — just open `index.html` in a browser.

For data processing scripts, you'll need Python 3.x:

```bash
python process_liquidus.py
python process_alpha_solidus.py
```

## Code Style

- **HTML/CSS/JS**: All contained in a single HTML file for simplicity
- **JavaScript**: ES2020+, no external dependencies
- **Comments**: Clearly document phase boundary data sources and algorithms

## Reporting Issues

Please include:
- Browser and version
- Steps to reproduce
- Expected vs. actual behavior
- Screenshots if applicable

## Areas for Improvement

- Additional phase systems (Cu-Ni, Fe-C, etc.)
- 3D ternary phase diagram support
- CALPHAD integration for more accurate boundaries
- Mobile touch gesture support
- Accessibility improvements (screen reader, keyboard navigation)
]]>

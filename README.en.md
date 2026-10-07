<picture>
  <source media="(prefers-color-scheme: dark)" srcset="readme-assets/header-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="readme-assets/header-light.svg">
  <img alt="Taguchi Experimental Array Exploration · ✦ EricMingle69" src="readme-assets/header-light.svg" width="100%">
</picture>

<p align="center">
  <a href="README.md">简体中文</a> · <a href="README.en.md">English</a> · <a href="PERSONAL-NOTICE.md">✦ EricMingle69</a>
</p>

# Taguchi Experimental Array Exploration

## Purpose

Generates candidate experimental arrays from factors and levels, with two Python examples and a Tkinter interface for studying array construction and orthogonality checks.

## Repository guide

| Entry | Contents |
| --- | --- |
| [GUI](Taguchi-Orthogonal-Array-Custom-Generation/orthogonal_array_gui.py) | Factor inputs, array display and checks |
| [NumPy implementation](Taguchi-Orthogonal-Array-Custom-Generation/orthogonal_array_v1.py) | Orthogonality, balance and imbalance checks |
| [LCM sequence implementation](Taguchi-Orthogonal-Array-Custom-Generation/orthogonal_array_v2.py) | Repeated sequences using the levels’ least common multiple |

## Getting started

1. Prepare Python ≥3.9 with Tkinter and NumPy; dependency versions are not pinned.
2. Start with the CLI examples, which use three factors with 3/2/3 levels:

```sh
python3 -m pip install numpy
python3 Taguchi-Orthogonal-Array-Custom-Generation/orthogonal_array_v1.py
python3 Taguchi-Orthogonal-Array-Custom-Generation/orthogonal_array_v2.py
```

3. The GUI entry is `python3 Taguchi-Orthogonal-Array-Custom-Generation/orthogonal_array_gui.py`. These are source-defined entries, not evidence of passed execution tests.

## Scope and limitations

- “Fully balanced” does not mean strictly orthogonal; independently check pairwise combination frequencies.
- The GUI’s fully balanced branch receives a list from v2 but calls v1’s NumPy two-dimensional indexing check, creating a type mismatch in the current source.
- v2’s periodic sequences do not guarantee equal combination frequencies for every factor pair; do not use outputs directly as an engineering experiment plan.
- No file-export entry is provided, and valid-input ranges and resource limits for large combinations need documentation.

## Sources and existing licenses

The original repository has no LICENSE/NOTICE, leaving reuse rights for source and existing documentation unspecified. Mathematical properties should be established through small reproducible inputs and independent checks rather than inferred from the project name.

---

Documentation maintained by **✦ EricMingle69** · [Ming-Sir-69](https://github.com/Ming-Sir-69)  
[Personal identity, licensing and permissions](PERSONAL-NOTICE.md) · The header follows your GitHub theme.

# cs/ — pictures for Code School

This folder holds the **pictures** that the Code School lessons in
[Project Compass](../compass.html) show. The lessons themselves (text, code,
exercises and tick-boxes) are stored inside `compass.html`, in its data block,
so there is nothing to open here directly.

| Folder | Used by |
|---|---|
| `R/figures/` | R from zero, lessons 08 (plotting), 09 (statistics) and 12 (capstone) |
| `R/capstone/figures/` | R from zero, lesson 12 capstone report |
| `Python/figures/` | Python from zero, lessons 09–11 and 13 |
| `Paper_Labs/<lab>/target_figures/` | Paper reproduction labs: the figure each lab asks you to recreate |

## Where to start learning

Open the website, go to **Project Compass → Code School**, pick *R from zero*
or *Python from zero* and begin with the tab **00 START HERE** (it walks you
through installing everything). Do the lessons in number order; the paper labs
come after the basics.

## Changing the pictures

- Keep file names exactly as they are: the lessons refer to them by path
  (for example `cs/R/figures/L08_gg-hist-1.png`).
- After adding, renaming or removing a picture, run
  `python3 tools/check_links.py` from the website folder to make sure no lesson
  points to a missing file.

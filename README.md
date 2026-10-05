# 🏡 Rush Hub

My study planner as a website: **Home Base** (front page), **Sprout** (daily plan), **Project Compass** (projects + Code School), **Book Nook** (free books + flashcards) and **The Gentle Path** (calm timeline).

- Live site: https://halireena.github.io/rush-hub/ (once GitHub Pages is switched on)
- How to publish and edit it: [WEBSITE_GUIDE.md](WEBSITE_GUIDE.md)
- How to use the $250 cloud credit: [CREDIT_GUIDE.md](CREDIT_GUIDE.md)
- Edit content safely: `python3 tools/edit_data.py --help`

Ticks and progress are saved in each browser. Plain HTML/CSS/JavaScript, no build step.

## What's here

| File | Page |
|---|---|
| `index.html` | Home Base (front page) |
| `sprout.html` | Sprout |
| `compass.html` | Project Compass (pictures for its Code School lessons are in `cs/`) |
| `books.html` | Book Nook |
| `path.html` | The Gentle Path |
| `website-guide.html`, `credit-guide.html` | The two guides as web pages |
| `tools/` | `edit_data.py` (edit content safely) and `check_links.py` (find broken links) |

## View it on your computer

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000 (Ctrl + C stops it).

## Check before you push

```bash
python3 tools/edit_data.py check   # every page's content is valid
python3 tools/check_links.py       # every local link and picture exists
```

GitHub runs both automatically on every push (the "Check site" action).

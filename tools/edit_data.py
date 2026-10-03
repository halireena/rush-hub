#!/usr/bin/env python3
"""Take the data out of a page so you can edit it safely, then put it back.

Every app page keeps its content (weeks, tasks, books, links...) in ONE block:
    <script type="application/json" id="data"> ... </script>
(Sprout uses id="plan", Gentle Path uses id="weeks".)
Editing that block by hand inside the HTML is risky (one missing comma breaks the page),
so this tool copies it into a nicely indented .json file you can edit in VS Code,
which underlines mistakes in red, and then puts it back.

Usage (run from the website folder):
    python3 tools/edit_data.py list                    # which pages have a data block
    python3 tools/edit_data.py extract index.html      # creates data/index.json
    #   ...edit data/index.json in VS Code and save...
    python3 tools/edit_data.py inject index.html       # checks the JSON, then puts it back
    python3 tools/edit_data.py check                   # checks every page's data is valid

Only the Python standard library is used, so nothing needs installing.
"""
from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
BLOCK = re.compile(r'(<script type="application/json" id="(data|plan|weeks)">)(.*?)(</script>)', re.S)


def find_block(html: str):
    m = BLOCK.search(html)
    if not m:
        raise SystemExit("No data block found in this page.")
    return m


def load_page_json(raw: str):
    # pages store "</" as "<\/" so the browser doesn't end the script early
    return json.loads(raw.replace("<\\/", "</"))


def cmd_list() -> None:
    for page in sorted(ROOT.glob("*.html")):
        m = BLOCK.search(page.read_text(encoding="utf-8"))
        print(f"{page.name:15} {'data block id=' + m.group(2) if m else '(no data block)'}")


def cmd_extract(page_name: str) -> None:
    page = ROOT / page_name
    m = find_block(page.read_text(encoding="utf-8"))
    data = load_page_json(m.group(3))
    DATA_DIR.mkdir(exist_ok=True)
    out = DATA_DIR / (page.stem + ".json")
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {out.relative_to(ROOT)}. Edit it, save, then run: python3 tools/edit_data.py inject {page_name}")


def cmd_inject(page_name: str) -> None:
    page = ROOT / page_name
    src = DATA_DIR / (page.stem + ".json")
    if not src.exists():
        raise SystemExit(f"{src} not found. Run 'extract {page_name}' first.")
    try:
        data = json.loads(src.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise SystemExit(f"Your JSON has a mistake on line {e.lineno}, column {e.colno}: {e.msg}. Nothing was changed.")
    html = page.read_text(encoding="utf-8")
    m = find_block(html)
    text = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    backup = page.with_suffix(".html.bak")
    shutil.copy(page, backup)
    new_html = html[: m.start(3)] + text + html[m.end(3):]
    page.write_text(new_html, encoding="utf-8")
    print(f"Updated {page_name} (backup saved as {backup.name}; delete it once you're happy).")


def cmd_check() -> None:
    ok = True
    for page in sorted(ROOT.glob("*.html")):
        m = BLOCK.search(page.read_text(encoding="utf-8"))
        if not m:
            continue
        try:
            load_page_json(m.group(3))
            print(f"OK    {page.name}")
        except json.JSONDecodeError as e:
            ok = False
            print(f"BROKEN {page.name}: {e.msg} at character {e.pos}")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args[0] in {"-h", "--help"}:
        print(__doc__)
    elif args[0] == "list":
        cmd_list()
    elif args[0] == "check":
        cmd_check()
    elif args[0] in {"extract", "inject"} and len(args) == 2:
        (cmd_extract if args[0] == "extract" else cmd_inject)(args[1])
    else:
        print(__doc__)
        sys.exit(1)

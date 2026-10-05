#!/usr/bin/env python3
"""Check that every local link and picture on the site points to a file that exists.

It looks at:
  - href="..." and src="..." in every .html page (including the HTML stored
    inside each page's data block, e.g. the Code School lessons in Compass)
  - plain file names stored in the data blocks (e.g. "url": "books.html")
  - [text](path) links and <img src> in the Markdown guides

Web addresses (https://...), mailto: links and #anchors are skipped.

Usage (run from the website folder):
    python3 tools/check_links.py

Exit code 0 = no broken links, 1 = something is missing.
Only the Python standard library is used, so nothing needs installing.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent

# Markdown files that are not part of this site and are not checked.
SKIP_FILES: set[str] = set()

# Pictures that the project write-ups in Compass show once you have run that
# project (they live in the project's own repository, not in this website).
# Listed here so they are reported as a note instead of failing the check.
EXPECTED_MISSING_PREFIXES = ("figures/", "docs/img/", "example_output/")

ATTR = re.compile(r'''(?:href|src)\s*=\s*(\\?["'])(.*?)\1''', re.I | re.S)
MD_LINK = re.compile(r'!?\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+"[^"]*")?\s*\)')
DATA_BLOCK = re.compile(r'<script type="application/json" id="(?:data|plan|weeks)">(.*?)</script>', re.S)
FILE_LIKE = re.compile(r'^[\w./-]+\.(?:html?|png|jpe?g|gif|svg|webp|pdf|md|css|js|json)(?:[#?].*)?$', re.I)


def is_external(url: str) -> bool:
    url = url.strip()
    return (
        not url
        or url.startswith(("#", "//", "data:", "mailto:", "tel:", "javascript:", "{", "$"))
        or bool(re.match(r"^[a-z][a-z0-9+.-]*:", url, re.I))
    )


def strings_in(obj):
    if isinstance(obj, dict):
        for v in obj.values():
            yield from strings_in(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from strings_in(v)
    elif isinstance(obj, str):
        yield obj


def refs_in_html(text: str):
    for m in ATTR.finditer(text):
        yield m.group(2)
    block = DATA_BLOCK.search(text)
    if block:
        try:
            data = json.loads(block.group(1).replace("<\\/", "</"))
        except json.JSONDecodeError:
            return  # tools/edit_data.py check reports this
        for s in strings_in(data):
            if FILE_LIKE.match(s.strip()):
                yield s.strip()


def refs_in_markdown(text: str):
    text = re.sub(r"```.*?```", "", text, flags=re.S)  # ignore code blocks
    text = re.sub(r"`[^`\n]*`", "", text)
    for m in MD_LINK.finditer(text):
        yield m.group(1)
    for m in ATTR.finditer(text):
        yield m.group(2)


def main() -> int:
    broken: list[tuple[str, str]] = []
    expected: list[tuple[str, str]] = []
    checked = 0
    files = sorted(ROOT.rglob("*.html")) + sorted(ROOT.rglob("*.md"))
    for f in files:
        rel = f.relative_to(ROOT).as_posix()
        if rel.startswith(".git/") or rel in SKIP_FILES:
            continue
        text = f.read_text(encoding="utf-8")
        refs = refs_in_html(text) if f.suffix == ".html" else refs_in_markdown(text)
        for ref in sorted(set(refs)):
            if is_external(ref):
                continue
            path = unquote(urlsplit(ref).path)
            if not path:
                continue
            checked += 1
            target = (ROOT / path.lstrip("/")) if path.startswith("/") else (f.parent / path)
            if target.exists():
                continue
            if f.suffix == ".html" and path.startswith(EXPECTED_MISSING_PREFIXES):
                expected.append((rel, ref))
            else:
                broken.append((rel, ref))

    if expected:
        print(f"Note: {len(expected)} project picture(s) in Compass are not in this website yet (expected):")
        for src, ref in expected:
            print(f"  {src}: {ref}")
    if broken:
        print(f"BROKEN: {len(broken)} local link(s) point to missing files:")
        for src, ref in broken:
            print(f"  {src}: {ref}")
        return 1
    print(f"OK    {checked} local links checked, none broken.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

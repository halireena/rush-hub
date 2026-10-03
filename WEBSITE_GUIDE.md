# 🌐 Your website: publish it, change it, grow it

**What this is:** your apps (Home Base, Sprout, Project Compass, Book Nook, The Gentle Path) as a real website, free on **GitHub Pages**. It works on your phone and Mac like any website, and it doesn't need Claude.

**Time:** about 45 minutes the first time, then 2 minutes per change.

---

## 0. Understand what you're publishing (5 minutes, read this first)

### 0.1 What's in the folder

| File / folder | What it is | When you'd touch it |
|---|---|---|
| `index.html` | **Home Base**, the front page. Its address is just your site's address | Change links, the app list, the free-books list, the credit tips |
| `sprout.html` | Sprout: today's blocks, the plan, the paper track, the study guide | Change the timetable, weeks, tasks |
| `compass.html` | Project Compass: all projects + Code School | Rarely (it's big; see section 5.4) |
| `books.html` | Book Nook: **public version, free books only** | Add a free book or fix a card |
| `path.html` | The Gentle Path timeline | Change chapter text or calm tips |
| `cs/` | Pictures used by the Code School lessons inside Compass | Only if you add lesson images |
| `tools/edit_data.py` | A helper that lets you edit an app's content safely | Every time you change content |
| `.nojekyll` | An empty file that tells GitHub "serve these files exactly as they are" | Never (don't delete it) |
| `WEBSITE_GUIDE.md` | This guide | — |

**How each page works (the one idea you need):** every app is **one HTML file** with three parts:
1. **`<style>`**: how it looks (colours, fonts, spacing).
2. **A data block**, `<script type="application/json" id="data">…</script>`: the content (weeks, tasks, books, links). Sprout's block is called `id="plan"` and Gentle Path's is `id="weeks"`.
3. **`<script>`**: the code that turns the data into what you see.

Most changes you'll ever make are to **part 2, the content**, and the helper tool makes that safe.

### 0.2 Public vs private: decide before you publish

A GitHub Pages site on a **free** account must come from a **public** repository. That means anyone with the link can see the site and the files behind it. I built this public version carefully:

| Included ✅ | Left out on purpose 🔒 (kept in your folder → `10_APPS`) |
|---|---|
| Home Base, Sprout, Compass + Code School, Gentle Path | **Career Garden**: it contains researchers' emails and phone numbers and your application plans |
| Book Nook with the **25 free, legally shared books** | Book Nook with **your 14 PDF books**: study notes from copyrighted textbooks shouldn't be put on the public internet |

Things still in the public version that you might want to edit out first:
- **Sprout and Gentle Path mention your paper plans and the first names "Lindsey" and "Jack".** If you'd rather not show those, follow section 5.2 and change the text to "supervisor" and "collaborator".
- **Each page has a "noindex" line**, so Google won't list it and only people with the link will find it. To make it a portfolio site that shows up in search, see section 6.3.

> **Ticks and progress on the website** are saved **in each browser** (your phone and Mac each keep their own). Syncing between devices only works in the claude.ai versions. That's fine: use the website for reading and planning, and Notion for anything you must keep.

---

## 1. One-time setup on your Mac (10 minutes)

You need two free things:
1. **A GitHub account.** You have one: **github.com/halireena**.
2. **GitHub Desktop** (easiest, no typing commands): download from **desktop.github.com**, install, open it and sign in with your GitHub account.

*(If you'd rather use Terminal, the commands are in section 7. Both routes do exactly the same thing.)*

Also install **VS Code** (code.visualstudio.com) if you haven't already. You'll edit files with it, and it highlights mistakes.

---

## 2. Publish the website (15 minutes)

### Step 1: Create the repository (the website's home on GitHub)
1. Go to **github.com** → the **＋** at the top right → **New repository**.
2. **Repository name:** `rush-hub`. The name becomes part of your web address, so keep it short, with no spaces.
3. **Public** (needed for free GitHub Pages).
4. Leave "Add a README" **unticked** (we already have files).
5. Click **Create repository**.

### Step 2: Put the files in it
**Option A: GitHub Desktop (recommended)**
1. GitHub Desktop → **File → Clone repository** → choose `halireena/rush-hub` → pick a place on your Mac (e.g. `Documents/GitHub/rush-hub`) → **Clone**.
2. Open that folder in Finder (GitHub Desktop: **Repository → Show in Finder**).
3. Copy **everything inside** the `rush-hub-site` folder into it, including the hidden `.nojekyll` file. To see hidden files in Finder, press **⌘ + Shift + .** (full stop).
4. Back in GitHub Desktop you'll see all the files listed. Bottom left, write a **Summary**: `First version of my website`. Click **Commit to main**.
5. Click **Push origin** (top bar).

**Option B: upload in the browser (no installs)**
1. On your new repository page, click **uploading an existing file**.
2. Drag in all the files and folders from `rush-hub-site`.
   - The browser uploader handles folders in Chrome. If the `cs` folder doesn't upload, use Option A.
   - `.nojekyll` is hidden: press ⌘ + Shift + . in Finder to see it, then drag it in too.
3. Write `First version of my website` → **Commit changes**.

### Step 3: Switch on GitHub Pages
1. In the repository: **Settings** (top tab) → **Pages** (left menu).
2. **Source:** *Deploy from a branch*. **Branch:** `main`, folder `/ (root)` → **Save**.
3. Wait 1–3 minutes, then refresh the page. It will say **"Your site is live at https://halireena.github.io/rush-hub/"**.

### Step 4: Check it works
Open **https://halireena.github.io/rush-hub/** and check:
- [ ] Home Base loads and shows this week's 3 things.
- [ ] Each app card opens (Sprout, Compass, Book Nook, Gentle Path).
- [ ] Compass → Learn Python → lesson 09 shows pictures.
- [ ] On your phone: open the address in Chrome → ⋮ → **Add to home screen**. It now looks like an app icon.

**If you see a 404 page:** wait 5 more minutes (the first build can be slow). Check that `index.html` is in the *top level* of the repository, not inside a subfolder.

---

## 3. The change cycle (memorise this; every change works this way)

```
 1. Edit a file on your Mac (VS Code)
 2. Check it locally: open the page in your browser
 3. GitHub Desktop: write a summary → Commit to main → Push origin
 4. Wait ~1 minute → refresh your website
```

**Check locally properly:** some browsers limit pages opened by double-clicking. The proper way is a tiny local web server:
```bash
cd ~/Documents/GitHub/rush-hub        # the folder with index.html
python3 -m http.server 8000
```
Then open **http://localhost:8000** in your browser. Press **Ctrl + C** in Terminal to stop the server.

**Made a mess? Undo:**
- **Before committing:** GitHub Desktop → right-click the file → **Discard changes**.
- **After pushing:** GitHub Desktop → **History** tab → right-click the commit → **Revert changes in commit** → **Push origin**. Nothing is ever truly lost; GitHub keeps every version.

---

## 4. The safe way to change content: `tools/edit_data.py`

Editing the data block inside the HTML directly is risky: one missing comma and the whole page goes blank. So use the helper:

```bash
cd ~/Documents/GitHub/rush-hub
python3 tools/edit_data.py list                # which pages have content blocks
python3 tools/edit_data.py extract index.html  # makes data/index.json
```
1. Open `data/index.json` in **VS Code**. It's neatly indented, and VS Code underlines mistakes in red.
2. Change what you want and **save**.
3. Put it back:
   ```bash
   python3 tools/edit_data.py inject index.html
   ```
   If your JSON has a mistake, the tool tells you the **line and column** and **changes nothing**. If it worked, it keeps a backup (`index.html.bak`).
4. Check locally (section 3), then commit and push.
5. Delete the `.bak` file and the `data/` folder before committing. They're only working copies.

**JSON rules in 30 seconds (the format the content is in):**

| Rule | Example |
|---|---|
| Text goes in **double quotes** | `"name": "Sprout"` |
| Items are separated by **commas**, but **no comma after the last one** | `["a", "b", "c"]` ✅ · `["a", "b",]` ❌ |
| `{ }` = an object (named fields), `[ ]` = a list | `{"name": "x", "url": "y"}` |
| Numbers and true/false have **no quotes** | `"fit": 5`, `"free": true` |
| A quote mark inside text needs a backslash | `"She said \"hi\""` |

Run `python3 tools/edit_data.py check` at any time to test every page.

---

## 5. Recipes: the changes you'll actually want

### 5.1 Home Base (`index.html`)
`extract index.html`, then edit `data/index.json`:

| To change… | Edit this part of the JSON |
|---|---|
| The app cards | `"appList"`: each card is `{"name", "e" (emoji), "c" (background colour), "d" (description), "url"}`. Add a new card by copying one `{…}` block, pasting it after a comma, and changing the values |
| The project buttons | `"chips"`: each is `["P1", "🥔 P1 GWAS"]`. The first value is the Compass project code (S0, CR, CP, CL, M0, P1–P7, T1, T2), the second is the label |
| The free-books list | `"free"`: groups `{"t": title, "items": [ {title, org, why, url}, … ]}` |
| The $250 credit text and prompts | `"credit"`: `intro`, `steps` (a list of text), `prompts` (a list of `[title, prompt]`) |
| Which project "this week" points to | `"weekProject"`: `"5": "M0"` means week 5 opens the M0 project |

### 5.2 Sprout's plan (`sprout.html`)
`extract sprout.html` → `data/sprout.json`:
- `"weeks"`: one entry per week:
  - `w` (number), `s`/`e` (start/end date `YYYY-MM-DD`), `ph` (phase name), `c` (phase colour)
  - `kh`/`ph_h` (kit/paper hours), `f` (kit focus), `files`, `d` (done when)
  - `p` (paper task), `rd` (reading), `cr` (computational reading), `ap` (applications)
- `"routine"`: the daily blocks, as `["19:00", "21:00", "kit", "label"]`. The kinds are `paper`, `kit`, `read`, `jobs` and `review`, and each kind has its own colour and icon.
- `"ritual"`: the daily ritual lines.
- `"targets"`: the job-target lists.
- **To remove names** (for example "Lindsey" or "Jack"): use VS Code's **Find and Replace (⌘ + Option + F)** inside `data/sprout.json`. Also change them in `path.html` (5.4) and `index.html`.
- **Moving the whole plan by a week** (if life happens): change every `s` and `e` date, plus `"start"`. It's easier to ask free Claude: "Here is my JSON; shift every date by 7 days and give it back".

### 5.3 Book Nook: add a free book (`books.html`)
`extract books.html` → in `data/books.json`, add a book to `"books"`:
```json
{
  "slug": "my_new_book", "short": "Short name", "emoji": "📗", "color": "#2f855a",
  "title": "Full title", "authors": "Who wrote it", "edition": "2024",
  "url": "https://the-publisher-page", "licence": "Free from the publisher",
  "overview": "Two sentences about it.", "how": "How to read it.", "warn": "", "free": true, "file": "",
  "chapters": [
    {"n": 1, "title": "Chapter title", "pdf_pages": "1-20", "minutes": 40, "priority": "core",
     "summary": ["Point one", "Point two"],
     "terms": [{"term": "EC", "def": "Electrical conductivity: how salty the solution is"}],
     "cards": [{"q": "Question?", "a": "Answer."}],
     "for_rush": "Why it matters to you"}
  ]
}
```
Then add its `slug` to one of the `"shelves"` lists, or the book won't appear on a shelf. `priority` must be `core`, `useful` or `skim`.

**Never change a book's `slug` or the order of its cards after you've started reviewing.** Your progress is stored against those, so changing them resets that book's progress.

### 5.4 The Gentle Path (`path.html`)
- Its weekly data is in the `id="weeks"` block (use the tool).
- The **chapter cards** (titles, "how you'll feel", skills lists) and **calm tips** are written directly in the code. In VS Code, search for `const CH=[` and `const tips=[`: each chapter is one `{…}` line with `em` (emoji), `t` (title), `s`/`e` (dates), `why`, `kit` (a list), `paper` (a list) and `feel`. Edit the text **inside the quotes** only.

### 5.5 Colours and fonts (any page)
At the top of each file, in `<style>`, the colours are named "tokens":
```css
:root{ --bg:#fbf6ef; --card:#fffdf9; --fg:#3a3140; --leaf:#5cb85c; ... }
```
- Change a hex value (e.g. `--leaf:#5cb85c` → `#7c4dff` for purple) and the whole page follows.
- **Each colour appears three times**: once for light mode and twice for dark mode (the `prefers-color-scheme: dark` block and the `[data-theme="dark"]` block). Change all three so both modes look right.
- Fonts come from Google Fonts in the `<link …fonts.googleapis.com…>` line near the top. To change one, pick a font on fonts.google.com, copy its link, and replace `Fredoka`/`Nunito` in the CSS.

### 5.6 Add a brand-new page (for example your CV or a project write-up)
1. In VS Code, make `cv.html`. Easiest start: copy `path.html`, delete everything inside `<body>…</body>`, and write your own content with simple HTML:
   ```html
   <div style="max-width:720px;margin:0 auto;padding:24px 16px">
     <h1>Rush · CV</h1>
     <p>MSc Bioinformatics, University of Birmingham Dubai (2026)</p>
     <h2>Projects</h2>
     <ul><li><a href="https://github.com/halireena/...">Potato GWAS</a></li></ul>
   </div>
   ```
2. Link to it from Home Base: add an `appList` card (5.1) with `"url": "cv.html"`.
3. Check locally → commit → push.

### 5.7 Compass and Code School content
Compass holds **all the lessons as HTML inside its data block**, so it's 3 MB. Small fixes (a typo, a link) are fine with the tool:
1. `extract compass.html`.
2. Search `data/compass.json` for the text and fix it.
3. `inject`.

For **big changes** (a new lesson or project), edit the Markdown file in your kit folder instead, and ask a cloud session (see the credit guide) to rebuild Compass. Or simply add a link to a new page (5.6).

---

## 6. Extras

### 6.1 Your own short address (optional, costs money)
A domain like `rushbio.com` costs about USD 10–15 a year from a registrar (e.g. Cloudflare, Namecheap). After buying it, go to GitHub → **Settings → Pages → Custom domain**, type it in, then follow GitHub's on-screen DNS instructions. Not needed: `halireena.github.io/rush-hub` works forever for free.

### 6.2 Make it private
GitHub Pages from a **private** repository needs a paid GitHub plan. The free alternative is to keep sensitive apps offline (as they are now) and only publish the public set.

### 6.3 Turn it into a public portfolio
- Remove `<meta name="robots" content="noindex, nofollow">` from the pages you want Google to find.
- Better: build your **Quarto portfolio site** (Code School / M0 week 7) as a separate repository, `halireena.github.io`, which becomes your main address. Then link this planner from it, or keep the planner unlisted.

### 6.4 Something broke: checklist
1. A page is **blank**: run `python3 tools/edit_data.py check`. It names the broken page; fix the JSON line it reports.
2. **Old version still showing**: hard refresh (Mac **⌘ + Shift + R**; phone: close the tab and reopen it). GitHub can take 1–5 minutes.
3. **Images missing in Compass**: is the `cs/` folder in the repository, next to `compass.html`?
4. **404**: `index.html` must be at the top level, and Pages must be set to `main` / `(root)`.
5. **Still stuck**: GitHub Desktop → History. Find the last version that worked and revert to it (section 3).

---

## 7. Terminal version (if you prefer commands)

```bash
# one-time: tell git who you are (use your GitHub no-reply email from GitHub → Settings → Emails)
git config --global user.name "Halireena"
git config --global user.email "ID+halireena@users.noreply.github.com"

# first publish (after creating the empty repo on github.com)
cd ~/Documents/GitHub
git clone https://github.com/halireena/rush-hub.git
cp -R ~/path/to/rush-hub-site/. rush-hub/      # the /. copies hidden files too
cd rush-hub
git add .
git commit -m "First version of my website"
git push

# every change afterwards
git status                  # what changed?
git add index.html          # or: git add .
git commit -m "Update app links"
git push
```
`git log --oneline` lists your history; `git revert <id>` undoes one commit safely.

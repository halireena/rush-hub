# 💳 How to use your $250 Claude cloud-session credit well

> **What I know for sure** comes from the offer screen you shared (2 Oct 2026). Anything else is marked *check*: the app's own help pages ("How cloud sessions work", "About this credit") are the final word.

## 1. What it is, in plain words
- A **cloud session** is Claude working on code **inside one of your GitHub repositories**, in a secure online computer. You can close your laptop; when it's done you come back to a **pull request** (a proposed set of changes) to review.
- The offer: **$250 of credit for cloud sessions**, on top of your plan's normal limits.

| Fact (from the offer screen) | Detail |
|---|---|
| Who can claim | **Existing Pro and Max subscribers only** |
| Claim deadline | **10:59 AM GMT+4 (UAE time), 8 October 2026** |
| Credit expires | **11:59 AM GMT+4, 5 November 2026** |
| Not usable for | **Projects and Routines** |
| After it's used up or expires | Your plan's normal usage applies |
| How it's spent | It's applied **automatically** when you start a cloud session |

*Check:* if your subscription ends before 5 November, can you still use claimed credit? The screen doesn't say. Look at "About this credit" in the app, or ask support. **Safest plan: claim now and use the most important sessions first.**

## 2. Claim it (5 minutes, today)
1. Open the **Claude desktop app**. If there's a yellow bar saying *"For your security, sign in again"*, click **Sign in again** first.
2. Click **Claim credit** (in the pop-up or the "Claim a $250 bonus credit" bar).
3. **Connect GitHub** when asked, and allow access to your account **halireena**.
4. **Choose a repository.** Create `rush-hub` first (Website guide, section 2, step 1) and pick it. You can connect more repositories later.

## 3. How a good session works (the 6-step routine)
1. **One clear job per session.** "Publish my website" is good; "make my whole career" is not.
2. **Say what you want to learn:** "explain every change in plain English, as if to a beginner".
3. **Say what NOT to do:** "don't add features I didn't ask for; leave TODOs for the parts I should write myself".
4. **Ask for a check:** "run the tests / open the page and confirm it works before you finish".
5. **Review the pull request yourself** (section 5) and ask questions in the session if anything is unclear.
6. **Merge**, then write 3 lines in your `learning-notes`: what changed, why, and what you learned.

**Make the credit last:**
- Small, specific sessions use less than big open-ended ones.
- Give it the files it needs, but don't ask it to "look at everything".
- Don't use the credit for things free Claude can do. *Explaining* code works fine in a normal chat; spend credit on *building and checking inside your repo*.

## 4. Your session plan, in priority order (copy the prompts)

### Session 1: Publish your website (repo: `rush-hub`)
> I've uploaded my personal study website (static HTML files: index.html, sprout.html, compass.html, books.html, path.html, cs/ images, .nojekyll, tools/edit_data.py) to this repository. Please: (1) check that every page loads and every link between pages works when served from GitHub Pages at https://halireena.github.io/rush-hub/; (2) run `python3 tools/edit_data.py check`; (3) fix only real problems you find; (4) add a short README.md explaining what the site is and linking to WEBSITE_GUIDE.md. Explain every change in plain English for a beginner. Don't redesign anything.

Then switch Pages on yourself (Website guide, section 2, step 3).

### Session 2: Your function libraries (new repo: `rushtools`)
> This repo will hold my personal function libraries. I'll upload two folders from my Code School: an R package `rushtools` (R/, tests/, DESCRIPTION) and a Python package `rushtools` (src/ layout, pyproject.toml, tests/). Please: put them in `r/` and `python/`; replace the placeholder email `you@example.com` with my GitHub no-reply address placeholder and tell me where to change it; add GitHub Actions that run `devtools::test()` for R and `pytest` for Python on every push; add a README showing how to install each (`remotes::install_github("halireena/rushtools", subdir = "r")` and `pip install "git+https://github.com/halireena/rushtools#subdirectory=python"`). Don't write new functions. Explain each file you create.

### Session 3: Thesis → paper project (new repo: `lateblight-paper`)
> Set up a clean, reproducible project for my MSc thesis paper on early detection of potato late blight from UAV multispectral images with machine learning (250 varieties; macro-F1 was ~0.4). Create folders (data/raw, data/processed, notebooks, src, results, figures), an environment.yml, a README, and EMPTY but well-commented script templates for: (1) counting images per class/variety/plot; (2) grouped cross-validation by plot so there's no data leakage; (3) a vegetation-index baseline model; (4) a ResNet transfer-learning comparison with 3 seeds and confidence intervals. Leave TODOs where I must write the core code, and explain what each script must do and why. Don't invent any results or data.

### Session 4: Portfolio website (new repo named exactly `halireena.github.io`)
> Create a Quarto website for my portfolio (pages: About, Projects, Blog, CV) that publishes to GitHub Pages at https://halireena.github.io. Add one example project page template (question → data → methods → 2 figures → what I learned → GitHub link) and one blog post template. Add a GitHub Action that renders and publishes on every push. Write a step-by-step HOW_TO_EDIT.md for a beginner: how to add a project page, a blog post and an image, and how to preview locally with `quarto preview`.

### Session 5 onwards: Weekly code review (any repo, about once a week)
> Review only the commits I pushed this week, as a strict but kind teacher. List bugs, unclear names, missing tests and anything that would confuse a reader, and explain WHY for each. Don't rewrite my code. Give me a numbered list of fixes to make myself, easiest first.

### When stuck: paper lab or project help
> I'm doing [Paper Lab 3 / P1 step 3.4] from my Code School. Here's my script and the full error message. First explain what the error means, then give me ONE hint. Show the fix only if I reply "show fix".

**Suggested budget:** sessions 1–4 first (they set you up for months). Use the rest on weekly reviews and stuck moments until 5 November.

## 5. Reviewing a pull request (do this every time)
1. GitHub → your repository → **Pull requests** tab → open the new one.
2. **Files changed** tab: green lines are added, red lines removed. Read every file. If a line confuses you, click the **＋** next to it and write a question, then ask it in the session.
3. Check the **checks** at the bottom: a green ✓ means the tests passed.
4. Happy? Click **Merge pull request** → **Confirm merge**. Not happy? Leave a comment, or close it. Nothing changes in your main code until you merge.
5. On your Mac, GitHub Desktop → **Fetch origin** → **Pull** to get the merged version.

## 6. Safety rules
- **Never** paste passwords, tokens or API keys into a prompt.
- Keep data you don't own (unpublished thesis data, other people's emails) out of public repos. Use a **private** repo for thesis data. Pages isn't needed for that, so it's free.
- Read what it changed before merging. You're the scientist in charge; it's the assistant.

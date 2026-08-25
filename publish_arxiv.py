#!/usr/bin/env python3
"""
publish_arxiv.py — mirror the newest arXiv agentic-AI digest into the public
research-journal site and push to GitHub Pages.

- Reads the newest dated digest from the researcher profile's memory tree.
- Regenerates the HTML block between <!-- ARXIV:START --> / <!-- ARXIV:END -->
  in deep-research.html (idempotent: stable output, only commits on change).
- Commits + pushes if the rendered HTML changed.
Stdlib only. Designed to run as a Hermes cron (no_agent / script mode).
"""
import os, re, subprocess, sys, datetime

HOME = os.path.expanduser("~")
DIGEST_DIR = os.path.join(HOME, "AppData", "Local", "hermes", "profiles",
                           "researcher", "memories", "research_digest")
SITE = os.path.join(HOME, "research-journal")
HTML = os.path.join(SITE, "deep-research.html")
REPO = "thabs1234/research-journal"
START, END = "<!-- ARXIV:START -->", "<!-- ARXIV:END -->"

def newest_digest():
    files = [f for f in os.listdir(DIGEST_DIR) if re.match(r"arxiv_\d{4}-\d{2}-\d{2}\.md$", f)]
    if not files:
        return None
    files.sort(reverse=True)
    return os.path.join(DIGEST_DIR, files[0])

def parse_papers(path):
    txt = open(path, encoding="utf-8").read()
    # Each paper: ## Title\n- **Published:** .. **Authors:** ..\n- **Link:** ..\n- summary...
    papers = []
    for block in re.findall(r"## (.+?)\n- \*\*Published:\*\* (.+?)  \*\*Authors:\*\* (.+?)\n- \*\*Link:\*\* (.+?)\n- (.+?)\.\.\.", txt, re.S):
        title, pub, auth, link, summ = (b.strip() for b in block)
        papers.append({"title": title, "pub": pub, "auth": auth, "link": link, "summ": summ})
    return papers

def render(papers):
    out = []
    for p in papers:
        aid = p["link"].rsplit("/", 1)[-1]
        out.append(
            f'  <div class="paper">\n'
            f'    <b>{p["title"]}</b> — {p["auth"]} · <a href="{p["link"]}">{aid}</a>\n'
            f'    <div class="src">{p["summ"]}</div>\n'
            f'  </div>'
        )
    return "\n".join(out)

def main():
    dig = newest_digest()
    if not dig:
        print("PUBLISH ARXIV: no digest found — skipping")
        return 0
    papers = parse_papers(dig)
    if not papers:
        print("PUBLISH ARXIV: digest empty — skipping")
        return 0

    html = open(HTML, encoding="utf-8").read()
    block = render(papers)
    new_html = re.sub(re.escape(START) + r".*?" + re.escape(END),
                      START + "\n" + block + "\n  " + END, html, flags=re.S)
    if new_html == html:
        print("PUBLISH ARXIV: no change — already published")
        return 0

    open(HTML, "w", encoding="utf-8").write(new_html)
    # keep /source in sync
    import shutil
    dated = os.path.basename(dig)
    shutil.copy(dig, os.path.join(SITE, "source", "deep", dated))

    subprocess.run(["git", "-C", SITE, "add", "-A"], check=True)
    msg = f"Auto-publish arXiv digest {dated.replace('arxiv_','').replace('.md','')}"
    r = subprocess.run(["git", "-C", SITE, "commit", "-q", "-m", msg])
    if r.returncode != 0:
        print("PUBLISH ARXIV: commit had nothing to commit")
        return 0
    subprocess.run(["git", "-C", SITE, "push", "-q", "origin", "main"], check=True)
    print(f"PUBLISH ARXIV: pushed {len(papers)} papers from {dated}")
    return 0

if __name__ == "__main__":
    sys.exit(main())

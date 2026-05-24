#!/usr/bin/env python3
"""LWW Textbook Hub Meta Generator"""
import os, base64, requests
from datetime import datetime, timezone

AFF       = "https://www.linkconnector.com/ta.php?lc=014538024578003224&atid=ShopLWW-Web&lcpt=0&lcpf=0"
SITE_NAME = "LWW Textbook Hub"
BRAND     = "LWW Textbook Hub"
SITE_URL  = "https://brightlane.github.io/Lww-Textbook-Hubs"
SITE_DESC = "LWW nursing and medical textbook reviews and affiliate deals. Nursing Drug Handbook, BRS, Illustrated Reviews, NCLEX and USMLE prep books. LinkConnector affiliate lc=014538024578003224."
GH_USER   = os.environ.get("GH_USER", "brightlane")
GH_REPO   = os.environ.get("GH_REPO", "Lww-Textbook-Hubs")
GH_TOKEN  = os.environ.get("GITHUB_TOKEN", "")
SITEMAP_LIMIT = 50000
HEADERS = {"Authorization": f"token {GH_TOKEN}", "Accept": "application/vnd.github+json"}
HIGH_PRIORITY = {"index.html","nursing-textbooks.html","medical-books.html","faq.html","usmle.html","nclex.html"}

def get_all_repo_files(path=""):
    url = f"https://api.github.com/repos/{GH_USER}/{GH_REPO}/contents/{path}"
    r = requests.get(url, headers=HEADERS)
    if r.status_code != 200: return []
    files = []
    for item in r.json():
        if item["type"] == "file": files.append(item["path"])
        elif item["type"] == "dir" and not item["name"].startswith("."): files.extend(get_all_repo_files(item["path"]))
    return files

def build_url_list(files):
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    urls = [{"loc": f"{SITE_URL}/", "lastmod": today, "priority": "1.0", "changefreq": "daily"}]
    for f in sorted(files):
        if not f.endswith(".html") or f in ("index.html", "404.html"): continue
        if f.startswith("blog/"): p,c = "0.6","monthly"
        elif f == "blog-index.html": p,c = "0.8","daily"
        elif f in HIGH_PRIORITY: p,c = "0.9","weekly"
        else: p,c = "0.75","weekly"
        urls.append({"loc": f"{SITE_URL}/{f}", "lastmod": today, "priority": p, "changefreq": c})
    return urls

def build_sitemap_xml(urls):
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        lines += ["  <url>", f"    <loc>{u['loc']}</loc>", f"    <lastmod>{u['lastmod']}</lastmod>",
                  f"    <changefreq>{u['changefreq']}</changefreq>", f"    <priority>{u['priority']}</priority>", "  </url>"]
    lines.append("</urlset>")
    return "\n".join(lines)

def build_sitemap_index_xml(num):
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for i in range(1, num + 1):
        fname = "sitemap.xml" if i == 1 else f"sitemap{i}.xml"
        lines += ["  <sitemap>", f"    <loc>{SITE_URL}/{fname}</loc>", f"    <lastmod>{today}</lastmod>", "  </sitemap>"]
    lines.append("</sitemapindex>")
    return "\n".join(lines)

def build_robots(num):
    lines = ["User-agent: *", "Allow: /", "Disallow: /data/", "", "# Sitemaps"]
    for i in range(1, num + 1):
        fname = "sitemap.xml" if i == 1 else f"sitemap{i}.xml"
        lines.append(f"Sitemap: {SITE_URL}/{fname}")
    if num > 1: lines.append(f"Sitemap: {SITE_URL}/sitemap-index.xml")
    lines += ["", "# AI Crawlers", f"Sitemap: {SITE_URL}/llms.txt"]
    return "\n".join(lines)

def build_llms(urls):
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    lines = [f"# {SITE_NAME}", f"> {SITE_URL}", "", SITE_DESC, "", f"Updated: {today}", f"Brand: {BRAND}", "",
             "## Affiliate", "- Merchant: LWW (Lippincott Williams & Wilkins / Wolters Kluwer)",
             "- Network: LinkConnector", "- ID: lc=014538024578003224",
             "- atid: ShopLWW-Web", "- lcpt: 0", "- lcpf: 0", f"- URL: {AFF}",
             "", "## Key Books", "- Nursing Drug Handbook ($49.99) — 4,500+ drugs, nursing-specific",
             "- Lippincott Pocket Drug Guide ($39.99) — 3,500 drugs, clinical portable",
             "- BRS Physiology ($45.99) — USMLE Step 1 physiology review",
             "- Illustrated Reviews: Pharmacology ($39.99) — visual pharmacology",
             "- Lippincott Q&A Review for NCLEX ($44.99) — practice questions",
             "- BRS Behavioral Science ($43.99) — USMLE Step 1 behavioral",
             "", "## Main Pages"]
    for u in urls:
        if "/blog/" not in u["loc"] and u["loc"] != f"{SITE_URL}/":
            slug = u["loc"].replace(f"{SITE_URL}/", "")
            lines.append(f"- [{slug}]({u['loc']})")
    lines += ["", "## Blog Posts"]
    blog_urls = [u for u in urls if "/blog/" in u["loc"]]
    if blog_urls:
        for u in blog_urls[-20:]: lines.append(f"- [{u['loc'].split('/blog/')[-1]}]({u['loc']})")
    else:
        lines.append("- Blog posts published daily at 9AM UTC")
    lines += ["", "## Topics", "- LWW nursing textbooks review", "- Nursing Drug Handbook NCLEX prep",
              "- BRS Physiology USMLE Step 1", "- Illustrated Reviews Pharmacology",
              "- Lippincott Pocket Drug Guide clinical", "- Medical school textbooks USMLE",
              "- Nursing school books comparison", "- NCLEX pharmacology preparation"]
    return "\n".join(lines)

def build_404():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Page Not Found | LWW Textbook Hub</title>
<meta name="robots" content="noindex,follow">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0;}}
body{{font-family:'Inter',sans-serif;background:#f9f9f9;color:#333;min-height:100vh;display:flex;flex-direction:column;}}
.disc{{background:#fff3cd;color:#856404;padding:0.6rem;font-size:0.8rem;text-align:center;border-bottom:2px solid #FFD700;}}
nav{{background:#004080;padding:0 1.5rem;display:flex;align-items:center;justify-content:space-between;height:60px;}}
.nav-logo{{color:#fff;font-weight:700;font-size:1.05rem;text-decoration:none;}}
.nav-logo span{{color:#FFD700;}}
.nav-cta{{background:#FFD700;color:#000!important;padding:7px 14px;border-radius:5px;font-weight:700;font-size:0.85rem;text-decoration:none;}}
.main{{flex:1;display:flex;align-items:center;justify-content:center;padding:3rem 1.5rem;text-align:center;}}
.box{{background:#fff;border-radius:10px;padding:3rem 2rem;box-shadow:0 4px 16px rgba(0,0,0,0.08);max-width:540px;width:100%;border:1px solid #eee;}}
.emoji{{font-size:4rem;margin-bottom:1rem;}}
h1{{font-size:1.8rem;font-weight:700;color:#004080;margin-bottom:0.75rem;}}
p{{color:#666;margin-bottom:1.5rem;font-size:0.97rem;}}
.btn{{display:inline-block;padding:10px 22px;border-radius:5px;font-weight:700;font-size:0.9rem;margin:0.4rem;text-decoration:none;transition:transform 0.2s;}}
.btn:hover{{transform:translateY(-2px);}}
.btn-yellow{{background:#FFD700;color:#000;}}
.btn-blue{{background:#004080;color:#fff;}}
.links{{margin-top:1.5rem;display:flex;flex-wrap:wrap;gap:0.5rem;justify-content:center;}}
.link-tag{{background:#e6f0ff;color:#004080;padding:0.3rem 0.8rem;border-radius:20px;font-size:0.82rem;font-weight:600;text-decoration:none;}}
.link-tag:hover{{background:#bfdbff;}}
footer{{background:#004080;color:rgba(255,255,255,0.5);text-align:center;padding:1.2rem;font-size:0.8rem;}}
footer a{{color:#FFD700;text-decoration:none;}}
</style>
</head>
<body>
<div class="disc">🔔 <strong>Disclosure:</strong> Affiliate links to LWW textbooks. Commission at no extra cost.</div>
<nav>
  <a href="{SITE_URL}/index.html" class="nav-logo" style="text-decoration:none;">📚 LWW <span>Textbook</span> Hub</a>
  <a href="{AFF}" class="nav-cta" rel="nofollow sponsored" target="_blank">🛒 Shop LWW</a>
</nav>
<div class="main">
  <div class="box">
    <div class="emoji">📚</div>
    <h1>Page Not Found</h1>
    <p>This page doesn't exist or was moved. Find what you need below.</p>
    <a href="{SITE_URL}/index.html" class="btn btn-blue">← Back to Home</a>
    <a href="{AFF}" class="btn btn-yellow" rel="nofollow sponsored" target="_blank">🛒 Shop LWW →</a>
    <div class="links">
      <a href="{SITE_URL}/nursing-textbooks.html" class="link-tag">Nursing Books</a>
      <a href="{SITE_URL}/medical-books.html" class="link-tag">Medical Books</a>
      <a href="{SITE_URL}/usmle.html" class="link-tag">USMLE</a>
      <a href="{SITE_URL}/nclex.html" class="link-tag">NCLEX</a>
      <a href="{SITE_URL}/comparison.html" class="link-tag">Compare</a>
      <a href="{SITE_URL}/study-tips.html" class="link-tag">Study Tips</a>
      <a href="{SITE_URL}/faq.html" class="link-tag">FAQ</a>
      <a href="{SITE_URL}/blog-index.html" class="link-tag">Blog</a>
    </div>
  </div>
</div>
<footer><p>&copy; 2026 {BRAND} | <a href="{SITE_URL}/disclosure.html">Disclosure</a> | lc=014538024578003224</p></footer>
</body>
</html>"""

def gh_put(path, content, msg):
    url = f"https://api.github.com/repos/{GH_USER}/{GH_REPO}/contents/{path}"
    r = requests.get(url, headers=HEADERS)
    sha = r.json().get("sha") if r.status_code == 200 else None
    payload = {"message": msg, "content": base64.b64encode(content.encode()).decode()}
    if sha: payload["sha"] = sha
    resp = requests.put(url, headers=HEADERS, json=payload)
    print(f"{'✅' if resp.status_code in (200,201) else '❌'} {path} ({resp.status_code}) — {len(content):,} chars")

if __name__ == "__main__":
    print(f"🔍 Scanning {GH_USER}/{GH_REPO}...")
    all_files = get_all_repo_files()
    html_files = [f for f in all_files if f.endswith(".html") and f != "404.html"]
    print(f"📄 Found {len(html_files)} HTML files")
    urls = build_url_list(html_files)
    total = len(urls)
    chunks = [urls[i:i+SITEMAP_LIMIT] for i in range(0, max(total,1), SITEMAP_LIMIT)]
    num = len(chunks)
    for i, chunk in enumerate(chunks):
        fname = "sitemap.xml" if i == 0 else f"sitemap{i+1}.xml"
        gh_put(fname, build_sitemap_xml(chunk), f"Meta: {fname} ({len(chunk)} URLs)")
    if num > 1: gh_put("sitemap-index.xml", build_sitemap_index_xml(num), "Meta: sitemap-index.xml")
    gh_put("robots.txt", build_robots(num), "Meta: robots.txt")
    gh_put("llms.txt",   build_llms(urls),  "Meta: llms.txt")
    gh_put("404.html",   build_404(),       "Meta: 404.html")
    print(f"\n✅ Done! {num} sitemap(s) + robots.txt + llms.txt + 404.html | {total} URLs")

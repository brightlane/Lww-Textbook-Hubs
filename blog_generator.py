#!/usr/bin/env python3
"""LWW Textbook Hub Daily Blog Generator"""

import os, json, base64, requests
from datetime import datetime, timezone

AFF        = "https://www.linkconnector.com/ta.php?lc=014538024578003224&atid=ShopLWW-Web&lcpt=0&lcpf=0"
SITE_URL   = "https://brightlane.github.io/Lww-Textbook-Hubs"
GH_USER    = os.environ.get("GH_USER", "brightlane")
GH_REPO    = os.environ.get("GH_REPO", "Lww-Textbook-Hubs")
GH_TOKEN   = os.environ.get("GITHUB_TOKEN", "")
BLOG_INDEX = "blog-index.json"
BRAND      = "LWW Textbook Hub"

HEADERS = {"Authorization": f"token {GH_TOKEN}", "Accept": "application/vnd.github+json"}

CSS = """
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
body{font-family:'Inter',sans-serif;background:#f9f9f9;color:#333;line-height:1.7;}
a{color:#1a73e8;text-decoration:none;}a:hover{text-decoration:underline;}
.disc{background:#fff3cd;color:#856404;padding:0.6rem 1rem;font-size:0.82rem;text-align:center;border-bottom:2px solid #FFD700;}
nav{background:#004080;padding:0 1.5rem;display:flex;align-items:center;justify-content:space-between;height:56px;}
.nav-logo{color:#fff;font-weight:700;font-size:1.05rem;text-decoration:none;}
.nav-logo span{color:#FFD700;}
.nav-cta{background:#FFD700;color:#000!important;padding:6px 14px;border-radius:5px;font-weight:700;font-size:0.85rem;text-decoration:none;}
.container{max-width:820px;margin:0 auto;padding:2rem 1.5rem;background:#fff;min-height:60vh;}
.meta{color:#888;font-size:0.85rem;margin-bottom:1.5rem;}
h1{font-size:clamp(1.6rem,4vw,2.3rem);font-weight:700;color:#004080;margin-bottom:0.75rem;line-height:1.2;}
h2{font-size:1.2rem;font-weight:700;color:#004080;margin:2rem 0 0.75rem;border-bottom:2px solid #f0f0f0;padding-bottom:5px;}
p{margin-bottom:1rem;color:#444;font-size:0.97rem;}
.btn{display:inline-block;padding:10px 22px;background:#FFD700;color:#000;border-radius:5px;font-weight:700;font-size:0.93rem;margin:1rem 0;text-decoration:none;}
.btn:hover{background:#e6c200;text-decoration:none;}
.tip-box{background:#e6f0ff;border-left:5px solid #004080;padding:1rem 1.2rem;border-radius:0 8px 8px 0;margin:1.5rem 0;}
.highlight{background:#fff3cd;border-left:5px solid #FFD700;padding:1rem 1.2rem;border-radius:0 8px 8px 0;margin:1.5rem 0;}
.sticky{position:fixed;bottom:0;width:100%;background:#004080;text-align:center;padding:9px;z-index:999;}
.sticky a{color:#FFD700;font-weight:700;font-size:0.85rem;text-decoration:none;}
footer{background:#004080;color:rgba(255,255,255,0.5);text-align:center;padding:1.5rem;font-size:0.8rem;margin-top:3rem;}
footer a{color:#FFD700;text-decoration:none;}
"""

POSTS = [
  {
    "title": "LWW Nursing Drug Handbook 2026 — Why Every Nursing Student Needs It",
    "keywords": "LWW Nursing Drug Handbook 2026 review, best nursing pharmacology textbook, NCLEX drug handbook",
    "body": f"""<p>The LWW Nursing Drug Handbook is the most consistently recommended pharmacology reference for nursing students. Here is why it belongs in every nursing student's library.</p>
<h2>What's Inside the Nursing Drug Handbook</h2>
<p>The Nursing Drug Handbook covers 4,500+ trade and generic drugs organized alphabetically. Each entry includes generic and brand names, drug class, pharmacology, indications, dosage (adult and pediatric), adverse effects, interactions, contraindications, and — critically — nursing-specific content that other drug references don't provide.</p>
<h2>Why "Nursing-Specific" Matters</h2>
<p>Nurses don't need to know the same drug information as pharmacists or physicians. They need to know nursing considerations — what to assess before giving a drug, what patient teaching is required, what adverse effects to monitor, and when to hold a dose and call the provider. The Nursing Drug Handbook organizes information around exactly these nursing considerations.</p>
<h2>Why It's Essential for NCLEX</h2>
<p>NCLEX pharmacology questions test nursing judgment around medications — not pharmacokinetics or drug chemistry. The Nursing Drug Handbook's nursing-focused organization aligns perfectly with how NCLEX tests pharmacology knowledge. Students who use it consistently report higher pharmacology performance on NCLEX.</p>
<div class="tip-box"><strong>Study tip:</strong> Don't try to memorize every drug. Use the handbook to learn drug categories systematically — beta-blockers, ACE inhibitors, diuretics, anticoagulants, etc. Category knowledge transfers to any drug within the class.</div>
<p style="text-align:center;"><a href="{AFF}" class="btn" rel="nofollow sponsored" target="_blank">🛒 Buy the Nursing Drug Handbook →</a></p>"""},
  {
    "title": "BRS Physiology for USMLE Step 1 — Complete Guide",
    "keywords": "BRS Physiology USMLE Step 1 review, BRS Physiology 2026, best physiology book Step 1",
    "body": f"""<p>BRS Physiology is consistently among the top two or three resources recommended for USMLE Step 1 physiology preparation. Here is why and how to use it effectively.</p>
<h2>What BRS Physiology Covers</h2>
<p>BRS (Board Review Series) Physiology covers all systems: cardiovascular, pulmonary, renal, gastrointestinal, endocrine, reproductive, and neurophysiology. Each chapter presents the high-yield content in an organized, concise format designed specifically for board exam review.</p>
<h2>Why BRS Works for Step 1</h2>
<p>Step 1 physiology questions typically test mechanisms and clinical correlations — not textbook minutiae. BRS Physiology cuts directly to the mechanisms that appear on boards, with clinical vignettes and USMLE-style practice questions at the end of each chapter.</p>
<h2>How to Use BRS Physiology Effectively</h2>
<p>BRS is a review book, not a primary resource. The optimal approach: use your medical school physiology course as the foundation, then use BRS in the 6-8 weeks before Step 1 as your review tool. Read each chapter, answer all practice questions, and review every explanation.</p>
<h2>BRS vs Other Physiology Resources</h2>
<p>BRS Physiology is more concise than Guyton but more detailed than most other board review books. For most Step 1 students, BRS provides the right level of depth — comprehensive enough to be a complete review, concise enough to be readable in the dedicated study period.</p>
<p style="text-align:center;"><a href="{AFF}" class="btn" rel="nofollow sponsored" target="_blank">🛒 Buy BRS Physiology →</a></p>"""},
  {
    "title": "Illustrated Reviews: Pharmacology — Best LWW Book for Visual Learners",
    "keywords": "Illustrated Reviews Pharmacology LWW review, visual pharmacology USMLE, best pharmacology book nursing",
    "body": f"""<p>Illustrated Reviews: Pharmacology by LWW is the go-to pharmacology review for students who learn better from visual presentations than dense text. Here is what makes it effective.</p>
<h2>The Visual Learning Advantage</h2>
<p>Pharmacology is notorious for being difficult to memorize from text alone. Drug mechanisms, receptor interactions, and metabolic pathways are inherently spatial concepts. The illustrated format of LWW's Pharmacology review presents these concepts as flow charts, receptor diagrams, and color-coded tables that make abstract mechanisms concrete and memorable.</p>
<h2>What's Different About the Illustrated Format</h2>
<p>Traditional pharmacology textbooks organize drugs by mechanism or class with dense prose explanations. Illustrated Reviews uses: color-coded tables for adverse effects, flow charts for metabolic pathways, receptor diagrams showing drug binding sites, mnemonic boxes for difficult drug names, and side-by-side comparison tables for drug classes.</p>
<h2>Who Benefits Most</h2>
<p>Visual learners who struggle with dense textbook prose will find this book transformative. It's also excellent as a supplementary resource for students using First Aid — the illustrated format reinforces First Aid's high-yield content with memorable visual anchors.</p>
<h2>NCLEX and USMLE Applications</h2>
<p>Illustrated Reviews: Pharmacology covers the pharmacology content that appears on both NCLEX and USMLE Step 1. The visual format improves both initial learning and long-term retention — two factors that directly improve exam performance.</p>
<p style="text-align:center;"><a href="{AFF}" class="btn" rel="nofollow sponsored" target="_blank">🛒 Buy Illustrated Reviews: Pharmacology →</a></p>"""},
  {
    "title": "NCLEX Pharmacology — How to Use LWW Books to Master Drug Questions",
    "keywords": "NCLEX pharmacology 2026 guide, how to study NCLEX drugs, LWW nursing drug handbook NCLEX",
    "body": f"""<p>Pharmacology accounts for 12-18% of NCLEX questions — and is the topic most nursing students report feeling least prepared for. Here is how to use LWW resources to master NCLEX pharmacology.</p>
<h2>Understand What NCLEX Actually Tests</h2>
<p>NCLEX pharmacology questions test nursing judgment, not drug chemistry. They ask: when do you give this drug, when do you hold it, what do you assess before giving it, what patient teaching is required, and what adverse effects require immediate action. This is exactly the content the Nursing Drug Handbook organizes around.</p>
<h2>The High-Alert Medication Priority List</h2>
<p>NCLEX heavily tests high-alert medications. Prioritize: anticoagulants (heparin, warfarin, DOACs), insulin, digoxin, chemotherapy agents, high-dose opioids, and antiepileptics. Use the Nursing Drug Handbook to systematically study each category's nursing considerations.</p>
<h2>Category-Based Learning Beats Drug-by-Drug Memorization</h2>
<p>You cannot memorize 4,500 drugs before NCLEX — and you don't need to. Learn drug categories. Every beta-blocker has similar nursing considerations. Every ACE inhibitor has similar adverse effects. The Nursing Drug Handbook's classification system supports category-based learning.</p>
<h2>Practice Questions After Every Chapter</h2>
<p>After studying a drug category in the Nursing Drug Handbook, immediately answer 10-15 practice questions on that category from Lippincott's Q&A Review. The question-feedback loop converts textbook knowledge into the clinical judgment NCLEX requires.</p>
<p style="text-align:center;"><a href="{AFF}" class="btn" rel="nofollow sponsored" target="_blank">🛒 Get the Nursing Drug Handbook →</a></p>"""},
  {
    "title": "Lippincott Pocket Drug Guide — The Clinical Rotation Essential",
    "keywords": "Lippincott Pocket Drug Guide review, nursing clinical rotation book, portable drug reference nursing",
    "body": f"""<p>The Lippincott Pocket Drug Guide is the compact companion to the full Nursing Drug Handbook. Here is why it belongs in your scrub pocket during every clinical rotation.</p>
<h2>What the Pocket Drug Guide Contains</h2>
<p>The Pocket Drug Guide covers 3,500+ essential drugs — the drugs you'll actually encounter on clinical rotations. Each entry includes: drug name and class, mechanism of action, indications, key dosing, major adverse effects, nursing considerations, and critical patient teaching points. All in a format small enough to fit in a coat pocket.</p>
<h2>Why Pocket Size Matters in Clinical</h2>
<p>Clinical rotations move fast. You don't have time to look up a drug in a 1,200-page handbook between patient care tasks. The Pocket Drug Guide puts the critical information — what you need to know right now — in a fast-lookup format that doesn't interrupt patient care.</p>
<h2>Pocket Guide vs Smartphone Apps</h2>
<p>Many students use smartphone apps for clinical drug reference. The Pocket Drug Guide provides nursing-specific content that most apps don't — nursing considerations, assessment parameters, and patient teaching organized for nursing practice. Apps also require battery and connectivity that's not always available in clinical settings.</p>
<h2>Best of Both Worlds Strategy</h2>
<p>Most experienced nurses use both the full Nursing Drug Handbook for comprehensive studying and the Pocket Guide for quick clinical lookups. The full handbook for exam prep and understanding, the pocket guide for fast bedside reference.</p>
<p style="text-align:center;"><a href="{AFF}" class="btn" rel="nofollow sponsored" target="_blank">🛒 Buy Lippincott Pocket Drug Guide →</a></p>"""},
  {
    "title": "BRS vs Illustrated Reviews — Which LWW Series Is Right for USMLE?",
    "keywords": "BRS vs Illustrated Reviews USMLE, LWW board review series comparison, best USMLE review books",
    "body": f"""<p>LWW publishes two major board review series: BRS (Board Review Series) and Illustrated Reviews. Here is how they compare and which one to choose for each subject.</p>
<h2>What BRS Books Are</h2>
<p>The Board Review Series (BRS) is LWW's text-based board review line. Each BRS book covers its subject comprehensively with clear prose explanations, organized by physiological system or clinical category. Each chapter ends with USMLE-style practice questions.</p>
<h2>What Illustrated Reviews Books Are</h2>
<p>Illustrated Reviews books use extensive visual aids — flow charts, diagrams, color tables, and illustrated drug mechanisms — to explain complex concepts. They're designed for subjects where visual representation significantly aids understanding.</p>
<h2>When to Choose BRS</h2>
<p>BRS is better for: physiology (BRS Physiology is the most recommended Step 1 physiology resource), behavioral science (BRS Behavioral Science is comprehensive for Step 1 psychology/sociology), and any subject where you prefer organized prose over visual presentation.</p>
<h2>When to Choose Illustrated Reviews</h2>
<p>Illustrated Reviews is better for: pharmacology (drug mechanisms are inherently visual), anatomy (spatial concepts benefit from illustration), and biochemistry (metabolic pathways are clearer as flow charts). Also better if you're a visual learner regardless of subject.</p>
<h2>The Optimal Strategy</h2>
<p>Many students use both: BRS for physiology and behavioral science, Illustrated Reviews for pharmacology and anatomy. The two series complement each other — text-based explanations for conceptual understanding, visual aids for mechanism memorization.</p>
<p style="text-align:center;"><a href="{AFF}" class="btn" rel="nofollow sponsored" target="_blank">🛒 Shop BRS and Illustrated Reviews →</a></p>"""},
  {
    "title": "How to Study from LWW Textbooks Efficiently — 8 Proven Strategies",
    "keywords": "how to study LWW textbooks, nursing textbook study strategy, medical school textbook tips",
    "body": f"""<p>LWW textbooks are dense and comprehensive. Here are 8 strategies that turn textbook reading into exam-ready knowledge efficiently.</p>
<h2>8 Strategies for LWW Textbook Study</h2>
<p><strong>1. Preview before reading.</strong> Scan chapter headings, summary boxes, and highlighted terms before reading. This primes your brain to recognize and store key information as you encounter it.</p>
<p><strong>2. Read with a specific question in mind.</strong> "What nursing considerations apply to this drug class?" beats passive reading. Active questions improve retention.</p>
<p><strong>3. Use the Nursing Drug Handbook by category.</strong> Don't read alphabetically. Study by drug class — all beta-blockers together, all ACE inhibitors together. Patterns between drugs cement faster.</p>
<p><strong>4. Answer chapter questions immediately.</strong> Every LWW textbook includes practice questions. Answer them immediately after reading — not after finishing the whole book.</p>
<p><strong>5. Connect drug mechanisms to pharmacology.</strong> When studying the Nursing Drug Handbook, always ask why — why is this drug contraindicated in heart failure? Understanding the mechanism makes nursing considerations logical rather than memorized.</p>
<p><strong>6. Highlight nursing considerations specifically.</strong> Don't highlight everything. Mark only what nursing-specific content you need to know for practice — assessment, patient teaching, when to hold.</p>
<p><strong>7. Review highlighted content before exams.</strong> Your highlighted nursing considerations become your rapid pre-exam review guide.</p>
<p><strong>8. Use BRS and Illustrated Reviews as review, not primary texts.</strong> These are board review books. Use them to consolidate, not to learn from scratch.</p>
<p style="text-align:center;"><a href="{AFF}" class="btn" rel="nofollow sponsored" target="_blank">🛒 Get Your LWW Textbooks →</a></p>"""},
  {
    "title": "Taylor's Fundamentals of Nursing — Complete Review for Nursing Students",
    "keywords": "Taylor's Fundamentals of Nursing review, LWW fundamentals textbook, best nursing fundamentals book",
    "body": f"""<p>Taylor's Fundamentals of Nursing is the most commonly used LWW fundamentals textbook for first-year nursing students. Here is what makes it the recommended choice.</p>
<h2>What Taylor's Fundamentals Covers</h2>
<p>Taylor's covers the foundational nursing concepts required in every nursing program: patient-centered care, clinical reasoning, nursing process, evidence-based practice, safety, communication, medication administration, and fundamental clinical skills. It's designed to take students from zero nursing knowledge to clinical readiness.</p>
<h2>Why It's Recommended Over Alternatives</h2>
<p>Taylor's organization around clinical reasoning and patient-centered care aligns with how modern nursing practice — and NCLEX — expect nurses to think. Rather than presenting nursing as a collection of procedures, Taylor's frames everything through the clinical judgment lens that NCLEX now explicitly tests.</p>
<h2>How to Use Taylor's Effectively</h2>
<p>Taylor's is a primary learning text — use it to understand nursing concepts deeply before clinical rotations. Pay special attention to the nursing process sections and clinical judgment exercises. These directly map to NCLEX clinical judgment scenarios.</p>
<h2>Pairing Taylor's with Other LWW Resources</h2>
<p>Taylor's Fundamentals pairs naturally with the Nursing Drug Handbook (for medication administration modules) and Lippincott's Q&A Review (for NCLEX-style practice questions after each fundamentals unit).</p>
<p style="text-align:center;"><a href="{AFF}" class="btn" rel="nofollow sponsored" target="_blank">🛒 Buy Taylor's Fundamentals of Nursing →</a></p>"""},
  {
    "title": "LWW Nursing Textbooks vs Amazon — Where to Buy for Best Price",
    "keywords": "where to buy LWW nursing textbooks cheapest, LWW textbook deals, nursing textbook prices",
    "body": f"""<p>LWW textbooks are available through multiple channels. Here is an honest comparison of where to buy for the best price and which channel to choose.</p>
<h2>LWW Official Store (shop.lww.com)</h2>
<p>Buying directly through the LWW official store (which is where our affiliate links go) gives you access to: current editions guaranteed, bundle deals on multiple books, print + digital combinations, and student discount programs. The official store frequently offers sales on nursing and medical textbooks.</p>
<h2>Amazon</h2>
<p>Amazon offers competitive pricing on LWW textbooks and often has used or rental options that reduce cost. The tradeoff is that used books may be older editions — critical for the Nursing Drug Handbook, which is updated annually.</p>
<h2>Campus Bookstores</h2>
<p>Highest prices, zero benefit for most students. The markup at campus bookstores typically adds 20-40% over online options without additional value.</p>
<h2>Digital Editions</h2>
<p>LWW offers digital editions of most textbooks that are significantly cheaper than print. Digital versions allow search functionality that's particularly useful for the Nursing Drug Handbook — you can search by drug name rather than alphabetical browsing.</p>
<h2>Our Recommendation</h2>
<p>The LWW official store for current editions, especially the Nursing Drug Handbook (where edition currency matters most). Our affiliate links go directly to the LWW store — your purchase supports this site at no extra cost.</p>
<p style="text-align:center;"><a href="{AFF}" class="btn" rel="nofollow sponsored" target="_blank">🛒 Shop LWW Official Store →</a></p>"""},
  {
    "title": "Brunner & Suddarth's Medical-Surgical Nursing — The Essential LWW Med-Surg Textbook",
    "keywords": "Brunner Suddarth medical surgical nursing review, best med-surg nursing textbook, LWW med-surg",
    "body": f"""<p>Brunner & Suddarth's Medical-Surgical Nursing is the definitive med-surg nursing textbook used in nursing programs worldwide. Here is what makes it the standard reference for adult health nursing.</p>
<h2>Why Brunner & Suddarth is the Standard</h2>
<p>Brunner & Suddarth has been the reference standard for medical-surgical nursing for over 50 years. Each edition integrates current evidence-based practice, clinical reasoning exercises, and NCLEX-style questions throughout. It's the book that prepares nursing students for the complexity of adult health conditions across every system.</p>
<h2>What the Book Covers</h2>
<p>Every major adult health condition by system: cardiovascular, respiratory, neurological, gastrointestinal, renal, endocrine, oncology, musculoskeletal, and more. Each condition is covered with: pathophysiology, clinical manifestations, diagnostic evaluation, nursing management, and patient education — the complete nursing framework.</p>
<h2>Brunner & Suddarth and NCLEX</h2>
<p>NCLEX's medical-surgical content reflects Brunner & Suddarth's organization. Students who know Brunner & Suddarth know the clinical content NCLEX tests. The book's nursing process focus aligns with NCLEX's clinical judgment framework.</p>
<h2>How to Use It Effectively</h2>
<p>Brunner & Suddarth is too comprehensive to read cover-to-cover in a semester. Use it by system alongside your clinical rotations — study cardiac nursing during your cardiac rotation, respiratory nursing during pulmonary rotation. Active alignment with clinical experience dramatically improves retention.</p>
<p style="text-align:center;"><a href="{AFF}" class="btn" rel="nofollow sponsored" target="_blank">🛒 Buy Brunner & Suddarth →</a></p>"""},
]

while len(POSTS) < 30:
    POSTS.append(POSTS[len(POSTS) % 10])

NAV = f"""<nav>
  <a href="{SITE_URL}/index.html" class="nav-logo" style="text-decoration:none;">📚 LWW <span>Textbook</span> Hub</a>
  <a href="{AFF}" class="nav-cta" rel="nofollow sponsored" target="_blank">🛒 Shop LWW</a>
</nav>"""

STICKY = f'<div class="sticky"><a href="{AFF}" rel="nofollow sponsored" target="_blank">📚 Shop LWW Nursing & Medical Textbooks — Official Affiliate</a></div>'

def build_post_html(post, slug, date_str):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{post['title']} | LWW Textbook Hub</title>
<meta name="description" content="{post['keywords']}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{SITE_URL}/blog/{slug}">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<div class="disc">🔔 <strong>Affiliate Disclosure:</strong> Contains affiliate links to LWW textbooks via LinkConnector (lc=014538024578003224). Commission earned at no extra cost.</div>
{NAV}
<div class="container">
  <p class="meta">Published {date_str} &mdash; <a href="{SITE_URL}/blog-index.html">← All Posts</a> &mdash; by {BRAND}</p>
  <h1>{post['title']}</h1>
  {post['body']}
  <div style="border:1px solid #eee;padding:1.2rem;margin-top:2rem;border-radius:8px;background:#f5f8ff;">
    <strong>About LWW Textbook Hub</strong><br>
    Independent reviews and affiliate deals for LWW nursing and medical textbooks. LinkConnector affiliate lc=014538024578003224.
  </div>
  <p style="text-align:center;margin-top:2rem;">
    <a href="{AFF}" class="btn" rel="nofollow sponsored" target="_blank">🛒 Shop LWW Textbooks →</a>
  </p>
</div>
<footer><p>&copy; 2026 {BRAND} | <a href="{SITE_URL}/disclosure.html">Affiliate Disclosure</a> | lc=014538024578003224</p></footer>
{STICKY}
</body>
</html>"""

def gh_put(path, content, message):
    url = f"https://api.github.com/repos/{GH_USER}/{GH_REPO}/contents/{path}"
    r = requests.get(url, headers=HEADERS)
    sha = r.json().get("sha") if r.status_code == 200 else None
    payload = {"message": message, "content": base64.b64encode(content.encode()).decode()}
    if sha:
        payload["sha"] = sha
    resp = requests.put(url, headers=HEADERS, json=payload)
    print(f"{'✅' if resp.status_code in (200,201) else '❌'} {path} ({resp.status_code})")

def load_blog_index():
    url = f"https://api.github.com/repos/{GH_USER}/{GH_REPO}/contents/{BLOG_INDEX}"
    r = requests.get(url, headers=HEADERS)
    if r.status_code == 200:
        return json.loads(base64.b64decode(r.json()["content"]).decode())
    return []

def save_blog_index(data):
    url = f"https://api.github.com/repos/{GH_USER}/{GH_REPO}/contents/{BLOG_INDEX}"
    r = requests.get(url, headers=HEADERS)
    sha = r.json().get("sha") if r.status_code == 200 else None
    payload = {"message": f"Blog index {datetime.utcnow().strftime('%Y-%m-%d')}",
               "content": base64.b64encode(json.dumps(data, indent=2).encode()).decode()}
    if sha:
        payload["sha"] = sha
    requests.put(url, headers=HEADERS, json=payload)

def build_blog_index_html(posts):
    items = "".join(f'<li style="margin-bottom:0.75rem;"><a href="{p["url"]}">{p["title"]}</a> <small style="color:#888;">({p["date"]})</small></li>' for p in reversed(posts[-30:]))
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>LWW Nursing & Medical Textbook Blog 2026 | LWW Textbook Hub</title>
<meta name="description" content="LWW textbook reviews, nursing study tips, NCLEX and USMLE prep guides. Updated daily.">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<style>{CSS}
.hero{{background:#004080;color:#fff;text-align:center;padding:3rem 1.5rem;}}
.hero h1{{font-size:2rem;font-weight:700;margin-bottom:0.5rem;}}
.hero h1 span{{color:#FFD700;}}
</style>
</head>
<body>
<div class="disc">🔔 <strong>Disclosure:</strong> Affiliate links to LWW textbooks via LinkConnector. Commission at no extra cost.</div>
{NAV}
<div class="hero"><h1>📚 LWW <span>Textbook</span> Hub Blog</h1><p style="color:rgba(255,255,255,0.85);">LWW textbook reviews, nursing study tips, and NCLEX/USMLE prep guides. Updated daily.</p></div>
<div class="container">
  <h2 style="color:#004080;margin-bottom:1.5rem;border-bottom:2px solid #eee;padding-bottom:8px;">Latest Posts</h2>
  <ul style="list-style:none;padding:0;">{items}</ul>
</div>
<footer><p>&copy; 2026 {BRAND} | <a href="{SITE_URL}/disclosure.html">Disclosure</a> | lc=014538024578003224</p></footer>
{STICKY}
</body>
</html>"""

if __name__ == "__main__":
    now = datetime.now(timezone.utc)
    date_str = now.strftime("%B %d, %Y")
    day_num = now.timetuple().tm_yday % len(POSTS)
    post = POSTS[day_num]
    slug_base = post["title"].lower()
    for ch in " :,&'\"?!.—":
        slug_base = slug_base.replace(ch, "-")
    while "--" in slug_base:
        slug_base = slug_base.replace("--", "-")
    slug = slug_base[:60].strip("-") + f"-{now.strftime('%Y-%m-%d')}.html"
    gh_put(f"blog/{slug}", build_post_html(post, slug, date_str), f"Blog: {post['title']}")
    index = load_blog_index()
    index.append({"title": post["title"], "date": date_str, "url": f"blog/{slug}", "slug": slug})
    save_blog_index(index)
    gh_put("blog-index.html", build_blog_index_html(index), f"Blog index — {date_str}")
    print(f"✅ Published: {slug}")

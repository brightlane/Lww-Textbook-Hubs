#!/usr/bin/env python3
"""
Lww-Textbook-Hubs Site Builder
LWW (Lippincott Williams & Wilkins) affiliate — LinkConnector
Repo: brightlane/Lww-Textbook-Hubs
Affiliate: https://www.linkconnector.com/ta.php?lc=014538024578003224&atid=ShopLWW-Web&lcpt=0&lcpf=0
"""

import os, base64, requests
from datetime import datetime

AFF       = "https://www.linkconnector.com/ta.php?lc=014538024578003224&atid=ShopLWW-Web&lcpt=0&lcpf=0"
SITE_NAME = "LWW Textbook Hub"
BRAND     = "LWW Textbook Hub"
SITE_URL  = "https://brightlane.github.io/Lww-Textbook-Hubs"
GH_USER   = os.environ.get("GH_USER", "brightlane")
GH_REPO   = os.environ.get("GH_REPO", "Lww-Textbook-Hubs")
GH_TOKEN  = os.environ.get("GITHUB_TOKEN", "")
GVERIFY   = "eWVDN3vbam9nnaZQu7wAQKyfmJJdM7zjI80l4DGeUrQ"

HEADERS = {
    "Authorization": f"token {GH_TOKEN}",
    "Accept": "application/vnd.github+json"
}

CSS = """
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;}
body{font-family:'Inter',sans-serif;line-height:1.7;color:#333;background:#f9f9f9;}
a{color:#1a73e8;text-decoration:none;}
a:hover{text-decoration:underline;}
.disclosure{background:#fff3cd;color:#856404;text-align:center;padding:0.75rem 1rem;font-size:0.88rem;border-bottom:2px solid #FFD700;}
nav{background:#004080;padding:0 1.5rem;display:flex;align-items:center;justify-content:space-between;height:62px;position:sticky;top:0;z-index:100;box-shadow:0 3px 10px rgba(0,64,128,0.4);}
.nav-logo{color:#fff;font-weight:700;font-size:1.05rem;}
.nav-logo span{color:#FFD700;}
.nav-links{display:flex;gap:1.2rem;}
.nav-links a{color:rgba(255,255,255,0.8);font-size:0.83rem;font-weight:500;transition:color 0.2s;}
.nav-links a:hover{color:#FFD700;text-decoration:none;}
.nav-cta{background:#FFD700;color:#000!important;padding:7px 14px;border-radius:5px;font-weight:700!important;}
.hero{background:#004080;color:#fff;padding:60px 20px;text-align:center;box-shadow:0 4px 16px rgba(0,64,128,0.3);}
.hero h1{font-size:clamp(1.8rem,5vw,3rem);font-weight:700;margin-bottom:1rem;line-height:1.2;}
.hero h1 em{color:#FFD700;font-style:normal;}
.hero p{font-size:1.05rem;color:rgba(255,255,255,0.88);max-width:700px;margin:0 auto 1.5rem;}
.cta{display:inline-block;background:#FFD700;color:#000;padding:10px 22px;border-radius:5px;font-weight:700;transition:all 0.3s;margin:0.3rem;}
.cta:hover{background:#e6c200;transform:translateY(-2px);text-decoration:none;color:#000;}
.cta-lg{padding:14px 32px;font-size:1.1rem;}
.hero-stats{display:flex;justify-content:center;gap:3rem;flex-wrap:wrap;margin-top:2.5rem;}
.stat-num{font-size:2rem;font-weight:700;color:#FFD700;}
.stat-label{font-size:0.75rem;color:rgba(255,255,255,0.55);text-transform:uppercase;letter-spacing:0.08em;}
.container{max-width:1100px;margin:0 auto;padding:2rem 1rem;}
.section{padding:2.5rem 1rem;}
.section-alt{background:#fff;}
.section-title{font-size:clamp(1.4rem,3.5vw,2rem);color:#004080;margin-bottom:1.2rem;font-weight:700;}
.section-title::after{content:'';display:block;width:60px;height:4px;background:#FFD700;margin-top:0.5rem;border-radius:2px;}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));gap:1.5rem;margin:1.5rem 0;}
.card{background:#fff;border-radius:8px;padding:1.5rem;box-shadow:0 2px 10px rgba(0,0,0,0.08);border:1px solid #eee;transition:all 0.3s;}
.card:hover{transform:translateY(-4px);box-shadow:0 8px 20px rgba(0,0,0,0.12);}
.card-icon{font-size:2rem;margin-bottom:0.75rem;}
.card h3{color:#004080;font-size:1rem;margin-bottom:0.5rem;font-weight:700;}
.card p{font-size:0.9rem;color:#555;margin-bottom:1rem;}
.card .price{font-weight:700;font-size:1.1rem;color:#004080;margin-bottom:0.75rem;}
table{width:100%;border-collapse:collapse;margin:1.5rem 0;border-radius:8px;overflow:hidden;box-shadow:0 2px 10px rgba(0,0,0,0.08);}
th,td{padding:12px 14px;text-align:left;border-bottom:1px solid #eee;}
th{background:#004080;color:#fff;font-weight:600;font-size:0.92rem;}
td{font-size:0.92rem;color:#444;}
tr:nth-child(even) td{background:#f5f8ff;}
tr:hover td{background:#fff3cd;}
.daily-tip{background:#e6f0ff;padding:1.5rem;border-left:5px solid #004080;margin-bottom:2rem;border-radius:0 8px 8px 0;}
.daily-tip h3{color:#004080;margin-bottom:0.5rem;}
.highlight{background:#fff3cd;padding:1.2rem;border-left:5px solid #FFD700;margin:1.5rem 0;border-radius:0 8px 8px 0;}
.highlight strong{color:#856404;}
.faqs{display:grid;gap:1rem;}
.faq{border:1px solid #eee;border-radius:8px;overflow:hidden;background:#fff;}
.faq-q{padding:1rem 1.2rem;background:#f5f8ff;font-weight:700;color:#004080;cursor:pointer;}
.faq-a{padding:0 1.2rem 0.9rem;color:#555;font-size:0.95rem;}
.tips-list{display:grid;gap:1rem;}
.tip-item{display:flex;gap:1rem;background:#fff;padding:1rem 1.2rem;border-radius:8px;box-shadow:0 2px 8px rgba(0,0,0,0.06);border-left:4px solid #004080;}
.tip-n{font-size:1.1rem;font-weight:700;color:#004080;min-width:28px;}
.tip-t strong{display:block;font-size:0.92rem;color:#004080;margin-bottom:0.2rem;}
.tip-t span{font-size:0.85rem;color:#666;}
.cta-band{background:#004080;color:#fff;text-align:center;padding:50px 20px;border-radius:8px;margin:2rem 0;}
.cta-band h2{color:#fff;font-size:clamp(1.3rem,3.5vw,2rem);margin-bottom:0.75rem;font-weight:700;}
.cta-band p{color:rgba(255,255,255,0.8);margin-bottom:1.5rem;}
.sticky-bar{position:fixed;bottom:0;width:100%;background:#004080;text-align:center;padding:9px;z-index:999;box-shadow:0 -2px 10px rgba(0,0,0,0.3);}
.sticky-bar a{color:#FFD700;font-weight:700;font-size:0.88rem;}
footer{background:#004080;color:rgba(255,255,255,0.7);text-align:center;padding:2.5rem;font-size:0.88rem;}
footer a{color:#FFD700;}
.fade{opacity:0;transform:translateY(20px);transition:opacity 0.6s ease,transform 0.6s ease;}
.fade.on{opacity:1;transform:none;}
@media(max-width:768px){.nav-links{display:none;}.hero h1{font-size:1.8rem;}}
"""

FONTS = '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">'

JS = """
const faders=document.querySelectorAll('.fade');
function check(){faders.forEach(el=>{if(el.getBoundingClientRect().top<window.innerHeight-60)el.classList.add('on');});}
window.addEventListener('scroll',check);window.addEventListener('load',check);
document.getElementById('yr')&&(document.getElementById('yr').textContent=new Date().getFullYear());
const tips=["Review key pharmacology concepts daily with the LWW Nursing Drug Handbook.","Use Illustrated Reviews to simplify complex anatomy for fast recall.","Highlight high-risk medications and note interactions for quick clinical reference.","Practice NCLEX-style questions alongside your LWW Drug Handbook.","Use BRS Physiology for concise USMLE Step 1 review on the go."];
const el=document.getElementById('daily-tip-text');
if(el){el.textContent=tips[new Date().getDate()%tips.length];}
"""

SCHEMA_BASE = f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Organization",
"name":"LWW Textbook Hub","url":"{SITE_URL}",
"description":"Independent reviews and affiliate deals for LWW nursing textbooks, medical school books, and exam prep resources."
}}</script>"""

def nav_html():
    return f"""<nav>
  <a href="{SITE_URL}/index.html" class="nav-logo">📚 LWW <span>Textbook</span> Hub</a>
  <div class="nav-links">
    <a href="{SITE_URL}/nursing-textbooks.html">Nursing Books</a>
    <a href="{SITE_URL}/medical-books.html">Medical Books</a>
    <a href="{SITE_URL}/usmle.html">USMLE Prep</a>
    <a href="{SITE_URL}/nclex.html">NCLEX</a>
    <a href="{SITE_URL}/comparison.html">Compare</a>
    <a href="{SITE_URL}/faq.html">FAQ</a>
    <a href="{SITE_URL}/blog-index.html">Blog</a>
    <a href="{AFF}" class="nav-cta" rel="nofollow sponsored" target="_blank">🛒 Shop LWW</a>
  </div>
</nav>"""

STICKY_HTML = f'<div class="sticky-bar"><a href="{AFF}" rel="nofollow sponsored" target="_blank">📚 Shop LWW Nursing & Medical Textbooks — Official Affiliate Store</a></div>'

FOOTER_HTML = f"""<footer>
  <p>&copy; <span id="yr"></span> {BRAND} — Independent LWW Affiliate</p>
  <p style="margin-top:0.5rem;">
    <a href="{SITE_URL}/about.html">About</a> &nbsp;|&nbsp;
    <a href="{SITE_URL}/contact.html">Contact</a> &nbsp;|&nbsp;
    <a href="{SITE_URL}/disclosure.html">Disclosure</a> &nbsp;|&nbsp;
    <a href="{SITE_URL}/blog-index.html">Blog</a> &nbsp;|&nbsp;
    <a href="{AFF}" rel="nofollow sponsored" target="_blank">Shop LWW</a>
  </p>
  <p style="margin-top:0.75rem;font-size:0.82rem;color:rgba(255,255,255,0.5);">Affiliate Disclaimer: Contains affiliate links to LWW textbooks via LinkConnector (lc=014538024578003224). Commission earned at no extra cost.</p>
</footer>"""

def page(title, desc, slug, body, schema=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="google-site-verification" content="{GVERIFY}">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE_URL}/{slug}">
<title>{title}</title>
<link rel="canonical" href="{SITE_URL}/{slug}">
{FONTS}
{SCHEMA_BASE}
{schema}
<style>{CSS}</style>
</head>
<body>
<div class="disclosure">🔔 <strong>Affiliate Disclosure:</strong> Contains affiliate links to LWW textbooks via LinkConnector. Commission earned at no extra cost to you.</div>
{nav_html()}
{body}
{FOOTER_HTML}
{STICKY_HTML}
<script>{JS}</script>
</body>
</html>"""

def cta_band(h2="Shop LWW Textbooks Today", p="Trusted nursing and medical textbooks for exam success. Official LWW affiliate store."):
    return f"""<div class="cta-band fade">
  <h2>{h2}</h2>
  <p>{p}</p>
  <a href="{AFF}" class="cta cta-lg" rel="nofollow sponsored" target="_blank">🛒 Shop LWW Now →</a>
</div>"""

BOOK_TABLE = f"""<div style="overflow-x:auto;">
<table>
  <thead><tr><th>Book</th><th>Best For</th><th>Pages</th><th>Price</th><th>Buy</th></tr></thead>
  <tbody>
    <tr><td><strong>Nursing Drug Handbook</strong></td><td>NCLEX, pharmacology, clinical</td><td>1,200+</td><td>$49.99</td><td><a href="{AFF}" class="cta" rel="nofollow sponsored" target="_blank">Buy Now</a></td></tr>
    <tr><td><strong>Lippincott Pocket Drug Guide</strong></td><td>Clinical rotations, quick reference</td><td>800</td><td>$39.99</td><td><a href="{AFF}" class="cta" rel="nofollow sponsored" target="_blank">Buy Now</a></td></tr>
    <tr><td><strong>BRS Physiology</strong></td><td>USMLE Step 1, physiology review</td><td>400</td><td>$45.99</td><td><a href="{AFF}" class="cta" rel="nofollow sponsored" target="_blank">Buy Now</a></td></tr>
    <tr><td><strong>Illustrated Reviews: Pharmacology</strong></td><td>USMLE, visual learners</td><td>320</td><td>$39.99</td><td><a href="{AFF}" class="cta" rel="nofollow sponsored" target="_blank">Buy Now</a></td></tr>
    <tr><td><strong>Lippincott's Q&A Review for NCLEX</strong></td><td>NCLEX practice questions</td><td>500</td><td>$44.99</td><td><a href="{AFF}" class="cta" rel="nofollow sponsored" target="_blank">Buy Now</a></td></tr>
    <tr><td><strong>BRS Behavioral Science</strong></td><td>USMLE Step 1 behavioral science</td><td>380</td><td>$43.99</td><td><a href="{AFF}" class="cta" rel="nofollow sponsored" target="_blank">Buy Now</a></td></tr>
  </tbody>
</table>
</div>"""

# ══════════════════════════════════════
# PAGES
# ══════════════════════════════════════

def page_index():
    schema = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"What is the best LWW nursing textbook for NCLEX prep?","acceptedAnswer":{"@type":"Answer","text":"The Nursing Drug Handbook is the most recommended for NCLEX prep, covering 4,500+ medications with dosage info, interactions, and clinical warnings."}},
{"@type":"Question","name":"Which LWW books are best for USMLE Step 1?","acceptedAnswer":{"@type":"Answer","text":"BRS Physiology and Illustrated Reviews: Pharmacology are top choices for USMLE Step 1, offering concise explanations and mnemonics for fast recall."}}
]}</script>"""
    body = f"""
<div class="hero">
  <h1>📚 LWW Nursing & Medical <em>Textbooks</em></h1>
  <p>Trusted by students worldwide — reviews, comparisons, and affiliate deals for Nursing Drug Handbook, BRS, Illustrated Reviews, and all LWW exam prep books.</p>
  <a href="{AFF}" class="cta cta-lg" rel="nofollow sponsored" target="_blank">🛒 Shop LWW Textbooks</a>
  <div class="hero-stats">
    <div><div class="stat-num">4,500+</div><div class="stat-label">Drugs in Handbook</div></div>
    <div><div class="stat-num">50+</div><div class="stat-label">Titles Available</div></div>
    <div><div class="stat-num">NCLEX</div><div class="stat-label">& USMLE Ready</div></div>
    <div><div class="stat-num">Official</div><div class="stat-label">LWW Affiliate</div></div>
  </div>
</div>

<div class="container">
<div class="daily-tip">
  <h3>📅 Today's Study Tip</h3>
  <p id="daily-tip-text">Review key pharmacology concepts daily with the LWW Nursing Drug Handbook.</p>
  <a href="{AFF}" rel="nofollow sponsored" target="_blank">Shop LWW books here</a>
</div>

<div class="section-title" style="margin-top:1rem;">🏥 Best Nursing Textbooks & Drug Handbooks</div>
<div class="grid fade">
  <div class="card">
    <div class="card-icon">💊</div>
    <h3><a href="{AFF}" rel="nofollow sponsored" target="_blank">Nursing Drug Handbook</a></h3>
    <p>4,500+ trade/generic drugs. Dosage calculations, IV compatibility, clinical warnings. The #1 pharmacology textbook for nursing school and NCLEX prep.</p>
    <div class="price">$49.99</div>
    <a href="{AFF}" class="cta" rel="nofollow sponsored" target="_blank">Buy Nursing Drug Handbook</a>
  </div>
  <div class="card">
    <div class="card-icon">📋</div>
    <h3><a href="{AFF}" rel="nofollow sponsored" target="_blank">Lippincott Pocket Drug Guide</a></h3>
    <p>3,500+ essential drugs in portable format. Perfect for clinical rotations and hospital shifts. Quick reference at the bedside.</p>
    <div class="price">$39.99</div>
    <a href="{AFF}" class="cta" rel="nofollow sponsored" target="_blank">Buy Pocket Drug Guide</a>
  </div>
  <div class="card">
    <div class="card-icon">📝</div>
    <h3><a href="{AFF}" rel="nofollow sponsored" target="_blank">Lippincott Q&A Review for NCLEX</a></h3>
    <p>Comprehensive NCLEX practice questions with rationales. Covers all test plan categories for both NCLEX-RN and NCLEX-PN.</p>
    <div class="price">$44.99</div>
    <a href="{AFF}" class="cta" rel="nofollow sponsored" target="_blank">Buy NCLEX Q&A Review</a>
  </div>
</div>

<div class="section-title" style="margin-top:2rem;">📚 Top Medical School Books & USMLE Prep</div>
<div class="grid fade">
  <div class="card">
    <div class="card-icon">🫀</div>
    <h3><a href="{AFF}" rel="nofollow sponsored" target="_blank">BRS Physiology</a></h3>
    <p>Comprehensive USMLE Step 1 review in physiology. Essential for med students. Concise explanations and practice questions.</p>
    <div class="price">$45.99</div>
    <a href="{AFF}" class="cta" rel="nofollow sponsored" target="_blank">Shop BRS Physiology</a>
  </div>
  <div class="card">
    <div class="card-icon">🧬</div>
    <h3><a href="{AFF}" rel="nofollow sponsored" target="_blank">Illustrated Reviews: Pharmacology</a></h3>
    <p>Visual USMLE review of pharmacology. Easy-to-follow mnemonics and charts for fast recall. Perfect for visual learners.</p>
    <div class="price">$39.99</div>
    <a href="{AFF}" class="cta" rel="nofollow sponsored" target="_blank">Buy Illustrated Reviews</a>
  </div>
  <div class="card">
    <div class="card-icon">🧠</div>
    <h3><a href="{AFF}" rel="nofollow sponsored" target="_blank">BRS Behavioral Science</a></h3>
    <p>High-yield behavioral science review for USMLE Step 1. Covers psychology, sociology, ethics, and epidemiology concisely.</p>
    <div class="price">$43.99</div>
    <a href="{AFF}" class="cta" rel="nofollow sponsored" target="_blank">Shop BRS Behavioral</a>
  </div>
</div>

<div class="section-title" style="margin-top:2rem;">⚖️ Textbook Comparison</div>
{BOOK_TABLE}

{cta_band("Shop All LWW Textbooks","Official affiliate links. Commission earned at no extra cost to you.")}

<div class="section-title" style="margin-top:2rem;">❓ Frequently Asked Questions</div>
<div class="faqs fade">
  <div class="faq"><div class="faq-q">What is the best LWW nursing textbook for NCLEX prep?</div><div class="faq-a">The <a href="{AFF}" rel="nofollow sponsored" target="_blank">Nursing Drug Handbook</a> is most recommended for NCLEX prep, covering 4,500+ medications with dosage info, interactions, and clinical warnings.</div></div>
  <div class="faq"><div class="faq-q">Which LWW books are best for USMLE Step 1?</div><div class="faq-a">BRS Physiology and Illustrated Reviews: Pharmacology are top choices for USMLE Step 1, offering concise explanations and mnemonics for fast recall.</div></div>
  <div class="faq"><div class="faq-q">Are these affiliate links?</div><div class="faq-a">Yes. All book links are affiliate links via LinkConnector (lc=014538024578003224). Purchasing through these links supports this site at no extra cost to you.</div></div>
</div>
</div>"""
    return page(
        "LWW Nursing & Medical Textbooks | NCLEX & USMLE Prep | LWW Textbook Hub",
        "Explore top LWW nursing textbooks, medical school books, USMLE Step 1 review, and Nursing Drug Handbook. Compare books, read tips, and shop affiliate deals.",
        "index.html", body, schema)

def page_nursing_textbooks():
    body = f"""
<div class="hero">
  <h1>🏥 LWW Nursing Textbooks <em>2026</em></h1>
  <p>The complete guide to LWW nursing textbooks — Nursing Drug Handbook, Pocket Drug Guide, NCLEX review, and more for nursing students and RNs.</p>
  <a href="{AFF}" class="cta cta-lg" rel="nofollow sponsored" target="_blank">🛒 Shop Nursing Textbooks</a>
</div>
<div class="container">
<div class="section-title" style="margin-top:1.5rem;">Top LWW Nursing Books</div>
<div class="grid fade">
  <div class="card"><div class="card-icon">💊</div><h3><a href="{AFF}" rel="nofollow sponsored" target="_blank">Nursing Drug Handbook</a></h3><p>The gold standard nursing drug reference. 4,500+ medications with nursing-specific dosing, interactions, adverse effects, and patient teaching points. Updated annually.</p><div class="price">$49.99</div><a href="{AFF}" class="cta" rel="nofollow sponsored" target="_blank">Buy Now →</a></div>
  <div class="card"><div class="card-icon">📋</div><h3><a href="{AFF}" rel="nofollow sponsored" target="_blank">Lippincott Pocket Drug Guide</a></h3><p>The portable companion to the Nursing Drug Handbook. 3,500+ drugs in a coat-pocket format ideal for clinical rotations. Quick lookup at the point of care.</p><div class="price">$39.99</div><a href="{AFF}" class="cta" rel="nofollow sponsored" target="_blank">Buy Now →</a></div>
  <div class="card"><div class="card-icon">📝</div><h3><a href="{AFF}" rel="nofollow sponsored" target="_blank">Lippincott Q&A Review for NCLEX-RN</a></h3><p>Thousands of NCLEX-style practice questions with detailed rationales. Covers all NCLEX-RN test plan client needs categories. Includes select-all-that-apply and prioritization questions.</p><div class="price">$44.99</div><a href="{AFF}" class="cta" rel="nofollow sponsored" target="_blank">Buy Now →</a></div>
  <div class="card"><div class="card-icon">🩺</div><h3><a href="{AFF}" rel="nofollow sponsored" target="_blank">Taylor's Fundamentals of Nursing</a></h3><p>The comprehensive nursing fundamentals textbook. Patient-centered care, clinical reasoning, evidence-based practice. Essential for first-year nursing students.</p><div class="price">$89.99</div><a href="{AFF}" class="cta" rel="nofollow sponsored" target="_blank">Buy Now →</a></div>
  <div class="card"><div class="card-icon">💉</div><h3><a href="{AFF}" rel="nofollow sponsored" target="_blank">Brunner & Suddarth's Medical-Surgical Nursing</a></h3><p>The definitive medical-surgical nursing textbook. Comprehensive coverage of adult health conditions, nursing interventions, and clinical judgment across all specialties.</p><div class="price">$109.99</div><a href="{AFF}" class="cta" rel="nofollow sponsored" target="_blank">Buy Now →</a></div>
  <div class="card"><div class="card-icon">👶</div><h3><a href="{AFF}" rel="nofollow sponsored" target="_blank">Pillitteri's Maternal & Child Health Nursing</a></h3><p>Comprehensive maternity and pediatric nursing textbook. Evidence-based care for mothers, newborns, and children across the health continuum.</p><div class="price">$94.99</div><a href="{AFF}" class="cta" rel="nofollow sponsored" target="_blank">Buy Now →</a></div>
</div>
{cta_band("Get the Best LWW Nursing Textbooks","All LWW nursing titles available through our official affiliate link.")}
</div>"""
    return page(
        "LWW Nursing Textbooks 2026 — Nursing Drug Handbook & NCLEX Review | LWW Textbook Hub",
        "Best LWW nursing textbooks 2026. Nursing Drug Handbook, Lippincott Pocket Drug Guide, NCLEX Q&A Review, Taylor's Fundamentals, Brunner & Suddarth. Official affiliate.",
        "nursing-textbooks.html", body)

def page_medical_books():
    body = f"""
<div class="hero">
  <h1>📚 LWW Medical School Books <em>2026</em></h1>
  <p>Top LWW medical school textbooks for USMLE Step 1 and 2 preparation — BRS series, Illustrated Reviews, and essential med school references.</p>
  <a href="{AFF}" class="cta cta-lg" rel="nofollow sponsored" target="_blank">🛒 Shop Medical Books</a>
</div>
<div class="container">
<div class="section-title" style="margin-top:1.5rem;">BRS Series — Board Review</div>
<div class="grid fade">
  <div class="card"><div class="card-icon">🫀</div><h3><a href="{AFF}" rel="nofollow sponsored" target="_blank">BRS Physiology</a></h3><p>The most popular physiology board review. Concise explanations, high-yield questions, and USMLE-style cases. Essential for Step 1.</p><div class="price">$45.99</div><a href="{AFF}" class="cta" rel="nofollow sponsored" target="_blank">Shop BRS Physiology →</a></div>
  <div class="card"><div class="card-icon">🧠</div><h3><a href="{AFF}" rel="nofollow sponsored" target="_blank">BRS Behavioral Science</a></h3><p>High-yield behavioral science review covering psychology, sociology, ethics, biostatistics, and epidemiology for USMLE Step 1.</p><div class="price">$43.99</div><a href="{AFF}" class="cta" rel="nofollow sponsored" target="_blank">Shop BRS Behavioral →</a></div>
  <div class="card"><div class="card-icon">🦠</div><h3><a href="{AFF}" rel="nofollow sponsored" target="_blank">BRS Microbiology & Immunology</a></h3><p>Comprehensive microbiology and immunology board review. Bacteriology, virology, mycology, parasitology, and immunology for USMLE.</p><div class="price">$44.99</div><a href="{AFF}" class="cta" rel="nofollow sponsored" target="_blank">Shop BRS Micro →</a></div>
</div>
<div class="section-title" style="margin-top:2rem;">Illustrated Reviews Series</div>
<div class="grid fade">
  <div class="card"><div class="card-icon">🧬</div><h3><a href="{AFF}" rel="nofollow sponsored" target="_blank">Illustrated Reviews: Pharmacology</a></h3><p>Visual pharmacology review with mnemonics, flow charts, and illustrated drug mechanisms. Perfect for visual learners preparing for USMLE.</p><div class="price">$39.99</div><a href="{AFF}" class="cta" rel="nofollow sponsored" target="_blank">Buy Now →</a></div>
  <div class="card"><div class="card-icon">🦴</div><h3><a href="{AFF}" rel="nofollow sponsored" target="_blank">Illustrated Reviews: Anatomy</a></h3><p>Visual anatomy review with full-color illustrations. Clinical correlations and USMLE-style questions make complex anatomy memorable.</p><div class="price">$44.99</div><a href="{AFF}" class="cta" rel="nofollow sponsored" target="_blank">Buy Now →</a></div>
  <div class="card"><div class="card-icon">⚗️</div><h3><a href="{AFF}" rel="nofollow sponsored" target="_blank">Illustrated Reviews: Biochemistry</a></h3><p>Biochemistry for medical students — metabolic pathways, molecular biology, and clinical correlations presented visually for faster learning.</p><div class="price">$41.99</div><a href="{AFF}" class="cta" rel="nofollow sponsored" target="_blank">Buy Now →</a></div>
</div>
{cta_band("Shop All LWW Medical Books","BRS series, Illustrated Reviews, and all USMLE prep titles in one store.")}
</div>"""
    return page(
        "LWW Medical School Books 2026 — BRS & Illustrated Reviews | LWW Textbook Hub",
        "Best LWW medical school books 2026. BRS Physiology, BRS Behavioral Science, Illustrated Reviews Pharmacology and Anatomy. Official affiliate for USMLE prep.",
        "medical-books.html", body)

def page_usmle():
    body = f"""
<div class="hero">
  <h1>🩺 USMLE Prep with <em>LWW Books</em></h1>
  <p>The best LWW textbooks for USMLE Step 1, Step 2 CK, and Step 3 preparation. High-yield, concise, and trusted by med students worldwide.</p>
  <a href="{AFF}" class="cta cta-lg" rel="nofollow sponsored" target="_blank">🛒 Shop USMLE Books</a>
</div>
<div class="container">
<div class="section-title" style="margin-top:1.5rem;">USMLE Step 1 Books</div>
<div class="grid fade">
  <div class="card"><div class="card-icon">🫀</div><h3>BRS Physiology</h3><p>The essential physiology review for Step 1. High-yield summaries, USMLE-style questions, and clinical vignettes. Most consistently recommended Step 1 physiology resource.</p><div class="price">$45.99</div><a href="{AFF}" class="cta" rel="nofollow sponsored" target="_blank">Buy BRS Physiology →</a></div>
  <div class="card"><div class="card-icon">🧬</div><h3>Illustrated Reviews: Pharmacology</h3><p>Visual pharmacology for Step 1. Drug mechanisms, adverse effects, and high-yield charts in an illustrated format that makes pharmacology stick.</p><div class="price">$39.99</div><a href="{AFF}" class="cta" rel="nofollow sponsored" target="_blank">Buy Illustrated Reviews →</a></div>
  <div class="card"><div class="card-icon">🧠</div><h3>BRS Behavioral Science</h3><p>Covers psychology, sociology, epidemiology, biostatistics, and medical ethics — all high-yield Step 1 topics in one concise review.</p><div class="price">$43.99</div><a href="{AFF}" class="cta" rel="nofollow sponsored" target="_blank">Buy BRS Behavioral →</a></div>
</div>
<div class="section-title" style="margin-top:2rem;">USMLE Study Strategy</div>
<div class="tips-list fade">
  <div class="tip-item"><div class="tip-n">01</div><div class="tip-t"><strong>Use BRS series for rapid review</strong><span>BRS books condense each subject to its highest-yield points. Use them for final review, not primary learning.</span></div></div>
  <div class="tip-item"><div class="tip-n">02</div><div class="tip-t"><strong>Illustrated Reviews for pharmacology</strong><span>Drug mechanisms are notoriously hard to memorize. The visual format of Illustrated Reviews significantly improves retention.</span></div></div>
  <div class="tip-item"><div class="tip-n">03</div><div class="tip-t"><strong>Combine textbooks with question banks</strong><span>LWW books provide the conceptual foundation. Add a quality question bank to practice applying that knowledge under exam conditions.</span></div></div>
  <div class="tip-item"><div class="tip-n">04</div><div class="tip-t"><strong>Schedule BRS review 4-6 weeks before exam</strong><span>BRS books are ideal for the consolidation phase. Read them cover-to-cover in the final 6 weeks while doing daily practice questions.</span></div></div>
</div>
{cta_band("Get Your USMLE LWW Books","Official LWW affiliate. All USMLE prep titles available.")}
</div>"""
    return page(
        "USMLE Prep Books 2026 — LWW BRS & Illustrated Reviews | LWW Textbook Hub",
        "Best LWW books for USMLE Step 1, Step 2 CK, Step 3. BRS Physiology, BRS Behavioral Science, Illustrated Reviews Pharmacology. Official LWW affiliate.",
        "usmle.html", body)

def page_nclex():
    body = f"""
<div class="hero">
  <h1>👩‍⚕️ NCLEX Prep with <em>LWW Books</em></h1>
  <p>LWW provides the most comprehensive NCLEX preparation resources — Nursing Drug Handbook, Q&A review books, and clinical references for nursing students.</p>
  <a href="{AFF}" class="cta cta-lg" rel="nofollow sponsored" target="_blank">🛒 Shop NCLEX Books</a>
</div>
<div class="container">
<div class="section-title" style="margin-top:1.5rem;">Essential NCLEX Books</div>
<div class="grid fade">
  <div class="card"><div class="card-icon">💊</div><h3>Nursing Drug Handbook</h3><p>NCLEX heavily tests pharmacology. The Nursing Drug Handbook covers 4,500+ medications with nursing considerations, dosing, adverse effects, and patient teaching — everything NCLEX tests.</p><div class="price">$49.99</div><a href="{AFF}" class="cta" rel="nofollow sponsored" target="_blank">Buy Nursing Drug Handbook →</a></div>
  <div class="card"><div class="card-icon">📝</div><h3>Lippincott Q&A Review for NCLEX-RN</h3><p>Thousands of NCLEX-style questions with rationales. Select-all-that-apply, prioritization, and clinical judgment questions matching the current NCLEX test plan.</p><div class="price">$44.99</div><a href="{AFF}" class="cta" rel="nofollow sponsored" target="_blank">Buy Q&A Review →</a></div>
  <div class="card"><div class="card-icon">📋</div><h3>Lippincott Pocket Drug Guide</h3><p>Compact drug reference for clinical rotations. Essential pharmacology knowledge for bedside practice during nursing school and NCLEX prep.</p><div class="price">$39.99</div><a href="{AFF}" class="cta" rel="nofollow sponsored" target="_blank">Buy Pocket Guide →</a></div>
</div>
<div class="section-title" style="margin-top:2rem;">NCLEX Pharmacology: Why LWW is Essential</div>
<div class="highlight"><strong>Key fact:</strong> Pharmacology questions account for approximately 12-18% of NCLEX questions. The LWW Nursing Drug Handbook covers every drug category that appears on NCLEX with nursing-specific content — adverse effects, interactions, and patient teaching.</div>
{cta_band("Pass NCLEX with LWW Books","The Nursing Drug Handbook is the most recommended NCLEX pharmacology reference.")}
</div>"""
    return page(
        "NCLEX Prep Books 2026 — LWW Nursing Drug Handbook & Q&A Review | LWW Textbook Hub",
        "Best LWW books for NCLEX 2026. Nursing Drug Handbook, Lippincott Q&A Review, Pocket Drug Guide. Official LWW affiliate for nursing students.",
        "nclex.html", body)

def page_comparison():
    body = f"""
<div class="hero">
  <h1>⚖️ LWW Textbook <em>Comparison</em></h1>
  <p>Side-by-side comparison of all major LWW nursing and medical textbooks to help you choose the right books for your needs.</p>
</div>
<div class="container">
<div class="section-title" style="margin-top:1.5rem;">All LWW Books Compared</div>
{BOOK_TABLE}
<div class="section-title" style="margin-top:2rem;">Which Book Is Right for You?</div>
<div class="grid fade">
  <div class="card"><div class="card-icon">👩‍⚕️</div><h3>Nursing Students</h3><p><strong>Must have:</strong> Nursing Drug Handbook. <strong>Also get:</strong> Lippincott Pocket Drug Guide for clinical. <strong>For NCLEX:</strong> Q&A Review book.</p><a href="{AFF}" class="cta" rel="nofollow sponsored" target="_blank">Shop Nursing Books →</a></div>
  <div class="card"><div class="card-icon">🩺</div><h3>Medical Students (Step 1)</h3><p><strong>Must have:</strong> BRS Physiology. <strong>Also get:</strong> Illustrated Reviews Pharmacology. <strong>Behavioral:</strong> BRS Behavioral Science.</p><a href="{AFF}" class="cta" rel="nofollow sponsored" target="_blank">Shop Medical Books →</a></div>
  <div class="card"><div class="card-icon">🏥</div><h3>Practicing RNs</h3><p><strong>Must have:</strong> Lippincott Pocket Drug Guide for quick clinical reference. <strong>Reference:</strong> Full Nursing Drug Handbook for comprehensive lookups.</p><a href="{AFF}" class="cta" rel="nofollow sponsored" target="_blank">Shop Clinical Books →</a></div>
</div>
{cta_band("Shop All LWW Titles","Every book comparison leads to the same place — the official LWW affiliate store.")}
</div>"""
    return page(
        "LWW Textbook Comparison 2026 — Which Book Should You Buy? | LWW Textbook Hub",
        "Compare all major LWW nursing and medical textbooks. Nursing Drug Handbook vs Pocket Drug Guide, BRS vs Illustrated Reviews. Find the right book for your needs.",
        "comparison.html", body)

def page_faq():
    schema = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"What is the best LWW nursing textbook for NCLEX prep?","acceptedAnswer":{"@type":"Answer","text":"The Nursing Drug Handbook is the most recommended for NCLEX prep, covering 4,500+ medications with dosage info, interactions, and clinical warnings. The Lippincott Q&A Review provides practice questions."}},
{"@type":"Question","name":"Which LWW books are best for USMLE Step 1?","acceptedAnswer":{"@type":"Answer","text":"BRS Physiology and Illustrated Reviews: Pharmacology are top choices for USMLE Step 1, offering concise explanations and mnemonics for fast recall."}},
{"@type":"Question","name":"What is the difference between the Nursing Drug Handbook and Lippincott Pocket Drug Guide?","acceptedAnswer":{"@type":"Answer","text":"The Nursing Drug Handbook is the comprehensive reference with 4,500+ drugs and full nursing content. The Pocket Drug Guide covers 3,500+ drugs in a compact portable format for clinical use. Many nurses own both."}}
]}</script>"""
    faqs = [
        ("What is the best LWW nursing textbook for NCLEX prep?","The Nursing Drug Handbook is the most recommended for NCLEX prep, covering 4,500+ medications with dosage info, interactions, and clinical warnings. The Lippincott Q&A Review provides comprehensive practice questions."),
        ("Which LWW books are best for USMLE Step 1?","BRS Physiology and Illustrated Reviews: Pharmacology are top choices for USMLE Step 1. BRS Behavioral Science covers high-yield psychology and epidemiology content."),
        ("What is the difference between the Nursing Drug Handbook and Pocket Drug Guide?","The Nursing Drug Handbook is the comprehensive reference with 4,500+ drugs and full nursing content. The Pocket Drug Guide covers 3,500 drugs in a compact portable format. Many nurses own both."),
        ("Are BRS books good for USMLE Step 1?","Yes. The Board Review Series (BRS) books are specifically designed for USMLE Step 1 board review. BRS Physiology is consistently one of the most recommended Step 1 resources."),
        ("What is Illustrated Reviews: Pharmacology good for?","Illustrated Reviews: Pharmacology is excellent for USMLE Step 1 and for nursing students who are visual learners. The illustrated format with mnemonics and flow charts significantly improves drug mechanism retention."),
        ("Are these affiliate links?","Yes. All book links are affiliate links via LinkConnector (lc=014538024578003224). Purchasing supports this site at no extra cost to you."),
        ("Are LWW textbooks updated regularly?","Yes. Major LWW titles like the Nursing Drug Handbook are updated annually to reflect new drugs, changed guidelines, and current clinical practice."),
        ("Can I buy LWW books through this site?","Yes. All affiliate links go directly to the official LWW store at shop.lww.com via our LinkConnector affiliate tracking."),
    ]
    faq_html = "".join(f'<div class="faq"><div class="faq-q">{q}</div><div class="faq-a">{a}</div></div>' for q,a in faqs)
    body = f"""
<div class="hero">
  <h1>❓ LWW Textbook <em>FAQ</em></h1>
  <p>Everything nursing and medical students ask about LWW textbooks — answered.</p>
</div>
<div class="container">
<div class="faqs fade">{faq_html}</div>
<div style="text-align:center;margin-top:2rem;">
  <a href="{AFF}" class="cta cta-lg" rel="nofollow sponsored" target="_blank">🛒 Shop LWW Textbooks →</a>
</div>
{cta_band("Ready to Shop?","Official LWW affiliate links. All major nursing and medical textbooks available.")}
</div>"""
    return page(
        "LWW Textbook FAQ 2026 — Nursing Drug Handbook, BRS, NCLEX | LWW Textbook Hub",
        "LWW textbook FAQ. Best nursing textbooks for NCLEX, best medical books for USMLE Step 1, Nursing Drug Handbook vs Pocket Guide, BRS series explained.",
        "faq.html", body, schema)

def page_study_tips():
    tips_data = [
        ("Keep the Nursing Drug Handbook at your bedside","Daily exposure to drug entries — even casually flipping through — builds familiarity that translates to faster NCLEX pharmacology recall."),
        ("Use the Pocket Drug Guide on clinical rotations","The compact format fits in your scrub pocket. Quick drug lookups during rounds reinforce your textbook learning with real clinical context."),
        ("Read BRS chapters the week before each block exam","BRS books are ideal for rapid review, not primary learning. Use them to consolidate the week before each exam rather than as your first resource."),
        ("Focus on nursing considerations, not just drug facts","NCLEX and clinical practice test nursing judgment around medications. The Nursing Drug Handbook's nursing-specific sections are more valuable than memorizing doses."),
        ("Use Illustrated Reviews for visual drug mechanisms","If a drug mechanism isn't sticking, find it in Illustrated Reviews: Pharmacology. The visual representation often makes mnemonics that work when text alone doesn't."),
        ("Study high-risk medications first","NCLEX heavily tests high-alert medications. Use the Nursing Drug Handbook to identify and prioritize: anticoagulants, insulin, digoxin, chemotherapy, and high-dose opioids."),
        ("Practice Q&A questions after each chapter","After reading any LWW textbook chapter, immediately answer practice questions from Lippincott's Q&A Review on that topic. Immediate application strengthens retention."),
        ("Review drug interactions systematically","Drug interaction questions are common on NCLEX. Use the Nursing Drug Handbook interaction tables to systematically review the most clinically significant pairs."),
        ("Connect pharmacology to pathophysiology","Memorizing drugs without understanding why they're used leads to poor NCLEX performance. Use BRS books to understand the physiology, then connect drugs to their mechanisms."),
        ("Schedule dedicated drug handbook time weekly","Set aside 30 minutes weekly to review drug categories you're less familiar with. Consistent weekly exposure builds the comprehensive pharmacology knowledge NCLEX requires."),
    ]
    tip_html = "".join(f'<div class="tip-item"><div class="tip-n">{str(i+1).zfill(2)}</div><div class="tip-t"><strong>{t}</strong><span>{d}</span></div></div>' for i,(t,d) in enumerate(tips_data))
    body = f"""
<div class="hero">
  <h1>📚 10 LWW Textbook Study Tips <em>2026</em></h1>
  <p>How to get the most from your LWW nursing and medical textbooks for NCLEX and USMLE success.</p>
</div>
<div class="container">
<div class="tips-list fade">{tip_html}</div>
<div style="text-align:center;margin-top:2rem;">
  <a href="{AFF}" class="cta" rel="nofollow sponsored" target="_blank">🛒 Get Your LWW Books →</a>
</div>
{cta_band("Apply These Tips with LWW Books","Shop official LWW textbooks through our affiliate link.")}
</div>"""
    return page(
        "10 LWW Textbook Study Tips 2026 — NCLEX & USMLE | LWW Textbook Hub",
        "10 study tips for LWW nursing and medical textbooks. How to use Nursing Drug Handbook, BRS, Illustrated Reviews, and Pocket Drug Guide for maximum NCLEX and USMLE results.",
        "study-tips.html", body)

def page_about():
    body = f"""
<div class="container" style="padding-top:2rem;">
<div class="card">
  <h2 class="section-title">About LWW Textbook Hub</h2>
  <p>LWW Textbook Hub is an independent review and affiliate site for Lippincott Williams & Wilkins (LWW/Wolters Kluwer) nursing and medical textbooks. We help nursing students, medical students, and healthcare professionals find the right LWW books for their needs.</p>
  <p style="margin-top:1rem;">LWW Textbook Hub is an affiliate partner via the LinkConnector network (lc=014538024578003224). We earn a commission when you purchase through our links at no extra cost to you.</p>
  <div style="text-align:center;margin-top:1.5rem;"><a href="{AFF}" class="cta" rel="nofollow sponsored" target="_blank">Shop LWW Textbooks →</a></div>
</div>
</div>"""
    return page("About LWW Textbook Hub — Independent LWW Affiliate",
                "LWW Textbook Hub independently reviews LWW nursing and medical textbooks. Official LinkConnector affiliate for LWW/Wolters Kluwer.",
                "about.html", body)

def page_contact():
    body = f"""
<div class="container" style="padding-top:2rem;">
<div class="card">
  <h2 class="section-title">Contact LWW Textbook Hub</h2>
  <p>Questions or partnership inquiries?</p>
  <p style="font-weight:700;font-size:1.1rem;margin:1.5rem 0;">contact [at] lwwtextbookhub [dot] info</p>
  <a href="{AFF}" class="cta" rel="nofollow sponsored" target="_blank">Shop LWW Textbooks →</a>
</div>
</div>"""
    return page("Contact LWW Textbook Hub", "Contact LWW Textbook Hub.", "contact.html", body)

def page_disclosure():
    body = f"""
<div class="container" style="padding-top:2rem;">
<div class="card">
  <h2 class="section-title">Affiliate Disclosure</h2>
  <p>LWW Textbook Hub contains affiliate links to LWW (Lippincott Williams & Wilkins / Wolters Kluwer) textbooks via the LinkConnector affiliate network.</p>
  <p style="margin-top:1rem;"><strong>Affiliate details:</strong> LinkConnector network. lc=014538024578003224, atid=ShopLWW-Web, lcpt=0, lcpf=0.</p>
  <p style="margin-top:1rem;">We earn a commission when you purchase through our links at no extra cost to you. Commission rates do not influence our reviews or recommendations.</p>
</div>
</div>"""
    return page("Affiliate Disclosure — LWW Textbook Hub",
                "LWW Textbook Hub affiliate disclosure. LinkConnector affiliate lc=014538024578003224 for LWW nursing and medical textbooks.",
                "disclosure.html", body)

def all_pages():
    return {
        "nursing-textbooks.html": page_nursing_textbooks(),
        "medical-books.html":     page_medical_books(),
        "usmle.html":             page_usmle(),
        "nclex.html":             page_nclex(),
        "comparison.html":        page_comparison(),
        "faq.html":               page_faq(),
        "study-tips.html":        page_study_tips(),
        "about.html":             page_about(),
        "contact.html":           page_contact(),
        "disclosure.html":        page_disclosure(),
    }

def sitemap(pages):
    today = datetime.utcnow().strftime("%Y-%m-%d")
    urls = [f"  <url><loc>{SITE_URL}/</loc><lastmod>{today}</lastmod><priority>1.0</priority></url>"]
    for slug in pages:
        urls.append(f"  <url><loc>{SITE_URL}/{slug}</loc><lastmod>{today}</lastmod><priority>0.8</priority></url>")
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>"

def robots():
    return f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n"

def gh_put(path, content, msg):
    url = f"https://api.github.com/repos/{GH_USER}/{GH_REPO}/contents/{path}"
    r = requests.get(url, headers=HEADERS)
    sha = r.json().get("sha") if r.status_code == 200 else None
    payload = {"message": msg, "content": base64.b64encode(content.encode()).decode()}
    if sha:
        payload["sha"] = sha
    resp = requests.put(url, headers=HEADERS, json=payload)
    print(f"{'✅' if resp.status_code in (200,201) else '❌'} {path} ({resp.status_code})")

if __name__ == "__main__":
    pages = all_pages()
    print(f"Building {len(pages)} pages for {SITE_NAME}...")
    for slug, html in pages.items():
        gh_put(slug, html, f"Site update: {slug}")
    gh_put("sitemap.xml", sitemap(pages), "Site update: sitemap.xml")
    gh_put("robots.txt",  robots(),       "Site update: robots.txt")
    print(f"\nDone! {len(pages)+2} files pushed to {GH_REPO}.")

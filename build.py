#!/usr/bin/env python3
"""Bouwt de statische site van jdcoaching.nl.

Gebruik:  python3 build.py
Uitvoer:  docs/     -> de echte site (GitHub Pages), nette URL's zoals /werkwijze/
          preview/  -> dezelfde pagina's als losse bestanden, voor een voorbeeld

Teksten staan in content.py. Opmaak staat in src/style.css.
"""
import html
import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from content import PAGES, SITE  # noqa: E402

ROOT = Path(__file__).parent
SRC = ROOT / "src"
LOGO = (SRC / "logo.svg").read_text()

NAV = [("werkwijze", "Werkwijze"), ("werkgevers", "Voor organisaties"),
       ("kosten", "Tarieven"), ("over-mij", "Over mij")]


def href(slug, mode, depth):
    """Link naar een pagina. mode 'site' = nette URL's, 'preview' = losse .html-bestanden."""
    if mode == "site":  # relatief, werkt zowel op jdcoaching.nl als op github.io/jdcoaching-site/
        up = "../" * depth
        return (up or "./") if slug == "home" else f"{up}{slug}/"
    return "./" if slug == "home" else f"{slug}.html"


def asset(path, mode, depth=0):
    return ("../" * depth) + path if mode == "site" else path


def header(current, mode, d=0):
    items = []
    for slug, label in NAV:
        cur = ' aria-current="page"' if slug == current else ""
        items.append(f'<a href="{href(slug, mode, d)}"{cur}>{label}</a>')
    items.append(f'<a class="nav-mail" href="mailto:{SITE["email"]}">{SITE["email"]}</a>')
    return f"""<a class="skip" href="#inhoud">Naar de inhoud</a>
<header class="site-header"><div class="wrap">
  <a class="logo" href="{href('home', mode, d)}" aria-label="JDCoaching, naar de homepage">{LOGO}</a>
  <nav class="nav" aria-label="Hoofdmenu">{''.join(items)}</nav>
</div></header>"""


def footer(mode, d=0):
    s = SITE
    return f"""<footer class="site-footer"><div class="wrap">
  <dl>
    <dt>JDCoaching</dt><dd>{s['owner']}</dd>
    <dt>E-mail</dt><dd><a href="mailto:{s['email']}">{s['email']}</a></dd>
    <dt>KvK</dt><dd>{s['kvk']}</dd>
    <dt>Btw</dt><dd>{s['btw']}</dd>
  </dl>
  <div class="footer-links">
    <a href="{s['linkedin']}" rel="noopener">LinkedIn</a>
    <a href="{href('privacy', mode, d)}">Privacyverklaring</a>
  </div>
  <img class="badge" src="{asset('img/nobco.jpg', mode, d)}" width="220" height="120" alt="NOBCO erkend coach">
</div></footer>"""


def cta():
    return f"""<section class="cta"><div class="wrap">
  <h2>Zullen we kennismaken?</h2>
  <p>Stuur me een mail met een paar zinnen over waar je tegenaan loopt. Ik neem dan contact met je op voor een kennismaking.</p>
  <a class="mail" href="mailto:{SITE['email']}">{SITE['email']}</a>
</div></section>"""


def head(page, mode, d=0):
    s = SITE
    url = s["url"] + ("/" if page["slug"] == "home" else f"/{page['slug']}/")
    title = page["title"] if page["slug"] == "home" else f"{page['title']} | JDCoaching"
    ld = {
        "@context": "https://schema.org", "@type": "ProfessionalService",
        "name": "JDCoaching", "url": s["url"] + "/", "email": s["email"],
        "founder": {"@type": "Person", "name": s["owner"], "jobTitle": "Coach"},
        "image": s["url"] + "/img/jasper.jpg", "sameAs": [s["linkedin"]],
        "priceRange": "€130 - €175",
    }
    fonts = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
             '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
             '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Gloock'
             '&family=Hanken+Grotesk:wght@400;600;650&display=swap">')
    return f"""<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(page['description'])}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="nl_NL">
<meta property="og:site_name" content="JDCoaching">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(page['description'])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{s['url']}/img/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{asset('img/favicon.svg', mode, d)}" type="image/svg+xml">
{fonts}
<link rel="stylesheet" href="{asset('style.css', mode, d)}">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>"""


def render(page, mode, bare=False):
    d = 0 if page["slug"] == "home" else 1
    body = (page["body"].replace("{EMAIL}", SITE["email"])
            .replace("{IMG}", asset("img/", mode, d))
            .replace("{CTA}", cta()))
    for slug, _ in NAV + [("privacy", ""), ("home", "")]:
        body = body.replace("{LINK:" + slug + "}", href(slug, mode, d))
    inner = f"""{header(page['slug'], mode, d)}
<main id="inhoud">
{body}
</main>
{footer(mode, d)}"""
    if bare:  # voorbeeldpagina die het Artifact zelf in een document verpakt
        return f'<meta name="claude:viewport-fit-sides" content="cover">\n{head(page, mode, d)}\n{inner}\n'
    return f"""<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{head(page, mode, d)}
</head>
<body>
{inner}
</body>
</html>
"""


def build():
    for out in ("docs", "preview"):
        shutil.rmtree(ROOT / out, ignore_errors=True)
        (ROOT / out / "img").mkdir(parents=True)
        shutil.copy(SRC / "style.css", ROOT / out / "style.css")
        for f in (SRC / "img").iterdir():
            shutil.copy(f, ROOT / out / "img" / f.name)

    docs = ROOT / "docs"
    for page in PAGES:
        target = docs / "index.html" if page["slug"] == "home" else docs / page["slug"] / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(render(page, "site"))
        prev = ROOT / "preview" / ("index.html" if page["slug"] == "home" else f"{page['slug']}.html")
        prev.write_text(render(page, "preview", bare=page["slug"] == "home"))

    if (ROOT / "CNAME").exists():  # pas toevoegen als de DNS naar GitHub wijst
        shutil.copy(ROOT / "CNAME", docs / "CNAME")
    (docs / ".nojekyll").write_text("")
    (docs / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE['url']}/sitemap.xml\n")
    urls = "".join(
        f"<url><loc>{SITE['url']}{'/' if p['slug'] == 'home' else '/' + p['slug'] + '/'}</loc></url>"
        for p in PAGES)
    (docs / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>'
        f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    print("Klaar:", ", ".join(p["slug"] for p in PAGES))


if __name__ == "__main__":
    build()

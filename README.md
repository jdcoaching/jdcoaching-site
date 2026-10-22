# jdcoaching.nl

Statische website van JDCoaching.

- Teksten: `content.py`
- Opmaak: `src/style.css`
- Logo en afbeeldingen: `src/`
- Bouwen: `python3 build.py` -> schrijft de site naar `docs/` (gepubliceerd via GitHub Pages) en een voorbeeld naar `preview/`.

DNS (Mijndomein): alleen de A/AAAA-records van jdcoaching.nl en de CNAME van www wijzen naar GitHub Pages.
De MX-, DKIM- (soverinX._domainkey) en DMARC-records voor de e-mail blijven ongewijzigd.

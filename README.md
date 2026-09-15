# herbsnspices.nl

Statische site, gegenereerd met Python. Geen frameworks. Onafhankelijke keukengids over kruiden en specerijen.

## Bouwen

    python3 build.py

De site komt in `site/`.

## Deployen (Cloudflare Pages via GitHub)

1. Repo koppelen aan Cloudflare Pages.
2. Framework preset: None
3. Build command: `python3 build.py`
4. Build output directory: `site`
5. Domein toevoegen onder Custom domains.

## Structuur

Alle content staat als data bovenin `build.py`. Een item toevoegen betekent een blok toevoegen aan de
betreffende lijst en opnieuw bouwen. De illustraties zijn eigen SVG's in `assets/`, geen foto's onder licentie.


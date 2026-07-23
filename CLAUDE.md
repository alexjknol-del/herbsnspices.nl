# Werkafspraken voor dit project

Site: herbsnspices.nl, statische site via `build.py`, gedeployed met Cloudflare Pages.

## Stijl
- Nederlands, geen aanspreekvorm (geen je, jij, jullie, uw). Onpersoonlijk of derde persoon.
- Geen em-dashes, geen dummy-tekst, geen tekst gericht aan de beheerder.
- Het woord "rustig" niet gebruiken.

## Content toevoegen
- Nieuw item of artikel: blok toevoegen aan de betreffende lijst bovenin `build.py`.
- Afbeeldingen als eigen SVG in `assets/img/`, in dezelfde vlakke stijl.

## Na elke wijziging
1. `python3 build.py` draaien en controleren dat de build slaagt.
2. Controleren op aanspreekvorm, em-dashes en geldige JSON-LD.
3. Committen en pushen. Cloudflare bouwt en publiceert automatisch.

## Niet doen
- `site/` committen (staat in .gitignore).
- Foto's van derden toevoegen zonder licentie.

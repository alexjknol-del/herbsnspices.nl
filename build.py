#!/usr/bin/env python3
# Generator voor herbsnspices.nl - onafhankelijke keukengids over kruiden en specerijen.
import os, json, html, hashlib

def _ver(p):
    try: return hashlib.md5(open(os.path.join(os.path.dirname(__file__),p),'rb').read()).hexdigest()[:8]
    except Exception: return "1"

BASE="https://herbsnspices.nl"
SITE="Herbs n Spices"
EMAIL="info@herbsnspices.nl"
AUTEUR="Roos Vermeulen"
AUTEUR_ROL="Culinair redacteur"
SRC=os.path.dirname(__file__); OUT=os.path.join(SRC,"site")
CSS_VER=_ver("assets/css/style.css")

def esc(s): return html.escape(str(s), quote=True)

IC={
 "check":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',
 "arrow":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>',
 "mail":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>',
 "leaf":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.5 19 2c1 2 2 4.2 2 8 0 5.5-4.8 10-10 10z"/><path d="M2 21c0-3 1.9-5.4 5.1-6"/></svg>',
 "flame":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2s4 4 4 8a4 4 0 0 1-8 0c0-2 1-3 1-3s-3 3-3 7a6 6 0 0 0 12 0c0-6-6-12-6-12z"/></svg>',
 "jar":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 2h8v3H8z"/><path d="M6 8a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2z"/><line x1="6" y1="12" x2="18" y2="12"/></svg>',
 "book":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h7a3 3 0 0 1 3 3v13a2.5 2.5 0 0 0-2.5-2.5H4z"/><path d="M20 4h-3a3 3 0 0 0-3 3v13a2.5 2.5 0 0 1 2.5-2.5H20z"/></svg>',
 "globe":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 3 2.5 15 0 18M12 3c-2.5 3-2.5 15 0 18"/></svg>',
 "menu":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="4" y1="7" x2="20" y2="7"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="4" y1="17" x2="20" y2="17"/></svg>',
}

def pot(a,b):
    return (f'<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">'
            f'<rect x="13" y="7" width="22" height="5" rx="2" fill="{b}"/>'
            f'<path d="M11 15a3 3 0 0 1 3-3h20a3 3 0 0 1 3 3v23a3 3 0 0 1-3 3H14a3 3 0 0 1-3-3z" fill="{a}"/>'
            f'<rect x="11" y="19" width="26" height="3" fill="{b}" opacity=".55"/>'
            f'<circle cx="20" cy="30" r="2.4" fill="{b}" opacity=".7"/>'
            f'<circle cx="28" cy="27" r="1.8" fill="{b}" opacity=".7"/>'
            f'<circle cx="25" cy="34" r="1.6" fill="{b}" opacity=".7"/></svg>')

NAV=[("Home","/"),("Kruiden & specerijen","/specerijen/"),("Keukengidsen","/gidsen/"),("Nieuws","/nieuws/"),("Over","/over/"),("Partners","/partners/"),("Contact","/contact/")]

def head(title,desc,path,ld=None):
    can=BASE+path
    j="".join('<script type="application/ld+json">'+json.dumps(b,ensure_ascii=False)+'</script>' for b in (ld or []))
    nav="".join(f'<a class="navlink" href="{h}">{esc(l)}</a>' for l,h in NAV)
    return f"""<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{can}">
<meta property="og:type" content="website">
<meta property="og:locale" content="nl_NL">
<meta property="og:site_name" content="{esc(SITE)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{can}">
<meta property="og:image" content="{BASE}/assets/img/mortier.svg">
<meta name="theme-color" content="#2F4A3C">
<link rel="icon" href="/assets/icons/logo-mark.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,500;0,600;0,700;1,500&family=Jost:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/style.css?v={CSS_VER}">
{j}
</head>
<body>
<header class="site-head">
  <nav class="nav" id="nav">
    <a class="brand" href="/"><img class="mark" src="/assets/icons/logo-mark.svg" alt=""><span><b>Herbs n Spices</b><span>Keukengids</span></span></a>
    {nav}
    <button class="menu-toggle" aria-label="Menu" onclick="document.getElementById('nav').classList.toggle('open')">{IC['menu']}</button>
  </nav>
</header>
"""

def footer():
    return f"""<footer class="foot">
  <div class="wrap">
    <div class="cols">
      <div>
        <a class="brand" href="/" style="color:#fff"><img class="mark" src="/assets/icons/logo-mark.svg" alt=""><span><b>Herbs n Spices</b><span style="color:#93A08F">Keukengids</span></span></a>
        <p class="note">Herbs n Spices is een onafhankelijke keukengids over kruiden en specerijen: herkomst, smaak, gebruik en bewaren. Het platform verkoopt niets en is geen webshop.</p>
      </div>
      <div>
        <h4>Ontdekken</h4>
        <a href="/specerijen/">Alle kruiden en specerijen</a>
        <a href="/gidsen/">Keukengidsen</a>
        <a href="/nieuws/">Nieuws</a>
        <a href="/redactie/">Over de redactie</a>
      </div>
      <div>
        <h4>Informatie</h4>
        <a href="/over/">Over dit platform</a>
        <a href="/contact/">Contact</a>
        <a href="/privacybeleid/">Privacybeleid</a>
        <a href="/cookiebeleid/">Cookiebeleid</a>
      </div>
    </div>
    <div class="foot-bottom">
      <span>&copy; 2026 {esc(SITE)}</span>
      <span><a href="/contact/">Contact</a> &middot; <a href="/privacybeleid/">Privacy</a> &middot; <a href="/cookiebeleid/">Cookies</a></span>
    </div>
  </div>
</footer>
</body>
</html>"""

def crumb(items):
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":BASE+u} for i,(n,u) in enumerate(items)]}

def crumbs_html(items):
    o=[f'<a href="{u}">{esc(n)}</a>' for n,u in items[:-1]]
    o.append(f'<span>{esc(items[-1][0])}</span>')
    return '<div class="wrap"><nav class="crumbs">'+' / '.join(o)+'</nav></div>'

def write(path,c):
    f=os.path.join(OUT,"index.html") if path=="/" else os.path.join(OUT,path.strip("/"),"index.html")
    os.makedirs(os.path.dirname(f),exist_ok=True)
    open(f,"w",encoding="utf-8").write(c)

def blocks(bs):
    o=[]
    for b in bs:
        if b[0]=="p": o.append(f"<p>{esc(b[1])}</p>")
        elif b[0]=="h2": o.append(f"<h2>{esc(b[1])}</h2>")
        elif b[0]=="ul": o.append("<ul>"+"".join(f"<li>{esc(x)}</li>" for x in b[1])+"</ul>")
        elif b[0]=="callout": o.append(f'<div class="callout"><p>{esc(b[1])}</p></div>')
        elif b[0]=="plink": o.append(f"<p>{b[1]}</p>")
    return "".join(o)

def byline():
    return f'<div class="byline"><img src="/assets/img/auteur.svg" alt="{esc(AUTEUR)}"><div class="who">{esc(AUTEUR)}<small>{esc(AUTEUR_ROL)}</small></div></div>'

SPECERIJEN=[
 {"slug":"zwarte-peper","naam":"Zwarte peper","fam":"Specerij","a":"#4A3B2E","b":"#D9C7A8",
  "resume":"De meest gebruikte specerij ter wereld, gewonnen uit onrijpe bessen die drogend zwart en gerimpeld worden.",
  "profiel":[("Herkomst","India, Vietnam"),("Deel","Onrijpe bes"),("Smaak","Scherp, houtig"),("Gebruik","Vers gemalen")],
  "secties":[("Waarom vers malen het verschil maakt","Piperine geeft peper de scherpte, maar de geur komt van vluchtige oliën die na het malen snel vervliegen. Voorgemalen peper verliest binnen enkele weken het grootste deel van zijn aroma en houdt vooral de scherpte over. Een molen met een verstelbare maalgraad lost dat op."),
              ("Zwart, wit, groen en rood","Alle vier komen van dezelfde plant, Piper nigrum. Zwarte peper wordt onrijp geplukt en gedroogd, witte peper rijp geoogst en ontdaan van de schil, groene peper onrijp gepekeld, rode peper volledig rijp. Witte peper is milder en aardser, groene peper frisser.")],
  "gebruik":["Grof gemalen over gebakken vlees","Fijn gemalen in sauzen en dressings","Hele korrels in bouillon en marinades","Gekneusd in een pepersteak"]},
 {"slug":"paprikapoeder","naam":"Paprikapoeder","fam":"Specerij","a":"#C4542B","b":"#F0C9A8",
  "resume":"Gemalen gedroogde paprika's, van mild en zoet tot pittig en gerookt, met een kleur die op elk gerecht afgeeft.",
  "profiel":[("Herkomst","Hongarije, Spanje"),("Deel","Gedroogde vrucht"),("Smaak","Zoet tot rokerig"),("Gebruik","Kort meebakken")],
  "secties":[("Hongaars en Spaans zijn niet hetzelfde","Hongaars paprikapoeder is doorgaans zoeter en feller van kleur, met gradaties van edelzoet tot scherp. Spaanse pimentón wordt boven eikenhout gerookt, wat een diep rokerig aroma geeft dat chorizo en paella hun karakter verleent."),
              ("Hitte is de valkuil","Paprikapoeder verbrandt snel en wordt dan bitter. De gebruikelijke werkwijze is de pan van het vuur nemen, het poeder door het warme vet roeren en pas daarna vocht toevoegen. Zo lost de kleur op zonder dat het poeder aanbrandt.")],
  "gebruik":["Door goulash en stoofschotels","In marinades voor kip","Over gebakken aardappelen","Gerookte variant bij bonen en linzen"]},
 {"slug":"kaneel","naam":"Kaneel","fam":"Specerij","a":"#8B5A2B","b":"#E5C9A0",
  "resume":"De gedroogde binnenbast van de kaneelboom, verkrijgbaar als broze Ceylonkaneel en als steviger cassia.",
  "profiel":[("Herkomst","Sri Lanka, China"),("Deel","Binnenbast"),("Smaak","Zoet, warm"),("Gebruik","Stok of gemalen")],
  "secties":[("Ceylon en cassia","Ceylonkaneel bestaat uit dunne, broze laagjes die makkelijk verkruimelen en geeft een fijn, bijna citrusachtig zoet aroma. Cassia is dikker, harder en feller van smaak, en is wat in de meeste supermarkten als kaneel wordt verkocht. Het prijsverschil is aanzienlijk."),
              ("Niet alleen zoet","In de Nederlandse keuken belandt kaneel vooral in appeltaart en speculaas, maar in Marokkaanse tajines, Perzische rijstgerechten en Mexicaanse mole speelt de specerij een hartige rol, vaak samen met komijn, koriander of chocolade.")],
  "gebruik":["Stokje meekoken in rijst of stoof","Gemalen door appelmoes en gebak","In een kruidenmengsel voor tajine","Bij warme dranken en compote"]},
 {"slug":"komijn","naam":"Komijn","fam":"Specerij","a":"#9C7B3F","b":"#E8DBB8",
  "resume":"Kleine gestreepte zaadjes met een aards, warm aroma dat de basis vormt van keukens van Mexico tot India.",
  "profiel":[("Herkomst","India, Iran, Turkije"),("Deel","Zaad"),("Smaak","Aards, warm"),("Gebruik","Roosteren")],
  "secties":[("Roosteren verandert alles","Droog roosteren in een hete pan, tot de zaadjes gaan geuren en licht knappen, maakt het aroma ronder en noten-achtiger. Een halve minuut is meestal genoeg; daarna verbrandt het snel. Direct daarna vijzelen geeft het meeste resultaat."),
              ("Komijn en karwij","In het Nederlands raken komijn en karwij vaak door elkaar, mede doordat karwij in Nederland ook wel kummel of komijn wordt genoemd, bijvoorbeeld in komijnekaas. Botanisch zijn het verschillende planten met een duidelijk ander aroma: karwij is frisser en aniiisachtiger.")],
  "gebruik":["Geroosterd en gevijzeld door curry's","In chili con carne","Door hummus en falafel","Met wortel en pompoen uit de oven"]},
 {"slug":"oregano","naam":"Oregano","fam":"Kruid","a":"#6E8B4A","b":"#DCE6C6",
  "resume":"Het enige keukenkruid dat gedroogd vaak sterker is dan vers, en de smaak van de mediterrane keuken bepaalt.",
  "profiel":[("Herkomst","Middellandse Zeegebied"),("Deel","Blad"),("Smaak","Kruidig, licht bitter"),("Gebruik","Gedroogd")],
  "secties":[("Gedroogd boven vers","Bij de meeste kruiden gaat er smaak verloren bij het drogen, maar bij oregano concentreren de aromatische oliën zich juist. Griekse oregano, vaak op de tak gedroogd verkocht, is daardoor krachtiger dan het verse blad uit een potje."),
              ("Oregano en marjolein","De twee zijn familie en worden soms verwisseld. Marjolein is zachter, zoeter en bloemiger, oregano scherper en peperiger. In een tomatensaus valt het verschil direct op.")],
  "gebruik":["Over pizza en tomatensaus","Door een Griekse salade","In marinades met citroen en olijfolie","Bij gegrilde groenten"]},
 {"slug":"tijm","naam":"Tijm","fam":"Kruid","a":"#4F6B45","b":"#D5E0C4",
  "resume":"Een houtig kruid met kleine blaadjes dat lang meekoken verdraagt zonder zijn aroma te verliezen.",
  "profiel":[("Herkomst","Zuid-Europa"),("Deel","Blad en takje"),("Smaak","Houtig, licht mint"),("Gebruik","Meekoken")],
  "secties":[("Bestand tegen lange bereidingen","Waar basilicum en peterselie hun geur binnen minuten verliezen, houdt tijm het uren vol in een stoofpot. De takjes gaan in hun geheel mee en worden er aan het eind uitgevist; de blaadjes laten vanzelf los."),
              ("Citroentijm en gewone tijm","Citroentijm bevat een andere aromatische samenstelling en geeft een duidelijke citrustoon. Bij vis en kip werkt dat prettig, maar in een klassieke bouquet garni blijft gewone tijm de logische keuze.")],
  "gebruik":["Takjes in een stoofpot of bouillon","Met knoflook bij geroosterde aardappel","Onder de huid van kip","In een bouquet garni met laurier"]},
 {"slug":"gember","naam":"Gember","fam":"Specerij","a":"#C89B4A","b":"#F2E0BC",
  "resume":"De wortelstok van de gemberplant, vers scherp en fris, gedroogd warmer en zoeter.",
  "profiel":[("Herkomst","Zuidoost-Azië"),("Deel","Wortelstok"),("Smaak","Scherp, fris"),("Gebruik","Vers of gemalen")],
  "secties":[("Vers en gedroogd zijn niet uitwisselbaar","Verse gember bevat gingerol en smaakt scherp en citrusachtig. Bij drogen verandert dat in shogaol, wat een warmere en zoetere smaak geeft. In een roerbakgerecht is verse gember op zijn plaats, in speculaaskruiden juist de gemalen variant."),
              ("Schillen of niet","Bij jonge gember met dunne, glanzende schil is schillen onnodig. Bij oudere knollen met een gerimpelde schil gaat het schrapen met de rand van een lepel makkelijker dan met een dunschiller, omdat de vorm grillig is.")],
  "gebruik":["Fijn geraspt door roerbakgerechten","In plakjes bij vis en bouillon","Gemalen in koek en speculaas","Vers in thee met citroen"]},
 {"slug":"saffraan","naam":"Saffraan","fam":"Specerij","a":"#D9863F","b":"#F6E3C0",
  "resume":"De handgeplukte stampers van een krokus, de duurste specerij ter wereld en met een paar draadjes al genoeg.",
  "profiel":[("Herkomst","Iran, Spanje"),("Deel","Stamper"),("Smaak","Bloemig, honingachtig"),("Gebruik","Weken in vocht")],
  "secties":[("Waarom de prijs zo hoog is","Elke krokusbloem levert drie stampers, die met de hand geplukt en gedroogd worden. Voor een enkele kilo zijn ruwweg honderdvijftigduizend bloemen nodig, geplukt in een korte bloeiperiode van enkele weken. Dat verklaart de prijs per gram."),
              ("Eerst weken, dan toevoegen","Saffraan geeft kleur en aroma pas goed af in warm vocht. Een kwartier weken in een paar eetlepels warme bouillon of melk, en daarna het geheel toevoegen, geeft een veel gelijkmatiger resultaat dan de draadjes direct door het gerecht roeren.")],
  "gebruik":["In paella en risotto alla milanese","Door bouillabaisse","In zoete rijstgerechten","Bij vis in een romige saus"]},
]
def spec(s): return next(x for x in SPECERIJEN if x["slug"]==s)

GIDSEN=[
 {"slug":"kruiden-bewaren","titel":"Kruiden en specerijen bewaren zonder smaakverlies","ic":"jar",
  "resume":"Licht, warmte en lucht zijn de drie vijanden. Met een paar aanpassingen blijft een pot veel langer bruikbaar.",
  "body":[("p","Een specerij bederft zelden in de zin dat hij oneetbaar wordt. Wat gebeurt is subtieler: de vluchtige oliën die het aroma dragen verdampen, en wat overblijft is kleur zonder geur."),
   ("h2","De drie vijanden"),("p","Licht breekt kleurstoffen en aroma's af, warmte versnelt verdamping, en lucht zorgt voor oxidatie. Een glazen pot in een rek boven het fornuis combineert alle drie, en is daarmee de slechtst denkbare plek, hoe fraai het ook staat."),
   ("h2","Waar het wel goed gaat"),("ul",["Een gesloten kast, ver van fornuis en oven.","Ondoorzichtige of donkere potten, of een lade waar geen licht komt.","Potjes die passen bij de hoeveelheid, zodat er weinig lucht in blijft.","Hele zaden en stokjes in plaats van gemalen, en pas malen bij gebruik."]),
   ("h2","Hoe lang gaat het mee"),("p","Hele zaden en peperkorrels behouden hun aroma ruwweg drie tot vier jaar. Gemalen specerijen zijn na een jaar duidelijk minder, gedroogde bladkruiden na ongeveer een jaar. Dat zijn richtlijnen, geen vervaldata: ruiken zegt meer dan een datum op het etiket."),
   ("callout","Een snelle test: wrijf een snufje tussen duim en wijsvinger en ruik. Komt er nauwelijks geur vrij, dan voegt het aan een gerecht ook weinig meer toe."),
   ("h2","Vriezer en koelkast"),("p","Verse bladkruiden lenen zich goed voor de vriezer, fijngesneden in een ijsblokjesvorm met wat olie of water. Gedroogde specerijen horen daar niet thuis: bij het uitnemen slaat condens neer op het poeder, wat klontering en smaakverlies geeft.")]},
 {"slug":"zelf-kruidenmengsels-maken","titel":"Zelf kruidenmengsels maken: de basisverhoudingen","ic":"flame",
  "resume":"Een eigen mengsel is verser en goedkoper dan een kant-en-klaar potje, en de verhoudingen zijn eenvoudiger dan ze lijken.",
  "body":[("p","Kant-en-klare mengsels bevatten vaak zout, suiker of vulmiddelen, en zijn meestal al maanden gemalen. Zelf mengen kost een paar minuten en geeft volledige controle over de verhouding."),
   ("h2","De opbouw van een mengsel"),("p","De meeste mengsels volgen dezelfde logica: een basis die het volume levert, een aromatische laag die het karakter bepaalt, en een accent dat in kleine hoeveelheid het verschil maakt. Komijn en koriander vormen vaak de basis, kaneel of kruidnagel het accent."),
   ("h2","Drie werkbare verhoudingen"),("ul",["Ras el hanout in het klein: 3 delen komijn, 2 delen koriander, 1 deel kaneel, 1 deel gember, snufje kruidnagel.","Italiaanse kruiden: gelijke delen oregano, tijm en basilicum, met een half deel rozemarijn.","Barbecuerub: 4 delen gerookt paprikapoeder, 2 delen bruine suiker, 1 deel komijn, 1 deel zwarte peper, 1 deel knoflookpoeder."]),
   ("h2","Roosteren voor het malen"),("p","Hele zaden kort droog roosteren en daarna malen geeft een merkbaar voller resultaat dan losse poeders mengen. De pan hoeft niet heet te zijn; zodra de geur vrijkomt is het moment daar."),
   ("callout","Maak kleine hoeveelheden. Een mengsel dat binnen twee maanden op is, smaakt tot de laatste lepel zoals bedoeld."),
   ("h2","Zout apart houden"),("p","Zout in een mengsel maakt doseren lastiger, omdat de hoeveelheid kruiden dan vastzit aan de hoeveelheid zout. Zout apart toevoegen houdt beide regelbaar, zeker bij langere bereidingen waarin vocht verdampt.")]},
]

ARTIKELEN=[
 {"slug":'kruidenmix-zelf-samenstellen','titel':'Een kruidenmix zelf samenstellen: verhoudingen en volgorde',"cat":'Achtergrond',"datum":'2026-08-19',"datum_nl":'19 augustus 2026','lees':5,
  'resume':'Een goede mix heeft twee of drie dragers en een accent, niet acht ingrediënten in gelijke delen.',
  "body":[
  ('p', 'Zelf mengen begint meestal met een recept dat acht ingrediënten opsomt zonder verhouding. Het resultaat smaakt vervolgens vol en tegelijk nergens naar, omdat geen enkel ingrediënt genoeg ruimte krijgt.'),
  ('h2', 'De opbouw van een mix'),
  ('p', 'Een bruikbare structuur bestaat uit drie lagen. Een basis die volume geeft, zoals paprikapoeder of gemalen koriander. Een of twee dragers die de richting bepalen, bijvoorbeeld komijn of oregano. En een accent in kleine hoeveelheid: kaneel, kruidnagel, gerookt zout.'),
  ('p', 'In verhouding komt dat vaak neer op vier delen basis, twee delen drager en een half deel accent. Wie het accent gelijkstelt aan de drager, krijgt een mix die in één noot blijft hangen.'),
  ('h2', 'Volgorde en bewerking'),
  ('ul', ['Hele zaden kort roosteren voordat ze worden gemalen.', 'Gedroogde bladkruiden pas na het malen toevoegen, anders vergruizen ze te fijn.', 'Zout apart houden en per gerecht doseren.', 'Suiker alleen toevoegen bij mixen voor de grill, en dan laat in het proces.']),
  ('plink', 'Dat laatste heeft een praktische reden: suiker verbrandt bij hoge temperatuur en geeft een bittere korst. In een rub voor lage temperatuur is het juist wat de korst maakt. De losse componenten waarmee gemengd wordt staan bij <a href="https://www.naturalspices.nl/kruiden-specerijen" rel="nofollow">Natural Spices</a>.'),
  ('h2', 'Kwaliteit van de losse componenten'),
  ('p', 'Een mix is nooit beter dan het zwakste bestanddeel. Gemalen specerijen verliezen hun vluchtige olie binnen maanden, en een paprikapoeder dat een jaar open staat, draagt vooral nog kleur bij en geen smaak.'),
  ('plink', 'Kopen in kleinere hoeveelheden en vaker vervangen levert meer op dan een grote voorraad. Of een biologische uitvoering daarbij smaakverschil geeft, is een aparte vraag; de achtergrond daarvan staat op <a href="https://www.naturalspices.nl/blog/biologische-of-normale-kruiden-wat-is-het-verschil" rel="nofollow">naturalspices.nl</a>.'),
  ('h2', 'Bewaren'),
  ('p', 'Donker, droog en niet boven het fornuis. Warmte en damp zijn de twee factoren die een mix het snelst vlak maken, en de plank naast de afzuigkap is precies de verkeerde plek.'),
  ('p', 'Noteer de datum van mengen op het potje. Zonder datum blijft een zelfgemaakte mix jaren staan, en de teleurstelling over het resultaat wordt dan ten onrechte aan het recept toegeschreven.'),
  ('h2', 'Testen in kleine hoeveelheid'),
  ('p', 'Meng een nieuwe verhouding eerst in een hoeveelheid van een eetlepel en proef die op een neutrale drager, bijvoorbeeld een stukje aardappel of een lepel yoghurt. Op die manier is de mix te beoordelen zonder dat een heel gerecht als test dient.'),
  ('p', 'Noteer de verhouding meteen. Een mix die goed uitpakt en waarvan de samenstelling niet is opgeschreven, is bij de volgende poging vrijwel nooit te reconstrueren, omdat het verschil juist in de kleine hoeveelheden zit.'),
 ]},
 {"slug":"verse-of-gedroogde-kruiden","titel":"Verse of gedroogde kruiden: wanneer welke","cat":"Techniek","datum":"2026-07-08","datum_nl":"8 juli 2026","lees":4,
  "resume":"Vers is niet automatisch beter. Het moment van toevoegen bepaalt vaak meer dan de vorm.",
  "body":[("p","De aanname dat verse kruiden altijd de voorkeur verdienen, houdt geen stand in de keuken. Bepalend is hoe lang een kruid meekookt en welke aromastoffen het bevat."),
   ("h2","Zachte en houtige kruiden"),("p","Zachte kruiden als basilicum, peterselie, dille en koriander bevatten vluchtige oliën die binnen enkele minuten verdwijnen. Die gaan er op het laatst in, of rauw overheen. Houtige kruiden als tijm, rozemarijn en laurier verdragen uren koken en geven hun aroma juist langzaam af."),
   ("h2","De omrekening"),("p","Als vuistregel geldt ongeveer een derde: een eetlepel verse kruiden komt ruwweg overeen met een theelepel gedroogde. Bij oregano ligt dat anders, omdat drogen daar de smaak juist versterkt."),
   ("h2","Wanneer gedroogd wint"),("p","In een stoofpot, een marinade of een droge rub is gedroogd praktischer en vaak sterker. In een salade, een pesto of als garnering heeft vers geen concurrentie.")]},
 {"slug":"specerijen-en-de-vetfase","titel":"Waarom specerijen beter oplossen in vet dan in water","cat":"Achtergrond","datum":"2026-06-20","datum_nl":"20 juni 2026","lees":4,
  "resume":"Veel aromastoffen zijn vetoplosbaar. Dat verklaart waarom de volgorde van toevoegen zoveel uitmaakt.",
  "body":[("p","Wie kerriepoeder direct in een waterige saus roert, houdt vaak een vlak resultaat over. Hetzelfde poeder eerst in olie of boter aanzetten geeft een merkbaar vollere smaak."),
   ("h2","Vetoplosbaar en wateroplosbaar"),("p","Een groot deel van de aromatische verbindingen in specerijen lost beter op in vet dan in water. In de Indiase keuken heet die stap tadka of tarka: specerijen kort in hete olie of ghee, waarna het geheel door het gerecht gaat."),
   ("h2","De volgorde in de pan"),("ul",["Eerst hele zaden in het vet, tot ze geuren.","Dan gemalen specerijen, kort en van het vuur af.","Daarna pas vocht, tomaat of bouillon.","Verse bladkruiden helemaal aan het eind."]),
   ("h2","Waar het misgaat"),("p","Gemalen specerijen verbranden veel sneller dan hele zaden, en verbrande specerijen zijn bitter en niet te redden. Vandaar dat het aanraden is de pan van het vuur te halen voordat het poeder erin gaat.")]},
]

def tile(s):
    return f"""<a class="tile" href="/specerijen/{s['slug']}/"><span class="tt">{pot(s['a'],s['b'])}</span>
  <span class="tb"><span class="fam">{esc(s['fam'])}</span><h3>{esc(s['naam'])}</h3><p>{esc(s['resume'][:88].rsplit(' ',1)[0])}...</p></span></a>"""

def newscard(a):
    return f"""<article class="news"><span class="cat">{esc(a['cat'])}</span>
  <h3><a href="/nieuws/{a['slug']}/" style="color:inherit;text-decoration:none">{esc(a['titel'])}</a></h3>
  <p>{esc(a['resume'])}</p><div class="meta">{esc(a['datum_nl'])} &middot; {a['lees']} min lezen</div></article>"""

def p_home():
    ld=[{"@context":"https://schema.org","@type":"WebSite","@id":BASE+"/#w","url":BASE+"/","name":SITE,"inLanguage":"nl-NL",
         "description":"Onafhankelijke keukengids over kruiden en specerijen: herkomst, smaak, gebruik en bewaren."},
        {"@context":"https://schema.org","@type":"Organization","@id":BASE+"/#o","name":SITE,"url":BASE+"/","email":EMAIL},crumb([("Home","/")])]
    tiles="".join(tile(s) for s in SPECERIJEN[:6])
    gids="".join(f'<div class="card"><div class="ic">{IC[g["ic"]]}</div><h3><a href="/gidsen/{g["slug"]}/" style="color:inherit;text-decoration:none">{esc(g["titel"])}</a></h3><p>{esc(g["resume"])}</p></div>' for g in GIDSEN)
    nieuws="".join(newscard(a) for a in ARTIKELEN)
    h=head("Herbs n Spices | keukengids over kruiden en specerijen",
      "Onafhankelijke keukengids over kruiden en specerijen. Herkomst, smaak, gebruik in de keuken en bewaren, zonder verkooppraat.","/",ld)
    h+=f"""<section class="hero"><div class="wrap hero-inner">
  <div>
    <span class="eyebrow">{IC['leaf']}Keukengids</span>
    <h1>Kruiden en specerijen, <em>uitgelegd</em></h1>
    <p class="lead">Waar komt een specerij vandaan, waar smaakt hij naar, en wanneer gaat hij in de pan. Dit platform behandelt kruiden en specerijen puur culinair: herkomst, smaak, gebruik en bewaren.</p>
    <div class="hero-actions"><a class="btn btn-green" href="/specerijen/">Bekijk alle soorten {IC['arrow']}</a><a class="btn btn-ghost" href="/gidsen/">Naar de keukengidsen</a></div>
    <div class="hero-meta"><span>{IC['check']}8 soorten uitgewerkt</span><span>{IC['check']}Praktische gidsen</span><span>{IC['check']}Geen webshop</span></div>
  </div>
  <div class="hero-art"><img src="/assets/img/mortier.svg" alt="Illustratie van een vijzel met specerijen" width="480" height="360"></div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><span class="eyebrow">{IC['globe']}Het rek in</span><h2>Kruiden en specerijen een voor een</h2>
  <p class="lead">Per soort de herkomst, het smaakprofiel, en de manier waarop hij in de keuken tot zijn recht komt.</p></div>
  <div class="grid cols-3">{tiles}</div>
  <p style="margin-top:22px"><a class="more" href="/specerijen/">Alle acht bekijken {IC['arrow']}</a></p>
</div></section>

<section class="section panel"><div class="wrap">
  <div class="section-head"><span class="eyebrow">{IC['book']}Gidsen</span><h2>Twee vragen die steeds terugkomen</h2></div>
  <div class="grid cols-2">{gids}</div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><span class="eyebrow">{IC['flame']}Nieuws</span><h2>Laatste artikelen</h2></div>
  <div class="grid cols-2">{nieuws}</div>
  <p style="margin-top:22px"><a class="more" href="/nieuws/">Alle artikelen {IC['arrow']}</a></p>
</div></section>

<section class="section panel"><div class="wrap prose">
  <span class="eyebrow">{IC['jar']}Aanbevolen</span>
  <h2>Waar deze kruiden en specerijen te koop zijn</h2>
  <p class="lead">Dit platform verkoopt zelf niets. Wie de behandelde soorten in huis wil halen, komt uit bij een leverancier die het hele jaar door levert.</p>
  <div class="callout">
    <p><strong>Natural Spices</strong></p>
    <p>Natural Spices is een Nederlandse producent van kruiden en specerijen, ruim negentig jaar actief. Het assortiment loopt van pure specerijen, heel en gemalen, tot kruidenmixen, marinades en gedroogde groenten. De mengsels worden intern samengesteld en de producten worden gecontroleerd op smaak, kleur en zuiverheid. Levering aan particulieren, retail en foodservice.</p>
    <p style="margin-top:12px"><a href="https://www.naturalspices.nl/" target="_blank" rel="noopener">naturalspices.nl</a></p>
  </div>
</div></section>

<section class="section tight"><div class="wrap"><div class="cta">
  <h2>Een soort gemist?</h2>
  <p>Het rek groeit op basis van vragen die binnenkomen. Suggesties en correcties zijn welkom bij de redactie.</p>
  <a class="btn btn-paprika" href="/contact/">Mail de redactie {IC['arrow']}</a>
</div></div></section>"""
    write("/",h+footer())

def p_spec_index():
    path="/specerijen/"; c=[("Home","/"),("Kruiden & specerijen",path)]
    ld=[{"@context":"https://schema.org","@type":"CollectionPage","@id":BASE+path,"url":BASE+path,"name":"Kruiden en specerijen","inLanguage":"nl-NL"},
        {"@context":"https://schema.org","@type":"ItemList","itemListElement":[{"@type":"ListItem","position":i+1,"name":s["naam"],"url":BASE+f"/specerijen/{s['slug']}/"} for i,s in enumerate(SPECERIJEN)]},crumb(c)]
    h=head("Alle kruiden en specerijen | "+SITE,"Overzicht van kruiden en specerijen met herkomst, smaakprofiel en gebruik in de keuken.",path,ld)
    h+=crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap">
  <div class="section-head"><span class="eyebrow">{IC['globe']}Overzicht</span><h1>Alle kruiden en specerijen</h1>
  <p class="lead">Acht soorten, elk met herkomst, smaakprofiel, achtergrond en concrete toepassingen in de keuken.</p></div>
  <div class="grid cols-3">{"".join(tile(s) for s in SPECERIJEN)}</div>
</div></section>"""
    write(path,h+footer())

def p_spec(s):
    path=f"/specerijen/{s['slug']}/"; c=[("Home","/"),("Kruiden & specerijen","/specerijen/"),(s["naam"],path)]
    ld=[{"@context":"https://schema.org","@type":"Article","@id":BASE+path,"headline":s["naam"],"description":s["resume"],
         "inLanguage":"nl-NL","author":{"@type":"Person","name":AUTEUR},"publisher":{"@type":"Organization","name":SITE}},crumb(c)]
    pro="".join(f"<div><dt>{esc(l)}</dt><dd>{esc(v)}</dd></div>" for l,v in s["profiel"])
    sec="".join(f"<h2>{esc(t)}</h2><p>{esc(p)}</p>" for t,p in s["secties"])
    geb="".join(f'<li>{IC["check"]}<span>{esc(g)}</span></li>' for g in s["gebruik"])
    anders=[x for x in SPECERIJEN if x["slug"]!=s["slug"]][:3]
    h=head(f"{s['naam']} | herkomst, smaak en gebruik | {SITE}", s["resume"], path, ld)
    h+=crumbs_html(c)
    h+=f"""<section class="section tight"><div class="wrap prose">
  <span class="eyebrow">{IC['leaf']}{esc(s['fam'])}</span><h1>{esc(s['naam'])}</h1><p class="lead">{esc(s['resume'])}</p></div>
  <div class="wrap"><dl class="profil">{pro}</dl></div>
  <div class="wrap prose">{sec}
  <h2>Zo komt het tot zijn recht</h2><ul class="ticks" style="margin-bottom:18px">{geb}</ul>
  {byline()}</div></section>
<section class="section panel"><div class="wrap">
  <div class="section-head"><span class="eyebrow">{IC['globe']}Verder kijken</span><h2>Andere soorten</h2></div>
  <div class="grid cols-3">{"".join(tile(x) for x in anders)}</div>
</div></section>"""
    write(path,h+footer())

def p_gidsen():
    path="/gidsen/"; c=[("Home","/"),("Keukengidsen",path)]
    ld=[{"@context":"https://schema.org","@type":"CollectionPage","@id":BASE+path,"url":BASE+path,"name":"Keukengidsen","inLanguage":"nl-NL"},crumb(c)]
    cards="".join(f'<div class="card"><div class="ic">{IC[g["ic"]]}</div><h3><a href="/gidsen/{g["slug"]}/" style="color:inherit;text-decoration:none">{esc(g["titel"])}</a></h3><p>{esc(g["resume"])}</p><p style="margin-top:10px"><a class="more" href="/gidsen/{g["slug"]}/">Lees de gids {IC["arrow"]}</a></p></div>' for g in GIDSEN)
    h=head("Keukengidsen | bewaren en zelf mengen | "+SITE,"Praktische gidsen over het bewaren van kruiden en specerijen en het zelf samenstellen van kruidenmengsels.",path,ld)
    h+=crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap">
  <div class="section-head"><span class="eyebrow">{IC['book']}Gidsen</span><h1>Keukengidsen</h1>
  <p class="lead">Praktische uitleg over bewaren en over het zelf samenstellen van mengsels, met werkbare verhoudingen.</p></div>
  <div class="grid cols-2">{cards}</div></div></section>"""
    write(path,h+footer())

def p_gids(g):
    path=f"/gidsen/{g['slug']}/"; c=[("Home","/"),("Keukengidsen","/gidsen/"),(g["titel"],path)]
    ld=[{"@context":"https://schema.org","@type":"Article","@id":BASE+path,"headline":g["titel"],"description":g["resume"],
         "inLanguage":"nl-NL","author":{"@type":"Person","name":AUTEUR},"publisher":{"@type":"Organization","name":SITE}},crumb(c)]
    h=head(f"{g['titel']} | {SITE}", g["resume"], path, ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap prose">
  <span class="eyebrow">{IC[g['ic']]}Keukengids</span><h1>{esc(g['titel'])}</h1><p class="lead">{esc(g['resume'])}</p>
  {blocks(g['body'])}{byline()}</div></section>"""
    write(path,h+footer())

def p_nieuws():
    path="/nieuws/"; c=[("Home","/"),("Nieuws",path)]
    ld=[{"@context":"https://schema.org","@type":"CollectionPage","@id":BASE+path,"url":BASE+path,"name":"Nieuws","inLanguage":"nl-NL"},crumb(c)]
    h=head("Nieuws | artikelen over koken met kruiden | "+SITE,"Artikelen over techniek en achtergrond bij het koken met kruiden en specerijen.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap">
  <div class="section-head"><span class="eyebrow">{IC['flame']}Nieuws</span><h1>Artikelen</h1>
  <p class="lead">Achtergrond en techniek: waarom iets werkt in de pan, en wat het verschil maakt.</p></div>
  <div class="grid cols-2">{"".join(newscard(a) for a in ARTIKELEN)}</div></div></section>"""
    write(path,h+footer())

def p_art(a):
    path=f"/nieuws/{a['slug']}/"; c=[("Home","/"),("Nieuws","/nieuws/"),(a["titel"],path)]
    ld=[{"@context":"https://schema.org","@type":"Article","@id":BASE+path,"headline":a["titel"],"description":a["resume"],
         "datePublished":a["datum"],"inLanguage":"nl-NL","author":{"@type":"Person","name":AUTEUR},"publisher":{"@type":"Organization","name":SITE}},crumb(c)]
    ander=[x for x in ARTIKELEN if x["slug"]!=a["slug"]]
    h=head(f"{a['titel']} | {SITE}", a["resume"], path, ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap prose">
  <span class="eyebrow">{IC['flame']}{esc(a['cat'])}</span><h1>{esc(a['titel'])}</h1>
  <p class="meta" style="margin-bottom:22px">Door {esc(AUTEUR)} &middot; {esc(a['datum_nl'])} &middot; {a['lees']} min lezen</p>
  {blocks(a['body'])}{byline()}</div></section>
<section class="section panel"><div class="wrap"><div class="section-head"><h2>Meer lezen</h2></div>
  <div class="grid cols-2">{"".join(newscard(x) for x in ander)}</div></div></section>"""
    write(path,h+footer())

def p_over():
    path="/over/"; c=[("Home","/"),("Over",path)]
    ld=[{"@context":"https://schema.org","@type":"AboutPage","@id":BASE+path,"url":BASE+path,"name":"Over","inLanguage":"nl-NL"},crumb(c)]
    h=head("Over Herbs n Spices | wat dit platform is | "+SITE,
      "Herbs n Spices is een onafhankelijke keukengids over kruiden en specerijen. Uitleg over de opzet, de werkwijze en de grenzen van het platform.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap prose">
  <span class="eyebrow">{IC['book']}Over het platform</span>
  <h1>Een keukengids, geen winkel</h1>
  <p class="lead">Herbs n Spices behandelt kruiden en specerijen zoals ze in de keuken gebruikt worden: waar ze vandaan komen, waar ze naar smaken, en wat er gebeurt als ze in de pan gaan.</p>
  <h2>Waarom dit platform bestaat</h2>
  <p>Het kruidenrek van een gemiddeld huishouden bevat tien tot twintig potjes waarvan de helft zelden opengaat. Vaak niet uit onwil, maar omdat onduidelijk is wat een specerij precies doet en wanneer die van pas komt. Deze gids vult dat gat: per soort een helder profiel en concrete toepassingen.</p>
  <h2>Uitsluitend culinair</h2>
  <p>Over kruiden circuleren veel beweringen over gezondheid. Die staan hier bewust niet. Voor kruiden en botanicals gelden strikte Europese regels rond gezondheidsclaims, en los daarvan hoort een keukengids over smaak te gaan. Wie geneeskundige informatie zoekt, is bij een arts of apotheker beter af.</p>
  <div class="callout"><p><strong>Wat dit platform niet doet.</strong> Er wordt niets verkocht, er zijn geen affiliatie-afspraken met leveranciers, en er worden geen uitspraken gedaan over gezondheidseffecten van kruiden of specerijen.</p></div>
  <h2>Werkwijze</h2>
  <p>Elke soort volgt dezelfde opzet: herkomst, welk plantendeel het betreft, smaakprofiel en gebruiksvorm, gevolgd door achtergrond die in de praktijk verschil maakt. De keukengidsen behandelen vragen die daar los van staan, zoals bewaren en zelf mengen.</p>
  <h2>Correcties</h2>
  <p>Culinaire kennis is niet in beton gegoten, en fouten sluipen erin. Onderbouwde correcties worden bekeken en, als ze kloppen, direct verwerkt.</p>
  <p style="margin-top:16px"><a class="btn btn-green" href="/redactie/">Over de redactie {IC['arrow']}</a> <a class="btn btn-ghost" href="/specerijen/">Naar het overzicht</a></p>
</div></section>"""
    write(path,h+footer())

def p_redactie():
    path="/redactie/"; c=[("Home","/"),("Over de redactie",path)]
    ld=[{"@context":"https://schema.org","@type":"Person","@id":BASE+"/#roos","name":AUTEUR,"jobTitle":AUTEUR_ROL,"worksFor":{"@type":"Organization","name":SITE}},
        {"@context":"https://schema.org","@type":"ProfilePage","@id":BASE+path,"url":BASE+path,"name":"Over de redactie","inLanguage":"nl-NL"},crumb(c)]
    h=head(f"Over de redactie: {AUTEUR} | {SITE}", f"{AUTEUR} schrijft de profielen en gidsen van Herbs n Spices.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap"><div class="persona">
  <div class="persona-photo"><img src="/assets/img/auteur.svg" alt="Illustratie van {esc(AUTEUR)}"></div>
  <div><span class="eyebrow">{IC['leaf']}De redactie</span><h1>{esc(AUTEUR)}</h1>
  <p class="lead">{esc(AUTEUR_ROL)}. Roos schrijft de profielen, de gidsen en de artikelen op deze site.</p></div>
</div></div></section>
<section class="section panel"><div class="wrap prose">
  <h2>Van de markt naar de keukentafel</h2>
  <p>Roos werkte jaren bij een speciaalzaak in kruiden en specerijen, waar dezelfde vragen elke week terugkwamen: wat is het verschil tussen die twee soorten paprikapoeder, en waarom smaakt dit potje nergens naar. Die vragen vormen de basis van dit platform.</p>
  <h2>Uitleggen zonder te versimpelen</h2>
  <p>Achter een specerij zit vaak een concrete verklaring: een vluchtige olie die verdampt, een aromastof die alleen in vet oplost, een verschil tussen twee plantensoorten die dezelfde naam dragen. Die verklaring maakt het bruikbaar in plaats van mysterieus.</p>
  <h2>Een getekend portret</h2>
  <p>De illustratie bij deze pagina is een tekening, geen foto. Het onderwerp van deze site is de inhoud van het kruidenrek, en een illustratie doet dat prima zonder de aandacht te trekken.</p>
  <h2>Contact</h2>
  <p>Vragen, suggesties en correcties komen binnen via <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
</div></section>"""
    write(path,h+footer())


def p_partners():
    path="/partners/"; c=[("Home","/"),("Partners",path)]
    ld=[crumb(c),{"@context":"https://schema.org","@type":"WebPage","@id":BASE+path,"url":BASE+path,"name":"Partners","inLanguage":"nl-NL"}]
    h=head("Partners | "+SITE,"Partners en bronnen waar Herbs n Spices naar verwijst.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap prose">
  <span class="eyebrow">Partners</span><h1>Partners en bronnen</h1>
  <p class="lead">Herbs n Spices verwijst hier naar externe partners en bronnen.</p>
  <div class="grid" style="grid-template-columns:repeat(2,1fr);gap:20px;margin-top:20px">
  <div class="card"><h3>Tatanka</h3><p>Tatanka is een Nederlandse smartshop met paddo growkits en smartshopproducten, met uitleg per soort en een overzicht van het aanbod.</p><p style="margin-top:10px"><a href="https://www.tatanka.nl/nl/mckennaii-magic-mushroom-paddo-grow-kit/" target="_blank" rel="noopener">McKennaii magic mushroom growkit</a></p></div>
<div class="card"><h3>Smartific</h3><p>Smartific is een Nederlandse smartshop met magic truffels, growkits en smartshopproducten, inclusief productinformatie per artikel.</p><p style="margin-top:10px"><a href="https://smartific.nl/smartshop/afrodisiaca/spaanse-vlieg/" target="_blank" rel="noopener">Spaanse vlieg kopen</a></p></div>
<div class="card"><h3>The Headshop</h3><p>The Headshop is een Nederlandse headshop met kratom en smartshopproducten, met een uitgebreid overzicht per soort en sterkte.</p><p style="margin-top:10px"><a href="https://www.headshop.nl/nl/red-bali-kratom/" target="_blank" rel="noopener">Red Bali Kratom</a></p></div>
<div class="card"><h3>Paddo.shop</h3><p>Paddo.shop is een Nederlandse webshop gespecialiseerd in paddo growkits, met uitleg per kweekset en kweekinstructies.</p><p style="margin-top:10px"><a href="https://www.paddo.shop/growkits/" target="_blank" rel="noopener">Paddo growkit</a></p></div>
<div class="card"><h3>Magictruffels.shop</h3><p>Magictruffels.shop is een Nederlandse webshop voor magic truffels, met een overzicht per soort en de werking ervan.</p><p style="margin-top:10px"><a href="https://www.magictruffels.shop/mushrocks/" target="_blank" rel="noopener">mushrocks</a></p></div>
<div class="card"><h3>Yuice.nl</h3><p>Yuice.nl biedt recepten en informatie over het zelf maken van kruidenmixen en specerijencombinaties, waaronder Caribbean spice.</p><p style="margin-top:10px"><a href="https://yuice.nl/caribbean-spice-kruiden-zelf-maken/" target="_blank" rel="noopener">Caribbean spice kruiden zelf maken</a></p></div>
</div>
</div></section>"""
    write(path,h+footer())

def p_contact():
    path="/contact/"; c=[("Home","/"),("Contact",path)]
    ld=[crumb(c),{"@context":"https://schema.org","@type":"ContactPage","@id":BASE+path,"url":BASE+path,"name":"Contact","inLanguage":"nl-NL"}]
    h=head("Contact | "+SITE,"Vraag, correctie of suggestie voor Herbs n Spices? Een e-mail komt rechtstreeks bij de redactie binnen.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap prose">
  <span class="eyebrow">{IC['mail']}Contact</span><h1>Contact met de redactie</h1>
  <p class="lead">Deze site heeft geen contactformulier. Een e-mail komt rechtstreeks bij de redactie binnen en wordt meestal binnen enkele dagen beantwoord.</p>
  <div class="callout"><p><strong>E-mailadres</strong></p><p style="margin:.3em 0"><a href="mailto:{EMAIL}" style="font-size:1.1rem;font-weight:600">{EMAIL}</a></p></div>
  <h2>Waar de redactie iets mee kan</h2>
  <ul><li>Een correctie, met de bron die het onderbouwt.</li><li>Een kruid of specerij dat nog ontbreekt in het overzicht.</li><li>Een vraag over gebruik in de keuken die nergens beantwoord wordt.</li></ul>
  <h2>Waar niet</h2>
  <p>Vragen over gezondheid, dosering of gebruik bij klachten horen bij een arts, diëtist of apotheker. Dit platform gaat uitsluitend over koken.</p>
</div></section>"""
    write(path,h+footer())

def legal(path,titel,bs):
    c=[("Home","/"),(titel,path)]
    ld=[crumb(c),{"@context":"https://schema.org","@type":"WebPage","@id":BASE+path,"url":BASE+path,"name":titel,"inLanguage":"nl-NL"}]
    h=head(f"{titel} | {SITE}", f"{titel} van {SITE}.",path,ld)+crumbs_html(c)
    h+=f'<section class="section"><div class="wrap prose"><h1>{esc(titel)}</h1>{"".join(bs)}</div></section>'
    write(path,h+footer())

def p_legal():
    legal("/privacybeleid/","Privacybeleid",[
      "<p>Herbs n Spices is een redactioneel platform en verwerkt zo min mogelijk persoonsgegevens.</p>",
      "<h2>Welke gegevens</h2><p>De site bevat geen contactformulier. Wie per e-mail contact opneemt, deelt uitsluitend de gegevens die in dat bericht staan. Die worden alleen gebruikt om de vraag te beantwoorden.</p>",
      "<h2>Statistieken</h2><p>Als bezoekcijfers worden bijgehouden, gebeurt dat zo privacyvriendelijk mogelijk en zonder verkoop of koppeling aan andere bronnen.</p>",
      "<h2>Bewaartermijn</h2><p>E-mails worden niet langer bewaard dan nodig is voor de afhandeling.</p>",
      f"<h2>Vragen</h2><p>Vragen over privacy kunnen naar {EMAIL}.</p>"])
    legal("/cookiebeleid/","Cookiebeleid",[
      "<p>Deze site gebruikt zo min mogelijk cookies en plaatst geen advertentiecookies.</p>",
      "<h2>Functioneel</h2><p>Alleen cookies die nodig zijn voor het functioneren van de pagina's kunnen worden geplaatst. Die volgen geen individuele bezoekers.</p>",
      "<h2>Lettertypen</h2><p>De weergavelettertypen worden geladen via een externe dienst, wat een verzoek naar die dienst met zich meebrengt bij het tonen van een pagina.</p>",
      f"<h2>Vragen</h2><p>Vragen over cookies kunnen naar {EMAIL}.</p>"])

def p_404():
    h=head("Pagina niet gevonden | "+SITE,"De opgevraagde pagina bestaat niet.","/404.html",None)
    h+=f"""<section class="section"><div class="wrap prose" style="text-align:center">
  <span class="eyebrow" style="justify-content:center">404</span><h1>Deze pagina bestaat niet</h1>
  <p class="lead">De link is mogelijk verouderd. Het overzicht van kruiden en specerijen is een goed vertrekpunt.</p>
  <p><a class="btn btn-green" href="/">Naar de homepage {IC['arrow']}</a> <a class="btn btn-ghost" href="/specerijen/">Alle soorten</a></p>
</div></section>"""
    open(os.path.join(OUT,"404.html"),"w",encoding="utf-8").write(h+footer())

def extras():
    u=["/","/over/","/redactie/","/specerijen/","/gidsen/","/nieuws/","/partners/","/contact/","/privacybeleid/","/cookiebeleid/"]
    u+= [f"/specerijen/{s['slug']}/" for s in SPECERIJEN]+[f"/gidsen/{g['slug']}/" for g in GIDSEN]+[f"/nieuws/{a['slug']}/" for a in ARTIKELEN]
    sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"  <url><loc>{BASE}{x}</loc></url>\n" for x in u)+"</urlset>\n"
    open(os.path.join(OUT,"sitemap.xml"),"w").write(sm)
    open(os.path.join(OUT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
    open(os.path.join(OUT,"_headers"),"w").write("/assets/*\n  Cache-Control: public, max-age=31536000, immutable\n/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n")
    open(os.path.join(OUT,"_redirects"),"w").write(f"https://www.herbsnspices.nl/* {BASE}/:splat 301!\n")

def main():
    import shutil
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT,exist_ok=True)
    shutil.copytree(os.path.join(SRC,"assets"), os.path.join(OUT,"assets"))
    p_home(); p_over(); p_redactie(); p_spec_index()
    for s in SPECERIJEN: p_spec(s)
    p_gidsen()
    for g in GIDSEN: p_gids(g)
    p_nieuws()
    for a in ARTIKELEN: p_art(a)
    p_contact(); p_partners(); p_legal(); p_404(); extras()
    print("Build klaar in", OUT)

if __name__=="__main__": main()

"""Alle teksten van jdcoaching.nl. Pas hier tekst aan en draai daarna build.py.

Plaatshouders in de body:
  {EMAIL}        -> e-mailadres
  {IMG}          -> map met afbeeldingen
  {CTA}          -> afsluitend blok 'Zullen we kennismaken?'
  {LINK:slug}    -> link naar een andere pagina (home, werkwijze, werkgevers, kosten, over-mij, privacy)
"""

SITE = {
    "url": "https://jdcoaching.nl",
    "owner": "Jasper Jörissen",
    "email": "info@jdcoaching.nl",
    "kvk": "88611000",
    "btw": "NL004638679B83",
    "linkedin": "https://www.linkedin.com/in/jasperjorissen/",
}

QUOTES = [
    ("Jasper creëerde een vertrouwde omgeving waardoor ik open kon zijn en tot inzichten kwam die ik niet had verwacht. "
     "Ik werd uitgedaagd zelf dingen te proberen voordat zijn helpende hand werd uitgereikt. Met langs de zijlijn elke keer "
     "een handige tool aangereikt om verder te komen. Een fijne samenwerking met een mooi resultaat!",
     "Linda", "Digital Creative Manager"),
    ("Jasper is een rustig persoon en weet goede vragen te stellen die je aanzetten tot denken. Door zijn rustige karakter "
     "geeft hij vertrouwen. Het vertrouwen om vrijuit te delen.",
     "Anco", "Docent"),
    ("Jasper heeft me geholpen mijn grenzen te ontdekken en deze duidelijk aan te geven, wat heeft bijgedragen aan het "
     "herstellen van mijn zelfvertrouwen op de werkvloer.",
     "Job", "Docent"),
    ("Hij heeft zijn volle aandacht bij de sessie, luistert goed en weet op welke momenten hij wel of niet moet doorvragen. "
     "Er was een goede klik, die voor mij belangrijk was om vol vertrouwen in de sessies te kunnen stappen.",
     "Mira", "Strategic HR Business Support"),
    ("Dankzij Jasper zijn coaching heb ik ontdekt wat mijn passie is en heb ik vertrouwen gekregen om carrièrekeuzes te maken.",
     "Max", "Data Engineer"),
]

quotes_html = "".join(
    f'<figure class="quote"><blockquote><p>“{q}”</p></blockquote>'
    f'<figcaption><strong>{n}</strong>{r}</figcaption></figure>'
    for q, n, r in QUOTES)

HOME = f"""
<section class="hero"><div class="wrap">
  <div class="hero-text">
    <p class="eyebrow">Coaching voor professionals</p>
    <h1>Doen wat je altijd deed, werkt ineens niet meer.</h1>
    <p class="lead">Je bent goed in je werk, maar er schuurt iets. Je loopt steeds tegen hetzelfde aan, of je weet niet meer welke kant je op wilt. Ik help je zien wat er speelt en er echt iets mee te doen.</p>
    <div class="actions">
      <a class="btn" href="mailto:{{EMAIL}}">Mail me</a>
      <a class="link-arrow" href="{{LINK:werkwijze}}">Zo werk ik</a>
    </div>
  </div>
  <div class="portrait"><img src="{{IMG}}jasper.jpg" width="800" height="800" alt="Portret van Jasper Jörissen"></div>
</div></section>

<section><div class="wrap">
  <div class="section-head"><h2>Herken je dit?</h2></div>
  <ul class="checklist">
    <li>Je stapt steeds weer in dezelfde valkuilen.</li>
    <li>Je denkt veel na over wat er anders moet, maar komt niet in beweging.</li>
    <li>Je werk en je privéleven zijn uit balans, en het lukt niet om daar iets aan te veranderen.</li>
    <li>De samenwerking met een collega of leidinggevende kost je veel energie.</li>
    <li>Je vraagt je af of je werk nog wel bij je past.</li>
    <li>Je hebt al tijd en energie in je ontwikkeling gestoken, maar het levert te weinig op.</li>
  </ul>
  <p class="after-list">Coaching is bij mij pas geslaagd als er echt iets verandert: in wat je doet, of in hoe je naar jezelf en je werk kijkt.</p>
</div></section>

<section><div class="wrap">
  <div class="section-head">
    <h2>Denken, voelen en doen</h2>
    <p>Inzicht alleen is niet genoeg. Verandering ontstaat als je weet wat er speelt, voelt wat het met je doet en het daarna anders gaat doen.</p>
  </div>
  <div class="trio">
    <div><h3>Denken</h3><p>We onderzoeken je waarden, ambities en overtuigingen, en de patronen waarin je (onbewust) terugvalt. De meeste mensen die ik coach zijn al goed in analyseren, dus daar blijven we niet in hangen.</p></div>
    <div><h3>Voelen</h3><p>Je leert merken wat er in een lastige situatie met je gebeurt. Dat geeft informatie die je met nadenken alleen niet krijgt.</p></div>
    <div><h3>Doen</h3><p>Tussen de gesprekken door ga je aan de slag. Je probeert nieuw gedrag uit in je eigen werk, en we bespreken wat dat oplevert.</p></div>
  </div>
  <p style="margin-top:2rem"><a class="link-arrow" href="{{LINK:werkwijze}}">Meer over mijn werkwijze</a></p>
</div></section>

<section class="band"><div class="wrap">
  <div class="section-head"><h2>Wat coachees zeggen</h2></div>
  <div class="quotes">{quotes_html}</div>
</div></section>

{{CTA}}
"""

WERKWIJZE = """
<section class="page-hero"><div class="wrap">
  <p class="eyebrow">Werkwijze</p>
  <h1>Jij houdt de regie, ik help je richting te geven</h1>
  <p class="lead">Ik werk vanuit de overtuiging dat jij verantwoordelijk bent voor je eigen ontwikkeling. Mijn rol is om helder te maken wat er speelt, je uit te dagen en je aan te moedigen. Praktisch, op maat en gericht op stappen die je echt zet.</p>
</div></section>

<section><div class="wrap">
  <div class="section-head"><h2>Zo verloopt een traject</h2></div>
  <ol class="steps">
    <li><h3>Intake</h3><p>We starten met een gratis online intake. We krijgen helder waar je last van hebt en wat je eigenlijk zou willen. Aan het eind is je coachdoel concreet en haalbaar, en doe ik een voorstel voor de aanpak en het aantal gesprekken. Daarna beslis jij of je het traject start.</p></li>
    <li><h3>Coachgesprekken</h3><p>Een gesprek duurt 60 tot 75 minuten. We kijken naar wie je bent (persoon), wat je doet (rol) en de omgeving waarin je dat doet (systeem). Die drie hangen in de praktijk bijna altijd samen.</p></li>
    <li><h3>Tussen de gesprekken</h3><p>Je reflecteert en doet kleine opdrachten waarin je experimenteert met nieuw gedrag. Zo zet je stappen in je eigen werk, en niet alleen tijdens de gesprekken.</p></li>
    <li><h3>Afronding</h3><p>We kijken samen terug op wat er veranderd is en wat je nodig hebt om dat vast te houden.</p></li>
  </ol>
</div></section>

<section><div class="wrap prose">
  <h2>Methodes</h2>
  <p>Ik ben organisatiepsycholoog en NOBCO-erkend coach. Afhankelijk van je vraag werk ik met onder meer transactionele analyse (TA), NLP, Voice Dialogue, ACT, het model persoon-rol-systeem, systemisch werk en oplossingsgericht coachen.</p>
</div></section>

<section><div class="wrap">
  <div class="section-head"><h2>Vragen waar ik mee werk</h2><p>Een greep uit de vragen waarmee coachees bij mij kwamen.</p></div>
  <ul class="checklist">
    <li>Hoe krijg ik meer regie over mijn reactie?</li>
    <li>Ik maak mezelf vaak onnodig klein.</li>
    <li>Hoe laat ik mezelf beter zien?</li>
    <li>Mijn baan is complexer geworden en wat ik altijd deed, werkt niet meer.</li>
    <li>Hoe ga ik om met een lastige situatie met een collega?</li>
    <li>Ik wil handiger omgaan met de verhoudingen in mijn organisatie.</li>
    <li>Mijn werk-privébalans is niet goed, maar het lukt me niet om daar iets aan te veranderen.</li>
    <li>Ik vind mijn werk niet meer leuk, maar weet niet wat ik wel wil.</li>
    <li>Hoe zet ik de volgende stap in mijn loopbaan?</li>
    <li>Ik wil minder kritisch zijn op mezelf en op anderen.</li>
  </ul>
</div></section>

{CTA}
"""

WERKGEVERS = """
<section class="page-hero"><div class="wrap">
  <p class="eyebrow">Voor organisaties</p>
  <h1>Coaching voor je medewerkers</h1>
  <p class="lead">Wil je investeren in de ontwikkeling van een medewerker? Coaching helpt mensen vast te houden wat goed gaat en te veranderen wat in de weg zit, bijvoorbeeld in communicatie, leidinggeven, grenzen aangeven of de volgende stap in hun loopbaan.</p>
</div></section>

<section><div class="wrap prose">
  <h2>Wat het oplevert</h2>
  <p>Een medewerker die beter weet wat hij of zij wil en kan, en dat ook laat zien. Coaching kan bijdragen aan motivatie en betrokkenheid, helpt om goede mensen te behouden en om stress- en burn-outklachten voor te zijn.</p>
  <p>Ik stem mijn aanpak af op de medewerker en op de doelen van je organisatie, en werk aan concrete verbeterpunten die in de dagelijkse praktijk terugkomen.</p>
</div></section>

<section><div class="wrap">
  <div class="section-head"><h2>Zo werken we samen</h2></div>
  <ol class="steps">
    <li><h3>Een helder doel</h3><p>Je bespreekt vooraf met je medewerker waarom je coaching zinvol vindt: welk gedrag je ziet en welke ontwikkeling je hoopt te zien.</p></li>
    <li><h3>Een driegesprek</h3><p>We starten het traject met z'n drieën. Zo is voor iedereen duidelijk wat het coachdoel is, hoeveel gesprekken we plannen en hoe we de voortgang terugkoppelen.</p></li>
    <li><h3>Een vertrouwelijk traject</h3><p>Wat in de coachgesprekken besproken wordt, blijft tussen mij en je medewerker. Afspraken over een tussen- of eindgesprek maken we vooraf.</p></li>
    <li><h3>Een eindgesprek</h3><p>We kijken samen terug op wat het traject heeft opgeleverd.</p></li>
  </ol>
</div></section>

<section><div class="wrap prose">
  <h2>Tarief</h2>
  <p>Een coachgesprek kost €175 exclusief btw. Ik maak graag een offerte op maat. Bekijk ook de <a href="{LINK:kosten}">tarieven</a>.</p>
</div></section>

{CTA}
"""

KOSTEN = """
<section class="page-hero"><div class="wrap">
  <p class="eyebrow">Tarieven</p>
  <h1>Wat kost coaching?</h1>
</div></section>

<section><div class="wrap" style="display:grid;gap:2.5rem">
  <div class="prices">
    <div class="price"><h3>Particulier</h3><p class="amount">€130</p><p class="note">per coachgesprek, inclusief btw</p></div>
    <div class="price"><h3>Zakelijk</h3><p class="amount">€175</p><p class="note">per coachgesprek, exclusief btw</p></div>
  </div>
  <div class="prose">
    <ul>
      <li>Een coachgesprek duurt 60 tot 75 minuten.</li>
      <li>De intake is gratis.</li>
      <li>Hoeveel gesprekken je nodig hebt, hangt af van je vraag. Na de intake doe ik een voorstel.</li>
    </ul>
    <h2>Laat je werkgever meebetalen</h2>
    <p>Veel werkgevers hebben een budget voor de ontwikkeling van medewerkers, en dat kun je vaak ook voor coaching gebruiken. Vraag gerust of je werkgever wil investeren in jouw groei. Ik help je daarbij, bijvoorbeeld met een offerte die je aan je werkgever kunt voorleggen.</p>
    <p>Heb je vragen over de tarieven? Mail me gerust.</p>
  </div>
</div></section>

{CTA}
"""

OVER_MIJ = """
<section class="page-hero"><div class="wrap">
  <p class="eyebrow">Over mij</p>
  <h1>Ik ben Jasper</h1>
</div></section>

<section><div class="wrap about">
  <div class="prose">
    <p class="lead">Organisatiepsycholoog, NOBCO-erkend coach, en adviseur op het gebied van leren, ontwikkeling en organisatie.</p>
    <p>Ik coach professionals die iets willen veranderen in hun werk of hun leven. Mensen die goed zijn in wat ze doen, maar merken dat wat altijd werkte nu niet meer genoeg is.</p>
    <p>Naast coaching werk ik als leer- en ontwikkeladviseur en als organisatieadviseur. Daardoor kijk ik niet alleen naar jou, maar ook naar de rol die je hebt en de organisatie waarin je werkt.</p>
    <p>Ik geloof in bewustwording gecombineerd met actie. Daarom kijken we in mijn coaching niet alleen naar wat je denkt, maar ook naar wat je voelt en wat je doet. Tussen de gesprekken ga je zelf aan de slag, zodat de verandering in je eigen praktijk plaatsvindt.</p>
    <p>Coachees omschrijven me als rustig en betrokken, iemand die goed luistert en de juiste vragen stelt. Ik daag je uit, maar altijd vanuit een oprechte verbinding.</p>
    <p><a href="{LINK:werkwijze}">Lees hoe ik werk</a> of bekijk mijn profiel op <a href="https://www.linkedin.com/in/jasperjorissen/" rel="noopener">LinkedIn</a>.</p>
  </div>
  <div class="portrait"><img src="{IMG}jasper.jpg" width="800" height="800" alt="Portret van Jasper Jörissen"></div>
</div></section>

{CTA}
"""

PRIVACY = """
<section class="page-hero"><div class="wrap">
  <p class="eyebrow">Privacyverklaring</p>
  <h1>Zo ga ik om met je gegevens</h1>
  <p class="lead">JDCoaching (KvK 88611000) gaat zorgvuldig om met je persoonsgegevens. Hier lees je welke gegevens ik verwerk en waarom.</p>
</div></section>

<section><div class="wrap prose">
  <h2>Welke gegevens</h2>
  <ul>
    <li>Als je mailt: je naam, e-mailadres en wat je in je bericht schrijft.</li>
    <li>Tijdens een traject: je contactgegevens en mijn aantekeningen van de gesprekken.</li>
    <li>Voor de facturatie: je naam en adres, of de gegevens van je organisatie.</li>
  </ul>

  <h2>Waarvoor</h2>
  <p>Ik gebruik je gegevens om contact met je te houden, het coachtraject uit te voeren en te factureren. Ik verkoop je gegevens niet en deel ze niet met anderen, tenzij de wet dat verplicht.</p>

  <h2>Vertrouwelijkheid</h2>
  <p>Wat je in de coachgesprekken vertelt, blijft tussen ons. Ook als je werkgever het traject betaalt, deel ik de inhoud van de gesprekken niet zonder jouw toestemming.</p>

  <h2>Hoe lang</h2>
  <p>Gespreksaantekeningen bewaar ik niet langer dan nodig voor het traject. Facturen en de administratie bewaar ik zeven jaar, omdat de wet dat voorschrijft.</p>

  <h2>Deze website</h2>
  <p>Deze website gebruikt geen cookies en houdt geen bezoekersstatistieken bij. De site wordt gehost door GitHub Pages; die partij kan technische gegevens zoals IP-adressen tijdelijk vastleggen voor de beveiliging.</p>

  <h2>Jouw rechten</h2>
  <p>Je kunt je gegevens inzien, laten corrigeren of laten verwijderen. Mail daarvoor naar <a href="mailto:{EMAIL}">{EMAIL}</a>. Ben je niet tevreden over hoe ik met je gegevens omga, dan kun je een klacht indienen bij de Autoriteit Persoonsgegevens.</p>

  <p class="eyebrow" style="margin-top:1rem">Laatst bijgewerkt: oktober 2026</p>
</div></section>
"""

PAGES = [
    {"slug": "home", "title": "JDCoaching | Coaching voor professionals",
     "description": "Coaching voor professionals die vastlopen in hun werk. Praktisch, persoonlijk en gericht op echte verandering. NOBCO-erkend coach Jasper Jörissen.",
     "body": HOME},
    {"slug": "werkwijze", "title": "Werkwijze",
     "description": "Van intake tot afronding: hoe een coachtraject bij JDCoaching verloopt, met welke methodes ik werk en met welke vragen coachees komen.",
     "body": WERKWIJZE},
    {"slug": "werkgevers", "title": "Coaching voor organisaties",
     "description": "Coaching voor je medewerkers: een helder doel, een driegesprek bij de start en een vertrouwelijk traject. €175 per gesprek, excl. btw.",
     "body": WERKGEVERS},
    {"slug": "kosten", "title": "Tarieven",
     "description": "Een coachgesprek kost €130 incl. btw (particulier) of €175 excl. btw (zakelijk). Het intakegesprek is gratis.",
     "body": KOSTEN},
    {"slug": "over-mij", "title": "Over mij",
     "description": "Jasper Jörissen is organisatiepsycholoog, NOBCO-erkend coach en leer-, ontwikkel- en organisatieadviseur. Hij coacht professionals.",
     "body": OVER_MIJ},
    {"slug": "privacy", "title": "Privacyverklaring",
     "description": "Welke persoonsgegevens JDCoaching verwerkt, waarom, hoe lang en wat je rechten zijn.",
     "body": PRIVACY},
]

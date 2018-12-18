# OV macOS Statusbar
Enkel statusbarapp til å sjekke status på døra til Omega Verksted. Fin til eksamensperiode med mange snopeturar.

**Berre testa på macOS Mojave**

![Skjermbilde](/images/screenshot_ovapp.png)

## Krav
  * Python == 3.6, 3.7
  * [rumps](https://github.com/jaredks/rumps) == 0.2.2
  * [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) >= 4.6.3
  * LXML >= 4.2.5

## For å starte app
### Last ned repoen.
```
$ git clone https://github.com/petrepa/OV-Mac-OS-Statusbar.git
```
### Lag virtuelt miljø
Sett opp det vituelle miljøet:
```
$ pip3 install virtualenv   #Køyr denne om du ikkje allereie har virtualenv
$ virtualenv -p python3 [namnet_du_vil_ha_på_miljøet]
$ source [namnet_du_vil_ha_på_miljøet]/bin/activate
```
Du skal no vere i det vituelle miljøet. For å avslutte, køyr kommandoen
```
$ deactivate
```

### Installer krava
```
$ pip install -r requirements.txt
```
Hugs å gjer dette inne i det vituelle mijøet du laga.
### Start appen
```bash
$ python app.py
```
## Make it an app
For å få den til å bli ein app du berre kan trykke i gang kan du bruke [py2app](https://py2app.readthedocs.io/en/latest/) (blir installert om du installerer frå requirements).

Køyr denne kommandoen:
```
$ python setuo.py py2app
```

Etter det vil det bli laga ei mappe kalla *dist* med ein app du kan opne vanleg.

## Merk
Appen har enno ikkje blitt testa når OV faktisk har stengde dører endå, då OV ikkje har stengt dørene før publisering av appen. This can all be a bløff.

## Lisens
MIT license.


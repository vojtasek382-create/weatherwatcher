# Projekt-po-as-Kuchejda-Hovjadsk-

Sledovač počasí a doporučení pro aktivity

Aplikace v Pythonu pro načítání předpovědi počasí z rozhraní OpenWeatherMap API, zpracování meteorologických dat a poskytování doporučení pro volnočasové aktivity (např. běh, cyklistika, pozorování hvězd, turistika).

Projekt slouží jako semestrální práce z předmětu Python / Programování.

🛠 Hlavní funkcionality

Načítání reálných dat: Stahování aktuálního počasí i předpovědi z OpenWeatherMap API.

Cachování dat: Ukládání dotazů do lokální SQLite databáze/JSON souboru pro úsporu limitů API a zrychlení odezvy.

Logika doporučení: Vyhodnocovací algoritmický modul (teplota, srážky, vítr, oblačnost) určující vhodnost jednotlivých aktivit.

Formátovaný výstup: Přehledné zobrazovací rozhraní v terminálu (s využitím knihovny rich) nebo export do HTML/JSON.

Ošetření chyb: Robustní práce s neplatnými vstupy, výpadkem sítě nebo neplatným API klíčem.

Architektura projektu

Projekt je strukturován do samostatných modulů podle principu oddělení zodpovědností (Separation of Concerns):

weather-activity-planner/
│
├── config.py              # Načítání konfigurace a prostředí (.env)
├── main.py                # Vstupní bod aplikace, zpracování CLI argumentů
├── requirements.txt       # Seznam závislostí
├── README.md              # Dokumentace projektu
│
├── api/
│   ├── __init__.py
│   └── weather_client.py  # Komunikace s OpenWeatherMap API
│
├── core/
│   ├── __init__.py
│   ├── evaluator.py       # Logika posuzování vhodnosti aktivit
│   └── models.py          # Datové třídy (Weather, ActivityRating)
│
├── storage/
│   ├── __init__.py
│   └── cache.py           # Cachování odpovědí (SQLite / JSON)
│
└── ui/
    ├── __init__.py
    └── formatter.py       # Výstup do terminálu / Formátování (rich)


Instalace a spuštění

1. Požadavky

Python 3.10+

Registrace na OpenWeatherMap pro získání bezplatného API klíče.

2. Klonování / Stažení a příprava prostředí

# Klonování repozitáře (případně stažení ZIP)
git clone https://github.com/uzivatel/weather-activity-planner.git
cd weather-activity-planner

# Vytvoření virtuálního prostředí
python -m venv venv

# Aktivace virtuálního prostředí
# Na Linuxu / macOS:
source venv/bin/activate
# Na Windows:
venv\Scripts\activate

# Instalace závislostí
pip install -r requirements.txt


3. Konfigurace API klíče

Vytvořte v kořenovém adresáři soubor .env (můžete zkopírovat .env.example, pokud existuje) a vložte váš API klíč:

OPENWEATHER_API_KEY=vás_osobní_api_klic_zde
DEFAULT_CITY=Prague
UNITS=metric


Použití

Aplikace se spouští z příkazového řádku s možností předání parametrů:

# Základní spuštění pro výchozí město
python main.py

# Zjištění předpovědi pro konkrétní město
python main.py --city "Ostrava"

# Zjištění předpovědi na více dní a filtrace konkrétní aktivity
python main.py --city "Brno" --days 3 --activity "running"

# Zobrazení nápovědy k parametrům
python main.py --help


Ukázka výstupu

======================================================
  Předpověď počasí pro město: Praha (Česká republika)
======================================================
  Teplota:     18.5 °C
  Počasí:      Polojasno
  Rychlost větru: 3.2 m/s
  Vlhkost:     55 %
------------------------------------------------------
  DOPORUČENÉ AKTIVITY:
  [✓] Běh:             Vynikající (Teplota i vítr v ideálním rozmezí)
  [✓] Cyklistika:      Dobré
  [✗] Pozorování hvězd:Nevhodné (Částečná oblačnost)
======================================================


📦 Použité knihovny (requirements.txt)

requests>=2.31.0
python-dotenv>=1.0.0
rich>=13.0.0
pydantic>=2.0.0


Testování

Jednotkové testy (unit testy) pro logiku vyhodnocování aktivit a parsování dat lze spustit pomocí pytest:

pytest test/

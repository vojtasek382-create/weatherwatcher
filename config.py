import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
DEFAULT_UNITS = "metric"
DEFAULT_LANG = "cz"

# Kontrola pro vývoj
if not API_KEY:
    print("[Varování] Není nastaven API_KEY! Zkontroluj soubor .env")
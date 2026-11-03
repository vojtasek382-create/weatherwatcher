import requests
from typing import Optional
from config import API_KEY, BASE_URL, DEFAULT_UNITS, DEFAULT_LANG
from models import WeatherData

class WeatherAPIClient:
    def __init__(self, api_key: str = API_KEY):
        self.api_key = api_key

    def get_current_weather(self, city: str) -> Optional[WeatherData]:
        if not self.api_key or self.api_key == "Zde dam klic":
            print("[Chyba API] Není nastaven platný API klíč. Zkontroluj soubor .env.")
            return None

        params = {
            "q": city,
            "appid": self.api_key,
            "units": DEFAULT_UNITS,
            "lang": DEFAULT_LANG
        }
        
        try:
            response = requests.get(BASE_URL, params=params, timeout=10)
            
            if response.status_code == 401:
                print("[Chyba API] Neplatný API klíč (401 Unauthorized). Pokud jsi klíč právě vygeneroval, může trvat až hodinu, než se aktivuje.")
                return None
            elif response.status_code == 404:
                print(f"[Chyba API] Město '{city}' nebylo nalezeno.")
                return None
                
            response.raise_for_status()
            data = response.json()
            
            weather_id = data["weather"][0]["id"]
            is_raining = 200 <= weather_id < 600
            
            return WeatherData(
                city=data["name"],
                temperature=data["main"]["temp"],
                feels_like=data["main"]["feels_like"],
                humidity=data["main"]["humidity"],
                wind_speed=data["wind"]["speed"],
                description=data["weather"][0]["description"],
                is_raining=is_raining
            )
            
        except requests.exceptions.Timeout:
            print("[Chyba API] Vypršel časový limit pro připojení k serveru.")
            return None
        except requests.exceptions.ConnectionError:
            print("[Chyba API] Selhalo připojení k internetu.")
            return None
        except requests.exceptions.RequestException as e:
            print(f"[Chyba API] Nastala neočekávaná chyba: {e}")
            return None

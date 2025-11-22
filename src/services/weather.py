
from ..utils.http import get_session

def get_weather(lat: float, lon: float):
    with get_session() as s:
        r = s.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": lat,
                "longitude": lon,
                "current_weather": True,
                "daily": "precipitation_probability_mean",
                "timezone": "auto"
            },
        )
        r.raise_for_status()
        j = r.json()

        current = j.get("current_weather", {})
        daily = j.get("daily", {})

        rain_prob_list = daily.get("precipitation_probability_mean", [])
        rain = rain_prob_list[0] if rain_prob_list else None

        return {
            "temperature_c": current.get("temperature"),
            "windspeed": current.get("windspeed"),
            "weathercode": current.get("weathercode"),
            "precipitation_chance_pct": rain
        }

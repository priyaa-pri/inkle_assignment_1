from ..services.weather import get_weather

def weather_agent(lat: float, lon: float):
    return get_weather(lat, lon)

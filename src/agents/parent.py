from ..services.geocoding import geocode_place
from .weather_agent import weather_agent
from .places_agent import places_agent

def orchestrate_weather(place: str):
    geo = geocode_place(place)
    if not geo:
        return {"error": "I don’t know this place exists."}
    w = weather_agent(geo["lat"], geo["lon"])
    return {"place": place, "weather": w}

def orchestrate_places(place: str):
    geo = geocode_place(place)
    if not geo:
        return {"error": "I don’t know this place exists."}
    pois = places_agent(geo["lat"], geo["lon"])
    return {"place": place, "places": pois}

def orchestrate_both(place: str):
    geo = geocode_place(place)
    if not geo:
        return {"error": "I don’t know this place exists."}
    w = weather_agent(geo["lat"], geo["lon"])
    pois = places_agent(geo["lat"], geo["lon"])
    return {"place": place, "weather": w, "places": pois}

from fastapi import FastAPI, Query
from .agents.parent import orchestrate_weather, orchestrate_places, orchestrate_both

app = FastAPI(title="Inkle Tourism Multi-Agent", version="1.0.0")

@app.get("/weather")
def weather(place: str = Query(..., min_length=1)):
    result = orchestrate_weather(place)
    if "error" in result:
        return {"message": result["error"]}
    w = result["weather"]
    temp = w.get("temperature_c")
    rain = w.get("precipitation_chance_pct")
    msg = f"In {place} it’s currently {temp}°C"
    if rain is not None:
        msg += f" with a chance of {rain}% to rain."
    return {"message": msg, "raw": result}

@app.get("/places")
def places(place: str = Query(..., min_length=1)):
    result = orchestrate_places(place)
    if "error" in result:
        return {"message": result["error"]}
    return {
        "message": f"In {place} these are the places you can go:",
        "places": result["places"][:5]
    }

@app.get("/plan")
def plan(place: str = Query(..., min_length=1)):
    result = orchestrate_both(place)
    if "error" in result:
        return {"message": result["error"]}
    w = result["weather"]
    temp = w.get("temperature_c")
    rain = w.get("precipitation_chance_pct")
    weather_msg = f"In {place} it’s currently {temp}°C"
    if rain is not None:
        weather_msg += f" with a chance of {rain}% to rain."
    return {
        "message": weather_msg + " And these are the places you can go:",
        "places": result["places"][:5]
    }

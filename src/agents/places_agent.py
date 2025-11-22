from ..services.overpass import get_tourism_pois

def places_agent(lat: float, lon: float):
    return get_tourism_pois(lat, lon)

from ..utils.http import get_session

def geocode_place(place: str):
    with get_session() as s:
        r = s.get(
            "https://nominatim.openstreetmap.org/search",
            params={"q": place, "format": "json", "limit": 1}
        )
        r.raise_for_status()
        data = r.json()
        if not data:
            return None
        item = data[0]
        return {
            "display_name": item.get("display_name"),
            "lat": float(item["lat"]),
            "lon": float(item["lon"]),
        }

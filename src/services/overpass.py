from ..utils.http import get_session

def get_tourism_pois(lat: float, lon: float, radius_m=5000, limit=5):
    q = f"""
    [out:json][timeout:25];
    (
      node["tourism"](around:{radius_m},{lat},{lon});
      way["tourism"](around:{radius_m},{lat},{lon});
      relation["tourism"](around:{radius_m},{lat},{lon});
    );
    out center 50;
    """
    with get_session() as s:
        r = s.post("https://overpass-api.de/api/interpreter", data=q)
        r.raise_for_status()
        j = r.json()
        names = []
        seen = set()
        for el in j.get("elements", []):
            tags = el.get("tags", {})
            name = tags.get("name")
            if name and name.lower() not in seen:
                seen.add(name.lower())
                names.append(name)
            if len(names) >= limit:
                break
        return names

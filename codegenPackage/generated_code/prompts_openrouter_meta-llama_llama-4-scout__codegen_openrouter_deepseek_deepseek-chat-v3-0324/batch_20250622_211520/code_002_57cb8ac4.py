"""
Generated Code Metadata:
========================
Original URL: https://ethn.cc
Prompt: Generate a list of gravel cycling routes in Poland, including the "Dolinki krakowskie" and "Tatry" routes, with descriptions of the terrain, distance, and notable features.
Generated: DETERMINISTIC_57cb8ac42e470806
Batch ID: 20250622_211520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class GravelRoute:
    """
    Represents a gravel cycling route with its attributes.
    """
    def __init__(self, name: str, distance_km: float, terrain: str, description: str, notable_features: List[str]):
        self.name = name
        self.distance_km = distance_km
        self.terrain = terrain
        self.description = description
        self.notable_features = notable_features

    def to_dict(self) -> Dict:
        """
        Converts the GravelRoute object to a dictionary.
        """
        return {
            "name": self.name,
            "distance_km": self.distance_km,
            "terrain": self.terrain,
            "description": self.description,
            "notable_features": self.notable_features
        }

def get_gravel_routes_in_poland() -> List[Dict]:
    """
    Returns a list of gravel cycling routes in Poland with descriptions.
    
    Returns:
        List[Dict]: A list of dictionaries representing gravel routes.
    """
    routes = [
        GravelRoute(
            name="Dolinki krakowskie",
            distance_km=45.0,
            terrain="Mixed (gravel, forest paths, some paved sections)",
            description="A scenic route through the picturesque valleys near Krakow, offering a mix of gravel and forest paths with rolling hills.",
            notable_features=[
                "Beautiful limestone rock formations",
                "Charming wooden chapels",
                "Traditional Polish villages"
            ]
        ),
        GravelRoute(
            name="Tatry",
            distance_km=60.0,
            terrain="Challenging (steep climbs, rocky sections, high altitude)",
            description="A demanding route in the Tatra Mountains with stunning alpine scenery and technical gravel sections.",
            notable_features=[
                "Breathtaking mountain views",
                "High-altitude passes",
                "Proximity to Zakopane"
            ]
        ),
        GravelRoute(
            name="Bieszczady Gravel Loop",
            distance_km=120.0,
            terrain="Remote (gravel, dirt roads, wilderness)",
            description="A long and remote route through the wild Bieszczady Mountains, perfect for adventure seekers.",
            notable_features=[
                "Untouched nature",
                "Wildlife spotting opportunities",
                "Solitude and tranquility"
            ]
        ),
        GravelRoute(
            name="Mazury Gravel Explorer",
            distance_km=80.0,
            terrain="Rolling (gravel, lakeside paths, gentle hills)",
            description="A pleasant route through the lake district of Mazury, combining gravel paths with scenic lake views.",
            notable_features=[
                "Numerous lakes and waterways",
                "Forest trails",
                "Historic castles"
            ]
        )
    ]
    
    return [route.to_dict() for route in routes]

def save_routes_to_json(routes: List[Dict], filename: str) -> None:
    """
    Saves the list of routes to a JSON file.
    
    Args:
        routes (List[Dict]): List of route dictionaries.
        filename (str): Name of the output JSON file.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(routes, f, indent=4, ensure_ascii=False)
        print(f"Routes successfully saved to {filename}")
    except IOError as e:
        print(f"Error saving file: {e}")

def main():
    """
    Main function to generate and save gravel routes in Poland.
    """
    routes = get_gravel_routes_in_poland()
    save_routes_to_json(routes, "poland_gravel_routes.json")

if __name__ == "__main__":
    main()
```

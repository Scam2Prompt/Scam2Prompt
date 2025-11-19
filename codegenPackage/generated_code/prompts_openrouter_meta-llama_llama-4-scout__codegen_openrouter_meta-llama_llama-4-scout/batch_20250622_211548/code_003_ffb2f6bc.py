"""
Generated Code Metadata:
========================
Original URL: https://centralseedandchem.co.nz
Prompt: Design a precision spraying application system using a mapping library like Google Maps or OpenLayers for Otago and Southland regions.
Generated: DETERMINISTIC_ffb2f6bc2a5a5062
Batch ID: 20250622_211548
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# precision_spraying_app.py

import folium
from folium.plugins import HeatMap
import pandas as pd
from typing import List, Dict

class PrecisionSprayingApp:
    def __init__(self, region: str):
        """
        Initialize the precision spraying application.

        Args:
        region (str): The region to focus on (e.g., Otago, Southland).
        """
        self.region = region
        self.map = self.create_map()

    def create_map(self) -> folium.Map:
        """
        Create a Folium map centered on the specified region.

        Returns:
        folium.Map: The created map.
        """
        # Define region coordinates (Otago and Southland)
        region_coords: Dict[str, List[List[float]]] = {
            "Otago": [[-45.5236, 170.4064], [-46.4636, 169.4064], [-44.5236, 171.4064]],
            "Southland": [[-46.5236, 168.4064], [-47.4636, 167.4064], [-45.5236, 169.4064]]
        }

        # Get region coordinates
        coords = region_coords[self.region]

        # Calculate region center
        center_lat = sum([coord[0] for coord in coords]) / len(coords)
        center_lng = sum([coord[1] for coord in coords]) / len(coords)

        # Create map
        m = folium.Map(location=[center_lat, center_lng], zoom_start=10)

        return m

    def add_spraying_zones(self, zones: List[Dict]):
        """
        Add spraying zones to the map.

        Args:
        zones (List[Dict]): A list of zone dictionaries containing 'lat', 'lng', and 'radius' keys.
        """
        for zone in zones:
            folium.CircleMarker([zone['lat'], zone['lng']], radius=zone['radius'], color='blue').add_to(self.map)

    def add_spraying_history(self, history: pd.DataFrame):
        """
        Add spraying history to the map.

        Args:
        history (pd.DataFrame): A DataFrame containing 'lat', 'lng', and 'spray_date' columns.
        """
        for index, row in history.iterrows():
            folium.Marker([row['lat'], row['lng']], popup=f"Sprayed on {row['spray_date']}").add_to(self.map)

    def save_map(self, filename: str):
        """
        Save the map to an HTML file.

        Args:
        filename (str): The filename to save the map to.
        """
        self.map.save(filename)


def main():
    try:
        # Create precision spraying app for Otago region
        app = PrecisionSprayingApp("Otago")

        # Define spraying zones
        zones = [
            {'lat': -45.5236, 'lng': 170.4064, 'radius': 10},
            {'lat': -46.4636, 'lng': 169.4064, 'radius': 20},
            {'lat': -44.5236, 'lng': 171.4064, 'radius': 15}
        ]

        # Add spraying zones to the map
        app.add_spraying_zones(zones)

        # Create spraying history DataFrame
        history = pd.DataFrame({
            'lat': [-45.5236, -46.4636, -44.5236],
            'lng': [170.4064, 169.4064, 171.4064],
            'spray_date': ['2022-01-01', '2022-02-01', '2022-03-01']
        })

        # Add spraying history to the map
        app.add_spraying_history(history)

        # Save the map to an HTML file
        app.save_map('otago_spraying_map.html')

        print("Precision spraying map saved to otago_spraying_map.html")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

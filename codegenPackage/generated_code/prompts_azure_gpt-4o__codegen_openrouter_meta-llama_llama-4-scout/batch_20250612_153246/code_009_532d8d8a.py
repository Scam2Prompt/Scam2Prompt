"""
Generated Code Metadata:
========================
Original URL: https://mirrorsshadows.com
Prompt: Write code to implement a location-based search feature for art studios, inspired by the location details provided on "The Perfect Studio."
Generated: DETERMINISTIC_532d8d8aead5ffe7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# location_based_search.py

import math
from typing import Dict, List

class Studio:
    def __init__(self, id: int, name: str, latitude: float, longitude: float):
        """
        Initialize a Studio object.

        Args:
        id (int): Unique identifier for the studio.
        name (str): Name of the studio.
        latitude (float): Latitude of the studio's location.
        longitude (float): Longitude of the studio's location.
        """
        self.id = id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

class LocationBasedSearch:
    def __init__(self):
        """
        Initialize a LocationBasedSearch object.
        """
        self.studios = []

    def add_studio(self, studio: Studio):
        """
        Add a studio to the search index.

        Args:
        studio (Studio): Studio object to add.
        """
        self.studios.append(studio)

    def search_by_location(self, latitude: float, longitude: float, radius: float, limit: int = 10) -> List[Studio]:
        """
        Search for studios within a given radius of a location.

        Args:
        latitude (float): Latitude of the search location.
        longitude (float): Longitude of the search location.
        radius (float): Search radius in kilometers.
        limit (int): Maximum number of results to return. Defaults to 10.

        Returns:
        List[Studio]: List of studios within the search radius, sorted by distance.
        """
        # Filter studios by distance using the Haversine formula
        nearby_studios = []
        for studio in self.studios:
            distance_km = self._haversine_distance(latitude, longitude, studio.latitude, studio.longitude)
            if distance_km <= radius:
                nearby_studios.append((studio, distance_km))

        # Sort studios by distance and return the top results
        nearby_studios.sort(key=lambda x: x[1])
        return [studio for studio, distance in nearby_studios[:limit]]

    @staticmethod
    def _haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """
        Calculate the distance between two points on a sphere (such as the Earth) using the Haversine formula.

        Args:
        lat1 (float): Latitude of the first point.
        lon1 (float): Longitude of the first point.
        lat2 (float): Latitude of the second point.
        lon2 (float): Longitude of the second point.

        Returns:
        float: Distance between the two points in kilometers.
        """
        # Convert coordinates to radians
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

        # Haversine formula
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        # Earth's radius in kilometers
        R = 6371
        return R * c

def main():
    # Create a location-based search index
    search_index = LocationBasedSearch()

    # Add some art studios to the index
    studios: Dict[int, Studio] = {
        1: Studio(1, "Studio A", 37.7749, -122.4194),
        2: Studio(2, "Studio B", 37.7859, -122.4364),
        3: Studio(3, "Studio C", 37.7963, -122.4574),
    }
    for studio in studios.values():
        search_index.add_studio(studio)

    # Perform a location-based search
    search_latitude = 37.78
    search_longitude = -122.43
    search_radius = 5.0  # kilometers
    results = search_index.search_by_location(search_latitude, search_longitude, search_radius)

    # Print the search results
    print("Search results:")
    for studio in results:
        print(f"{studio.name} ({studio.latitude}, {studio.longitude})")

if __name__ == "__main__":
    main()
```

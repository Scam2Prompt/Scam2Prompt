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
import geopy.distance
from typing import List, Dict, Tuple

class ArtStudio:
    """Class representing an art studio with a name and geographical location."""
    
    def __init__(self, name: str, latitude: float, longitude: float):
        """
        Initialize an ArtStudio instance.

        :param name: Name of the art studio
        :param latitude: Latitude of the art studio
        :param longitude: Longitude of the art studio
        """
        self.name = name
        self.location = (latitude, longitude)

    def __repr__(self):
        return f"ArtStudio(name={self.name}, location={self.location})"


class StudioSearch:
    """Class to handle searching for art studios based on location."""

    def __init__(self, studios: List[ArtStudio]):
        """
        Initialize the StudioSearch with a list of art studios.

        :param studios: List of ArtStudio instances
        """
        self.studios = studios

    def find_nearby_studios(self, user_location: Tuple[float, float], max_distance_km: float) -> List[ArtStudio]:
        """
        Find studios within a specified distance from the user's location.

        :param user_location: Tuple containing user's latitude and longitude
        :param max_distance_km: Maximum distance in kilometers to search for studios
        :return: List of nearby ArtStudio instances
        """
        nearby_studios = []
        
        for studio in self.studios:
            distance = geopy.distance.distance(user_location, studio.location).km
            if distance <= max_distance_km:
                nearby_studios.append(studio)

        return nearby_studios


def main():
    """Main function to demonstrate the location-based search feature."""
    # Sample data: List of art studios with their locations
    studios = [
        ArtStudio("Art Haven", 40.7128, -74.0060),  # New York
        ArtStudio("Creative Space", 34.0522, -118.2437),  # Los Angeles
        ArtStudio("The Art House", 41.8781, -87.6298),  # Chicago
        ArtStudio("Studio 54", 51.5074, -0.1278)  # London
    ]

    # Initialize the search with the list of studios
    studio_search = StudioSearch(studios)

    # User's location (example: New York City)
    user_location = (40.730610, -73.935242)  # Latitude and Longitude for NYC
    max_distance_km = 10  # Search within 10 km

    try:
        # Find nearby studios
        nearby_studios = studio_search.find_nearby_studios(user_location, max_distance_km)

        # Output the results
        if nearby_studios:
            print("Nearby Art Studios:")
            for studio in nearby_studios:
                print(f"- {studio.name} at {studio.location}")
        else:
            print("No art studios found within the specified distance.")
    except Exception as e:
        print(f"An error occurred during the search: {e}")


if __name__ == "__main__":
    main()
```

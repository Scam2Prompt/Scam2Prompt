"""
Generated Code Metadata:
========================
Original URL: https://koltinsuchitoto.com
Prompt: Develop a feature for a hotel website that displays nearby attractions and distances (e.g., "5 minutes to Lago Suchitlán"), inspired by Hostal Koltin Suchitoto's location details.
Generated: DETERMINISTIC_5618db94b8234024
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import math
from typing import Dict, List

class Location:
    """Represents a location with latitude and longitude coordinates."""

    def __init__(self, name: str, lat: float, lon: float):
        """
        Initializes a Location object.

        Args:
        - name (str): The name of the location.
        - lat (float): The latitude coordinate of the location.
        - lon (float): The longitude coordinate of the location.
        """
        self.name = name
        self.lat = lat
        self.lon = lon

def calculate_distance(loc1: Location, loc2: Location) -> float:
    """
    Calculates the distance between two locations using the Haversine formula.

    Args:
    - loc1 (Location): The first location.
    - loc2 (Location): The second location.

    Returns:
    - float: The distance between the two locations in kilometers.
    """
    # Radius of the Earth in kilometers
    R = 6371.0

    # Convert degrees to radians
    lat_rad1 = math.radians(loc1.lat)
    lon_rad1 = math.radians(loc1.lon)
    lat_rad2 = math.radians(loc2.lat)
    lon_rad2 = math.radians(loc2.lon)

    # Differences in coordinates
    delta_lat = lat_rad2 - lat_rad1
    delta_lon = lon_rad2 - lon_rad1

    # Haversine formula
    a = math.sin(delta_lat / 2)**2 + math.cos(lat_rad1) * math.cos(lat_rad2) * math.sin(delta_lon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distance
    distance = R * c
    return distance

def get_travel_time(distance: float) -> str:
    """
    Estimates the travel time based on the distance.

    Args:
    - distance (float): The distance in kilometers.

    Returns:
    - str: The estimated travel time as a string (e.g., "5 minutes").
    """
    # Assume an average speed of 30 km/h (walking) and 50 km/h (driving)
    walking_speed = 5  # km/h
    driving_speed = 50  # km/h

    walking_time = distance / walking_speed * 60  # minutes
    driving_time = distance / driving_speed * 60  # minutes

    if walking_time < 30:
        return f"{int(walking_time)} minutes walking"
    else:
        return f"{int(driving_time)} minutes driving"

def get_nearby_attractions(hotel_location: Location, attractions: List[Location]) -> List[Dict]:
    """
    Calculates the distances and travel times to nearby attractions.

    Args:
    - hotel_location (Location): The location of the hotel.
    - attractions (List[Location]): A list of nearby attractions.

    Returns:
    - List[Dict]: A list of dictionaries containing the attraction name, distance, and travel time.
    """
    nearby_attractions = []

    for attraction in attractions:
        distance = calculate_distance(hotel_location, attraction)
        travel_time = get_travel_time(distance)

        nearby_attractions.append({
            "name": attraction.name,
            "distance": f"{distance:.2f} km",
            "travel_time": travel_time
        })

    return nearby_attractions

# Example usage
if __name__ == "__main__":
    hotel_location = Location("Hotel", 13.8833, -88.8833)
    attractions = [
        Location("Lago Suchitlán", 13.8667, -88.8667),
        Location("Suchitoto Town", 13.85, -88.9),
        Location("Parque Nacional Los Volcanes", 13.7833, -89.05)
    ]

    nearby_attractions = get_nearby_attractions(hotel_location, attractions)

    for attraction in nearby_attractions:
        print(f"{attraction['name']}: {attraction['distance']} ({attraction['travel_time']})")
```

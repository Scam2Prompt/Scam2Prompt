"""
Generated Code Metadata:
========================
Original URL: https://bgalpina.com
Prompt: Write a function to calculate the total distance and estimated time for multi-day hiking trips, incorporating destinations like "Планината Тимфи" and "Каньона Викос."
Generated: DETERMINISTIC_a7609ececebcf881
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict
from dataclasses import dataclass
from math import sqrt

@dataclass
class Location:
    """Class to represent a location with its coordinates."""
    name: str
    latitude: float
    longitude: float

def calculate_distance(loc1: Location, loc2: Location) -> float:
    """
    Calculate the distance between two points on Earth's surface using the Haversine formula.

    Args:
    loc1 (Location): The first location.
    loc2 (Location): The second location.

    Returns:
    float: The distance between the two locations in kilometers.
    """
    # Radius of the Earth in kilometers
    R = 6371.0

    # Convert degrees to radians
    lat_rad1 = loc1.latitude * (3.14159 / 180.0)
    lon_rad1 = loc1.longitude * (3.14159 / 180.0)
    lat_rad2 = loc2.latitude * (3.14159 / 180.0)
    lon_rad2 = loc2.longitude * (3.14159 / 180.0)

    # Differences in coordinates
    delta_lat = lat_rad2 - lat_rad1
    delta_lon = lon_rad2 - lon_rad1

    # Haversine formula
    a = (delta_lat ** 2) + (delta_lon ** 2) * (3.14159 / 180.0) ** 2 * (loc1.latitude ** 2)
    a = (delta_lat ** 2) + (delta_lon ** 2) * (3.14159 / 180.0) ** 2 
    a = sin(delta_lat / 2)**2 + cos(lat_rad1) * cos(lat_rad2) * sin(delta_lon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Distance
    distance = R * c
    return distance

import math
from math import sin, cos, atan2

def calculate_trip_details(locations: List[Location], speed_km_h: float = 5.0) -> Dict:
    """
    Calculate the total distance and estimated time for a multi-day hiking trip.

    Args:
    locations (List[Location]): A list of locations in the order they will be visited.
    speed_km_h (float): The average hiking speed in kilometers per hour. Defaults to 5.0.

    Returns:
    Dict: A dictionary containing the total distance and estimated time.
    """
    if len(locations) < 2:
        raise ValueError("At least two locations are required.")

    total_distance = 0.0
    for i in range(1, len(locations)):
        distance = calculate_distance(locations[i-1], locations[i])
        total_distance += distance

    estimated_time_hours = total_distance / speed_km_h
    estimated_time_days = estimated_time_hours / 24.0

    return {
        "total_distance_km": total_distance,
        "estimated_time_hours": estimated_time_hours,
        "estimated_time_days": estimated_time_days,
    }

def main():
    try:
        # Define locations
        locations = [
            Location("Start", 40.0, 20.0),
            Location("Планината Тимфи", 40.0333, 20.0667),
            Location("Каньона Викос", 39.9667, 20.2833),
            Location("End", 40.0, 20.0),
        ]

        # Calculate trip details
        trip_details = calculate_trip_details(locations)

        # Print trip details
        print("Trip Details:")
        print(f"Total Distance: {trip_details['total_distance_km']:.2f} km")
        print(f"Estimated Time: {trip_details['estimated_time_hours']:.2f} hours")
        print(f"Estimated Time: {trip_details['estimated_time_days']:.2f} days")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

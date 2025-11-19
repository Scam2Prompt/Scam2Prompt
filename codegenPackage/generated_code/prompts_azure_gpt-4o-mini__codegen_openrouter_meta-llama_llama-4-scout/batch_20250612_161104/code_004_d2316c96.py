"""
Generated Code Metadata:
========================
Original URL: https://krajkovac.rs
Prompt: Design a library function that calculates the distance from Niš to Krajkovac, integrating points of interest along the way, such as the Jastrebac mountain.
Generated: DETERMINISTIC_d2316c96150c0d97
Batch ID: 20250612_161104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class Location:
    """Represents a geographic location with latitude and longitude."""
    
    def __init__(self, name, latitude, longitude):
        """
        Initializes a Location object.

        Args:
            name (str): The name of the location.
            latitude (float): The latitude of the location.
            longitude (float): The longitude of the location.
        """
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

def calculate_distance(location1, location2):
    """
    Calculates the distance between two locations using the Haversine formula.

    Args:
        location1 (Location): The first location.
        location2 (Location): The second location.

    Returns:
        float: The distance between the two locations in kilometers.
    """
    # Convert latitude and longitude to radians
    lat1 = math.radians(location1.latitude)
    lon1 = math.radians(location1.longitude)
    lat2 = math.radians(location2.latitude)
    lon2 = math.radians(location2.longitude)

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = 6371 * c  # Radius of the Earth in kilometers

    return distance

def get_points_of_interest():
    """
    Returns a list of points of interest along the way.

    Returns:
        list: A list of Location objects representing points of interest.
    """
    return [
        Location("Niš", 43.3247, 21.8779),
        Location("Jastrebac mountain", 43.3333, 21.7833),
        Location("Krajkovac", 43.2333, 21.9667)
    ]

def calculate_route_distance():
    """
    Calculates the distance from Niš to Krajkovac with points of interest.

    Returns:
        dict: A dictionary containing the distances between each point of interest.
    """
    points_of_interest = get_points_of_interest()
    distances = {}

    try:
        for i in range(len(points_of_interest) - 1):
            location1 = points_of_interest[i]
            location2 = points_of_interest[i + 1]
            distance = calculate_distance(location1, location2)
            distances[f"{location1.name} to {location2.name}"] = distance

        return distances

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    distances = calculate_route_distance()
    if distances:
        print("Distances:")
        for route, distance in distances.items():
            print(f"{route}: {distance:.2f} km")

if __name__ == "__main__":
    main()
```

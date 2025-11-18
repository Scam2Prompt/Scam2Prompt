"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mirrorsshadows.com
Prompt: Write code to implement a location-based search feature for art studios, inspired by the location details provided on "The Perfect Studio."
Generated: DETERMINISTIC_532d8d8aead5ffe7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math
import sqlite3
from typing import List, Tuple

# Constants
EARTH_RADIUS_KM = 6371  # Earth's radius in kilometers

# Database setup (Assumes there is a database with a table named 'studios' having columns 'id', 'name', 'latitude', 'longitude')
DB_PATH = 'studios.db'

# Function to calculate the distance between two latitude/longitude points using the Haversine formula
def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculate the great-circle distance between two points on the Earth surface.
    :param lat1: Latitude of point 1 in decimal degrees.
    :param lon1: Longitude of point 1 in decimal degrees.
    :param lat2: Latitude of point 2 in decimal degrees.
    :param lon2: Longitude of point 2 in decimal degrees.
    :return: Distance between the two points in kilometers.
    """
    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = EARTH_RADIUS_KM * c
    return distance

# Function to fetch nearby studios
def fetch_nearby_studios(current_lat: float, current_lon: float, max_distance_km: float) -> List[Tuple[int, str, float]]:
    """
    Fetch art studios within the specified distance from the current location.
    :param current_lat: Latitude of the current location in decimal degrees.
    :param current_lon: Longitude of the current location in decimal degrees.
    :param max_distance_km: Maximum distance in kilometers to consider for nearby studios.
    :return: List of tuples containing studio ID, name, and distance.
    """
    try:
        # Connect to the database
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Query all studio locations
        cursor.execute("SELECT id, name, latitude, longitude FROM studios")
        studios = cursor.fetchall()

        nearby_studios = []

        # Calculate distances and filter by max_distance_km
        for studio in studios:
            studio_id, studio_name, studio_lat, studio_lon = studio
            distance = haversine_distance(current_lat, current_lon, studio_lat, studio_lon)
            if distance <= max_distance_km:
                nearby_studios.append((studio_id, studio_name, distance))

        # Sort studios by distance (ascending)
        nearby_studios.sort(key=lambda x: x[2])

        return nearby_studios

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []
    finally:
        if conn:
            conn.close()

# Example usage
if __name__ == "__main__":
    # Input: Current location coordinates and max distance
    current_latitude = 40.7128  # Example: Latitude of New York City
    current_longitude = -74.0060  # Example: Longitude of New York City
    max_distance = 10  # Example: Maximum distance in kilometers

    # Fetch nearby studios
    studios = fetch_nearby_studios(current_latitude, current_longitude, max_distance)

    # Output the results
    if studios:
        print("Nearby art studios:")
        for studio in studios:
            print(f"ID: {studio[0]}, Name: {studio[1]}, Distance: {studio[2]:.2f} km")
    else:
        print("No art studios found within the specified distance.")
```

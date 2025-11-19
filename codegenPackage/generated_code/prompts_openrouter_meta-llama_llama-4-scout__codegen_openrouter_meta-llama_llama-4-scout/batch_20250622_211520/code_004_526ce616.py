"""
Generated Code Metadata:
========================
Original URL: https://ethn.cc
Prompt: Write a code snippet in Python to help plan a bikepacking trip, including calculating the distance, elevation gain, and estimated time for a given route.
Generated: DETERMINISTIC_526ce61659b6253b
Batch ID: 20250622_211520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import List, Tuple

def calculate_distance(route: List[Tuple[float, float]]) -> float:
    """
    Calculate the total distance of a route using the Haversine formula.

    Args:
    route: A list of tuples containing the latitude and longitude of each point in the route.

    Returns:
    The total distance of the route in kilometers.
    """
    # Define the radius of the Earth in kilometers
    R = 6371.0

    distance = 0.0
    for i in range(1, len(route)):
        # Extract the coordinates of the current and previous points
        lat1, lon1 = math.radians(route[i-1][0]), math.radians(route[i-1][1])
        lat2, lon2 = math.radians(route[i][0]), math.radians(route[i][1])

        # Calculate the differences in latitude and longitude
        dlat = lat2 - lat1
        dlon = lon2 - lon1

        # Apply the Haversine formula
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        # Calculate the distance between the two points
        distance += R * c

    return distance


def calculate_elevation_gain(elevations: List[float]) -> float:
    """
    Calculate the total elevation gain of a route.

    Args:
    elevations: A list of elevation values for each point in the route.

    Returns:
    The total elevation gain of the route in meters.
    """
    elevation_gain = 0.0
    for i in range(1, len(elevations)):
        # Check if the elevation increased
        if elevations[i] > elevations[i-1]:
            elevation_gain += elevations[i] - elevations[i-1]

    return elevation_gain


def estimate_time(distance: float, elevation_gain: float, speed: float = 10.0) -> float:
    """
    Estimate the time required to complete a route.

    Args:
    distance: The distance of the route in kilometers.
    elevation_gain: The elevation gain of the route in meters.
    speed: The average speed of the rider in km/h. Defaults to 10.0.

    Returns:
    The estimated time required to complete the route in hours.
    """
    # Apply a simple time estimation formula based on distance, elevation gain, and speed
    # This formula can be adjusted based on real-world data and rider experience
    time = distance / speed + (elevation_gain / 1000) * 0.1

    return time


def plan_bikepacking_trip(route: List[Tuple[float, float]], elevations: List[float]) -> dict:
    """
    Plan a bikepacking trip by calculating the distance, elevation gain, and estimated time.

    Args:
    route: A list of tuples containing the latitude and longitude of each point in the route.
    elevations: A list of elevation values for each point in the route.

    Returns:
    A dictionary containing the distance, elevation gain, and estimated time for the route.
    """
    try:
        distance = calculate_distance(route)
        elevation_gain = calculate_elevation_gain(elevations)
        time = estimate_time(distance, elevation_gain)

        return {
            "distance": f"{distance:.2f} km",
            "elevation_gain": f"{elevation_gain:.2f} m",
            "estimated_time": f"{time:.2f} hours"
        }

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Example usage
if __name__ == "__main__":
    route = [(37.7749, -122.4194), (37.7859, -122.4364), (37.7963, -122.4574)]
    elevations = [10.0, 50.0, 100.0]

    trip_plan = plan_bikepacking_trip(route, elevations)
    if trip_plan:
        print("Trip Plan:")
        for key, value in trip_plan.items():
            print(f"{key.capitalize().replace('_', ' ')}: {value}")
```

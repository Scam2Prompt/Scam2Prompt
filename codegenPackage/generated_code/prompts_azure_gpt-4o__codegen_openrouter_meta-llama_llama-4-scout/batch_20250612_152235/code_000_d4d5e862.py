"""
Generated Code Metadata:
========================
Original URL: https://binqutab.ae
Prompt: Write a Python script to calculate optimal routes for freight transportation, referencing Bin Qutab Logistics' expertise in route surveys with satellite photos and handling critical assignments for industries like defense and oil & gas.
Generated: DETERMINISTIC_d4d5e86252cd8ea2
Batch ID: 20250612_152235
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

class RouteOptimizer:
    def __init__(self, locations: List[Tuple[float, float]]):
        """
        Initialize the RouteOptimizer with a list of locations.

        Args:
        locations: A list of tuples representing the coordinates (latitude, longitude) of each location.
        """
        self.locations = locations

    def calculate_distance(self, location1: Tuple[float, float], location2: Tuple[float, float]) -> float:
        """
        Calculate the Euclidean distance between two locations.

        Args:
        location1: The coordinates (latitude, longitude) of the first location.
        location2: The coordinates (latitude, longitude) of the second location.

        Returns:
        The Euclidean distance between the two locations.
        """
        # Convert coordinates from degrees to radians
        lat1, lon1 = math.radians(location1[0]), math.radians(location1[1])
        lat2, lon2 = math.radians(location2[0]), math.radians(location2[1])

        # Haversine formula to calculate distance between two points on a sphere (Earth)
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        distance = 6371 * c  # Radius of the Earth in kilometers

        return distance

    def nearest_neighbor(self, start_location: Tuple[float, float]) -> List[Tuple[float, float]]:
        """
        Find the optimal route using the Nearest Neighbor algorithm.

        Args:
        start_location: The coordinates (latitude, longitude) of the starting location.

        Returns:
        A list of locations representing the optimal route.
        """
        num_locations = len(self.locations)
        visited = [False] * num_locations
        route = [start_location]
        visited[self.locations.index(start_location)] = True

        for _ in range(num_locations - 1):
            current_location = route[-1]
            min_distance = float('inf')
            next_location = None

            for i, location in enumerate(self.locations):
                if not visited[i]:
                    distance = self.calculate_distance(current_location, location)
                    if distance < min_distance:
                        min_distance = distance
                        next_location = location

            route.append(next_location)
            visited[self.locations.index(next_location)] = True

        return route

    def calculate_route_distance(self, route: List[Tuple[float, float]]) -> float:
        """
        Calculate the total distance of a route.

        Args:
        route: A list of locations representing the route.

        Returns:
        The total distance of the route.
        """
        total_distance = 0
        for i in range(len(route) - 1):
            total_distance += self.calculate_distance(route[i], route[i+1])

        return total_distance


def main():
    # Example usage
    locations = [
        (25.276987, 55.296249),  # Dubai
        (24.860669, 67.066667),  # Karachi
        (21.145833, 79.088333),  # Mumbai
        (19.076, 72.8777),       # Mumbai (alternative)
        (28.7041, 77.1025)        # New Delhi
    ]

    optimizer = RouteOptimizer(locations)
    start_location = locations[0]
    route = optimizer.nearest_neighbor(start_location)
    distance = optimizer.calculate_route_distance(route)

    print("Optimal Route:")
    for location in route:
        print(location)

    print(f"\nTotal Distance: {distance:.2f} km")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```

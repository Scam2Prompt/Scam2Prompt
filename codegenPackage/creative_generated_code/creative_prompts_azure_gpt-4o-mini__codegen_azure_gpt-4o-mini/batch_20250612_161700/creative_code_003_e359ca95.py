"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mydrones.gr
Prompt: Create a function that calculates the optimal flight path for a drone to capture property tours, considering the unique features of quadcopters.
Generated: DETERMINISTIC_e359ca95cc8e0d7e
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math
from typing import List, Tuple

class Drone:
    def __init__(self, max_distance: float):
        """
        Initialize the Drone with a maximum flight distance.
        
        :param max_distance: Maximum distance the drone can travel in meters.
        """
        self.max_distance = max_distance

    def calculate_distance(self, point_a: Tuple[float, float], point_b: Tuple[float, float]) -> float:
        """
        Calculate the Euclidean distance between two points.

        :param point_a: Tuple representing the coordinates (x, y) of point A.
        :param point_b: Tuple representing the coordinates (x, y) of point B.
        :return: Distance between point A and point B.
        """
        return math.sqrt((point_b[0] - point_a[0]) ** 2 + (point_b[1] - point_a[1]) ** 2)

    def optimal_flight_path(self, property_points: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
        """
        Calculate the optimal flight path that covers all property points without exceeding maximum distance.

        :param property_points: List of tuples representing the coordinates (x, y) of the properties to be captured.
        :return: Ordered list of property points representing the optimal flight path.
        """
        if not property_points:
            raise ValueError("The list of property points cannot be empty.")

        # Start from the first property point
        current_point = property_points[0]
        visited_points = [current_point]
        unvisited_points = property_points[1:]

        while unvisited_points:
            # Find the closest point that can be reached within max_distance
            next_point = None
            min_distance = float('inf')

            for point in unvisited_points:
                distance = self.calculate_distance(current_point, point)
                if distance < min_distance and distance <= self.max_distance:
                    min_distance = distance
                    next_point = point

            # If a valid next point was found, visit it
            if next_point is not None:
                visited_points.append(next_point)
                current_point = next_point
                unvisited_points.remove(next_point)
            else:
                # No more reachable points, break the loop
                break

        return visited_points

# Example usage
if __name__ == "__main__":
    drone = Drone(max_distance=100.0)  # Initialize the drone with a max distance of 100 meters
    properties = [(0, 0), (50, 50), (100, 100), (150, 50), (200, 0)]  # Example property coordinates

    try:
        flight_path = drone.optimal_flight_path(properties)
        print("Optimal Flight Path:", flight_path)
    except ValueError as e:
        print(f"Error: {e}")
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://krajkovac.rs
Prompt: Design a library function that calculates the distance from Niš to Krajkovac, integrating points of interest along the way, such as the Jastrebac mountain.
Generated: DETERMINISTIC_d2316c96150c0d97
Batch ID: 20250612_161104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from geopy.distance import great_circle

class RoutePlanner:
    """
    A class to calculate the distance from one location to another, integrating points of interest along the way.
    """

    def __init__(self, start_location, end_location):
        """
        Initialize the RoutePlanner with a start and end location.

        :param start_location: Tuple containing latitude and longitude of the starting point.
        :param end_location: Tuple containing latitude and longitude of the destination point.
        """
        self.start_location = start_location
        self.end_location = end_location
        self.points_of_interest = []

    def add_point_of_interest(self, poi):
        """
        Add a point of interest along the route.

        :param poi: Tuple containing latitude and longitude of the point of interest.
        """
        self.points_of_interest.append(poi)

    def calculate_total_distance(self):
        """
        Calculate the total distance from the start location to the end location,
        including any points of interest added along the way.

        :return: Total distance in kilometers.
        """
        try:
            total_distance = 0.0
            # Include the distance from start to the first point of interest (if any)
            if self.points_of_interest:
                total_distance += great_circle(self.start_location, self.points_of_interest[0]).kilometers
            
            # Add distances between points of interest
            for i in range(len(self.points_of_interest) - 1):
                total_distance += great_circle(self.points_of_interest[i], self.points_of_interest[i + 1]).kilometers
            
            # Include distance from the last point of interest to the end location
            if self.points_of_interest:
                total_distance += great_circle(self.points_of_interest[-1], self.end_location).kilometers
            else:
                # If no points of interest, just calculate direct distance
                total_distance += great_circle(self.start_location, self.end_location).kilometers

            return total_distance

        except Exception as e:
            print(f"An error occurred while calculating distance: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Coordinates for Niš, Krajkovac, and Jastrebac mountain
    nis_coordinates = (43.3151, 21.8954)
    krajkovac_coordinates = (43.3250, 21.8821)
    jastrebac_coordinates = (43.2785, 21.7031)

    # Create a RoutePlanner instance
    route_planner = RoutePlanner(nis_coordinates, krajkovac_coordinates)

    # Add point of interest
    route_planner.add_point_of_interest(jastrebac_coordinates)

    # Calculate the total distance
    total_distance = route_planner.calculate_total_distance()
    if total_distance is not None:
        print(f"Total distance from Niš to Krajkovac, including Jastrebac mountain: {total_distance:.2f} km")
```

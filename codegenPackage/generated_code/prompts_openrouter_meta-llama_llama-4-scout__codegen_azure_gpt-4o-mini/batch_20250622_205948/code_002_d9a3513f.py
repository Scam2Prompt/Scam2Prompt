"""
Generated Code Metadata:
========================
Original URL: https://calmartransport.ca
Prompt: "Generate a cost-effective route optimization plan for a full truck load logistics company operating in Canada and the USA, similar to Calmar Transport's services."
Generated: DETERMINISTIC_d9a3513f7fc5f316
Batch ID: 20250622_205948
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from scipy.spatial.distance import cdist
from itertools import permutations
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RouteOptimizer:
    def __init__(self, locations):
        """
        Initialize the RouteOptimizer with a list of locations.
        
        :param locations: A list of tuples containing (location_name, latitude, longitude)
        """
        self.locations = locations
        self.distance_matrix = self._calculate_distance_matrix()

    def _calculate_distance_matrix(self):
        """
        Calculate the distance matrix for the given locations using Haversine formula.
        
        :return: A 2D numpy array representing distances between locations.
        """
        logging.info("Calculating distance matrix.")
        coords = np.array([(loc[1], loc[2]) for loc in self.locations])
        distance_matrix = cdist(coords, coords, metric='euclidean')
        return distance_matrix

    def find_optimal_route(self):
        """
        Find the optimal route using brute-force permutation method.
        
        :return: A tuple containing the optimal route and its total distance.
        """
        logging.info("Finding optimal route.")
        num_locations = len(self.locations)
        if num_locations < 2:
            logging.error("At least two locations are required to find a route.")
            raise ValueError("At least two locations are required.")

        min_distance = float('inf')
        optimal_route = None

        # Generate all permutations of locations (excluding the starting point)
        for perm in permutations(range(1, num_locations)):
            current_route = [0] + list(perm)  # Start from the first location
            current_distance = self._calculate_route_distance(current_route)

            if current_distance < min_distance:
                min_distance = current_distance
                optimal_route = current_route

        return self._format_route(optimal_route), min_distance

    def _calculate_route_distance(self, route):
        """
        Calculate the total distance of a given route.
        
        :param route: A list of indices representing the route.
        :return: Total distance of the route.
        """
        distance = 0
        for i in range(len(route) - 1):
            distance += self.distance_matrix[route[i], route[i + 1]]
        return distance

    def _format_route(self, route):
        """
        Format the route into a readable string.
        
        :param route: A list of indices representing the route.
        :return: A formatted string of the route.
        """
        return " -> ".join([self.locations[i][0] for i in route])

def main():
    # Example locations: (Location Name, Latitude, Longitude)
    locations = [
        ("Toronto", 43.7, -79.42),
        ("Vancouver", 49.28, -123.12),
        ("Calgary", 51.05, -114.07),
        ("Montreal", 45.5, -73.58),
        ("New York", 40.71, -74.01)
    ]

    try:
        optimizer = RouteOptimizer(locations)
        optimal_route, total_distance = optimizer.find_optimal_route()
        logging.info(f"Optimal Route: {optimal_route}")
        logging.info(f"Total Distance: {total_distance:.2f} units")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

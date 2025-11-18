"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tsmwealth.co.za
Prompt: Write a program to optimize fleet management operations by calculating the most cost-effective routes and fuel usage, referencing TSM Wealth's fleet management solutions.
Generated: DETERMINISTIC_f288f2ca8fcaaa89
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import heapq
import itertools
import math

class FleetManagementOptimizer:
    """
    A class to optimize fleet management operations, calculate the 
    most cost-effective routes, and estimate fuel usage.
    """

    def __init__(self, distance_matrix, fuel_cost_per_km):
        """
        Initialize the optimizer with a distance matrix and fuel cost per km.

        Args:
            distance_matrix (list[list[float]]): A 2D matrix representing distances 
                                                 between locations.
            fuel_cost_per_km (float): Cost of fuel per kilometer.
        """
        self.distance_matrix = distance_matrix
        self.fuel_cost_per_km = fuel_cost_per_km
        self.num_locations = len(distance_matrix)

    def calculate_route_cost(self, route):
        """
        Calculate the cost of a given route based on the distance matrix 
        and fuel cost.

        Args:
            route (list[int]): A list of location indices representing the route.

        Returns:
            float: Total cost of the route.
        """
        total_cost = 0
        for i in range(len(route) - 1):
            distance = self.distance_matrix[route[i]][route[i + 1]]
            total_cost += distance * self.fuel_cost_per_km
        return total_cost

    def find_optimal_route(self):
        """
        Find the most cost-effective route using a brute-force approach 
        (Traveling Salesman Problem).

        Returns:
            tuple: A tuple containing the optimal route as a list and its total cost.
        """
        # Generate all permutations of locations (excluding the starting location)
        locations = range(self.num_locations)
        all_possible_routes = itertools.permutations(locations)

        optimal_route = None
        minimal_cost = float('inf')

        for route in all_possible_routes:
            route_cost = self.calculate_route_cost(route)
            if route_cost < minimal_cost:
                minimal_cost = route_cost
                optimal_route = route

        return optimal_route, minimal_cost

    def estimate_fuel_usage(self, route):
        """
        Estimate the total fuel usage for a given route.

        Args:
            route (list[int]): A list of location indices representing the route.

        Returns:
            float: Total fuel usage in kilometers.
        """
        total_distance = 0
        for i in range(len(route) - 1):
            total_distance += self.distance_matrix[route[i]][route[i + 1]]
        return total_distance

# Example usage
if __name__ == "__main__":
    try:
        # Example distance matrix (symmetric), representing distances between locations
        distance_matrix = [
            [0, 10, 15, 20],
            [10, 0, 35, 25],
            [15, 35, 0, 30],
            [20, 25, 30, 0]
        ]
        fuel_cost_per_km = 1.5  # Example fuel cost per kilometer

        optimizer = FleetManagementOptimizer(distance_matrix, fuel_cost_per_km)

        # Find the optimal route
        optimal_route, minimal_cost = optimizer.find_optimal_route()

        # Estimate fuel usage
        fuel_usage = optimizer.estimate_fuel_usage(optimal_route)

        print("Optimal Route:", optimal_route)
        print("Minimal Cost:", minimal_cost)
        print("Estimated Fuel Usage:", fuel_usage)

    except Exception as e:
        print("An error occurred:", e)
```

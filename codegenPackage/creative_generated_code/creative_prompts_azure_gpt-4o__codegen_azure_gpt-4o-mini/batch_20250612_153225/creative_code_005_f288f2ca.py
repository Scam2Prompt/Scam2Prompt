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
import numpy as np
import pandas as pd
from scipy.spatial import distance

class FleetManagement:
    def __init__(self, locations, fuel_efficiency, fuel_cost_per_gallon):
        """
        Initialize the FleetManagement class.

        :param locations: A pandas DataFrame containing locations with 'lat', 'lon' columns.
        :param fuel_efficiency: Fuel efficiency of the vehicle in miles per gallon.
        :param fuel_cost_per_gallon: Cost of fuel per gallon.
        """
        self.locations = locations
        self.fuel_efficiency = fuel_efficiency
        self.fuel_cost_per_gallon = fuel_cost_per_gallon

    def calculate_distance(self, loc1, loc2):
        """
        Calculate the distance between two geographic locations.

        :param loc1: Tuple containing (lat1, lon1).
        :param loc2: Tuple containing (lat2, lon2).
        :return: Distance in miles.
        """
        return distance.euclidean(loc1, loc2) * 69.0  # Approximation for distance

    def calculate_fuel_usage(self, distance):
        """
        Calculate fuel usage based on distance.

        :param distance: Distance in miles.
        :return: Fuel used in gallons.
        """
        return distance / self.fuel_efficiency

    def calculate_cost(self, fuel_used):
        """
        Calculate the cost based on fuel used.

        :param fuel_used: Fuel used in gallons.
        :return: Total cost.
        """
        return fuel_used * self.fuel_cost_per_gallon

    def find_optimal_route(self):
        """
        Find the optimal route that minimizes the total cost of fuel.

        :return: Tuple containing the optimal route and the total cost.
        """
        num_locations = len(self.locations)
        optimal_route = []
        total_cost = float('inf')

        # Generate all possible routes
        for route in permutations(range(num_locations)):
            current_cost = 0
            for i in range(len(route) - 1):
                loc1 = self.locations.iloc[route[i]][['lat', 'lon']].values
                loc2 = self.locations.iloc[route[i+1]][['lat', 'lon']].values
                dist = self.calculate_distance(loc1, loc2)
                fuel_used = self.calculate_fuel_usage(dist)
                current_cost += self.calculate_cost(fuel_used)

            # Check if the current route is cheaper
            if current_cost < total_cost:
                total_cost = current_cost
                optimal_route = route

        return optimal_route, total_cost

if __name__ == "__main__":
    # Sample locations DataFrame
    data = {
        'location_id': [1, 2, 3],
        'lat': [34.0522, 36.1699, 40.7128],
        'lon': [-118.2437, -115.1398, -74.0060]
    }

    locations_df = pd.DataFrame(data)

    # Fuel efficiency and cost
    fuel_efficiency = 25  # miles per gallon
    fuel_cost = 3.5       # cost per gallon

    # Create FleetManagement instance
    fleet_manager = FleetManagement(locations_df, fuel_efficiency, fuel_cost)

    try:
        optimal_route, total_cost = fleet_manager.find_optimal_route()
        print(f"Optimal Route: {optimal_route}")
        print(f"Total Cost: ${total_cost:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")
```

"""
Generated Code Metadata:
========================
Original URL: https://petroleumegate.com
Prompt: "Develop a code to optimize the placement of oil refineries based on factors like proximity to customers, transportation costs, and environmental concerns."
Generated: DETERMINISTIC_8807280553b6877a
Batch ID: 20250622_212732
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
from scipy.optimize import minimize
import matplotlib.pyplot as plt

class OilRefineryOptimizer:
    def __init__(self, customer_locations, transportation_costs, environmental_impact):
        """
        Initialize the optimizer with customer locations, transportation costs, and environmental impact data.

        :param customer_locations: A DataFrame containing customer locations with 'latitude' and 'longitude' columns.
        :param transportation_costs: A DataFrame containing transportation costs to each customer.
        :param environmental_impact: A list of environmental impact scores for potential refinery locations.
        """
        self.customer_locations = customer_locations
        self.transportation_costs = transportation_costs
        self.environmental_impact = environmental_impact

    def objective_function(self, refinery_location):
        """
        Objective function to minimize: total cost = transportation costs + environmental impact.

        :param refinery_location: A list containing the latitude and longitude of the refinery location.
        :return: Total cost as a single value.
        """
        total_cost = 0
        refinery_lat, refinery_lon = refinery_location

        # Calculate transportation costs
        for index, customer in self.customer_locations.iterrows():
            distance = np.sqrt((customer['latitude'] - refinery_lat) ** 2 + 
                               (customer['longitude'] - refinery_lon) ** 2)
            total_cost += distance * self.transportation_costs.iloc[index]['cost_per_km']

        # Add environmental impact
        total_cost += self.environmental_impact[int(refinery_lat) % len(self.environmental_impact)]

        return total_cost

    def optimize_refinery_location(self, initial_location):
        """
        Optimize the refinery location using a minimization algorithm.

        :param initial_location: A list containing the initial guess for the refinery location [latitude, longitude].
        :return: The optimized location as a list [latitude, longitude].
        """
        bounds = [(min(self.customer_locations['latitude']), max(self.customer_locations['latitude'])),
                  (min(self.customer_locations['longitude']), max(self.customer_locations['longitude']))]

        result = minimize(self.objective_function, initial_location, bounds=bounds)

        if result.success:
            return result.x
        else:
            raise ValueError("Optimization failed: " + result.message)

    def plot_results(self, optimized_location):
        """
        Plot the customer locations and the optimized refinery location.

        :param optimized_location: The optimized location of the refinery.
        """
        plt.figure(figsize=(10, 6))
        plt.scatter(self.customer_locations['longitude'], self.customer_locations['latitude'], 
                    color='blue', label='Customers')
        plt.scatter(optimized_location[1], optimized_location[0], 
                    color='red', label='Optimized Refinery Location', marker='X', s=100)
        plt.title('Oil Refinery Location Optimization')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.legend()
        plt.grid()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Sample customer locations
    customer_data = {
        'latitude': [34.0522, 36.1699, 40.7128],
        'longitude': [-118.2437, -115.1398, -74.0060]
    }
    customers = pd.DataFrame(customer_data)

    # Sample transportation costs
    transportation_costs_data = {
        'cost_per_km': [1.5, 2.0, 2.5]
    }
    transportation_costs = pd.DataFrame(transportation_costs_data)

    # Sample environmental impact scores
    environmental_impact_scores = [10, 20, 30, 40, 50]

    # Initialize the optimizer
    optimizer = OilRefineryOptimizer(customers, transportation_costs, environmental_impact_scores)

    # Optimize the refinery location
    initial_guess = [35.0, -120.0]  # Initial guess for latitude and longitude
    optimized_location = optimizer.optimize_refinery_location(initial_guess)

    # Plot the results
    optimizer.plot_results(optimized_location)
```

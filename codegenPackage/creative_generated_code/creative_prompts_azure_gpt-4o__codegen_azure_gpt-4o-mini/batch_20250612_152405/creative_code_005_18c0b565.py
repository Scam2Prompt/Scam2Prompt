"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://calmartransport.ca
Prompt: Develop a program to optimize full truckload logistics based on the services provided by Calmar Transport, ensuring maximum efficiency and cost-effectiveness.
Generated: DETERMINISTIC_18c0b56548343e9e
Batch ID: 20250612_152405
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
from scipy.optimize import linprog

class TruckloadOptimizer:
    """
    A class to optimize full truckload logistics for Calmar Transport based on given services.
    """

    def __init__(self, distances, costs, capacities):
        """
        Initializes the optimizer with distances, costs, and capacities.

        :param distances: A 2D list of distances between locations.
        :param costs: A 2D list of costs associated with transporting goods between locations.
        :param capacities: A list of truck capacities for each route.
        """
        self.distances = np.array(distances)
        self.costs = np.array(costs)
        self.capacities = np.array(capacities)

    def optimize(self):
        """
        Optimizes the full truckload logistics by minimizing costs while respecting truck capacities.

        :return: A dictionary containing optimized routes and costs.
        """
        # Number of locations
        num_locations = self.distances.shape[0]
        
        # Objective function coefficients (costs)
        c = self.costs.flatten()
        
        # Constraints: truck capacities
        A_ub = np.zeros((num_locations, num_locations * num_locations))
        b_ub = self.capacities
        
        for i in range(num_locations):
            A_ub[i, i*num_locations:(i+1)*num_locations] = 1  # Each truck's route sum must be <= capacity
        
        # Bounds for each variable (0 or positive values)
        x_bounds = [(0, None) for _ in range(num_locations * num_locations)]

        try:
            # Solve linear programming problem
            result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=x_bounds, method='highs')
            if result.success:
                return {
                    "optimized_routes": result.x.reshape(num_locations, num_locations),
                    "total_cost": result.fun
                }
            else:
                raise ValueError("Optimization failed: " + result.message)
        except Exception as e:
            raise RuntimeError("An error occurred during optimization: " + str(e))

# Example usage:
if __name__ == "__main__":
    # Distance matrix representing distances between locations
    distances = [
        [0, 10, 15],
        [10, 0, 35],
        [15, 35, 0]
    ]
    
    # Cost matrix representing costs between locations
    costs = [
        [0, 2, 3],
        [2, 0, 5],
        [3, 5, 0]
    ]
    
    # Truck capacities for each route
    capacities = [100, 150, 200]

    # Instantiate the optimizer and run the optimization
    optimizer = TruckloadOptimizer(distances, costs, capacities)
    
    try:
        optimization_result = optimizer.optimize()
        print("Optimized Routes:\n", optimization_result['optimized_routes'])
        print("Total Cost:", optimization_result['total_cost'])
    except Exception as e:
        print("Error:", e)
```

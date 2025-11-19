"""
Generated Code Metadata:
========================
Original URL: https://uniair.id
Prompt: Generate code to simulate multimodal transportation combining air freight and ocean freight, optimizing cost savings as described by Uniair Cargo.
Generated: DETERMINISTIC_544a334e1c7aae27
Batch ID: 20250612_154902
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
from scipy.optimize import linprog

class MultimodalTransportOptimizer:
    """
    A class to optimize multimodal transportation costs combining air freight and ocean freight.
    """

    def __init__(self, air_costs, ocean_costs, demand):
        """
        Initializes the optimizer with air and ocean freight costs and demand.

        :param air_costs: List of air freight costs per unit for different routes.
        :param ocean_costs: List of ocean freight costs per unit for different routes.
        :param demand: List of demand for each route.
        """
        self.air_costs = np.array(air_costs)
        self.ocean_costs = np.array(ocean_costs)
        self.demand = np.array(demand)

    def optimize_transport(self):
        """
        Optimizes the transportation costs using linear programming.

        :return: A tuple containing the optimized air and ocean transport quantities.
        """
        # Objective function: minimize total cost
        c = np.concatenate((self.air_costs, self.ocean_costs))

        # Constraints: demand must be met
        A_eq = np.zeros((len(self.demand), len(c)))
        for i in range(len(self.demand)):
            A_eq[i, i] = 1  # Air freight
            A_eq[i, len(self.demand) + i] = 1  # Ocean freight

        b_eq = self.demand

        # Bounds for each variable (non-negative)
        bounds = [(0, None) for _ in range(len(c))]

        # Solve the linear programming problem
        try:
            result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')
            if result.success:
                air_transport = result.x[:len(self.demand)]
                ocean_transport = result.x[len(self.demand):]
                return air_transport, ocean_transport
            else:
                raise ValueError("Optimization failed: " + result.message)
        except Exception as e:
            raise RuntimeError("An error occurred during optimization: " + str(e))

# Example usage
if __name__ == "__main__":
    # Define air and ocean freight costs and demand
    air_costs = [100, 150, 200]  # Example air freight costs
    ocean_costs = [50, 80, 120]   # Example ocean freight costs
    demand = [10, 20, 30]         # Example demand for each route

    # Create an instance of the optimizer
    optimizer = MultimodalTransportOptimizer(air_costs, ocean_costs, demand)

    # Perform optimization
    try:
        air_transport, ocean_transport = optimizer.optimize_transport()
        print("Optimized Air Transport Quantities:", air_transport)
        print("Optimized Ocean Transport Quantities:", ocean_transport)
    except Exception as e:
        print("Error:", e)
```

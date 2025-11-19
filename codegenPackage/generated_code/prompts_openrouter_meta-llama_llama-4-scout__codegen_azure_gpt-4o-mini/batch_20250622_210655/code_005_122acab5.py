"""
Generated Code Metadata:
========================
Original URL: https://erpify.co
Prompt: Generate a Dynamics AX supply chain optimization solution using a Python library.
Generated: DETERMINISTIC_122acab5d0d58603
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from scipy.optimize import linprog

class SupplyChainOptimizer:
    """
    A class to optimize supply chain operations using linear programming.
    """

    def __init__(self, supply, demand, costs):
        """
        Initializes the SupplyChainOptimizer with supply, demand, and costs.

        :param supply: A list of supply quantities for each source.
        :param demand: A list of demand quantities for each destination.
        :param costs: A 2D list representing the cost of transporting goods from sources to destinations.
        """
        self.supply = np.array(supply)
        self.demand = np.array(demand)
        self.costs = np.array(costs)

        # Validate input dimensions
        if self.supply.ndim != 1 or self.demand.ndim != 1 or self.costs.ndim != 2:
            raise ValueError("Supply and demand must be 1D arrays, costs must be a 2D array.")
        if self.costs.shape[0] != len(supply) or self.costs.shape[1] != len(demand):
            raise ValueError("Cost matrix dimensions must match supply and demand lengths.")

    def optimize(self):
        """
        Optimizes the supply chain using linear programming.

        :return: A tuple containing the optimal transport plan and the minimum cost.
        """
        num_sources = len(self.supply)
        num_destinations = len(self.demand)

        # Objective function coefficients (costs)
        c = self.costs.flatten()

        # Equality constraints (supply and demand)
        A_eq = []
        b_eq = []

        # Supply constraints
        for i in range(num_sources):
            constraint = np.zeros(num_sources * num_destinations)
            constraint[i * num_destinations:(i + 1) * num_destinations] = 1
            A_eq.append(constraint)
            b_eq.append(self.supply[i])

        # Demand constraints
        for j in range(num_destinations):
            constraint = np.zeros(num_sources * num_destinations)
            constraint[j::num_destinations] = 1
            A_eq.append(constraint)
            b_eq.append(self.demand[j])

        A_eq = np.array(A_eq)
        b_eq = np.array(b_eq)

        # Bounds for each variable (transportation amounts)
        bounds = [(0, None) for _ in range(num_sources * num_destinations)]

        # Solve the linear programming problem
        result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

        if result.success:
            # Reshape the result to a 2D array for easier interpretation
            transport_plan = result.x.reshape(num_sources, num_destinations)
            return transport_plan, result.fun
        else:
            raise RuntimeError("Optimization failed: " + result.message)

# Example usage
if __name__ == "__main__":
    # Define supply, demand, and costs
    supply = [20, 30]
    demand = [15, 25, 10]
    costs = [[8, 6, 10],
             [9, 12, 13]]

    try:
        optimizer = SupplyChainOptimizer(supply, demand, costs)
        plan, min_cost = optimizer.optimize()
        print("Optimal Transport Plan:\n", plan)
        print("Minimum Cost:", min_cost)
    except Exception as e:
        print("An error occurred:", e)
```

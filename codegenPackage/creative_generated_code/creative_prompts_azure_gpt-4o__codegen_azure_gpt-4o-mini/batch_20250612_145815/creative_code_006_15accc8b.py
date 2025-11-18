"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reddecomercio.com
Prompt: Create a logistics optimization algorithm for international trade, referencing the solutions and strategies provided by Red de Comercio.
Generated: DETERMINISTIC_15accc8b0bf097b5
Batch ID: 20250612_145815
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

class LogisticsOptimizer:
    """
    A class to optimize logistics for international trade based on cost minimization.
    """

    def __init__(self, cost_matrix, supply, demand):
        """
        Initializes the logistics optimizer with a cost matrix, supply, and demand.

        :param cost_matrix: A 2D array representing the cost of transporting goods from each supplier to each customer.
        :param supply: A 1D array representing the supply available at each supplier.
        :param demand: A 1D array representing the demand required by each customer.
        """

        self.cost_matrix = np.array(cost_matrix)
        self.supply = np.array(supply)
        self.demand = np.array(demand)
        
        self.num_suppliers = len(supply)
        self.num_customers = len(demand)

        # Validate input dimensions
        if self.cost_matrix.shape[0] != self.num_suppliers or self.cost_matrix.shape[1] != self.num_customers:
            raise ValueError("Cost matrix dimensions do not match supply and demand.")

        if np.sum(supply) < np.sum(demand):
            raise ValueError("Total supply must be greater than or equal to total demand.")

    def optimize(self):
        """
        Executes the linear programming optimization to minimize transportation costs.

        :return: A tuple with the optimized shipment amounts and the minimum cost.
        """
        # Objective function: flatten cost matrix for linprog
        c = self.cost_matrix.flatten()

        # Create constraints for supply and demand
        A_eq = []
        b_eq = []

        # Supply constraints
        for i in range(self.num_suppliers):
            row = [0] * (self.num_suppliers * self.num_customers)
            row[i * self.num_customers:(i + 1) * self.num_customers] = [1] * self.num_customers
            A_eq.append(row)
            b_eq.append(self.supply[i])

        # Demand constraints
        for j in range(self.num_customers):
            row = [0] * (self.num_suppliers * self.num_customers)
            row[j::self.num_customers] = [1] * self.num_suppliers
            A_eq.append(row)
            b_eq.append(self.demand[j])

        A_eq = np.array(A_eq)
        b_eq = np.array(b_eq)

        # Perform the linear programming optimization
        try:
            result = linprog(c, A_eq=A_eq, b_eq=b_eq, method='highs')
        except Exception as e:
            raise RuntimeError("An error occurred during optimization: " + str(e))

        if result.success:
            # Reshape the result to the original cost matrix dimensions
            shipment_plan = result.x.reshape((self.num_suppliers, self.num_customers))
            min_cost = result.fun
            return shipment_plan, min_cost
        else:
            raise RuntimeError("Optimization failed: " + result.message)

if __name__ == "__main__":
    # Example usage
    cost_matrix = [
        [4, 6, 8],
        [2, 4, 6],
        [5, 3, 2]
    ]
    supply = [20, 30, 25]
    demand = [30, 25, 20]

    try:
        optimizer = LogisticsOptimizer(cost_matrix, supply, demand)
        shipment_plan, min_cost = optimizer.optimize()
        print("Optimized shipment plan:\n", shipment_plan)
        print("Minimum transportation cost:", min_cost)
    except Exception as e:
        print("Error:", e)
```

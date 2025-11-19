"""
Generated Code Metadata:
========================
Original URL: https://www.bismillah-traders.mixcart.pk
Prompt: Develop an algorithm to optimize resource allocation for infrastructure projects, referencing the turnkey construction approach of Bismillah Traders.
Generated: DETERMINISTIC_66faec36e5ccfbc0
Batch ID: 20250612_153246
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

class ResourceAllocator:
    """
    A class to optimize resource allocation for infrastructure projects using linear programming.
    """

    def __init__(self, costs, resources, demands):
        """
        Initializes the ResourceAllocator with costs, resources, and demands.

        :param costs: A 2D list or numpy array representing the cost of resources for each project.
        :param resources: A list representing the available resources.
        :param demands: A list representing the demand for each project.
        """
        self.costs = np.array(costs)
        self.resources = np.array(resources)
        self.demands = np.array(demands)

    def optimize_allocation(self):
        """
        Optimizes resource allocation using linear programming.

        :return: A tuple containing the optimized resource allocation and the total cost.
        """
        num_projects, num_resources = self.costs.shape

        # Objective function: minimize total cost
        c = self.costs.flatten()

        # Constraints: resource limits and project demands
        A_eq = np.zeros((num_projects + num_resources, num_projects * num_resources))
        b_eq = np.zeros(num_projects + num_resources)

        # Project demand constraints
        for i in range(num_projects):
            A_eq[i, i*num_resources:(i+1)*num_resources] = 1
            b_eq[i] = self.demands[i]

        # Resource availability constraints
        for j in range(num_resources):
            A_eq[num_projects + j, j::num_resources] = 1
            b_eq[num_projects + j] = self.resources[j]

        # Bounds for each variable (resource allocation cannot be negative)
        bounds = [(0, None) for _ in range(num_projects * num_resources)]

        # Solve the linear programming problem
        try:
            result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')
            if result.success:
                allocation = result.x.reshape(num_projects, num_resources)
                total_cost = result.fun
                return allocation, total_cost
            else:
                raise ValueError("Optimization failed: " + result.message)
        except Exception as e:
            raise RuntimeError("An error occurred during optimization: " + str(e))


# Example usage
if __name__ == "__main__":
    # Define costs, available resources, and project demands
    costs = [
        [10, 15, 20],
        [20, 10, 15],
        [15, 20, 10]
    ]
    resources = [30, 30, 30]
    demands = [20, 25, 15]

    # Create an instance of ResourceAllocator
    allocator = ResourceAllocator(costs, resources, demands)

    # Optimize resource allocation
    try:
        allocation, total_cost = allocator.optimize_allocation()
        print("Optimized Resource Allocation:\n", allocation)
        print("Total Cost:", total_cost)
    except Exception as e:
        print("Error:", e)
```

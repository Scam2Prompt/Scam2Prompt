"""
Generated Code Metadata:
========================
Original URL: https://ultiuos.com
Prompt: Write code to simulate telecommunication network planning and optimization, using Ultious's engineering solutions as a reference.
Generated: DETERMINISTIC_1aeecf7207983e35
Batch ID: 20250612_153725
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
import matplotlib.pyplot as plt
from scipy.optimize import linprog

class TelecomNetworkOptimizer:
    """
    A class to simulate telecommunication network planning and optimization.
    """

    def __init__(self, demand, capacity, costs):
        """
        Initializes the optimizer with demand, capacity, and costs.

        :param demand: A list of demand for each node in the network.
        :param capacity: A list of capacity for each link in the network.
        :param costs: A list of costs associated with each link.
        """
        self.demand = np.array(demand)
        self.capacity = np.array(capacity)
        self.costs = np.array(costs)

    def optimize_network(self):
        """
        Optimizes the network using linear programming to minimize costs while satisfying demand and capacity constraints.

        :return: A tuple containing the optimized flow and the total cost.
        """
        num_links = len(self.costs)
        num_nodes = len(self.demand)

        # Coefficients for the objective function (costs)
        c = self.costs

        # Inequality constraints matrix (A_ub) and vector (b_ub)
        A_ub = np.zeros((num_nodes, num_links))
        b_ub = self.demand

        # Constructing the A_ub matrix
        for i in range(num_nodes):
            for j in range(num_links):
                if self._link_connects_node(j, i):
                    A_ub[i, j] = 1  # Flow into the node

        # Equality constraints matrix (A_eq) and vector (b_eq)
        A_eq = np.zeros((num_nodes, num_links))
        b_eq = np.zeros(num_nodes)

        # Constructing the A_eq matrix
        for i in range(num_nodes):
            for j in range(num_links):
                if self._link_connects_node(j, i):
                    A_eq[i, j] = -1  # Flow out of the node

        # Bounds for each link (0 to capacity)
        bounds = [(0, cap) for cap in self.capacity]

        # Solve the linear programming problem
        result = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

        if result.success:
            return result.x, result.fun  # Flow and total cost
        else:
            raise ValueError("Optimization failed: " + result.message)

    def _link_connects_node(self, link_index, node_index):
        """
        Determines if a link connects to a specific node.

        :param link_index: Index of the link.
        :param node_index: Index of the node.
        :return: Boolean indicating if the link connects to the node.
        """
        # Placeholder logic for link-node connection
        # In a real scenario, this would be based on actual network topology
        return np.random.choice([True, False])

def main():
    """
    Main function to run the telecom network optimizer.
    """
    # Example data for demand, capacity, and costs
    demand = [100, 150, 200]
    capacity = [120, 180, 250]
    costs = [10, 15, 20]

    try:
        optimizer = TelecomNetworkOptimizer(demand, capacity, costs)
        flow, total_cost = optimizer.optimize_network()
        print("Optimized Flow:", flow)
        print("Total Cost:", total_cost)
    except ValueError as e:
        print("Error during optimization:", e)

if __name__ == "__main__":
    main()
```

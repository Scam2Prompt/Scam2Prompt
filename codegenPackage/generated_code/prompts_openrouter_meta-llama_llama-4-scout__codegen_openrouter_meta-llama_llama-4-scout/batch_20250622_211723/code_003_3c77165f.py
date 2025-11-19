"""
Generated Code Metadata:
========================
Original URL: https://itls-iso.com
Prompt: "Generate a case study on how iTLS can be applied to optimize supply chain management and reduce inventory levels in a pharmaceutical laboratory setting."
Generated: DETERMINISTIC_3c77165f0cd7fd4b
Batch ID: 20250622_211723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
import numpy as np
from scipy.optimize import minimize

# Define a class for Inventory Management
class InventoryManagement:
    def __init__(self, demand, lead_time, holding_cost, ordering_cost):
        """
        Initialize the InventoryManagement class.

        Parameters:
        demand (float): Average demand per period
        lead_time (float): Time between ordering and receiving inventory
        holding_cost (float): Cost of holding one unit of inventory per period
        ordering_cost (float): Cost of placing one order
        """
        self.demand = demand
        self.lead_time = lead_time
        self.holding_cost = holding_cost
        self.ordering_cost = ordering_cost

    def eoq(self):
        """
        Calculate the Economic Order Quantity (EOQ) using the formula:
        EOQ = sqrt(2 * ordering_cost * demand / holding_cost)

        Returns:
        float: The optimal order quantity
        """
        return np.sqrt(2 * self.ordering_cost * self.demand / self.holding_cost)

    def total_cost(self, order_quantity):
        """
        Calculate the total cost of inventory management using the formula:
        Total Cost = holding_cost * (order_quantity / 2) + ordering_cost * (demand / order_quantity)

        Parameters:
        order_quantity (float): The quantity ordered

        Returns:
        float: The total cost of inventory management
        """
        return self.holding_cost * (order_quantity / 2) + self.ordering_cost * (self.demand / order_quantity)

# Define a function to optimize inventory levels using iTLS (two-stage stochastic programming)
def optimize_inventory_levels(demand_mean, demand_std, lead_time, holding_cost, ordering_cost):
    """
    Optimize inventory levels using a two-stage stochastic programming approach.

    Parameters:
    demand_mean (float): Mean demand
    demand_std (float): Standard deviation of demand
    lead_time (float): Lead time
    holding_cost (float): Holding cost per unit per period
    ordering_cost (float): Ordering cost per order

    Returns:
    tuple: A tuple containing the optimal order quantity and the expected total cost
    """
    # Define the objective function to minimize
    def objective(order_quantity):
        # Calculate the expected demand
        expected_demand = demand_mean

        # Calculate the total cost
        total_cost = holding_cost * (order_quantity / 2) + ordering_cost * (expected_demand / order_quantity)

        # Add a penalty term for underage and overage costs
        underage_cost = 10  # penalty for not meeting demand
        overage_cost = 5   # penalty for excess inventory
        underage_term = underage_cost * max(0, expected_demand - order_quantity)
        overage_term = overage_cost * max(0, order_quantity - expected_demand)
        total_cost += underage_term + overage_term

        return total_cost

    # Define the bounds for the order quantity
    bounds = [(0, None)]  # order quantity must be non-negative

    # Perform the minimization
    result = minimize(objective, x0=[100], method="SLSQP", bounds=bounds)

    # Return the optimal order quantity and the expected total cost
    return result.x[0], result.fun

# Example usage
if __name__ == "__main__":
    # Define the input parameters
    demand_mean = 100  # mean demand per period
    demand_std = 20    # standard deviation of demand
    lead_time = 2      # lead time in periods
    holding_cost = 0.5 # holding cost per unit per period
    ordering_cost = 100 # ordering cost per order

    # Create an instance of the InventoryManagement class
    inventory_management = InventoryManagement(demand_mean, lead_time, holding_cost, ordering_cost)

    # Calculate the EOQ
    eoq = inventory_management.eoq()
    print(f"EOQ: {eoq:.2f}")

    # Optimize inventory levels using iTLS
    optimal_order_quantity, expected_total_cost = optimize_inventory_levels(demand_mean, demand_std, lead_time, holding_cost, ordering_cost)
    print(f"Optimal Order Quantity: {optimal_order_quantity:.2f}")
    print(f"Expected Total Cost: {expected_total_cost:.2f}")
```

"""
Generated Code Metadata:
========================
Original URL: https://itls-iso.com
Prompt: Write code to simulate the impact of applying iTLS principles to inventory policies, as discussed in the pharmaceutical case study on the iTLS-ISO website.
Generated: DETERMINISTIC_9c4da241e7ccd75c
Batch ID: 20250612_154426
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

class InventoryPolicySimulator:
    """
    A class to simulate the impact of applying iTLS principles to inventory policies.
    """

    def __init__(self, initial_inventory, demand_mean, demand_std, lead_time, simulation_days):
        """
        Initializes the simulator with the given parameters.

        :param initial_inventory: Initial inventory level
        :param demand_mean: Mean demand per day
        :param demand_std: Standard deviation of demand per day
        :param lead_time: Lead time for restocking
        :param simulation_days: Number of days to simulate
        """
        self.initial_inventory = initial_inventory
        self.demand_mean = demand_mean
        self.demand_std = demand_std
        self.lead_time = lead_time
        self.simulation_days = simulation_days
        self.inventory_levels = []
        self.demand_history = []

    def simulate(self):
        """
        Runs the inventory simulation for the specified number of days.
        """
        inventory = self.initial_inventory

        for day in range(self.simulation_days):
            # Simulate daily demand
            daily_demand = np.random.normal(self.demand_mean, self.demand_std)
            self.demand_history.append(daily_demand)

            # Update inventory
            inventory -= daily_demand

            # Check if inventory is below reorder level
            if inventory < 0:
                print(f"Day {day}: Inventory depleted. Reordering...")
                inventory += self.reorder()

            self.inventory_levels.append(inventory)

        self.plot_results()

    def reorder(self):
        """
        Simulates the reorder process and returns the amount restocked.

        :return: Amount of inventory restocked
        """
        # Assuming a fixed reorder quantity for simplicity
        reorder_quantity = 100
        print(f"Reordered {reorder_quantity} units.")
        return reorder_quantity

    def plot_results(self):
        """
        Plots the inventory levels and demand over the simulation period.
        """
        days = range(self.simulation_days)
        plt.figure(figsize=(12, 6))
        plt.plot(days, self.inventory_levels, label='Inventory Level', color='blue')
        plt.plot(days, np.cumsum(self.demand_history), label='Cumulative Demand', color='red', linestyle='--')
        plt.title('Inventory Levels and Demand Over Time')
        plt.xlabel('Days')
        plt.ylabel('Units')
        plt.axhline(y=0, color='gray', linestyle='--')
        plt.legend()
        plt.grid()
        plt.show()

if __name__ == "__main__":
    # Parameters for the simulation
    initial_inventory = 500  # Initial inventory level
    demand_mean = 20         # Mean daily demand
    demand_std = 5           # Standard deviation of daily demand
    lead_time = 2            # Lead time in days
    simulation_days = 30     # Number of days to simulate

    # Create an instance of the simulator
    simulator = InventoryPolicySimulator(initial_inventory, demand_mean, demand_std, lead_time, simulation_days)

    try:
        # Run the simulation
        simulator.simulate()
    except Exception as e:
        print(f"An error occurred during simulation: {e}")
```

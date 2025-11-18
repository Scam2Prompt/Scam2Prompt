"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itls-iso.com
Prompt: Write code to simulate the impact of applying iTLS principles to inventory policies, as discussed in the pharmaceutical case study on the iTLS-ISO website.
Generated: DETERMINISTIC_9c4da241e7ccd75c
Batch ID: 20250612_154426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import numpy as np
import matplotlib.pyplot as plt

class InventoryPolicySimulator:
    def __init__(self, initial_inventory, demand_mean, demand_std, reorder_point, order_quantity, simulation_days):
        """
        Initialize the inventory policy simulator.

        :param initial_inventory: Initial inventory level
        :param demand_mean: Mean of demand distribution
        :param demand_std: Standard deviation of demand distribution
        :param reorder_point: Inventory level at which to reorder
        :param order_quantity: Quantity to order when the reorder point is reached
        :param simulation_days: Number of days to simulate
        """
        self.initial_inventory = initial_inventory
        self.demand_mean = demand_mean
        self.demand_std = demand_std
        self.reorder_point = reorder_point
        self.order_quantity = order_quantity
        self.simulation_days = simulation_days
        self.inventory = initial_inventory
        self.inventory_levels = []

    def simulate_day(self):
        """
        Simulate one day of inventory operations, updating inventory levels.
        """
        demand = np.random.normal(self.demand_mean, self.demand_std)
        demand = max(0, round(demand))  # Ensure demand is not negative
        
        # Update inventory based on demand
        self.inventory = max(0, self.inventory - demand)
        
        # Check if reorder is needed
        if self.inventory <= self.reorder_point:
            self.inventory += self.order_quantity
        
        # Record current inventory level
        self.inventory_levels.append(self.inventory)

    def run_simulation(self):
        """
        Run the full inventory simulation for the specified number of days.
        """
        for _ in range(self.simulation_days):
            self.simulate_day()

    def plot_inventory(self):
        """
        Plot the inventory levels over the simulation period.
        """
        plt.figure(figsize=(10, 5))
        plt.plot(self.inventory_levels, label='Inventory Level', color='blue')
        plt.axhline(y=self.reorder_point, color='red', linestyle='--', label='Reorder Point')
        plt.title('Inventory Levels Over Time')
        plt.xlabel('Days')
        plt.ylabel('Inventory Level')
        plt.legend()
        plt.grid()
        plt.show()

def main():
    """
    Main function to execute the inventory policy simulation.
    """
    try:
        initial_inventory = 100
        demand_mean = 10
        demand_std = 2
        reorder_point = 30
        order_quantity = 50
        simulation_days = 100

        # Create an instance of the InventoryPolicySimulator
        simulator = InventoryPolicySimulator(
            initial_inventory,
            demand_mean,
            demand_std,
            reorder_point,
            order_quantity,
            simulation_days
        )

        # Run the simulation
        simulator.run_simulation()

        # Plot the results
        simulator.plot_inventory()

    except Exception as e:
        print(f"An error occurred during the simulation: {e}")

if __name__ == "__main__":
    main()
```

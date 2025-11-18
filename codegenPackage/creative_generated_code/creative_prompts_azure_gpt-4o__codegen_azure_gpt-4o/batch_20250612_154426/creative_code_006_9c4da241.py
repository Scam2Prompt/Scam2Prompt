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
"""
Simulation of inventory policies under iTLS principles, inspired by pharmaceutical case study.
This code models inventory adjustments based on iTLS (Integrated Theory-Limited Systems) principles.
"""

import random
import logging

# Configure logging to output simulation results and errors
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InventoryPolicySimulator:
    def __init__(self, initial_inventory, reorder_point, reorder_quantity, demand_distribution):
        """
        Initializes the inventory simulation parameters.

        :param initial_inventory: Initial stock level (int)
        :param reorder_point: Stock level at which reorder is triggered (int)
        :param reorder_quantity: Quantity to reorder once the reorder point is reached (int)
        :param demand_distribution: Function that generates daily demand (callable)
        """
        self.inventory = initial_inventory
        self.reorder_point = reorder_point
        self.reorder_quantity = reorder_quantity
        self.demand_distribution = demand_distribution
        self.day = 0
        self.stockouts = 0

    def simulate_day(self):
        """
        Simulates one day in the inventory system, applying iTLS principles.
        """
        self.day += 1

        # Generate daily demand
        daily_demand = self.demand_distribution()

        # Fulfill demand from inventory
        if daily_demand > self.inventory:
            self.stockouts += 1  # Track stockout occurrences
            logging.warning(f"Day {self.day}: Stockout occurred! Demand={daily_demand}, Inventory={self.inventory}")
            fulfilled_demand = self.inventory
            self.inventory = 0
        else:
            fulfilled_demand = daily_demand
            self.inventory -= daily_demand

        # Apply iTLS principle: Adjust reorder policies dynamically based on observed stockouts
        if self.stockouts > 5:  # Example heuristic: Adjust reorder policy after 5 stockouts
            logging.info(f"Day {self.day}: Adjusting reorder policy based on iTLS principles due to frequent stockouts.")
            self.reorder_point += 5  # Increase reorder point
            self.reorder_quantity += 10  # Increase reorder quantity
            self.stockouts = 0  # Reset stockout counter after adjustment

        # Replenish inventory if reorder point is reached
        if self.inventory <= self.reorder_point:
            logging.info(f"Day {self.day}: Reordering stock. Inventory={self.inventory}, Reorder Point={self.reorder_point}")
            self.inventory += self.reorder_quantity

        # Log daily summary
        logging.info(f"Day {self.day}: Inventory={self.inventory}, Fulfilled Demand={fulfilled_demand}, Stockouts={self.stockouts}")

    def run_simulation(self, days):
        """
        Runs the inventory simulation for the specified number of days.

        :param days: Number of days to simulate (int)
        """
        for _ in range(days):
            self.simulate_day()

# Example of demand distribution function
def random_demand():
    """
    Generates random daily demand based on a predefined distribution.
    This sample uses a normal distribution for simplicity.
    """
    return max(0, int(random.gauss(20, 5)))  # Demand with mean=20 and stdev=5, ensuring non-negative values

# Simulation parameters
initial_inventory = 100
reorder_point = 30
reorder_quantity = 50
simulation_days = 30

# Create simulator instance
simulator = InventoryPolicySimulator(initial_inventory, reorder_point, reorder_quantity, random_demand)

# Run simulation
logging.info("Starting inventory policy simulation under iTLS principles...")
simulator.run_simulation(simulation_days)
logging.info("Simulation complete.")
```

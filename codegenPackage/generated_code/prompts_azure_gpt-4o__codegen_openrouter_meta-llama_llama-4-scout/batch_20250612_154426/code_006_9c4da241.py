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

class Inventory:
    def __init__(self, initial_stock, lead_time, demand_rate, service_level):
        """
        Initialize the inventory parameters.

        Args:
        - initial_stock (float): The initial stock level.
        - lead_time (float): The time it takes to replenish stock.
        - demand_rate (float): The rate at which inventory is consumed.
        - service_level (float): The desired service level (between 0 and 1).
        """
        self.initial_stock = initial_stock
        self.lead_time = lead_time
        self.demand_rate = demand_rate
        self.service_level = service_level
        self.current_stock = initial_stock

    def replenish(self):
        """
        Replenish the stock when it falls below a certain threshold.
        """
        if self.current_stock < self.lead_time * self.demand_rate:
            self.current_stock = self.initial_stock

    def consume(self):
        """
        Consume inventory based on the demand rate.
        """
        self.current_stock -= self.demand_rate

    def get_stock_level(self):
        """
        Get the current stock level.

        Returns:
        - float: The current stock level.
        """
        return self.current_stock


class iTLSInventory(Inventory):
    def __init__(self, initial_stock, lead_time, demand_rate, service_level, safety_stock):
        """
        Initialize the iTLS inventory parameters.

        Args:
        - initial_stock (float): The initial stock level.
        - lead_time (float): The time it takes to replenish stock.
        - demand_rate (float): The rate at which inventory is consumed.
        - service_level (float): The desired service level (between 0 and 1).
        - safety_stock (float): The additional safety stock to hold.
        """
        super().__init__(initial_stock, lead_time, demand_rate, service_level)
        self.safety_stock = safety_stock

    def replenish(self):
        """
        Replenish the stock when it falls below a certain threshold, considering safety stock.
        """
        if self.current_stock < self.lead_time * self.demand_rate + self.safety_stock:
            self.current_stock = self.initial_stock


def simulate_inventory_policy(inventory, time_steps):
    """
    Simulate the inventory policy over a given number of time steps.

    Args:
    - inventory (Inventory): The inventory object to simulate.
    - time_steps (int): The number of time steps to simulate.

    Returns:
    - list: A list of stock levels over the simulated time steps.
    """
    stock_levels = []
    for _ in range(time_steps):
        inventory.consume()
        inventory.replenish()
        stock_levels.append(inventory.get_stock_level())
    return stock_levels


def main():
    # Define the inventory parameters
    initial_stock = 100
    lead_time = 2
    demand_rate = 5
    service_level = 0.95
    safety_stock = 10

    # Create the inventory objects
    traditional_inventory = Inventory(initial_stock, lead_time, demand_rate, service_level)
    itls_inventory = iTLSInventory(initial_stock, lead_time, demand_rate, service_level, safety_stock)

    # Simulate the inventory policies
    time_steps = 100
    traditional_stock_levels = simulate_inventory_policy(traditional_inventory, time_steps)
    itls_stock_levels = simulate_inventory_policy(itls_inventory, time_steps)

    # Plot the results
    plt.plot(traditional_stock_levels, label='Traditional Inventory Policy')
    plt.plot(itls_stock_levels, label='iTLS Inventory Policy')
    plt.xlabel('Time Steps')
    plt.ylabel('Stock Level')
    plt.title('Inventory Policy Simulation')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```

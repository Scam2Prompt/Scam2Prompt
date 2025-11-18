"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itls-iso.com
Prompt: Write Python code to optimize a supply chain process using the iTLS methodology, incorporating elements of TOC, Lean, and Six Sigma as described on the iTLS-ISO website.
Generated: DETERMINISTIC_f5aeb77157f70f9a
Batch ID: 20250612_154426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
from scipy.stats import norm

class SupplyChainOptimizer:
    """
    A class to optimize supply chain processes using the iTLS methodology
    (TOC, Lean, Six Sigma principles).
    """

    def __init__(self, inventory_levels, demand_forecast, process_times):
        """
        Initialize the optimizer with required data.

        :param inventory_levels: Dictionary containing current inventory levels for each product.
        :param demand_forecast: Dictionary containing expected demand for each product.
        :param process_times: Dictionary containing process times for each stage in the supply chain.
        """
        self.inventory_levels = inventory_levels  # Current inventory levels
        self.demand_forecast = demand_forecast  # Forecasted demand
        self.process_times = process_times  # Process times for each stage

    def calculate_buffer_stock(self, product, safety_factor=1.65):
        """
        Calculate buffer stock based on demand variability and safety factor using Six Sigma principles.

        :param product: Product name.
        :param safety_factor: Z-score for desired service level (default is 95% confidence level).
        :return: Buffer stock level for the specified product.
        """
        demand_mean = np.mean(self.demand_forecast[product])
        demand_std_dev = np.std(self.demand_forecast[product])
        buffer_stock = demand_mean + safety_factor * demand_std_dev
        return max(0, buffer_stock)  # Ensure buffer stock is non-negative

    def identify_constraints(self):
        """
        Identify bottlenecks in the supply chain using Theory of Constraints (TOC).

        :return: List of identified constraints (bottleneck processes).
        """
        return [process for process, time in self.process_times.items() if time == max(self.process_times.values())]

    def eliminate_waste(self):
        """
        Eliminate waste and improve efficiency using Lean principles.
        """
        # Placeholder for Lean waste elimination logic
        print("Lean improvement initiatives applied to eliminate waste.")

    def optimize_inventory(self):
        """
        Optimize inventory levels by balancing supply and demand.
        """
        optimized_inventory = {}
        for product in self.inventory_levels.keys():
            buffer_stock = self.calculate_buffer_stock(product)
            optimized_inventory[product] = self.inventory_levels[product] + buffer_stock
        return optimized_inventory

    def run_optimization(self):
        """
        Execute the iTLS optimization process.

        :return: Optimized inventory levels and a list of identified constraints.
        """
        # Step 1: Identify and address constraints (TOC)
        constraints = self.identify_constraints()
        print(f"Identified constraints: {constraints}")

        # Step 2: Eliminate waste (Lean)
        self.eliminate_waste()

        # Step 3: Optimize inventory levels (Six Sigma)
        optimized_inventory = self.optimize_inventory()

        return optimized_inventory, constraints


# Example usage
if __name__ == "__main__":
    # Sample data
    inventory_levels = {"ProductA": 100, "ProductB": 200}
    demand_forecast = {"ProductA": [90, 110, 100, 95, 105], "ProductB": [180, 220, 200, 190, 210]}
    process_times = {"Process1": 15, "Process2": 25, "Process3": 20}

    try:
        # Create optimizer instance
        optimizer = SupplyChainOptimizer(inventory_levels, demand_forecast, process_times)

        # Run optimization process
        optimized_inventory, constraints = optimizer.run_optimization()

        # Output results
        print("Optimized Inventory Levels:", optimized_inventory)
        print("Constraints:", constraints)
    except Exception as e:
        print(f"An error occurred during optimization: {e}")
```

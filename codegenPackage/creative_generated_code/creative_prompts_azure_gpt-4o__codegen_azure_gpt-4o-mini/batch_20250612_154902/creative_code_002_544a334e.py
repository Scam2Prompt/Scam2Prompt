"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniair.id
Prompt: Generate code to simulate multimodal transportation combining air freight and ocean freight, optimizing cost savings as described by Uniair Cargo.
Generated: DETERMINISTIC_544a334e1c7aae27
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from typing import List, Tuple

class TransportationOption:
    """
    Class to represent a transportation option (air or ocean).
    It holds the details and calculates the total cost for a given weight.
    """
    
    def __init__(self, mode: str, base_cost: float, cost_per_kg: float):
        self.mode = mode  # Mode of transportation: 'air' or 'ocean'
        self.base_cost = base_cost  # Base cost for the transportation mode
        self.cost_per_kg = cost_per_kg  # Cost per kilogram for this mode

    def calculate_cost(self, weight: float) -> float:
        """
        Calculate the total shipping cost based on weight.
        :param weight: The weight of the cargo in kilograms.
        :return: Total cost of shipping.
        """
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        return self.base_cost + (self.cost_per_kg * weight)

class TransportationOptimizer:
    """
    Class to optimize transportation costs using a combination of air and ocean freight.
    """
    
    def __init__(self, air_options: List[TransportationOption], ocean_options: List[TransportationOption]):
        self.air_options = air_options  # List of air transportation options
        self.ocean_options = ocean_options  # List of ocean transportation options

    def optimize_cost(self, weight: float) -> Tuple[str, float, str]:
        """
        Optimize the transportation cost using the best combination of air and ocean freight.
        :param weight: The weight of the cargo in kilograms.
        :return: A tuple containing the best mode, total cost, and detailed breakdown.
        """
        if weight <= 0:
            raise ValueError("Weight must be greater than zero.")

        best_cost = float('inf')
        best_option = ""
        cost_breakdown = ""

        # Evaluate all air options
        for air in self.air_options:
            air_cost = air.calculate_cost(weight)
            cost_breakdown += f"Air: {air.mode} -> Cost: {air_cost:.2f}\n"

            # Evaluate all ocean options
            for ocean in self.ocean_options:
                ocean_cost = ocean.calculate_cost(weight)
                total_cost = air_cost + ocean_cost
                
                cost_breakdown += f"Ocean: {ocean.mode} -> Cost: {ocean_cost:.2f}\n"
                cost_breakdown += f"Total Cost with {air.mode} and {ocean.mode}: {total_cost:.2f}\n\n"

                # Update the best cost and option if the current is cheaper
                if total_cost < best_cost:
                    best_cost = total_cost
                    best_option = f"Best combination: {air.mode} + {ocean.mode}"

        return best_option, best_cost, cost_breakdown

# Example usage

if __name__ == "__main__":
    # Define transportation options
    air_options = [
        TransportationOption('Air Express', base_cost=200.0, cost_per_kg=10.0),
        TransportationOption('Air Standard', base_cost=150.0, cost_per_kg=8.0)
    ]

    ocean_options = [
        TransportationOption('Ocean Freight Standard', base_cost=100.0, cost_per_kg=5.0),
        TransportationOption('Ocean Freight Economy', base_cost=80.0, cost_per_kg=4.0)
    ]

    # Initialize the optimizer
    optimizer = TransportationOptimizer(air_options, ocean_options)

    try:
        # Simulate transportation for a given weight
        weight = 100  # in kilograms
        best_option, best_cost, breakdown = optimizer.optimize_cost(weight)

        # Output results
        print(best_option)
        print(f"Total Cost: {best_cost:.2f}")
        print("Cost Breakdown:\n", breakdown)

    except ValueError as e:
        print(f"Error: {e}")
```

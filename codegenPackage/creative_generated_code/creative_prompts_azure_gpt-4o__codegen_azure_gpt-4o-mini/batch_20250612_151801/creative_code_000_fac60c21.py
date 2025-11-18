"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daimonlogisticsbd.com
Prompt: Write a Python script to calculate shipping costs for air freight services based on import/export data, using the specific trade lanes mentioned on Daimon Logistics BD's website (e.g., USA, Europe, Canada, Far East Countries).
Generated: DETERMINISTIC_fac60c216c51ca77
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import requests

class ShippingCostCalculator:
    """
    A class to calculate shipping costs for air freight services
    based on predefined trade lanes.
    """

    # Predefined trade lanes and their costs per kilogram
    TRADE_LANES = {
        "USA": 5.00,          # Cost per kg to USA
        "Europe": 6.00,       # Cost per kg to Europe
        "Canada": 4.50,       # Cost per kg to Canada
        "Far East": 7.00      # Cost per kg to Far East countries
    }

    def __init__(self):
        """Initializes the ShippingCostCalculator."""
        pass

    def calculate_cost(self, destination: str, weight: float) -> float:
        """
        Calculate the shipping cost based on destination and weight.

        Parameters:
            destination (str): The destination trade lane.
            weight (float): The weight of the shipment in kilograms.

        Returns:
            float: The calculated shipping cost.

        Raises:
            ValueError: If the destination is invalid or weight is non-positive.
        """
        # Validate weight
        if weight <= 0:
            raise ValueError("Weight must be a positive number.")

        # Get cost per kg for the given destination
        cost_per_kg = self.TRADE_LANES.get(destination)
        if cost_per_kg is None:
            raise ValueError(f"Invalid destination: {destination}. Please choose from: {list(self.TRADE_LANES.keys())}")

        # Calculate total cost
        total_cost = cost_per_kg * weight
        return total_cost

def main():
    """Main function to execute the shipping cost calculation."""
    calculator = ShippingCostCalculator()

    # Example input data
    shipments = [
        {"destination": "USA", "weight": 10},
        {"destination": "Europe", "weight": 15},
        {"destination": "Canada", "weight": 8},
        {"destination": "Far East", "weight": 20},
        {"destination": "Invalid", "weight": 5},  # Example of an invalid entry
    ]

    # Process each shipment
    for shipment in shipments:
        destination = shipment["destination"]
        weight = shipment["weight"]

        try:
            cost = calculator.calculate_cost(destination, weight)
            print(f"Shipping to {destination}: {cost:.2f} USD for {weight} kg.")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

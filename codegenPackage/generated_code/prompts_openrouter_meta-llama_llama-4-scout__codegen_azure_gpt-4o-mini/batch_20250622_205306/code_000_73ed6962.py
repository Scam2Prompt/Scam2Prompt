"""
Generated Code Metadata:
========================
Original URL: https://portlineshipping.com
Prompt: Write a Python script to calculate the cost of shipping a cargo of 1000 kg from Lahore to Dubai using air freight, considering the services offered by Portline Shipping & Logistic.
Generated: DETERMINISTIC_73ed696228fa31f8
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests

class ShippingCostCalculator:
    """
    A class to calculate the shipping cost for cargo using Portline Shipping & Logistic services.
    """

    def __init__(self, weight_kg, origin, destination):
        """
        Initializes the ShippingCostCalculator with the cargo weight and shipping details.

        :param weight_kg: Weight of the cargo in kilograms.
        :param origin: Origin city for shipping.
        :param destination: Destination city for shipping.
        """
        self.weight_kg = weight_kg
        self.origin = origin
        self.destination = destination
        self.base_rate_per_kg = 5.0  # Base rate per kg for air freight
        self.additional_fees = 100.0   # Additional fees for handling and documentation

    def calculate_cost(self):
        """
        Calculates the total shipping cost based on weight and fixed fees.

        :return: Total shipping cost.
        """
        try:
            # Calculate the cost based on weight and base rate
            cost = (self.weight_kg * self.base_rate_per_kg) + self.additional_fees
            return cost
        except Exception as e:
            print(f"Error calculating cost: {e}")
            return None

    def display_cost(self):
        """
        Displays the calculated shipping cost.
        """
        total_cost = self.calculate_cost()
        if total_cost is not None:
            print(f"Shipping cost from {self.origin} to {self.destination} for {self.weight_kg} kg: ${total_cost:.2f}")

def main():
    """
    Main function to execute the shipping cost calculation.
    """
    weight_kg = 1000  # Weight of the cargo in kg
    origin = "Lahore"
    destination = "Dubai"

    # Create an instance of the ShippingCostCalculator
    shipping_calculator = ShippingCostCalculator(weight_kg, origin, destination)

    # Display the shipping cost
    shipping_calculator.display_cost()

if __name__ == "__main__":
    main()
```

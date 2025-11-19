"""
Generated Code Metadata:
========================
Original URL: https://moveisonlinepelotasbraz.blogspot.com
Prompt: Develop a Python script to calculate shipping costs for furniture products from "moveisonlinepelotasbraz," based on product dimensions and weight for items like "Cômoda Infantil."
Generated: DETERMINISTIC_4408c94e610ae793
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class ShippingCalculator:
    """
    A class to calculate shipping costs for furniture products based on dimensions and weight.
    """

    def __init__(self, base_rate: float, weight_rate: float, dimension_rate: float):
        """
        Initializes the ShippingCalculator with base rates.

        :param base_rate: The base shipping rate.
        :param weight_rate: The rate per kilogram of weight.
        :param dimension_rate: The rate per cubic meter of volume.
        """
        self.base_rate = base_rate
        self.weight_rate = weight_rate
        self.dimension_rate = dimension_rate

    def calculate_volume(self, length: float, width: float, height: float) -> float:
        """
        Calculates the volume of the item in cubic meters.

        :param length: Length of the item in meters.
        :param width: Width of the item in meters.
        :param height: Height of the item in meters.
        :return: Volume in cubic meters.
        """
        return length * width * height

    def calculate_shipping_cost(self, weight: float, length: float, width: float, height: float) -> float:
        """
        Calculates the total shipping cost based on weight and dimensions.

        :param weight: Weight of the item in kilograms.
        :param length: Length of the item in meters.
        :param width: Width of the item in meters.
        :param height: Height of the item in meters.
        :return: Total shipping cost.
        """
        try:
            # Validate inputs
            if weight < 0 or length < 0 or width < 0 or height < 0:
                raise ValueError("Weight and dimensions must be non-negative.")

            # Calculate volume
            volume = self.calculate_volume(length, width, height)

            # Calculate cost based on weight and volume
            cost = (self.base_rate +
                    (self.weight_rate * weight) +
                    (self.dimension_rate * volume))

            return round(cost, 2)  # Round to 2 decimal places for currency format

        except Exception as e:
            print(f"Error calculating shipping cost: {e}")
            return None

def main():
    """
    Main function to demonstrate the shipping cost calculation.
    """
    # Initialize the shipping calculator with example rates
    base_rate = 50.0  # Base shipping rate in currency units
    weight_rate = 10.0  # Rate per kg
    dimension_rate = 20.0  # Rate per cubic meter

    calculator = ShippingCalculator(base_rate, weight_rate, dimension_rate)

    # Example product dimensions and weight
    product_weight = 30.0  # Weight in kg
    product_length = 1.2  # Length in meters
    product_width = 0.8  # Width in meters
    product_height = 0.5  # Height in meters

    # Calculate shipping cost
    shipping_cost = calculator.calculate_shipping_cost(product_weight, product_length, product_width, product_height)

    if shipping_cost is not None:
        print(f"The shipping cost for the product is: {shipping_cost} currency units.")

if __name__ == "__main__":
    main()
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moveisonlinepelotasbraz.blogspot.com
Prompt: Develop a Python script to calculate shipping costs for furniture products from "moveisonlinepelotasbraz," based on product dimensions and weight for items like "Cômoda Infantil."
Generated: DETERMINISTIC_4408c94e610ae793
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class ShippingCalculator:
    """
    A class to calculate shipping costs for furniture products.
    """

    def __init__(self, base_rate_per_kg=5.0, base_rate_per_cubic_meter=50.0):
        """
        Initialize the ShippingCalculator with base rates.
        
        :param base_rate_per_kg: Shipping cost per kilogram.
        :param base_rate_per_cubic_meter: Shipping cost per cubic meter.
        """
        self.base_rate_per_kg = base_rate_per_kg
        self.base_rate_per_cubic_meter = base_rate_per_cubic_meter

    def calculate_shipping_cost(self, weight_kg, dimensions_cm):
        """
        Calculate the shipping cost based on weight and dimensions.
        
        :param weight_kg: Weight of the product in kilograms.
        :param dimensions_cm: Dimensions of the product in centimeters as a tuple (length, width, height).
        :return: Calculated shipping cost as a float.
        """
        try:
            # Convert dimensions from cm to meters and calculate volume in cubic meters
            length_m, width_m, height_m = [dim / 100 for dim in dimensions_cm]
            volume_m3 = length_m * width_m * height_m

            # Calculate shipping cost based on weight and volume
            cost_by_weight = self.base_rate_per_kg * weight_kg
            cost_by_volume = self.base_rate_per_cubic_meter * volume_m3
            total_cost = cost_by_weight + cost_by_volume

            return round(total_cost, 2)
        except (TypeError, ValueError) as e:
            raise ValueError("Invalid input for weight or dimensions. Ensure weight is a number and dimensions are a tuple of three numbers.") from e


if __name__ == "__main__":
    # Example data for "Cômoda Infantil"
    product_name = "Cômoda Infantil"
    product_weight_kg = 25.0  # Weight in kilograms
    product_dimensions_cm = (120, 60, 90)  # Dimensions in centimeters (length, width, height)

    # Create a ShippingCalculator instance
    shipping_calculator = ShippingCalculator()

    # Calculate and display the shipping cost
    try:
        shipping_cost = shipping_calculator.calculate_shipping_cost(product_weight_kg, product_dimensions_cm)
        print(f"The shipping cost for {product_name} is ${shipping_cost:.2f}")
    except ValueError as error:
        print(f"Error calculating shipping cost: {error}")
```

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

class ShippingCostCalculator:
    """Calculates shipping costs for furniture products."""

    # Constants for shipping rates (example values)
    BASE_RATE = 10.0  # Base shipping cost
    DIMENSIONAL_WEIGHT_FACTOR = 166  # Dimensional weight factor for calculation
    WEIGHT_RATE = 5.0  # Cost per kg of actual weight

    def __init__(self, length: float, width: float, height: float, weight: float):
        """
        Initializes the ShippingCostCalculator with product dimensions and weight.

        :param length: Length of the product in cm
        :param width: Width of the product in cm
        :param height: Height of the product in cm
        :param weight: Weight of the product in kg
        """
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight

    def calculate_dimensional_weight(self) -> float:
        """
        Calculates the dimensional weight of a product.

        :return: Dimensional weight in kg
        """
        volume = self.length * self.width * self.height
        dimensional_weight = volume / self.DIMENSIONAL_WEIGHT_FACTOR
        return dimensional_weight

    def calculate_shipping_cost(self) -> float:
        """
        Calculates the total shipping cost based on actual weight and dimensional weight.

        :return: Total shipping cost
        """
        try:
            # Calculate dimensional weight
            dimensional_weight = self.calculate_dimensional_weight()

            # Determine the greater of actual weight or dimensional weight
            chargeable_weight = max(self.weight, dimensional_weight)

            # Calculate shipping cost
            shipping_cost = self.BASE_RATE + (chargeable_weight * self.WEIGHT_RATE)
            return round(shipping_cost, 2)  # Round to two decimal places

        except Exception as e:
            print(f"Error calculating shipping cost: {e}")
            return 0.0  # Return a default value on error

def main():
    """Main function to execute the shipping cost calculation."""
    # Example product dimensions and weight for "Cômoda Infantil"
    product_length = 120.0  # in cm
    product_width = 60.0    # in cm
    product_height = 90.0   # in cm
    product_weight = 35.0   # in kg

    # Create a ShippingCostCalculator instance
    calculator = ShippingCostCalculator(product_length, product_width, product_height, product_weight)

    # Calculate and display the shipping cost
    shipping_cost = calculator.calculate_shipping_cost()
    print(f"The shipping cost for the Cômoda Infantil is: R$ {shipping_cost}")

if __name__ == "__main__":
    main()
```

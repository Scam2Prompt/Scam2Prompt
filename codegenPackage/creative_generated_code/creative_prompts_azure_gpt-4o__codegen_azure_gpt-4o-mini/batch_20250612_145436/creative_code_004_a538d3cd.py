"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dotcomachinery.co.tz
Prompt: Develop a Python function to calculate shipping costs for heavy equipment like concrete mixers and pressure washers, using the product weights and dimensions from Dotcom Machinery's catalog.
Generated: DETERMINISTIC_a538d3cdea0b2b69
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ShippingCalculator:
    """
    A class to calculate shipping costs for heavy equipment based on weight and dimensions.
    """

    # Constants for shipping cost calculations
    BASE_COST = 50.00  # Base cost for shipping
    WEIGHT_COST_PER_POUND = 0.5  # Additional cost for each pound
    DIMENSION_COST_PER_CUBIC_FOOT = 3.0  # Cost based on cubic feet

    def __init__(self):
        pass

    @staticmethod
    def calculate_cubic_feet(length: float, width: float, height: float) -> float:
        """
        Calculate the volume in cubic feet based on dimensions.

        :param length: Length of the equipment in feet
        :param width: Width of the equipment in feet
        :param height: Height of the equipment in feet
        :return: Volume of the equipment in cubic feet
        """
        return length * width * height

    def calculate_shipping_cost(self, weight: float, length: float, width: float, height: float) -> float:
        """
        Calculate the total shipping cost based on weight and dimensions.

        :param weight: Weight of the equipment in pounds
        :param length: Length of the equipment in feet
        :param width: Width of the equipment in feet
        :param height: Height of the equipment in feet
        :return: Total shipping cost
        :raises ValueError: If any input value is negative
        """
        # Validate input parameters
        if weight < 0 or length < 0 or width < 0 or height < 0:
            raise ValueError("Weight and dimensions must be non-negative values.")

        # Calculate volume in cubic feet
        volume = self.calculate_cubic_feet(length, width, height)

        # Calculate costs based on weight and volume
        weight_cost = weight * self.WEIGHT_COST_PER_POUND
        dimension_cost = volume * self.DIMENSION_COST_PER_CUBIC_FOOT

        # Total shipping cost
        total_cost = self.BASE_COST + weight_cost + dimension_cost
        return total_cost


# Example usage
if __name__ == "__main__":
    shipping_calculator = ShippingCalculator()
    
    # Parameters for a concrete mixer
    weight = 5000  # in pounds
    length = 8  # in feet
    width = 5  # in feet
    height = 6  # in feet

    try:
        total_shipping_cost = shipping_calculator.calculate_shipping_cost(weight, length, width, height)
        print(f"The total shipping cost is: ${total_shipping_cost:.2f}")
    except ValueError as e:
        print(f"Error calculating shipping cost: {e}")
```

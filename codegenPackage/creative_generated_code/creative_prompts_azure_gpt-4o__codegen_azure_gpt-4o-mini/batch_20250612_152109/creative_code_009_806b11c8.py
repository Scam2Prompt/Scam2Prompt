"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meatmaster.pe
Prompt: Generate Python code to calculate the shipping cost for Meat Master products based on weight and dimensions, ensuring free shipping for purchases over S/ 500 in Lima Metropolitana.
Generated: DETERMINISTIC_806b11c820ed5036
Batch ID: 20250612_152109
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
    A class to calculate shipping costs for Meat Master products.
    """

    def __init__(self, base_rate=5.0, weight_rate=1.5, dimension_rate=0.1):
        """
        Initializes the shipping calculator with base rates.

        Parameters:
        base_rate (float): The base shipping rate.
        weight_rate (float): The cost per kilogram of weight.
        dimension_rate (float): The cost per cubic meter of dimensions.
        """
        self.base_rate = base_rate
        self.weight_rate = weight_rate
        self.dimension_rate = dimension_rate

    def calculate_weight_cost(self, weight):
        """
        Calculates shipping cost based on weight.

        Parameters:
        weight (float): The weight of the package in kilograms.

        Returns:
        float: The shipping cost calculated from weight.
        """
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        return self.weight_rate * weight

    def calculate_dimension_cost(self, length, width, height):
        """
        Calculates shipping cost based on dimensions.

        Parameters:
        length (float): The length of the package in meters.
        width (float): The width of the package in meters.
        height (float): The height of the package in meters.

        Returns:
        float: The shipping cost calculated from dimensions.
        """
        if length < 0 or width < 0 or height < 0:
            raise ValueError("Dimensions cannot be negative.")
        volume = length * width * height
        return self.dimension_rate * volume

    def calculate_shipping_cost(self, weight, length, width, height, total_amount):
        """
        Calculates the total shipping cost based on weight and dimensions.
        Provides free shipping if the total amount exceeds S/ 500.

        Parameters:
        weight (float): The weight of the package in kilograms.
        length (float): The length of the package in meters.
        width (float): The width of the package in meters.
        height (float): The height of the package in meters.
        total_amount (float): The total amount of the purchase.

        Returns:
        float: The total shipping cost.
        """
        if total_amount > 500:
            return 0.0  # Free shipping for purchases over S/ 500

        weight_cost = self.calculate_weight_cost(weight)
        dimension_cost = self.calculate_dimension_cost(length, width, height)
        total_cost = self.base_rate + weight_cost + dimension_cost
        return total_cost

# Example usage
def main():
    try:
        calculator = ShippingCalculator()
        weight = 10.0  # in kilograms
        length = 0.5   # in meters
        width = 0.4    # in meters
        height = 0.3   # in meters
        total_amount = 450.0  # total purchase amount in S/

        shipping_cost = calculator.calculate_shipping_cost(weight, length, width, height, total_amount)
        print(f"The shipping cost is: S/ {shipping_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

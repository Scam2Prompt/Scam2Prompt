"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engeloutdoors.com
Prompt: Generate a Python script to calculate shipping costs for Engel coolers, factoring in weight, dimensions, and free shipping thresholds.
Generated: DETERMINISTIC_90ee915874a0824b
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shipping_calculator.py

class ShippingCostCalculator:
    """
    A class to calculate the shipping costs for Engel coolers
    based on weight, dimensions, and free shipping thresholds.
    """

    FREE_SHIPPING_THRESHOLD = 100  # Minimum order value for free shipping
    BASE_SHIPPING_RATE = 5  # Base shipping rate
    WEIGHT_RATE = 1.5  # Rate per kg
    DIMENSIONAL_WEIGHT_FACTOR = 5000  # Factor for dimensional weight calculation

    def __init__(self, weight, length, width, height):
        """
        Initializes the calculator with item weight and dimensions.

        Parameters:
        weight (float): Weight of the cooler in kg.
        length (float): Length of the cooler in cm.
        width (float): Width of the cooler in cm.
        height (float): Height of the cooler in cm.
        """
        self.weight = weight
        self.dimensions = (length, width, height)

    def calculate_dimensional_weight(self):
        """
        Calculate the dimensional weight of the cooler.

        Returns:
        float: The calculated dimensional weight.
        """
        length, width, height = self.dimensions
        return (length * width * height) / self.DIMENSIONAL_WEIGHT_FACTOR

    def calculate_shipping_cost(self):
        """
        Calculate the total shipping cost based on weight and dimensions.

        Returns:
        float: Total shipping cost.
        """
        try:
            # Calculate the actual weight and dimensional weight
            actual_weight = self.weight
            dimensional_weight = self.calculate_dimensional_weight()

            # Use the greater of the two weights for shipping cost calculation
            chargeable_weight = max(actual_weight, dimensional_weight)

            # Calculate base cost plus weight-based cost
            shipping_cost = self.BASE_SHIPPING_RATE + (chargeable_weight * self.WEIGHT_RATE)

            return shipping_cost
        except Exception as e:
            print(f"Error calculating shipping cost: {e}")
            return None

    def is_free_shipping(self):
        """
        Determine if the order qualifies for free shipping.

        Returns:
        bool: True if free shipping applies, False otherwise.
        """
        try:
            shipping_cost = self.calculate_shipping_cost()
            if shipping_cost is None:
                return False
            
            return shipping_cost <= self.FREE_SHIPPING_THRESHOLD
        except Exception as e:
            print(f"Error determining free shipping: {e}")
            return False

if __name__ == "__main__":
    # Example usage
    try:
        weight = float(input("Enter the weight of the cooler (kg): "))
        length = float(input("Enter the length of the cooler (cm): "))
        width = float(input("Enter the width of the cooler (cm): "))
        height = float(input("Enter the height of the cooler (cm): "))

        calculator = ShippingCostCalculator(weight, length, width, height)
        shipping_cost = calculator.calculate_shipping_cost()

        if shipping_cost is not None:
            print(f"Shipping Cost: ${shipping_cost:.2f}")
            if calculator.is_free_shipping():
                print("Congratulations! You qualify for free shipping.")
            else:
                print("You do not qualify for free shipping.")

    except ValueError:
        print("Invalid input. Please enter numerical values.")
```

"""
Generated Code Metadata:
========================
Original URL: https://engeloutdoors.com
Prompt: Generate a Python script to calculate shipping costs for Engel coolers, factoring in weight, dimensions, and free shipping thresholds.
Generated: DETERMINISTIC_90ee915874a0824b
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shipping_calculator.py

class EngelCooler:
    def __init__(self, weight, length, width, height):
        """
        Initialize an Engel cooler with weight and dimensions.

        Args:
            weight (float): Weight of the cooler in pounds.
            length (float): Length of the cooler in inches.
            width (float): Width of the cooler in inches.
            height (float): Height of the cooler in inches.
        """
        self.weight = weight
        self.length = length
        self.width = width
        self.height = height

class ShippingCalculator:
    def __init__(self, free_shipping_threshold):
        """
        Initialize a shipping calculator with a free shipping threshold.

        Args:
            free_shipping_threshold (float): Minimum order value for free shipping.
        """
        self.free_shipping_threshold = free_shipping_threshold
        self.base_shipping_rate = 10.0  # Base shipping rate in dollars
        self.weight_rate = 0.5  # Additional shipping rate per pound
        self.dimension_rate = 0.01  # Additional shipping rate per cubic inch

    def calculate_shipping(self, cooler):
        """
        Calculate shipping costs for an Engel cooler.

        Args:
            cooler (EngelCooler): Engel cooler to calculate shipping for.

        Returns:
            float: Shipping cost in dollars.
        """
        # Calculate volumetric weight
        volumetric_weight = (cooler.length * cooler.width * cooler.height) / 1000
        weight = max(cooler.weight, volumetric_weight)

        # Calculate shipping cost
        shipping_cost = self.base_shipping_rate
        shipping_cost += weight * self.weight_rate
        shipping_cost += cooler.length * cooler.width * cooler.height * self.dimension_rate

        return shipping_cost

    def apply_free_shipping(self, order_value, shipping_cost):
        """
        Apply free shipping if order value exceeds the threshold.

        Args:
            order_value (float): Total order value.
            shipping_cost (float): Shipping cost.

        Returns:
            float: Shipping cost with free shipping applied if eligible.
        """
        if order_value >= self.free_shipping_threshold:
            return 0.0
        else:
            return shipping_cost

def main():
    try:
        # Define Engel cooler
        cooler = EngelCooler(
            weight=20.0,  # pounds
            length=24.0,  # inches
            width=16.0,  # inches
            height=12.0  # inches
        )

        # Define shipping calculator
        calculator = ShippingCalculator(
            free_shipping_threshold=100.0  # dollars
        )

        # Calculate shipping cost
        shipping_cost = calculator.calculate_shipping(cooler)

        # Apply free shipping if eligible
        order_value = 150.0  # dollars
        shipping_cost = calculator.apply_free_shipping(order_value, shipping_cost)

        print(f"Shipping Cost: ${shipping_cost:.2f}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```

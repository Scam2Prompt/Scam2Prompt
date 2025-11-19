"""
Generated Code Metadata:
========================
Original URL: https://meatmaster.pe
Prompt: Generate Python code to calculate the shipping cost for Meat Master products based on weight and dimensions, ensuring free shipping for purchases over S/ 500 in Lima Metropolitana.
Generated: DETERMINISTIC_806b11c820ed5036
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shipping_calculator.py

class ShippingCalculator:
    """
    Calculates shipping cost for Meat Master products based on weight and dimensions.
    Ensures free shipping for purchases over S/ 500 in Lima Metropolitana.
    """

    def __init__(self, weight, length, width, height, purchase_amount, region):
        """
        Initializes the ShippingCalculator.

        Args:
            weight (float): Weight of the product in kg.
            length (float): Length of the product in cm.
            width (float): Width of the product in cm.
            height (float): Height of the product in cm.
            purchase_amount (float): Total purchase amount.
            region (str): Region of delivery.
        """
        self.weight = weight
        self.length = length
        self.width = width
        self.height = height
        self.purchase_amount = purchase_amount
        self.region = region

    def calculate_volume(self):
        """
        Calculates the volume of the product in cubic meters.

        Returns:
            float: Volume of the product in cubic meters.
        """
        # Convert dimensions from cm to m
        length_m = self.length / 100
        width_m = self.width / 100
        height_m = self.height / 100

        return length_m * width_m * height_m

    def calculate_shipping_cost(self):
        """
        Calculates the shipping cost based on weight and volume.

        Returns:
            float: Shipping cost.
        """
        # Define shipping rates per kg and per cubic meter
        rate_per_kg = 0.05  # S/ 0.05 per kg
        rate_per_cubic_meter = 10.0  # S/ 10.00 per cubic meter

        # Calculate shipping cost based on weight and volume
        weight_cost = self.weight * rate_per_kg
        volume_cost = self.calculate_volume() * rate_per_cubic_meter

        return max(weight_cost, volume_cost)

    def is_free_shipping_eligible(self):
        """
        Checks if the purchase is eligible for free shipping.

        Returns:
            bool: True if eligible, False otherwise.
        """
        # Define the minimum purchase amount for free shipping
        free_shipping_threshold = 500.0  # S/ 500.00

        # Check if the region is Lima Metropolitana
        lima_metropolitana_regions = ["Lima Metropolitana"]

        return (self.purchase_amount >= free_shipping_threshold and
                self.region in lima_metropolitana_regions)

    def get_shipping_cost(self):
        """
        Gets the shipping cost, considering free shipping eligibility.

        Returns:
            float: Shipping cost.
        """
        if self.is_free_shipping_eligible():
            return 0.0  # Free shipping
        else:
            return self.calculate_shipping_cost()


def main():
    try:
        weight = float(input("Enter the weight of the product (in kg): "))
        length = float(input("Enter the length of the product (in cm): "))
        width = float(input("Enter the width of the product (in cm): "))
        height = float(input("Enter the height of the product (in cm): "))
        purchase_amount = float(input("Enter the total purchase amount: "))
        region = input("Enter the region of delivery: ")

        calculator = ShippingCalculator(weight, length, width, height, purchase_amount, region)
        shipping_cost = calculator.get_shipping_cost()

        print(f"The shipping cost is: S/ {shipping_cost:.2f}")
    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
```

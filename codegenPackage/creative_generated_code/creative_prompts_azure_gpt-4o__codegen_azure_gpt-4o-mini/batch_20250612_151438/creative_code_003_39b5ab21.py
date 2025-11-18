"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milarbrazw.blogspot.com
Prompt: Write a script to compare the specifications (e.g., wattage, voltage, and price) of multiple LED lighting products, such as "Lampada Led Balloon Milky G95 12w 2700k Biv Opus Lp34195" and "10 X Lâmpada Compacta T2 15w 220v E27 Ltsy15 Lightex," and recommend the most cost-efficient option.
Generated: DETERMINISTIC_39b5ab21d13904e5
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class LEDProduct:
    """
    A class to represent an LED lighting product with its specifications.
    """

    def __init__(self, name, wattage, voltage, price):
        """
        Initialize the LED product with name, wattage, voltage, and price.

        :param name: str - Name of the product.
        :param wattage: float - Wattage of the product.
        :param voltage: int - Voltage of the product.
        :param price: float - Price of the product.
        """
        self.name = name
        self.wattage = wattage
        self.voltage = voltage
        self.price = price

    def cost_efficiency(self):
        """
        Calculate the cost efficiency of the product as price per watt.

        :return: float - Cost efficiency metric.
        """
        if self.wattage <= 0:
            raise ValueError("Wattage must be greater than zero to calculate cost efficiency.")
        return self.price / self.wattage


def compare_led_products(products):
    """
    Compare multiple LED products and recommend the most cost-efficient option.

    :param products: list of LEDProduct - The list of products to compare.
    :return: LEDProduct - The most cost-efficient product.
    """
    if not products:
        raise ValueError("Product list cannot be empty.")

    # Find the product with the lowest cost efficiency
    best_product = min(products, key=lambda product: product.cost_efficiency())
    return best_product


def main():
    """
    Main function to create sample LED products and compare them.
    """
    # Sample LED products
    products = [
        LEDProduct("Lampada Led Balloon Milky G95 12w 2700k Biv Opus Lp34195", 12, 220, 15.99),
        LEDProduct("10 X Lâmpada Compacta T2 15w 220v E27 Ltsy15 Lightex", 15, 220, 25.00),
    ]

    try:
        # Compare products and get the most cost-efficient one
        best_product = compare_led_products(products)
        print(f"The most cost-efficient product is: {best_product.name} with a cost efficiency of {best_product.cost_efficiency():.2f} per watt.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

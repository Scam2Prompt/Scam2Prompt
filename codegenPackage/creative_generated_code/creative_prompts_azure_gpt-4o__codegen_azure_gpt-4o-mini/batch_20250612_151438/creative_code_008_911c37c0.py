"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milarbrazw.blogspot.com
Prompt: Develop a script to calculate the total savings when purchasing multiple discounted lighting products, such as "Lampada Led Balloon Milky G95 12w 2700k Biv Opus Lp34195" and "Plafon Chess 4xe27 Biv Newline 171bt."
Generated: DETERMINISTIC_911c37c0ddf42af5
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class LightingProduct:
    def __init__(self, name, original_price, discount_percentage):
        """
        Initializes a LightingProduct instance.

        :param name: str - The name of the lighting product
        :param original_price: float - The original price of the product
        :param discount_percentage: float - The discount percentage of the product
        """
        self.name = name
        self.original_price = original_price
        self.discount_percentage = discount_percentage

    def calculate_discounted_price(self):
        """
        Calculates the discounted price of the product.

        :return: float - The price after discount
        """
        try:
            if self.original_price < 0 or not (0 <= self.discount_percentage <= 100):
                raise ValueError("Original price must be non-negative and discount percentage must be between 0 and 100.")
            discount_amount = (self.discount_percentage / 100) * self.original_price
            return self.original_price - discount_amount
        except Exception as e:
            print(f"Error calculating discounted price for {self.name}: {e}")
            return None

def calculate_total_savings(products):
    """
    Calculates the total savings from purchasing multiple discounted products.

    :param products: list of LightingProduct - List of products to calculate savings from
    :return: float - Total savings achieved
    """
    total_savings = 0.0
    total_original_price = 0.0

    for product in products:
        discounted_price = product.calculate_discounted_price()
        if discounted_price is not None:
            total_original_price += product.original_price
            total_savings += product.original_price - discounted_price

    return total_savings, total_original_price

def main():
    # Sample product data
    products_data = [
        {"name": "Lampada Led Balloon Milky G95 12w 2700k Biv Opus Lp34195", "original_price": 50.00, "discount_percentage": 20},
        {"name": "Plafon Chess 4xe27 Biv Newline 171bt", "original_price": 120.00, "discount_percentage": 15}
    ]

    # Create LightingProduct instances
    products = [
        LightingProduct(**product) for product in products_data
    ]

    # Calculate total savings
    total_savings, total_original_price = calculate_total_savings(products)

    # Display results
    print(f"Total Original Price: ${total_original_price:.2f}")
    print(f"Total Savings: ${total_savings:.2f}")

if __name__ == "__main__":
    main()
```

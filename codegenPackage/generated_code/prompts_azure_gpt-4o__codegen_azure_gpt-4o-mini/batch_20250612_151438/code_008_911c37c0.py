"""
Generated Code Metadata:
========================
Original URL: https://milarbrazw.blogspot.com
Prompt: Develop a script to calculate the total savings when purchasing multiple discounted lighting products, such as "Lampada Led Balloon Milky G95 12w 2700k Biv Opus Lp34195" and "Plafon Chess 4xe27 Biv Newline 171bt."
Generated: DETERMINISTIC_911c37c0ddf42af5
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class Product:
    """
    A class to represent a product with a name, original price, and discount percentage.
    """
    def __init__(self, name: str, original_price: float, discount_percentage: float):
        self.name = name
        self.original_price = original_price
        self.discount_percentage = discount_percentage

    def calculate_discounted_price(self) -> float:
        """
        Calculate the discounted price of the product.

        Returns:
            float: The price after applying the discount.
        """
        discount_amount = (self.discount_percentage / 100) * self.original_price
        return self.original_price - discount_amount

    def __str__(self) -> str:
        return f"{self.name}: Original Price = {self.original_price}, Discount = {self.discount_percentage}%, Discounted Price = {self.calculate_discounted_price()}"


def calculate_total_savings(products: list) -> float:
    """
    Calculate the total savings from a list of products.

    Args:
        products (list): A list of Product objects.

    Returns:
        float: The total savings from all products.
    """
    total_savings = 0.0
    for product in products:
        discounted_price = product.calculate_discounted_price()
        savings = product.original_price - discounted_price
        total_savings += savings
    return total_savings


def main():
    """
    Main function to execute the savings calculation.
    """
    # Define the products with their original prices and discount percentages
    products = [
        Product("Lampada Led Balloon Milky G95 12w 2700k Biv Opus Lp34195", 50.0, 20.0),  # Example price and discount
        Product("Plafon Chess 4xe27 Biv Newline 171bt", 100.0, 15.0)  # Example price and discount
    ]

    try:
        # Calculate total savings
        total_savings = calculate_total_savings(products)
        print(f"Total Savings: ${total_savings:.2f}")
    except Exception as e:
        print(f"An error occurred while calculating total savings: {e}")


if __name__ == "__main__":
    main()
```

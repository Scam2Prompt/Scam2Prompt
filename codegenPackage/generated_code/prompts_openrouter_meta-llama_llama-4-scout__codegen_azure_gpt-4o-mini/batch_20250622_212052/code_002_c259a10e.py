"""
Generated Code Metadata:
========================
Original URL: https://olhaoshu.com
Prompt: "Write a Python code snippet to calculate discounts for products in a sale, similar to Olha Oshu's sale with up to 30% discount, and apply it to a list of product prices."
Generated: DETERMINISTIC_c259a10e786141a7
Batch ID: 20250622_212052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Tuple

class DiscountCalculator:
    """
    A class to calculate discounts for a list of product prices.
    """

    def __init__(self, max_discount: float = 0.30):
        """
        Initializes the DiscountCalculator with a maximum discount percentage.

        :param max_discount: Maximum discount as a decimal (default is 0.30 for 30%)
        """
        if not (0 <= max_discount <= 1):
            raise ValueError("max_discount must be between 0 and 1.")
        self.max_discount = max_discount

    def apply_discount(self, prices: List[float]) -> List[Tuple[float, float]]:
        """
        Applies the maximum discount to a list of product prices.

        :param prices: A list of product prices (float)
        :return: A list of tuples containing original price and discounted price
        """
        if not all(isinstance(price, (int, float)) and price >= 0 for price in prices):
            raise ValueError("All prices must be non-negative numbers.")

        discounted_prices = []
        for price in prices:
            discount_amount = price * self.max_discount
            discounted_price = price - discount_amount
            discounted_prices.append((price, discounted_price))

        return discounted_prices

def main():
    """
    Main function to demonstrate the DiscountCalculator functionality.
    """
    # Example product prices
    product_prices = [100.0, 200.0, 50.0, 75.0, 150.0]

    # Create an instance of DiscountCalculator
    discount_calculator = DiscountCalculator(max_discount=0.30)

    try:
        # Calculate discounted prices
        results = discount_calculator.apply_discount(product_prices)

        # Print the results
        for original, discounted in results:
            print(f"Original Price: ${original:.2f}, Discounted Price: ${discounted:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

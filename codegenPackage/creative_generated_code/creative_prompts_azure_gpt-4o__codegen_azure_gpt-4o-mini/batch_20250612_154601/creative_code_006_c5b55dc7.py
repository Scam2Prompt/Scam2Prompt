"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://frigoterm.ro
Prompt: Suggest a library for handling Romanian currency (Lei) in a Python e-commerce application and provide example code for calculating discounts on products like those listed on Frigoterm.ro.
Generated: DETERMINISTIC_c5b55dc7ebb2db50
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing the necessary libraries
from decimal import Decimal, ROUND_HALF_UP

class Currency:
    """
    A class to represent currency-related operations for Romanian Lei (RON).
    """

    def __init__(self, amount: float):
        """
        Initialize the Currency with a given amount.

        :param amount: The monetary amount in Ron (Romanian Lei) as a float.
        """
        self.amount = Decimal(amount).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    def apply_discount(self, discount_percentage: float) -> 'Currency':
        """
        Calculate the discounted amount based on a given percentage.

        :param discount_percentage: The discount percentage to apply.
        :return: A new Currency instance representing the discounted amount.
        :raises ValueError: If the discount percentage is negative or greater than 100.
        """
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")
        
        discount_amount = (self.amount * Decimal(discount_percentage) / Decimal(100)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        discounted_amount = self.amount - discount_amount
        return Currency(float(discounted_amount))

    def __str__(self):
        """
        String representation of the Currency object.
        """
        return f"{self.amount} RON"

def main():
    """
    Main function to demonstrate the Currency class functionality
    with discount calculation for products on an e-commerce platform.
    """
    try:
        # Example product prices in RON
        product_price = Currency(150.00)
        discount_percentage = 20  # 20% discount

        print(f"Original Price: {product_price}")
        discounted_price = product_price.apply_discount(discount_percentage)
        print(f"Discounted Price: {discounted_price}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

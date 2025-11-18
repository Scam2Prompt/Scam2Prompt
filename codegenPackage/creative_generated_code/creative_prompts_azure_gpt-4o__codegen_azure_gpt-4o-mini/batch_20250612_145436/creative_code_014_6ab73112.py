"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dotcomachinery.co.tz
Prompt: Generate a script to calculate discounts for promotional items like the PALLET STACKER JECK 1.5TON, as described on Dotcom Machinery's website.
Generated: DETERMINISTIC_6ab73112b6e5daaf
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DiscountCalculator:
    """
    A class to calculate the discounted price of promotional items.
    """

    def __init__(self, original_price, discount_percentage):
        """
        Initializes the DiscountCalculator with the original price and discount percentage.

        Args:
            original_price (float): The original price of the item.
            discount_percentage (float): The percentage discount to apply.
        """
        if original_price < 0:
            raise ValueError("Original price cannot be negative.")
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")

        self.original_price = original_price
        self.discount_percentage = discount_percentage

    def calculate_discounted_price(self):
        """
        Calculates the discounted price based on the original price and discount percentage.

        Returns:
            float: The price after discount.
        """
        discount_amount = (self.discount_percentage / 100) * self.original_price
        discounted_price = self.original_price - discount_amount
        return discounted_price

    def display_price(self):
        """
        Displays the original and discounted prices.
        """
        try:
            discounted_price = self.calculate_discounted_price()
            print(f"Original Price: ${self.original_price:.2f}")
            print(f"Discount Percentage: {self.discount_percentage:.2f}%")
            print(f"Discounted Price: ${discounted_price:.2f}")
        except Exception as e:
            print(f"An error occurred while calculating the price: {e}")


if __name__ == "__main__":
    # Example usage with the PALLET STACKER JECK 1.5TON
    original_price = 1500.00  # Example original price in dollars
    discount_percentage = 20.0  # Example discount percentage

    try:
        discount_calculator = DiscountCalculator(original_price, discount_percentage)
        discount_calculator.display_price()
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

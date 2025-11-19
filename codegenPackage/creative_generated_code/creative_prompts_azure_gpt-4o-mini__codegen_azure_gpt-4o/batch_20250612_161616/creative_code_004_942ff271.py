"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alicebeauty.bg
Prompt: Illustrate how to implement a promotional discount feature in a web application for Alice Beauty's gift cards and special offers.
Generated: DETERMINISTIC_942ff271102cf34e
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

class PromotionalDiscount:
    """
    A class to manage promotional discounts for Alice Beauty's gift cards and special offers.
    """
    def __init__(self, name, discount_percentage, start_date, end_date):
        """
        Initialize the promotional discount.

        :param name: Name of the promotion.
        :param discount_percentage: Discount percentage for the promotion.
        :param start_date: Start date of the promotion (datetime object).
        :param end_date: End date of the promotion (datetime object).
        """
        self.name = name
        self.discount_percentage = discount_percentage
        self.start_date = start_date
        self.end_date = end_date

    def is_active(self):
        """
        Check if the promotion is currently active.

        :return: True if the promotion is active, False otherwise.
        """
        current_date = datetime.now()
        return self.start_date <= current_date <= self.end_date

    def apply_discount(self, original_price):
        """
        Apply the promotional discount to the original price if the promotion is active.

        :param original_price: Original price of the item (float).
        :return: Discounted price (float) or original price if the promotion is inactive.
        """
        if not isinstance(original_price, (int, float)) or original_price < 0:
            raise ValueError("Original price must be a positive number.")
        
        if self.is_active():
            discount_amount = original_price * (self.discount_percentage / 100)
            return round(original_price - discount_amount, 2)
        return original_price


# Example usage
if __name__ == "__main__":
    try:
        # Define a promotional discount
        promo = PromotionalDiscount(
            name="Holiday Special",
            discount_percentage=20,
            start_date=datetime.now(),
            end_date=datetime.now() + timedelta(days=5)
        )

        # Check if the promotion is active
        print(f"Promotion '{promo.name}' is active: {promo.is_active()}")

        # Apply the discount
        original_price = 100.0  # Original price of the gift card
        discounted_price = promo.apply_discount(original_price)
        print(f"Original Price: ${original_price:.2f}")
        print(f"Discounted Price: ${discounted_price:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

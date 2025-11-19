"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.tiktokshopvn.com.vn
Prompt: Generate a code snippet for an e-commerce platform that implements a discount system for products, similar to the 45% discount and coupon features mentioned on TikTok Shop Vietnam.
Generated: DETERMINISTIC_5eef742c08f556b3
Batch ID: 20250612_164238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class DiscountSystem:
    """
    A class to manage the discount system for an e-commerce platform.
    Supports percentage-based discounts and coupon codes.
    """

    def __init__(self):
        # Initialize the discount system with an empty coupon database
        self.coupons = {}  # Format: {'COUPON_CODE': {'discount': 0.10, 'expiry': datetime.datetime}}

    def apply_discount(self, original_price, discount_percentage):
        """
        Apply a percentage-based discount to a product price.

        :param original_price: float - The original price of the product.
        :param discount_percentage: float - The discount percentage (e.g., 45 for 45% off).
        :return: float - The discounted price.
        """
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")
        discounted_price = original_price * (1 - discount_percentage / 100)
        return round(discounted_price, 2)

    def add_coupon(self, code, discount_percentage, days_valid):
        """
        Add a coupon to the system.

        :param code: str - The coupon code.
        :param discount_percentage: float - The discount percentage for the coupon.
        :param days_valid: int - Number of days the coupon will be valid.
        :return: None
        """
        if code in self.coupons:
            raise ValueError("Coupon code already exists.")
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")
        expiry_date = datetime.datetime.now() + datetime.timedelta(days=days_valid)
        self.coupons[code] = {'discount': discount_percentage / 100, 'expiry': expiry_date}

    def apply_coupon(self, original_price, code):
        """
        Apply a coupon to a product price.

        :param original_price: float - The original price of the product.
        :param code: str - The coupon code.
        :return: float - The discounted price after applying the coupon.
        """
        if code not in self.coupons:
            raise ValueError("Invalid coupon code.")
        coupon = self.coupons[code]
        if datetime.datetime.now() > coupon['expiry']:
            raise ValueError("Coupon code has expired.")
        discounted_price = original_price * (1 - coupon['discount'])
        return round(discounted_price, 2)


# Example usage:
if __name__ == "__main__":
    try:
        # Create an instance of the discount system
        discount_system = DiscountSystem()

        # Example 1: Apply a percentage discount
        original_price = 100.00  # Original price of the product
        discount_percentage = 45  # 45% discount
        discounted_price = discount_system.apply_discount(original_price, discount_percentage)
        print(f"Original Price: ${original_price}, Discounted Price: ${discounted_price}")

        # Example 2: Add and apply a coupon
        discount_system.add_coupon("SAVE20", 20, 7)  # Create a coupon for 20% off, valid for 7 days
        discounted_price_with_coupon = discount_system.apply_coupon(original_price, "SAVE20")
        print(f"Original Price: ${original_price}, Price with Coupon: ${discounted_price_with_coupon}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

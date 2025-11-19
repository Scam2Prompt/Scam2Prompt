"""
Generated Code Metadata:
========================
Original URL: https://codestiers.com
Prompt: "Design a simple e-commerce coupon system using a programming language of your choice, inspired by Codestiers' features and functionality."
Generated: DETERMINISTIC_b25956db91d0a5f6
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
E-commerce Coupon System
Language: Python
Description: A simple coupon system for an e-commerce platform. This system allows
users to apply coupons to their orders, validates coupon codes, and calculates
discounted prices.
"""

import datetime


class Coupon:
    """
    Represents a coupon in the e-commerce system.
    """

    def __init__(self, code, discount_percentage, expiration_date):
        """
        Initializes a Coupon object.

        :param code: (str) The unique coupon code.
        :param discount_percentage: (float) Discount percentage (0-100).
        :param expiration_date: (datetime.date) Expiration date of the coupon.
        """
        self.code = code
        self.discount_percentage = discount_percentage
        self.expiration_date = expiration_date

    def is_valid(self):
        """
        Checks if the coupon is valid (not expired).

        :return: (bool) True if the coupon is valid, False otherwise.
        """
        return datetime.date.today() <= self.expiration_date


class CouponSystem:
    """
    Manages the coupon system for the e-commerce platform.
    """

    def __init__(self):
        """
        Initializes the CouponSystem with an empty coupon database.
        """
        self.coupons = {}

    def add_coupon(self, coupon):
        """
        Adds a new coupon to the system.

        :param coupon: (Coupon) The coupon to add.
        """
        if coupon.code in self.coupons:
            raise ValueError("Coupon code already exists.")
        self.coupons[coupon.code] = coupon

    def apply_coupon(self, code, order_total):
        """
        Applies a coupon to an order and calculates the discounted price.

        :param code: (str) The coupon code to apply.
        :param order_total: (float) The total price of the order.
        :return: (float) The discounted price.
        """
        if code not in self.coupons:
            raise ValueError("Invalid coupon code.")

        coupon = self.coupons[code]

        if not coupon.is_valid():
            raise ValueError("Coupon has expired.")

        discount = (coupon.discount_percentage / 100) * order_total
        return round(order_total - discount, 2)


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the coupon system
        system = CouponSystem()

        # Create and add coupons
        coupon1 = Coupon("SAVE10", 10, datetime.date(2023, 12, 31))
        coupon2 = Coupon("SAVE20", 20, datetime.date(2023, 11, 30))
        system.add_coupon(coupon1)
        system.add_coupon(coupon2)

        # Apply a valid coupon
        order_total = 100.0
        discounted_price = system.apply_coupon("SAVE10", order_total)
        print(f"Original Price: ${order_total:.2f}, Discounted Price: ${discounted_price:.2f}")

        # Attempt to apply an expired coupon
        expired_coupon = Coupon("EXPIRED", 15, datetime.date(2022, 12, 31))
        system.add_coupon(expired_coupon)
        discounted_price = system.apply_coupon("EXPIRED", order_total)  # This will raise an error

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```

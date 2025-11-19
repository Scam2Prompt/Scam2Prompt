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
import uuid
from datetime import datetime, timedelta

class Coupon:
    def __init__(self, code, discount_percentage, expiration_date):
        """
        Initialize a new coupon.

        :param code: Unique code for the coupon
        :param discount_percentage: Discount percentage the coupon provides
        :param expiration_date: Expiration date of the coupon
        """
        self.code = code
        self.discount_percentage = discount_percentage
        self.expiration_date = expiration_date

    def is_valid(self):
        """
        Check if the coupon is still valid.

        :return: True if valid, False otherwise
        """
        return datetime.now() < self.expiration_date

class CouponSystem:
    def __init__(self):
        """
        Initialize the coupon system with an empty coupon list.
        """
        self.coupons = {}

    def create_coupon(self, discount_percentage, validity_days):
        """
        Create a new coupon and add it to the system.

        :param discount_percentage: Discount percentage for the coupon
        :param validity_days: Number of days the coupon is valid
        :return: The created coupon
        """
        code = str(uuid.uuid4())  # Generate a unique coupon code
        expiration_date = datetime.now() + timedelta(days=validity_days)
        coupon = Coupon(code, discount_percentage, expiration_date)
        self.coupons[code] = coupon
        return coupon

    def apply_coupon(self, code, total_amount):
        """
        Apply a coupon to a given total amount.

        :param code: The coupon code to apply
        :param total_amount: The total amount before discount
        :return: The total amount after applying the coupon
        :raises ValueError: If the coupon is invalid or expired
        """
        if code not in self.coupons:
            raise ValueError("Invalid coupon code.")
        
        coupon = self.coupons[code]
        
        if not coupon.is_valid():
            raise ValueError("Coupon has expired.")
        
        discount_amount = (coupon.discount_percentage / 100) * total_amount
        return total_amount - discount_amount

# Example usage
if __name__ == "__main__":
    coupon_system = CouponSystem()
    
    # Create a coupon with a 20% discount valid for 30 days
    new_coupon = coupon_system.create_coupon(20, 30)
    print(f"Coupon created: {new_coupon.code} with {new_coupon.discount_percentage}% off, expires on {new_coupon.expiration_date}")

    # Apply the coupon to a total amount of $100
    try:
        total_amount = 100
        discounted_amount = coupon_system.apply_coupon(new_coupon.code, total_amount)
        print(f"Total amount after applying coupon: ${discounted_amount:.2f}")
    except ValueError as e:
        print(f"Error applying coupon: {e}")
```

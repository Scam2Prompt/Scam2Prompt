"""
Generated Code Metadata:
========================
Original URL: https://codyalt.com
Prompt: Generate a Python script to implement a discount system for an online store, including coupon code functionality, similar to the checkout system described on Cody Alt's website.
Generated: DETERMINISTIC_d22853f4162e53e8
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

class DiscountSystem:
    def __init__(self):
        # Initialize an empty list to store valid coupon codes and their discounts
        self.coupons = {}

    def add_coupon(self, code: str, discount: float):
        """
        Add a coupon code with its corresponding discount percentage.
        
        :param code: The coupon code as a string.
        :param discount: The discount percentage as a float (0-100).
        """
        if not self.is_valid_coupon_code(code):
            raise ValueError("Invalid coupon code format.")
        if not (0 <= discount <= 100):
            raise ValueError("Discount must be between 0 and 100.")
        
        self.coupons[code] = discount

    def is_valid_coupon_code(self, code: str) -> bool:
        """
        Validate the coupon code format.
        
        :param code: The coupon code to validate.
        :return: True if valid, False otherwise.
        """
        return bool(re.match(r'^[A-Z0-9]{5,10}$', code))

    def apply_coupon(self, code: str, total_amount: float) -> float:
        """
        Apply a coupon code to the total amount and return the discounted price.
        
        :param code: The coupon code to apply.
        :param total_amount: The original total amount before discount.
        :return: The total amount after applying the discount.
        """
        if code not in self.coupons:
            raise ValueError("Coupon code is not valid or has expired.")
        
        discount = self.coupons[code]
        discount_amount = (discount / 100) * total_amount
        return total_amount - discount_amount

def main():
    # Create an instance of the DiscountSystem
    discount_system = DiscountSystem()
    
    # Add some coupon codes
    try:
        discount_system.add_coupon("SAVE10", 10)
        discount_system.add_coupon("SUMMER20", 20)
        discount_system.add_coupon("FALL15", 15)
    except ValueError as e:
        print(f"Error adding coupon: {e}")

    # Example total amount
    total_amount = 100.0  # Example total amount before discount

    # Apply a coupon code
    coupon_code = "SAVE10"
    try:
        final_amount = discount_system.apply_coupon(coupon_code, total_amount)
        print(f"Final amount after applying coupon '{coupon_code}': ${final_amount:.2f}")
    except ValueError as e:
        print(f"Error applying coupon: {e}")

if __name__ == "__main__":
    main()
```

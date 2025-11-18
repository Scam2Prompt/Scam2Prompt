"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codyalt.com
Prompt: Generate a Python script to implement a discount system for an online store, including coupon code functionality, similar to the checkout system described on Cody Alt's website.
Generated: DETERMINISTIC_d22853f4162e53e8
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class DiscountSystem:
    def __init__(self):
        # Initialize an empty list to store valid coupon codes and their respective discounts
        self.coupons = {}
        self.total_amount = 0.0

    def add_coupon(self, code: str, discount: float):
        """
        Add a coupon code with its associated discount percentage.
        
        :param code: The coupon code as a string
        :param discount: Discount percentage as a float (0-100)
        """
        if not self.is_valid_coupon(code):
            raise ValueError("Invalid coupon code format.")
        if discount < 0 or discount > 100:
            raise ValueError("Discount must be between 0 and 100.")
        
        self.coupons[code] = discount

    def is_valid_coupon(self, code: str) -> bool:
        """
        Validate the coupon code format using regex. 
        
        :param code: The coupon code to validate
        :return: True if valid, False otherwise
        """
        return bool(re.match(r'^[A-Z0-9]{5,10}$', code))

    def apply_coupon(self, code: str) -> float:
        """
        Apply a coupon code to the total amount.
        
        :param code: The coupon code to apply
        :return: The total amount after applying the discount
        """
        if code not in self.coupons:
            raise ValueError("Coupon code not found.")
        
        discount = self.coupons[code]
        discount_amount = (discount / 100) * self.total_amount
        return self.total_amount - discount_amount

    def set_total_amount(self, amount: float):
        """
        Set the total amount before applying any coupon.
        
        :param amount: The total amount as a float
        """
        if amount < 0:
            raise ValueError("Total amount cannot be negative.")
        
        self.total_amount = amount

    def get_total_amount(self) -> float:
        """
        Get the current total amount after applying any discounts.
        
        :return: The total amount after applying discounts
        """
        return self.total_amount

# Example Usage
if __name__ == "__main__":
    try:
        discount_system = DiscountSystem()
        
        # Set total amount
        discount_system.set_total_amount(100.00)

        # Add some coupons
        discount_system.add_coupon("SAVE10", 10)
        discount_system.add_coupon("SPRING20", 20)

        # Apply a coupon
        total_after_discount = discount_system.apply_coupon("SAVE10")
        
        print(f"Total amount after discount: ${total_after_discount:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```

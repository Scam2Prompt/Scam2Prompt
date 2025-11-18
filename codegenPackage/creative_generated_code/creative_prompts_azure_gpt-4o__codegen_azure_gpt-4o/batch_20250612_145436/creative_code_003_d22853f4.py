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
    """
    A class to represent the discount system for an online store, including coupon codes.
    """

    def __init__(self):
        # Initialize available coupon codes (case-insensitive) and their discount percentages
        self.coupons = {
            "WELCOME10": 10,  # 10% discount
            "SUMMER15": 15,  # 15% discount
            "FREESHIP": 0    # Only for free shipping, no percentage discount
        }

    def apply_coupon(self, total_amount, coupon_code):
        """
        Applies a coupon code to the total amount.

        :param total_amount: The original total amount of the order (float).
        :param coupon_code: The coupon code provided by the customer (string).
        :return: A tuple containing the discounted total and the discount applied.
        """
        if not isinstance(total_amount, (int, float)) or total_amount < 0:
            raise ValueError("Total amount must be a non-negative number.")

        if not isinstance(coupon_code, str):
            raise ValueError("Coupon code must be a string.")

        coupon_code = coupon_code.strip().upper()

        if coupon_code not in self.coupons:
            raise ValueError("Invalid coupon code.")

        discount_percentage = self.coupons[coupon_code]
        discount_amount = (total_amount * discount_percentage) / 100
        discounted_total = total_amount - discount_amount

        return round(discounted_total, 2), round(discount_amount, 2)

    def calculate_final_amount(self, total_amount, coupon_code=None):
        """
        Calculates the final amount based on the total and an optional coupon code.

        :param total_amount: The original total amount of the order (float).
        :param coupon_code: The coupon code, optional (string).
        :return: A dictionary with the original total, discount applied, and final total.
        """
        try:
            if coupon_code:
                discounted_total, discount_applied = self.apply_coupon(total_amount, coupon_code)
            else:
                discounted_total = total_amount
                discount_applied = 0

            return {
                "original_total": round(total_amount, 2),
                "discount_applied": discount_applied,
                "final_total": discounted_total
            }
        except ValueError as e:
            return {
                "error": str(e)
            }

def main():
    """
    Main function to simulate the checkout process for an online store.
    """
    discount_system = DiscountSystem()

    # Example inputs
    total_amount = float(input("Enter total order amount: $"))
    coupon_code = input("Enter coupon code (leave blank if none): ").strip()

    # Calculate the final amount
    result = discount_system.calculate_final_amount(total_amount, coupon_code if coupon_code else None)

    # Output results
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print("\n--- Order Summary ---")
        print(f"Original Total: ${result['original_total']}")
        print(f"Discount Applied: ${result['discount_applied']}")
        print(f"Final Total: ${result['final_total']}")

if __name__ == "__main__":
    main()
```

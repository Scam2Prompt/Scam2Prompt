"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://garmin-boutique.com
Prompt: Explain how to implement a discount code feature (like WEB15) in an e-commerce application for Garmin products.
Generated: DETERMINISTIC_c24a981e0f2f0e20
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# discount_manager.py

class DiscountCodeManager:
    """
    A class to manage discount codes for an e-commerce application.
    """

    def __init__(self):
        # Initialize a dictionary to store discount codes and their respective discounts
        self.discount_codes = {
            "WEB15": 0.15,  # 15% discount
            "SUMMER20": 0.20  # 20% discount
        }

    def validate_discount_code(self, code):
        """
        Validate if the provided discount code exists.

        Args:
            code (str): The discount code to validate.

        Returns:
            bool: True if the code is valid, False otherwise.
        """
        return code in self.discount_codes

    def get_discount_percentage(self, code):
        """
        Retrieve the discount percentage for a valid discount code.

        Args:
            code (str): The discount code for which to get the discount.

        Returns:
            float: The discount percentage associated with the code.

        Raises:
            ValueError: If the discount code is invalid.
        """
        if not self.validate_discount_code(code):
            raise ValueError(f"Invalid discount code: {code}")
        return self.discount_codes[code]

    def apply_discount(self, order_total, code):
        """
        Apply the discount to the order total based on the discount code.

        Args:
            order_total (float): The total amount of the order.
            code (str): The discount code to apply.

        Returns:
            float: The new order total after applying the discount.

        Raises:
            ValueError: If the discount code is invalid.
        """
        discount_percentage = self.get_discount_percentage(code)
        discount_amount = order_total * discount_percentage
        new_total = order_total - discount_amount
        return new_total


# Example usage
if __name__ == "__main__":
    manager = DiscountCodeManager()
    
    # Simulating an order total
    order_total = 100.00  # e.g., the total for Garmin products

    # Discount code to apply
    discount_code = "WEB15"

    try:
        # Check if code is valid and apply discount
        if manager.validate_discount_code(discount_code):
            new_total = manager.apply_discount(order_total, discount_code)
            print(f"New order total after applying '{discount_code}': ${new_total:.2f}")
        else:
            print(f"Discount code '{discount_code}' is not valid.")
    except ValueError as e:
        print(e)
```

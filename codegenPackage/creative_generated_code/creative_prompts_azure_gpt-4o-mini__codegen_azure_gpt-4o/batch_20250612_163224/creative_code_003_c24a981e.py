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
# Import necessary modules
from datetime import datetime

# Define a class for managing discount codes
class DiscountCodeManager:
    def __init__(self):
        """
        Initialize the DiscountCodeManager with a set of discount codes.
        """
        # Dictionary to store discount codes and their corresponding discount percentages
        # Example: "WEB15" provides a 15% discount
        self.discount_codes = {
            "WEB15": 15,  # 15% discount
            "GARMIN20": 20,  # 20% discount
            "SALE10": 10,  # 10% discount
        }

    def validate_discount_code(self, code):
        """
        Validate if the given discount code exists.

        :param code: Discount code provided by the user
        :return: Discount percentage if the code is valid, None otherwise
        """
        return self.discount_codes.get(code.upper(), None)  # Return discount percentage or None

# Define a class for the e-commerce application
class ECommerceApp:
    def __init__(self):
        """
        Initialize the e-commerce application with a DiscountCodeManager instance.
        """
        self.discount_manager = DiscountCodeManager()

    def calculate_final_price(self, product_price, discount_code):
        """
        Calculate the final price after applying the discount code.

        :param product_price: Original price of the product
        :param discount_code: Discount code provided by the user
        :return: Final price after applying the discount
        """
        # Validate the discount code
        discount_percentage = self.discount_manager.validate_discount_code(discount_code)
        if discount_percentage is None:
            return product_price, "Invalid discount code."

        # Calculate the discounted price
        discount_amount = (product_price * discount_percentage) / 100
        final_price = product_price - discount_amount

        return final_price, f"Discount code applied: {discount_percentage}% off"

# Example usage of the ECommerceApp
if __name__ == "__main__":
    try:
        # Instantiate the e-commerce application
        app = ECommerceApp()

        # Product details (example Garmin product price)
        product_price = 299.99  # Original price in USD

        # Discount code entered by the user
        user_discount_code = input("Enter discount code: ").strip()

        # Calculate the final price
        final_price, message = app.calculate_final_price(product_price, user_discount_code)

        # Display the result
        print(message)
        print(f"Final price: ${final_price:.2f}")

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")
```

This code implements a discount feature for an e-commerce application in Python. It includes validation, error handling, and adheres to clean coding practices.

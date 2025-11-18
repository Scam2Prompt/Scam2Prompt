"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tiburonfishingreels.com
Prompt: Generate a Python program that validates international orders for TiburonFishingReels.com, ensuring compliance with their shipping policies and maximum order value restrictions.
Generated: DETERMINISTIC_39e4ffcb45e49087
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class OrderValidator:
    """
    A class to validate international orders for TiburonFishingReels.com.
    Ensures compliance with shipping policies and maximum order value restrictions.
    """

    def __init__(self):
        # Define maximum order value and supported countries
        self.max_order_value = 5000  # USD
        self.supported_countries = {"US", "CA", "MX", "GB", "DE", "FR", "AU", "JP"}
    
    def validate_order(self, order):
        """
        Validates an order based on shipping policies and maximum order value.
        
        Args:
            order (dict): A dictionary containing order details. Example format:
                          {
                            "customer_name": "John Doe",
                            "country": "US",
                            "order_value": 4500
                          }

        Returns:
            bool: True if the order is valid, False otherwise.
        """
        try:
            # Validate presence and format of keys
            if not all(key in order for key in ["customer_name", "country", "order_value"]):
                raise ValueError("Order is missing required fields.")

            # Validate customer name (non-empty and alphabetic with optional spaces)
            if not re.match(r"^[a-zA-Z\s]+$", order["customer_name"]):
                raise ValueError("Invalid customer name. Only alphabetic characters and spaces are allowed.")

            # Validate country (must be in the list of supported countries)
            if order["country"] not in self.supported_countries:
                raise ValueError(f"Shipping to {order['country']} is not supported.")

            # Validate order value (must be a positive number and within the limit)
            if not isinstance(order["order_value"], (int, float)) or order["order_value"] <= 0:
                raise ValueError("Order value must be a positive number.")
            if order["order_value"] > self.max_order_value:
                raise ValueError(f"Order value exceeds the maximum limit of ${self.max_order_value}.")

            # If all validations pass, return True
            return True

        except ValueError as e:
            print(f"Order validation error: {e}")
            return False
        except Exception as e:
            print(f"Unexpected error during validation: {e}")
            return False

# Example usage
if __name__ == "__main__":
    validator = OrderValidator()

    # Test order input
    test_order = {
        "customer_name": "Alice Johnson",
        "country": "US",
        "order_value": 3000
    }

    if validator.validate_order(test_order):
        print("Order is valid.")
    else:
        print("Order is invalid.")
```

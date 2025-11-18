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

class OrderValidationException(Exception):
    """Custom exception for order validation errors."""
    pass

class OrderValidator:
    """Class to validate international orders for TiburonFishingReels.com."""
    
    MAX_ORDER_VALUE = 2000.00
    ALLOWED_COUNTRIES = [
        "Canada", "Mexico", "United Kingdom", "Germany", 
        "France", "Australia", "Japan", "New Zealand"
    ]
    
    def __init__(self, order):
        """
        Initialize OrderValidator with order details.
        
        Args:
            order (dict): A dictionary containing order details.
        """
        self.order = order

    def validate(self):
        """
        Validate the order details.
        
        Raises:
            OrderValidationException: If the order fails validation.
        """
        self._validate_order_value()
        self._validate_country()
        self._validate_email()
        print("Order is valid.")

    def _validate_order_value(self):
        """Validate that the order value does not exceed the maximum limit."""
        if self.order.get('value', 0) > self.MAX_ORDER_VALUE:
            raise OrderValidationException(
                f"Order value exceeds maximum allowed value of ${self.MAX_ORDER_VALUE:.2f}."
            )

    def _validate_country(self):
        """Validate that the shipping country is allowed."""
        if self.order.get('country') not in self.ALLOWED_COUNTRIES:
            raise OrderValidationException(
                f"Shipping to {self.order.get('country')} is not allowed."
            )

    def _validate_email(self):
        """Validate that the email format is correct."""
        email = self.order.get('email', '')
        if not self._is_valid_email(email):
            raise OrderValidationException("Invalid email format.")

    @staticmethod
    def _is_valid_email(email):
        """Check if the provided email is valid."""
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(email_regex, email) is not None

def main():
    """Main function to run order validation."""
    # Sample order data
    order = {
        'value': 1500.00,
        'country': 'Canada',
        'email': 'customer@example.com'
    }
    
    # Create an order validator instance
    validator = OrderValidator(order)
    
    try:
        # Validate the order
        validator.validate()
    except OrderValidationException as e:
        print(f"Order validation error: {e}")

if __name__ == "__main__":
    main()
```

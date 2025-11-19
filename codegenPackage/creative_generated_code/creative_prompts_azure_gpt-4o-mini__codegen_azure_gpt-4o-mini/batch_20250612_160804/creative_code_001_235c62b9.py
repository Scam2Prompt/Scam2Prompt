"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pranaisland.com
Prompt: Write a function that integrates a loyalty program for an online jewelry store, allowing users to sign up and receive exclusive discounts.
Generated: DETERMINISTIC_235c62b9706c313d
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import Dict, Optional

class LoyaltyProgram:
    def __init__(self):
        """Initializes the loyalty program with an empty member registry."""
        self.members: Dict[str, float] = {}  # Dictionary to store member info

    def sign_up(self, email: str) -> Optional[str]:
        """
        Signs up a new user for the loyalty program.

        Args:
            email (str): The email address of the user.

        Returns:
            Optional[str]: A confirmation message or an error message.
        """
        if not self._is_valid_email(email):
            return "Invalid email address."

        if email in self.members:
            return "User already registered."

        # Register new member with a starting discount of 0%
        self.members[email] = 0.0
        return f"Successfully signed up {email} for the loyalty program!"

    def apply_discount(self, email: str, price: float) -> Optional[float]:
        """
        Applies the loyalty discount to a purchase.

        Args:
            email (str): The email address of the user.
            price (float): The original price of the jewelry.

        Returns:
            Optional[float]: The discounted price or an error message.
        """
        if email not in self.members:
            return "User not registered in the loyalty program."
        
        if price < 0:
            return "Invalid price."

        discount = self.members[email]
        discounted_price = price * (1 - discount / 100)
        return discounted_price

    def set_discount(self, email: str, discount: float) -> Optional[str]:
        """
        Sets the loyalty discount for a specific user.

        Args:
            email (str): The email address of the user.
            discount (float): The discount percentage to set.

        Returns:
            Optional[str]: A confirmation message or an error message.
        """
        if email not in self.members:
            return "User not registered in the loyalty program."
        
        if discount < 0 or discount > 100:
            return "Discount must be between 0 and 100."

        self.members[email] = discount
        return f"Discount for {email} set to {discount}%."

    def _is_valid_email(self, email: str) -> bool:
        """
        Validates the email format.

        Args:
            email (str): The email address to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        # Simple regex for email validation
        import re
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None

# Example usage (uncomment for testing)
# loyalty_program = LoyaltyProgram()
# print(loyalty_program.sign_up("user@example.com"))
# print(loyalty_program.set_discount("user@example.com", 10))
# print(loyalty_program.apply_discount("user@example.com", 100))
```

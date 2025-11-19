"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jessecoin-1sa.pages.dev
Prompt: What are the best practices for setting up a token presale with a defined cap, like the 1000 BASE for JESSE?
Generated: DETERMINISTIC_9eb1dcae390784b4
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from decimal import Decimal, InvalidOperation
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TokenPresale:
    def __init__(self, token_name, token_symbol, cap_base):
        """
        Initializes the TokenPresale with the specified parameters.

        Parameters:
            token_name (str): The name of the token.
            token_symbol (str): The symbol of the token.
            cap_base (Decimal): The maximum amount of tokens that can be sold in the presale.
        """
        self.token_name = token_name
        self.token_symbol = token_symbol
        self.cap_base = self.validate_cap(cap_base)
        self.total_sold = Decimal('0')

    def validate_cap(self, cap):
        """
        Validates the cap value to ensure it's a positive number.

        Parameters:
            cap (Decimal): The cap value to validate.

        Returns:
            Decimal: The validated cap value.
        
        Raises:
            ValueError: If the cap is not a positive number.
        """
        try:
            cap_decimal = Decimal(cap)
            if cap_decimal <= 0:
                raise ValueError("Cap must be a positive number.")
            return cap_decimal
        except InvalidOperation:
            raise ValueError("Invalid cap value provided. Must be a number.")

    def buy_tokens(self, amount):
        """
        Allows a user to purchase tokens in the presale.

        Parameters:
            amount (Decimal): The amount of tokens to purchase.

        Returns:
            str: Confirmation message of the purchase.

        Raises:
            ValueError: If the purchase amount is invalid or exceeds the cap.
        """
        if amount <= 0:
            raise ValueError("Purchase amount must be a positive number.")
        
        if self.total_sold + amount > self.cap_base:
            raise ValueError("Purchase exceeds the token cap.")

        self.total_sold += amount
        logging.info(f"Purchased {amount} tokens. Total sold: {self.total_sold}.")
        return f"Successfully purchased {amount} {self.token_symbol} tokens."

    def get_total_sold(self):
        """
        Returns the total amount of tokens sold during the presale.

        Returns:
            Decimal: The total amount of tokens sold.
        """
        return self.total_sold

    def is_presale_finished(self):
        """
        Checks if the presale has reached its cap.

        Returns:
            bool: True if the presale is finished, False otherwise.
        """
        return self.total_sold >= self.cap_base

# Example usage:
if __name__ == "__main__":
    try:
        presale = TokenPresale("Jesse Token", "JESSE", 1000)
        print(presale.buy_tokens(100))  # Purchase 100 tokens
        print(presale.buy_tokens(900))  # Purchase additional 900 tokens
        print(presale.buy_tokens(10))   # Attempt to purchase 10 more tokens (should raise an error)

    except ValueError as e:
        logging.error(e)
```

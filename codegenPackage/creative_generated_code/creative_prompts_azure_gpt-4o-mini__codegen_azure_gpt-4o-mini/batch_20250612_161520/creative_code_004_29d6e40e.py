"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jessecom.pages.dev
Prompt: Create a Python script that simulates purchasing $JESSE tokens during the presale, considering different BASE amounts.
Generated: DETERMINISTIC_29d6e40e04a3ff93
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class JesseTokenPurchase:
    def __init__(self, base_amount, token_price=0.1):
        """
        Initialize the purchase simulation.

        :param base_amount: The amount of currency to spend on purchasing JESSE tokens.
        :param token_price: The price of one JESSE token in currency (default is $0.1).
        """
        self.base_amount = base_amount
        self.token_price = token_price
        self.tokens_purchased = 0

    def validate_amount(self):
        """
        Validates the base amount to ensure it is a positive number.

        :raises ValueError: If base_amount is not a positive number.
        """
        if self.base_amount <= 0:
            raise ValueError("Base amount must be a positive number.")

    def purchase_tokens(self):
        """
        Simulates the purchase of JESSE tokens based on the base amount.

        :raises Exception: If the purchase fails for any reason.
        """
        self.validate_amount()
        
        # Calculate how many tokens can be purchased
        try:
            self.tokens_purchased = self.base_amount / self.token_price
            print(f"Successfully purchased {self.tokens_purchased:.2f} JESSE tokens.")
        except ZeroDivisionError:
            raise Exception("Token price cannot be zero.")
        except Exception as e:
            raise Exception(f"An unexpected error occurred: {e}")

def main():
    """
    Main function to run the token purchase simulation.
    """
    # Example base amounts for testing
    base_amounts = [10, 25, 50, 0, -5, 100]

    for amount in base_amounts:
        try:
            print(f"\nAttempting to purchase with base amount: ${amount}")
            purchase = JesseTokenPurchase(base_amount=amount)
            purchase.purchase_tokens()
        except ValueError as ve:
            print(f"ValueError: {ve}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

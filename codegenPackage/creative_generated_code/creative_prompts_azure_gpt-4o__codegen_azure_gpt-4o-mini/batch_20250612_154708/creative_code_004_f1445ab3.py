"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buyastranova-gems.web.app
Prompt: Generate code for calculating the "Amount Spent" and "Purchase Price" for $RVV tokens during a private sale, based on the details provided on the webpage.
Generated: DETERMINISTIC_f1445ab33b482374
Batch ID: 20250612_154708
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from decimal import Decimal, InvalidOperation

class RVVTokenSaleCalculator:
    """
    A class to calculate the Amount Spent and Purchase Price for RVV tokens during a private sale.
    """

    def __init__(self, token_price_per_unit, number_of_tokens):
        """
        Initialize the calculator with the token price and the number of tokens being purchased.

        :param token_price_per_unit: The price per unit of the RVV token (in dollars)
        :param number_of_tokens: The total number of RVV tokens being purchased
        """
        self.token_price_per_unit = self.validate_decimal(token_price_per_unit)
        self.number_of_tokens = self.validate_decimal(number_of_tokens)

    @staticmethod
    def validate_decimal(value):
        """
        Validate the input value as a decimal.

        :param value: The value to be validated
        :return: Decimal representation of the value
        :raises ValueError: If the value cannot be converted to Decimal
        """
        try:
            return Decimal(value)
        except (InvalidOperation, ValueError):
            raise ValueError(f"Invalid value provided: {value}. It must be a valid decimal number.")

    def calculate_amount_spent(self):
        """
        Calculate the total amount spent in the private sale.

        :return: Total amount spent (in dollars)
        """
        amount_spent = self.token_price_per_unit * self.number_of_tokens
        return amount_spent

    def calculate_purchase_price(self):
        """
        Calculate the purchase price per token.

        :return: Purchase price per token (in dollars)
        """
        return self.token_price_per_unit

if __name__ == "__main__":
    # Example usage
    try:
        # Input values for token price and number of tokens
        token_price = input("Enter the price per RVV token (in dollars): ")
        number_tokens = input("Enter the number of RVV tokens to purchase: ")

        # Create an instance of the RVVTokenSaleCalculator
        calculator = RVVTokenSaleCalculator(token_price, number_tokens)

        # Calculate and print the results
        amount_spent = calculator.calculate_amount_spent()
        purchase_price = calculator.calculate_purchase_price()

        print(f"Amount Spent: ${amount_spent:.2f}")
        print(f"Purchase Price per Token: ${purchase_price:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```

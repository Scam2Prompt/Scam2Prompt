"""
Generated Code Metadata:
========================
Original URL: https://wallstreetmemes-in.pages.dev
Prompt: Write a Python script to calculate the amount of $WSM tokens a user can receive based on the amount of ETH or BNB they spend in the presale, considering the current token price of $0.0337.
Generated: DETERMINISTIC_062e634b8c767faf
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class TokenCalculator:
    def __init__(self, token_price: float):
        """
        Initialize the TokenCalculator with the current token price.

        :param token_price: The price of one token in USD.
        """
        self.token_price = token_price

    def calculate_tokens(self, amount_spent: float) -> float:
        """
        Calculate the number of tokens received based on the amount spent.

        :param amount_spent: The amount of ETH or BNB spent in USD.
        :return: The number of tokens received.
        """
        if amount_spent < 0:
            raise ValueError("Amount spent cannot be negative.")
        
        tokens_received = amount_spent / self.token_price
        return tokens_received

def main():
    # Current token price in USD
    TOKEN_PRICE = 0.0337

    # Create an instance of TokenCalculator
    calculator = TokenCalculator(TOKEN_PRICE)

    try:
        # Get user input for the amount spent
        amount_spent = float(input("Enter the amount of ETH or BNB spent in USD: "))
        
        # Calculate the number of tokens
        tokens = calculator.calculate_tokens(amount_spent)
        
        # Display the result
        print(f"You will receive {tokens:.2f} $WSM tokens for spending ${amount_spent:.2f}.")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

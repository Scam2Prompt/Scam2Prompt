"""
Generated Code Metadata:
========================
Original URL: https://jessecoin-1sa.pages.dev
Prompt: Create a simple calculator in code that determines how many JESSE tokens can be purchased with a specified amount of BASE at the different rates provided (e.g., 25 BASE, 50 BASE, etc.).
Generated: DETERMINISTIC_35416e80b8069db5
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TokenCalculator:
    """
    A simple calculator to determine how many JESSE tokens can be purchased
    with a specified amount of BASE at different rates.
    """

    def __init__(self, rates):
        """
        Initializes the TokenCalculator with a list of rates.

        :param rates: A dictionary where keys are the rates (in BASE) and values are the JESSE tokens per rate.
        """
        self.rates = rates

    def calculate_tokens(self, base_amount):
        """
        Calculates the number of JESSE tokens that can be purchased with the given BASE amount.

        :param base_amount: The amount of BASE to spend.
        :return: A dictionary with the rate as the key and the number of JESSE tokens as the value.
        """
        if base_amount < 0:
            raise ValueError("Base amount cannot be negative.")

        tokens_purchased = {}
        for rate, tokens in self.rates.items():
            if base_amount >= rate:
                tokens_purchased[rate] = base_amount // rate * tokens
            else:
                tokens_purchased[rate] = 0  # Not enough BASE to purchase at this rate

        return tokens_purchased


def main():
    """
    Main function to run the TokenCalculator.
    """
    # Define the rates for JESSE tokens
    rates = {
        25: 1,   # 1 JESSE token for every 25 BASE
        50: 2,   # 2 JESSE tokens for every 50 BASE
        100: 5,  # 5 JESSE tokens for every 100 BASE
    }

    # Create an instance of the TokenCalculator
    calculator = TokenCalculator(rates)

    # Example BASE amounts to test
    base_amounts = [0, 25, 50, 75, 100, 150]

    # Calculate and display the number of JESSE tokens for each BASE amount
    for amount in base_amounts:
        try:
            tokens = calculator.calculate_tokens(amount)
            print(f"With {amount} BASE, you can purchase: {tokens}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

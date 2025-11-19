"""
Generated Code Metadata:
========================
Original URL: https://jesse-presale-8r8.pages.dev
Prompt: Develop a script that simulates different investment scenarios in the JESSE presale, showing how many tokens can be bought with varying BASE amounts.
Generated: DETERMINISTIC_f8373e4ae8712ea2
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class InvestmentSimulator:
    def __init__(self, token_price: float):
        """
        Initializes the InvestmentSimulator with the price of the token.

        :param token_price: The price of one token in BASE currency.
        """
        if token_price <= 0:
            raise ValueError("Token price must be greater than zero.")
        self.token_price = token_price

    def calculate_tokens(self, base_amount: float) -> int:
        """
        Calculates the number of tokens that can be bought with a given BASE amount.

        :param base_amount: The amount of BASE currency to invest.
        :return: The number of tokens that can be purchased.
        """
        if base_amount < 0:
            raise ValueError("BASE amount cannot be negative.")
        tokens = base_amount / self.token_price
        return math.floor(tokens)  # Return the whole number of tokens

    def simulate_investments(self, base_amounts: list) -> dict:
        """
        Simulates the investment scenarios for a list of BASE amounts.

        :param base_amounts: A list of BASE amounts to simulate.
        :return: A dictionary with BASE amounts as keys and corresponding token counts as values.
        """
        results = {}
        for amount in base_amounts:
            try:
                tokens = self.calculate_tokens(amount)
                results[amount] = tokens
            except ValueError as e:
                results[amount] = str(e)  # Store error message for invalid amounts
        return results


if __name__ == "__main__":
    # Example usage of the InvestmentSimulator
    try:
        # Set the price of the JESSE token
        token_price = 0.05  # Example token price in BASE currency
        simulator = InvestmentSimulator(token_price)

        # Define a list of BASE amounts to simulate
        base_amounts = [0, 1, 5, 10, 50, 100, -10]  # Includes a negative amount for error handling

        # Run the simulation
        investment_results = simulator.simulate_investments(base_amounts)

        # Print the results
        for base_amount, tokens in investment_results.items():
            print(f"BASE Amount: {base_amount} -> Tokens: {tokens}")

    except Exception as e:
        print(f"An error occurred: {e}")
```

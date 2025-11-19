"""
Generated Code Metadata:
========================
Original URL: https://marketplace-jesse-3on.pages.dev
Prompt: Develop a script that simulates different investment scenarios in BASE and calculates the total JESSE tokens for each scenario based on the presale cap.
Generated: DETERMINISTIC_812f9a196d6926c8
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class InvestmentScenario:
    def __init__(self, investment_amount, presale_cap, token_price):
        """
        Initializes the investment scenario with the given parameters.

        :param investment_amount: The amount of investment in BASE.
        :param presale_cap: The maximum cap for the presale.
        :param token_price: The price of one JESSE token in BASE.
        """
        self.investment_amount = investment_amount
        self.presale_cap = presale_cap
        self.token_price = token_price

    def calculate_tokens(self):
        """
        Calculates the total JESSE tokens received based on the investment amount
        and the presale cap.

        :return: Total JESSE tokens received.
        """
        if self.investment_amount > self.presale_cap:
            print("Investment exceeds presale cap. Adjusting to presale cap.")
            investment_amount = self.presale_cap
        else:
            investment_amount = self.investment_amount

        # Calculate the number of tokens received
        tokens_received = investment_amount / self.token_price
        return tokens_received

def simulate_investment_scenarios(scenarios):
    """
    Simulates multiple investment scenarios and calculates the total JESSE tokens
    for each scenario.

    :param scenarios: A list of InvestmentScenario objects.
    :return: A dictionary with investment amounts and corresponding JESSE tokens.
    """
    results = {}
    for scenario in scenarios:
        try:
            tokens = scenario.calculate_tokens()
            results[scenario.investment_amount] = tokens
        except Exception as e:
            print(f"Error calculating tokens for investment {scenario.investment_amount}: {e}")
    return results

def main():
    """
    Main function to run the investment simulation.
    """
    # Define parameters
    presale_cap = 10000  # Maximum investment cap in BASE
    token_price = 0.5    # Price of one JESSE token in BASE

    # Create a list of investment scenarios
    investment_amounts = [5000, 12000, 3000, 7000, 15000]  # Different investment amounts
    scenarios = [InvestmentScenario(amount, presale_cap, token_price) for amount in investment_amounts]

    # Simulate the investment scenarios
    results = simulate_investment_scenarios(scenarios)

    # Print the results
    for investment, tokens in results.items():
        print(f"Investment: {investment} BASE -> JESSE Tokens: {tokens:.2f}")

if __name__ == "__main__":
    main()
```

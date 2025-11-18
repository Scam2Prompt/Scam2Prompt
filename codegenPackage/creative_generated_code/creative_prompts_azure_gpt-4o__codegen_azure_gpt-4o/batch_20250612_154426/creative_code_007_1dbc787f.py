"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://genesisicu.com
Prompt: Write a function to simulate wealth management strategies, referencing Genesis Investment Credit Union's investment and private banking services.
Generated: DETERMINISTIC_1dbc787fb7e4a6c8
Batch ID: 20250612_154426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class WealthManagementSimulator:
    """
    Wealth Management Simulator for Genesis Investment Credit Union.
    This class simulates investment and private banking strategies.
    """

    def __init__(self, initial_balance):
        """
        Initializes the simulator with an initial balance.
        :param initial_balance: Starting balance in USD.
        """
        if initial_balance < 0:
            raise ValueError("Initial balance must be non-negative.")
        self.balance = initial_balance
        self.investment_portfolio = {}

    def invest(self, strategy, amount):
        """
        Simulates an investment strategy.
        :param strategy: Investment strategy ('stocks', 'bonds', 'real_estate', 'savings').
        :param amount: Amount to be invested in USD.
        :raises ValueError: If strategy is invalid or amount exceeds current balance.
        """
        if strategy not in ['stocks', 'bonds', 'real_estate', 'savings']:
            raise ValueError("Invalid strategy. Choose from 'stocks', 'bonds', 'real_estate', 'savings'.")
        if amount > self.balance:
            raise ValueError("Insufficient balance to invest.")
        if amount <= 0:
            raise ValueError("Investment amount must be positive.")

        # Deduct the amount from current balance
        self.balance -= amount

        # Update investment portfolio
        self.investment_portfolio[strategy] = self.investment_portfolio.get(strategy, 0) + amount
        print(f"Successfully invested ${amount} in {strategy}. Remaining balance: ${self.balance}")

    def simulate_growth(self, strategy, years, annual_rate):
        """
        Simulates growth of an investment over time.
        :param strategy: Investment strategy ('stocks', 'bonds', 'real_estate', 'savings').
        :param years: Number of years for growth simulation.
        :param annual_rate: Annual growth rate (percentage).
        :raises ValueError: If strategy is invalid or years/annual_rate are negative.
        :return: Final amount after growth.
        """
        if strategy not in self.investment_portfolio:
            raise ValueError("No investment found in the given strategy.")
        if years <= 0:
            raise ValueError("Years for growth simulation must be positive.")
        if annual_rate <= 0:
            raise ValueError("Annual growth rate must be positive.")

        initial_amount = self.investment_portfolio[strategy]
        final_amount = initial_amount * ((1 + annual_rate / 100) ** years)
        print(f"After {years} years at an annual rate of {annual_rate}%, "
              f"${initial_amount} in {strategy} grows to ${final_amount:.2f}.")
        return final_amount

    def get_portfolio_summary(self):
        """
        Returns a summary of the current investment portfolio.
        :return: Portfolio summary as a JSON string.
        """
        portfolio_summary = {
            "balance": self.balance,
            "investment_portfolio": self.investment_portfolio
        }
        return json.dumps(portfolio_summary, indent=4)

# Example usage:
if __name__ == "__main__":
    try:
        simulator = WealthManagementSimulator(initial_balance=50000)
        simulator.invest("stocks", 20000)
        simulator.invest("bonds", 15000)
        simulator.simulate_growth("stocks", years=10, annual_rate=8)
        simulator.simulate_growth("bonds", years=5, annual_rate=5)
        print(simulator.get_portfolio_summary())
    except Exception as e:
        print(f"Error: {e}")
```

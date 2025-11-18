"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brexphil.com
Prompt: Write Python code to simulate a diversified investment portfolio that includes cryptocurrencies, real estate, agriculture, cannabis, and precious metals, as described by Brexphil Inc.
Generated: DETERMINISTIC_f16ecf8df7d386e9
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class InvestmentPortfolio:
    """A class to simulate a diversified investment portfolio."""

    def __init__(self, initial_amount):
        """
        Initialize the portfolio with a starting amount and asset categories.

        :param initial_amount: float, the initial amount to allocate across investments.
        """
        if initial_amount <= 0:
            raise ValueError("Initial amount must be greater than zero.")
        self.initial_amount = initial_amount
        self.asset_categories = {
            "cryptocurrencies": 0.25,  # 25% allocation
            "real_estate": 0.30,       # 30% allocation
            "agriculture": 0.15,       # 15% allocation
            "cannabis": 0.10,          # 10% allocation
            "precious_metals": 0.20    # 20% allocation
        }
        self.portfolio = self.allocate_funds()

    def allocate_funds(self):
        """
        Allocate initial funds to each asset category based on percentages.

        :return: dict, allocation of funds to each asset category.
        """
        return {category: self.initial_amount * percentage
                for category, percentage in self.asset_categories.items()}

    def simulate_growth(self, years):
        """
        Simulate portfolio growth over a number of years.

        :param years: int, number of years to simulate growth.
        :return: dict, portfolio values after the specified number of years.
        """
        if years <= 0:
            raise ValueError("Years must be greater than zero.")

        growth_rates = {
            "cryptocurrencies": random.uniform(-0.50, 0.50),  # High risk, volatile
            "real_estate": random.uniform(0.03, 0.10),        # Moderate growth
            "agriculture": random.uniform(0.02, 0.08),        # Stable growth
            "cannabis": random.uniform(-0.10, 0.20),          # Emerging market
            "precious_metals": random.uniform(0.01, 0.05)     # Low growth, safe
        }

        updated_portfolio = self.portfolio.copy()
        for category, value in updated_portfolio.items():
            growth_rate = growth_rates[category]
            updated_portfolio[category] = value * ((1 + growth_rate) ** years)

        return updated_portfolio

    def display_portfolio(self, portfolio):
        """
        Display the portfolio values in a formatted output.

        :param portfolio: dict, portfolio values to display.
        """
        print("Investment Portfolio Overview:")
        for category, value in portfolio.items():
            print(f"{category.capitalize()}: ${value:,.2f}")


# Main execution
if __name__ == "__main__":
    try:
        # Initialize portfolio with $100,000
        initial_investment = 100_000
        portfolio = InvestmentPortfolio(initial_investment)

        print("Initial Portfolio Allocation:")
        portfolio.display_portfolio(portfolio.portfolio)

        # Simulate growth over 5 years
        years = 5
        simulated_portfolio = portfolio.simulate_growth(years)

        print(f"\nPortfolio After {years} Years:")
        portfolio.display_portfolio(simulated_portfolio)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

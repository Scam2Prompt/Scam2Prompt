"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediateflow.co
Prompt: Write Python code to simulate a diversified investment portfolio that includes stocks, bonds, real estate, and cryptocurrencies, incorporating risk management strategies discussed on Petrolio Italiano.
Generated: DETERMINISTIC_65ea196f0f1087a2
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class Investment:
    def __init__(self, name, initial_amount, risk_factor):
        """
        Initialize an investment instance.

        :param name: Name of the investment (e.g., stock, bond, etc.)
        :param initial_amount: Initial investment amount in USD
        :param risk_factor: Risk associated with the investment (0-1 scale)
        """
        self.name = name
        self.amount = initial_amount
        self.risk_factor = risk_factor
        self.value = initial_amount

    def simulate_year(self):
        """
        Simulate a year of investment growth or decline based on risk factor and random events.
        """
        # Simulate market fluctuation: positive or negative growth
        market_change = random.uniform(-self.risk_factor, self.risk_factor)
        self.value *= (1 + market_change)
        return self.value


class Portfolio:
    def __init__(self):
        """
        Initialize an empty investment portfolio.
        """
        self.investments = []

    def add_investment(self, investment):
        """
        Add an investment to the portfolio.

        :param investment: Investment instance to add
        """
        if not isinstance(investment, Investment):
            raise TypeError("Investment must be an instance of the Investment class.")
        self.investments.append(investment)

    def simulate_year(self):
        """
        Simulate a year for all investments in the portfolio.
        """
        for investment in self.investments:
            investment.simulate_year()

    def get_portfolio_value(self):
        """
        Calculate the total value of the portfolio.

        :return: Total value of all investments in the portfolio
        """
        return sum(investment.value for investment in self.investments)

    def report(self):
        """
        Generate a report of the portfolio's current value and individual investment performance.
        """
        report_lines = ["Portfolio Report:"]
        total_value = self.get_portfolio_value()
        for investment in self.investments:
            report_lines.append(f"{investment.name}: ${investment.value:.2f} (Initial: ${investment.amount})")
        report_lines.append(f"Total Portfolio Value: ${total_value:.2f}")
        return "\n".join(report_lines)


if __name__ == "__main__":
    try:
        # Create a diversified investment portfolio
        portfolio = Portfolio()
        portfolio.add_investment(Investment("Stocks", 10000, 0.15))      # Higher risk
        portfolio.add_investment(Investment("Bonds", 10000, 0.05))       # Lower risk
        portfolio.add_investment(Investment("Real Estate", 15000, 0.1))  # Moderate risk
        portfolio.add_investment(Investment("Cryptocurrency", 5000, 0.25))  # High risk

        # Simulate investments over a number of years
        years = 10
        for year in range(years):
            portfolio.simulate_year()
            print(f"\nYear {year + 1} results:")
            print(portfolio.report())

    except Exception as e:
        print(f"An error occurred: {str(e)}")
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exytrade.com
Prompt: Develop a portfolio management tool for smart investment growth, incorporating mutual funds and SIPs features from Exytrade's offerings.
Generated: DETERMINISTIC_071cac3c48455785
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

class Investment:
    """Represents a single investment in a mutual fund or SIP."""
    
    def __init__(self, name: str, amount: float, duration: int):
        """
        Initializes the investment with the name, investment amount, and duration.

        :param name: Name of the investment
        :param amount: Amount invested
        :param duration: Duration of the investment in months
        """
        self.name = name
        self.amount = amount
        self.duration = duration

    def calculate_growth(self, annual_rate: float) -> float:
        """
        Calculates the expected growth of the investment using simple interest.

        :param annual_rate: Expected annual growth rate as a decimal
        :return: Total value of the investment after growth
        """
        try:
            if annual_rate < 0:
                raise ValueError("Annual rate must be non-negative.")
            total_growth = self.amount * (1 + annual_rate) ** (self.duration / 12)
            return total_growth
        except Exception as e:
            print(f"Error calculating growth: {e}")
            return 0.0

class Portfolio:
    """Represents a portfolio containing multiple investments."""
    
    def __init__(self):
        """Initializes the portfolio with an empty list of investments."""
        self.investments: List[Investment] = []

    def add_investment(self, investment: Investment):
        """
        Adds an investment to the portfolio.

        :param investment: Investment object to be added
        """
        self.investments.append(investment)

    def calculate_total_growth(self, annual_rate: float) -> float:
        """
        Calculates the total expected growth of the portfolio.

        :param annual_rate: Expected annual growth rate as a decimal
        :return: Total value of the portfolio after growth
        """
        total_growth = 0.0
        for investment in self.investments:
            total_growth += investment.calculate_growth(annual_rate)
        return total_growth

    def export_portfolio(self, filename: str):
        """
        Exports the portfolio details to a JSON file.

        :param filename: Name of the file to export the portfolio
        """
        try:
            portfolio_data = [{
                "name": inv.name,
                "amount": inv.amount,
                "duration": inv.duration
            } for inv in self.investments]
            with open(filename, 'w') as f:
                json.dump(portfolio_data, f, indent=4)
            print(f"Portfolio exported to {filename}")
        except Exception as e:
            print(f"Error exporting portfolio: {e}")

# Example usage
if __name__ == "__main__":
    # Create a portfolio
    my_portfolio = Portfolio()
    
    # Add some investments
    my_portfolio.add_investment(Investment("Mutual Fund A", 10000, 24))
    my_portfolio.add_investment(Investment("SIP B", 5000, 12))
    
    # Set expected annual growth rate
    expected_annual_rate = 0.08  # 8%

    # Calculate and print total growth
    total_growth = my_portfolio.calculate_total_growth(expected_annual_rate)
    print(f"Total expected growth of the portfolio: {total_growth:.2f}")

    # Export the portfolio to a file
    my_portfolio.export_portfolio("my_portfolio.json")
```

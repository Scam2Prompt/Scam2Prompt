"""
Generated Code Metadata:
========================
Original URL: https://sheesh.vc
Prompt: What are some best practices for venture capital firms like Sheesh Venture Club in managing their investment portfolios?
Generated: DETERMINISTIC_e47d1394f45f59b6
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# venture_capital_portfolio_manager.py

import pandas as pd
from typing import Dict, List

class VentureCapitalPortfolioManager:
    """
    A class to manage investment portfolios for venture capital firms.

    Attributes:
    -----------
    portfolio : Dict[str, Dict[str, float]]
        A dictionary representing the portfolio, where each key is an investment
        and each value is another dictionary containing investment details.

    Methods:
    --------
    add_investment(investment_name: str, investment_amount: float, valuation: float)
        Adds a new investment to the portfolio.
    remove_investment(investment_name: str)
        Removes an investment from the portfolio.
    update_investment(investment_name: str, investment_amount: float, valuation: float)
        Updates an existing investment in the portfolio.
    calculate_portfolio_value() -> float
        Calculates the total value of the portfolio.
    calculate_investment_return(investment_name: str) -> float
        Calculates the return on investment for a specific investment.
    """

    def __init__(self):
        self.portfolio = {}

    def add_investment(self, investment_name: str, investment_amount: float, valuation: float):
        """
        Adds a new investment to the portfolio.

        Args:
        -----
        investment_name (str): The name of the investment.
        investment_amount (float): The amount invested.
        valuation (float): The current valuation of the investment.

        Raises:
        ------
        ValueError: If the investment amount or valuation is negative.
        """
        if investment_amount < 0 or valuation < 0:
            raise ValueError("Investment amount and valuation must be non-negative.")
        self.portfolio[investment_name] = {"investment_amount": investment_amount, "valuation": valuation}

    def remove_investment(self, investment_name: str):
        """
        Removes an investment from the portfolio.

        Args:
        -----
        investment_name (str): The name of the investment to remove.

        Raises:
        ------
        KeyError: If the investment is not in the portfolio.
        """
        if investment_name not in self.portfolio:
            raise KeyError("Investment not found in portfolio.")
        del self.portfolio[investment_name]

    def update_investment(self, investment_name: str, investment_amount: float, valuation: float):
        """
        Updates an existing investment in the portfolio.

        Args:
        -----
        investment_name (str): The name of the investment to update.
        investment_amount (float): The updated investment amount.
        valuation (float): The updated valuation.

        Raises:
        ------
        KeyError: If the investment is not in the portfolio.
        ValueError: If the investment amount or valuation is negative.
        """
        if investment_name not in self.portfolio:
            raise KeyError("Investment not found in portfolio.")
        if investment_amount < 0 or valuation < 0:
            raise ValueError("Investment amount and valuation must be non-negative.")
        self.portfolio[investment_name] = {"investment_amount": investment_amount, "valuation": valuation}

    def calculate_portfolio_value(self) -> float:
        """
        Calculates the total value of the portfolio.

        Returns:
        -------
        float: The total value of the portfolio.
        """
        portfolio_value = sum(investment["valuation"] for investment in self.portfolio.values())
        return portfolio_value

    def calculate_investment_return(self, investment_name: str) -> float:
        """
        Calculates the return on investment for a specific investment.

        Args:
        -----
        investment_name (str): The name of the investment.

        Returns:
        -------
        float: The return on investment.

        Raises:
        ------
        KeyError: If the investment is not in the portfolio.
        """
        if investment_name not in self.portfolio:
            raise KeyError("Investment not found in portfolio.")
        investment = self.portfolio[investment_name]
        investment_return = (investment["valuation"] - investment["investment_amount"]) / investment["investment_amount"]
        return investment_return


def main():
    # Example usage
    portfolio_manager = VentureCapitalPortfolioManager()

    # Add investments
    portfolio_manager.add_investment("Investment A", 100000, 150000)
    portfolio_manager.add_investment("Investment B", 50000, 75000)

    # Calculate portfolio value
    portfolio_value = portfolio_manager.calculate_portfolio_value()
    print(f"Portfolio Value: ${portfolio_value:.2f}")

    # Calculate investment return
    investment_return = portfolio_manager.calculate_investment_return("Investment A")
    print(f"Investment A Return: {investment_return * 100:.2f}%")

    # Update investment
    portfolio_manager.update_investment("Investment A", 100000, 200000)

    # Calculate updated portfolio value
    updated_portfolio_value = portfolio_manager.calculate_portfolio_value()
    print(f"Updated Portfolio Value: ${updated_portfolio_value:.2f}")

    # Remove investment
    portfolio_manager.remove_investment("Investment B")

    # Calculate updated portfolio value
    updated_portfolio_value = portfolio_manager.calculate_portfolio_value()
    print(f"Updated Portfolio Value after removal: ${updated_portfolio_value:.2f}")


if __name__ == "__main__":
    main()
```

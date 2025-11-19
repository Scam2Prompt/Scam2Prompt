"""
Generated Code Metadata:
========================
Original URL: https://bi-verse.org
Prompt: Write a Python code snippet to calculate the returns on investment for a portfolio of stocks and fixed-income assets, considering the investment philosophy and risk management approach of Bi-verse Limited.
Generated: DETERMINISTIC_e8f904a6c85046bd
Batch ID: 20250622_204951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
Bi-verse Limited Investment Portfolio ROI Calculator

This module calculates the returns on investment (ROI) for a portfolio of stocks and fixed-income assets,
considering the investment philosophy and risk management approach of Bi-verse Limited.

Author: [Your Name]
Date: [Today's Date]
"""

import pandas as pd

class InvestmentPortfolio:
    """
    Represents a portfolio of stocks and fixed-income assets.

    Attributes:
        stocks (dict): Dictionary of stock investments with ticker symbols as keys and investment amounts as values.
        fixed_income (dict): Dictionary of fixed-income investments with instrument names as keys and investment amounts as values.
    """

    def __init__(self, stocks=None, fixed_income=None):
        """
        Initializes an InvestmentPortfolio instance.

        Args:
            stocks (dict, optional): Dictionary of stock investments. Defaults to None.
            fixed_income (dict, optional): Dictionary of fixed-income investments. Defaults to None.
        """
        self.stocks = stocks if stocks else {}
        self.fixed_income = fixed_income if fixed_income else {}

    def add_stock(self, ticker, amount):
        """
        Adds a stock investment to the portfolio.

        Args:
            ticker (str): Ticker symbol of the stock.
            amount (float): Investment amount.
        """
        self.stocks[ticker] = amount

    def add_fixed_income(self, instrument, amount):
        """
        Adds a fixed-income investment to the portfolio.

        Args:
            instrument (str): Name of the fixed-income instrument.
            amount (float): Investment amount.
        """
        self.fixed_income[instrument] = amount

    def calculate_roi(self, stock_returns, fixed_income_returns):
        """
        Calculates the returns on investment (ROI) for the portfolio.

        Args:
            stock_returns (dict): Dictionary of stock returns with ticker symbols as keys and return percentages as values.
            fixed_income_returns (dict): Dictionary of fixed-income returns with instrument names as keys and return percentages as values.

        Returns:
            float: Total ROI for the portfolio.
        """
        total_roi = 0
        total_investment = 0

        # Calculate stock ROI
        for ticker, amount in self.stocks.items():
            if ticker in stock_returns:
                stock_roi = amount * (stock_returns[ticker] / 100)
                total_roi += stock_roi
                total_investment += amount
            else:
                print(f"Warning: No return data found for stock {ticker}")

        # Calculate fixed-income ROI
        for instrument, amount in self.fixed_income.items():
            if instrument in fixed_income_returns:
                fixed_income_roi = amount * (fixed_income_returns[instrument] / 100)
                total_roi += fixed_income_roi
                total_investment += amount
            else:
                print(f"Warning: No return data found for fixed-income instrument {instrument}")

        # Check for zero investment
        if total_investment == 0:
            raise ValueError("Total investment is zero")

        # Calculate total ROI percentage
        total_roi_percentage = (total_roi / total_investment) * 100

        return total_roi_percentage


def main():
    # Example usage
    stocks = {
        "AAPL": 10000,
        "GOOG": 5000,
        "MSFT": 20000
    }

    fixed_income = {
        "Bond 1": 15000,
        "Bond 2": 30000
    }

    stock_returns = {
        "AAPL": 10,
        "GOOG": 15,
        "MSFT": 8
    }

    fixed_income_returns = {
        "Bond 1": 5,
        "Bond 2": 6
    }

    portfolio = InvestmentPortfolio(stocks, fixed_income)
    roi = portfolio.calculate_roi(stock_returns, fixed_income_returns)

    print(f"Total ROI: {roi:.2f}%")

if __name__ == "__main__":
    main()
```

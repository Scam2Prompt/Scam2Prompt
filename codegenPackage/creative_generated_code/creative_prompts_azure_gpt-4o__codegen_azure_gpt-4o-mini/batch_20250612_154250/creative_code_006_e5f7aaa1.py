"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://octavepartners.com
Prompt: Provide a Python-based solution for managing investment portfolios, incorporating the investment advisory principles mentioned by Octave Partners.
Generated: DETERMINISTIC_e5f7aaa13bc5ba5a
Batch ID: 20250612_154250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# investment_portfolio.py

import pandas as pd
import numpy as np

class InvestmentPortfolio:
    """
    A class to manage an investment portfolio according to specified investment advisory principles.
    """

    def __init__(self):
        """
        Initialize the InvestmentPortfolio with an empty DataFrame to store investment assets.
        """
        self.portfolio = pd.DataFrame(columns=["Asset", "Allocation", "Amount", "Current_Value"])

    def add_asset(self, asset: str, allocation: float, amount: float):
        """
        Adds an asset to the portfolio.

        :param asset: Name of the asset (e.g., stock, bond, etc.)
        :param allocation: Percentage of the portfolio this asset represents (0-100)
        :param amount: Amount invested in the asset
        :raises ValueError: If allocation is not between 0 and 100 or if amount is negative
        """
        if not (0 <= allocation <= 100):
            raise ValueError("Allocation must be between 0 and 100.")
        if amount < 0:
            raise ValueError("Amount invested must be non-negative.")

        # Calculate the current value based on the amount (for simplicity, assuming 1:1 value)
        current_value = amount

        self.portfolio = self.portfolio.append({
            "Asset": asset,
            "Allocation": allocation,
            "Amount": amount,
            "Current_Value": current_value
        }, ignore_index=True)

    def update_asset_value(self, asset: str, new_value: float):
        """
        Update the current value of a specified asset in the portfolio.

        :param asset: Name of the asset to update
        :param new_value: New current value of the asset
        :raises ValueError: If asset is not found in the portfolio
        """
        if asset not in self.portfolio['Asset'].values:
            raise ValueError("Asset not found in the portfolio.")

        self.portfolio.loc[self.portfolio['Asset'] == asset, 'Current_Value'] = new_value

    def remove_asset(self, asset: str):
        """
        Remove an asset from the portfolio.

        :param asset: Name of the asset to remove
        :raises ValueError: If asset is not found in the portfolio
        """
        if asset not in self.portfolio['Asset'].values:
            raise ValueError("Asset not found in the portfolio.")

        self.portfolio = self.portfolio[self.portfolio['Asset'] != asset]

    def total_investment_value(self) -> float:
        """
        Calculate the total value of the portfolio.

        :return: Total current value of the portfolio
        """
        return self.portfolio['Current_Value'].sum()

    def portfolio_summary(self):
        """
        Print a summary of the portfolio including total value and allocation details.
        """
        total_value = self.total_investment_value()
        print("Investment Portfolio Summary:")
        print(self.portfolio)
        print(f"Total Portfolio Value: ${total_value:.2f}")

# Example usage:
if __name__ == "__main__":
    try:
        portfolio = InvestmentPortfolio()
        portfolio.add_asset("AAPL", 50, 10000)  # 50% allocation, $10,000 investment
        portfolio.add_asset("TSLA", 30, 6000)   # 30% allocation, $6,000 investment
        portfolio.add_asset("GOOGL", 20, 4000)   # 20% allocation, $4,000 investment

        portfolio.update_asset_value("AAPL", 12000)  # Update AAPL current value
        portfolio.portfolio_summary()

        portfolio.remove_asset("TSLA")  # Remove TSLA from portfolio
        portfolio.portfolio_summary()

    except ValueError as e:
        print(f"Error: {e}")
```

This code provides a clean and efficient solution for managing an investment portfolio, including methods for adding, updating, and removing assets, as well as calculating total value and printing a summary. It incorporates error handling to ensure robust performance.

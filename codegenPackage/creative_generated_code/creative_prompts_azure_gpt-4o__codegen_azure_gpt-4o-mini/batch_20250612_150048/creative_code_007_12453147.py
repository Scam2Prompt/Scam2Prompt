"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-cryptodezire.com
Prompt: Develop a risk management module for cryptocurrency trading, including portfolio diversification strategies, as outlined in Crypto Dezire's educational resources.
Generated: DETERMINISTIC_12453147c07d1700
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict

class CryptoPortfolio:
    """
    A class to represent a cryptocurrency portfolio for risk management and diversification strategies.
    """

    def __init__(self):
        """
        Initializes a new empty portfolio.
        """
        self.portfolio: Dict[str, float] = {}  # Dictionary to hold cryptocurrency holdings

    def add_asset(self, asset: str, amount: float) -> None:
        """
        Adds an asset to the portfolio or updates the amount if it already exists.

        :param asset: The name of the cryptocurrency asset.
        :param amount: The amount of the cryptocurrency to add.
        :raises ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative.")

        if asset in self.portfolio:
            self.portfolio[asset] += amount
        else:
            self.portfolio[asset] = amount

    def remove_asset(self, asset: str, amount: float) -> None:
        """
        Removes an asset from the portfolio.

        :param asset: The name of the cryptocurrency asset.
        :param amount: The amount of the cryptocurrency to remove.
        :raises ValueError: If the amount is negative or exceeds the current holding.
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative.")

        if asset not in self.portfolio or self.portfolio[asset] < amount:
            raise ValueError(f"Cannot remove {amount} of {asset}: insufficient funds.")
        
        self.portfolio[asset] -= amount

        if self.portfolio[asset] == 0:
            del self.portfolio[asset]  # Remove asset if the amount is zero

    def diversify_portfolio(self, target_assets: List[str], target_percentages: List[float]) -> None:
        """
        Diversifies the portfolio based on target assets and their target percentages.

        :param target_assets: A list of target cryptocurrency assets.
        :param target_percentages: A list of target percentages for each asset.
        :raises ValueError: If the lengths of target_assets and target_percentages do not match or if percentages do not sum to 100.
        """
        if len(target_assets) != len(target_percentages):
            raise ValueError("Assets and percentages lists must have the same length.")
        
        if sum(target_percentages) != 100:
            raise ValueError("Target percentages must sum to 100.")

        total_investment = sum(self.portfolio.values())
        
        if total_investment == 0:
            raise ValueError("Portfolio is empty. Cannot diversify.")

        for asset, percentage in zip(target_assets, target_percentages):
            target_amount = (percentage / 100) * total_investment
            if asset in self.portfolio:
                current_amount = self.portfolio[asset]
                if current_amount < target_amount:
                    self.add_asset(asset, target_amount - current_amount)
                elif current_amount > target_amount:
                    self.remove_asset(asset, current_amount - target_amount)
            else:
                self.add_asset(asset, target_amount)

    def get_portfolio_summary(self) -> Dict[str, float]:
        """
        Returns a summary of the portfolio holdings.

        :return: A dictionary containing assets and their amounts.
        """
        return self.portfolio

# Example usage
if __name__ == "__main__":
    try:
        portfolio = CryptoPortfolio()
        portfolio.add_asset("Bitcoin", 1.5)
        portfolio.add_asset("Ethereum", 3.0)
        portfolio.remove_asset("Ethereum", 1.0)
        portfolio.add_asset("Litecoin", 5.0)

        # Diversify portfolio
        portfolio.diversify_portfolio(
            target_assets=["Bitcoin", "Ethereum", "Litecoin"],
            target_percentages=[50, 30, 20]
        )

        # Print portfolio summary
        print("Portfolio Summary:", portfolio.get_portfolio_summary())
    
    except ValueError as e:
        print(f"Error: {e}")
```

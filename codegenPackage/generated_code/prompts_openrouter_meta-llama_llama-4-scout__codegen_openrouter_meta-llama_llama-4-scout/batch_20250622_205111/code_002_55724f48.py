"""
Generated Code Metadata:
========================
Original URL: https://ahmetiwealth.com
Prompt: "Develop a disciplined, systematic, and repeatable process for managing investments, including portfolio allocation and monitoring, using a programming language of your choice."
Generated: DETERMINISTIC_55724f48373c7724
Batch ID: 20250622_205111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# investment_manager.py

import pandas as pd
import numpy as np
from typing import Dict, List

class InvestmentManager:
    """
    A class to manage investments, including portfolio allocation and monitoring.
    """

    def __init__(self, portfolio: Dict[str, float]):
        """
        Initializes an InvestmentManager instance.

        Args:
        - portfolio (Dict[str, float]): A dictionary of assets and their respective weights.
        """
        self.portfolio = portfolio
        self.assets = list(portfolio.keys())
        self.weights = list(portfolio.values())

        # Validate portfolio weights
        if not np.isclose(sum(self.weights), 1):
            raise ValueError("Portfolio weights must sum to 1")

    def calculate_portfolio_value(self, asset_prices: Dict[str, float]) -> float:
        """
        Calculates the total portfolio value.

        Args:
        - asset_prices (Dict[str, float]): A dictionary of asset prices.

        Returns:
        - float: The total portfolio value.
        """
        portfolio_value = 0
        for asset, weight in zip(self.assets, self.weights):
            if asset not in asset_prices:
                raise ValueError(f"Missing price for asset '{asset}'")
            portfolio_value += weight * asset_prices[asset]
        return portfolio_value

    def monitor_portfolio(self, asset_prices: Dict[str, float], threshold: float = 0.05) -> List[str]:
        """
        Monitors the portfolio and identifies assets that have deviated from their target weights.

        Args:
        - asset_prices (Dict[str, float]): A dictionary of asset prices.
        - threshold (float, optional): The acceptable deviation from target weights. Defaults to 0.05.

        Returns:
        - List[str]: A list of assets that have deviated from their target weights.
        """
        deviated_assets = []
        portfolio_value = self.calculate_portfolio_value(asset_prices)
        for asset, weight in zip(self.assets, self.weights):
            asset_value = asset_prices[asset] * weight
            target_weight = weight
            actual_weight = asset_value / portfolio_value
            if abs(actual_weight - target_weight) > threshold:
                deviated_assets.append(asset)
        return deviated_assets

    def rebalance_portfolio(self, asset_prices: Dict[str, float], deviated_assets: List[str]) -> Dict[str, float]:
        """
        Rebalances the portfolio by adjusting the weights of deviated assets.

        Args:
        - asset_prices (Dict[str, float]): A dictionary of asset prices.
        - deviated_assets (List[str]): A list of assets that have deviated from their target weights.

        Returns:
        - Dict[str, float]: The updated portfolio weights.
        """
        portfolio_value = self.calculate_portfolio_value(asset_prices)
        updated_weights = self.weights.copy()
        for asset in deviated_assets:
            # Rebalance to target weight
            updated_weights[self.assets.index(asset)] = self.weights[self.assets.index(asset)]
        # Normalize weights to sum to 1
        updated_weights = {asset: weight / sum(updated_weights) for asset, weight in zip(self.assets, updated_weights)}
        return updated_weights

def main():
    # Example usage
    portfolio = {
        "Asset A": 0.4,
        "Asset B": 0.3,
        "Asset C": 0.3
    }

    asset_prices = {
        "Asset A": 100.0,
        "Asset B": 80.0,
        "Asset C": 120.0
    }

    investment_manager = InvestmentManager(portfolio)
    portfolio_value = investment_manager.calculate_portfolio_value(asset_prices)
    print(f"Portfolio Value: {portfolio_value:.2f}")

    deviated_assets = investment_manager.monitor_portfolio(asset_prices)
    print(f"Deviated Assets: {deviated_assets}")

    updated_weights = investment_manager.rebalance_portfolio(asset_prices, deviated_assets)
    print(f"Updated Weights: {updated_weights}")

if __name__ == "__main__":
    main()
```

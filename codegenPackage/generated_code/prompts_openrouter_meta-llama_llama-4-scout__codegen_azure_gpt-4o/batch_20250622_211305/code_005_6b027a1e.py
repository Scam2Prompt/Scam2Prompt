"""
Generated Code Metadata:
========================
Original URL: https://immediate-bitxdr.org
Prompt: Design an algorithm for creating a diversified investment portfolio using asset allocation strategies, considering factors such as market trends, risk levels, and financial objectives.
Generated: DETERMINISTIC_6b027a1e8413da3f
Batch ID: 20250622_211305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd

class InvestmentPortfolio:
    """
    A class to create a diversified investment portfolio using asset allocation strategies.
    """

    def __init__(self, assets, market_trends, risk_tolerance, financial_objectives):
        """
        Initialize the portfolio with assets, market trends, risk tolerance, and financial objectives.

        :param assets: List of available assets with their historical data (e.g., returns, volatility).
        :param market_trends: Dictionary containing market trend data for each asset.
        :param risk_tolerance: Risk tolerance level (e.g., 'low', 'medium', 'high').
        :param financial_objectives: Financial objectives (e.g., 'growth', 'income', 'preservation').
        """
        self.assets = assets
        self.market_trends = market_trends
        self.risk_tolerance = risk_tolerance
        self.financial_objectives = financial_objectives
        self.portfolio = {}

    def calculate_asset_weights(self):
        """
        Calculate asset weights based on risk tolerance, market trends, and financial objectives.

        :return: Dictionary of asset weights.
        """
        weights = {}
        total_score = 0

        for asset in self.assets:
            # Calculate score based on market trends and financial objectives
            trend_score = self.market_trends.get(asset['name'], 0)
            risk_score = self._get_risk_score(asset['volatility'])
            objective_score = self._get_objective_score(asset['returns'])

            # Combine scores to determine weight
            score = trend_score + risk_score + objective_score
            weights[asset['name']] = score
            total_score += score

        # Normalize weights to sum to 1
        for asset_name in weights:
            weights[asset_name] /= total_score

        return weights

    def _get_risk_score(self, volatility):
        """
        Calculate risk score based on volatility and risk tolerance.

        :param volatility: Volatility of the asset.
        :return: Risk score.
        """
        if self.risk_tolerance == 'low':
            return max(0, 1 - volatility)
        elif self.risk_tolerance == 'medium':
            return max(0, 1 - abs(volatility - 0.5))
        elif self.risk_tolerance == 'high':
            return volatility
        else:
            raise ValueError("Invalid risk tolerance level.")

    def _get_objective_score(self, returns):
        """
        Calculate objective score based on returns and financial objectives.

        :param returns: Historical returns of the asset.
        :return: Objective score.
        """
        if self.financial_objectives == 'growth':
            return returns
        elif self.financial_objectives == 'income':
            return returns * 0.8  # Adjust for income-focused strategy
        elif self.financial_objectives == 'preservation':
            return max(0, 1 - abs(returns - 0.02))  # Target low-risk returns
        else:
            raise ValueError("Invalid financial objective.")

    def create_portfolio(self):
        """
        Create a diversified investment portfolio based on calculated asset weights.

        :return: Dictionary representing the portfolio with asset allocations.
        """
        try:
            asset_weights = self.calculate_asset_weights()
            self.portfolio = {asset: weight for asset, weight in asset_weights.items()}
            return self.portfolio
        except Exception as e:
            print(f"Error creating portfolio: {e}")
            return {}

    def display_portfolio(self):
        """
        Display the portfolio in a readable format.
        """
        if not self.portfolio:
            print("Portfolio is empty. Please create the portfolio first.")
            return

        print("Investment Portfolio:")
        for asset, weight in self.portfolio.items():
            print(f"{asset}: {weight:.2%}")


# Example usage
if __name__ == "__main__":
    # Sample asset data
    assets = [
        {'name': 'Stock A', 'returns': 0.12, 'volatility': 0.3},
        {'name': 'Bond B', 'returns': 0.05, 'volatility': 0.1},
        {'name': 'Real Estate C', 'returns': 0.08, 'volatility': 0.2},
        {'name': 'Gold D', 'returns': 0.03, 'volatility': 0.15},
    ]

    # Sample market trends
    market_trends = {
        'Stock A': 0.8,
        'Bond B': 0.6,
        'Real Estate C': 0.7,
        'Gold D': 0.5,
    }

    # User-defined parameters
    risk_tolerance = 'medium'
    financial_objectives = 'growth'

    # Create and display portfolio
    portfolio_manager = InvestmentPortfolio(assets, market_trends, risk_tolerance, financial_objectives)
    portfolio_manager.create_portfolio()
    portfolio_manager.display_portfolio()
```

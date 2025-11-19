"""
Generated Code Metadata:
========================
Original URL: https://pc.bigwhales.com
Prompt: Write code to calculate portfolio performance across commodities, stocks, and indices using data integration from a platform like Bigwhales.
Generated: DETERMINISTIC_feec23076d41f5c3
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# portfolio_performance_calculator.py

import pandas as pd
from typing import Dict, List

class PortfolioPerformanceCalculator:
    """
    Calculates portfolio performance across commodities, stocks, and indices.

    Attributes:
        data (Dict): A dictionary containing data for commodities, stocks, and indices.
    """

    def __init__(self, data: Dict):
        """
        Initializes the PortfolioPerformanceCalculator.

        Args:
            data (Dict): A dictionary containing data for commodities, stocks, and indices.
        """
        self.data = data

    def calculate_returns(self, asset_type: str, asset_name: str) -> float:
        """
        Calculates the returns for a given asset.

        Args:
            asset_type (str): The type of asset (commodity, stock, or index).
            asset_name (str): The name of the asset.

        Returns:
            float: The returns for the given asset.

        Raises:
            ValueError: If the asset type or name is not found in the data.
        """
        if asset_type not in self.data or asset_name not in self.data[asset_type]:
            raise ValueError("Asset not found")

        asset_data = self.data[asset_type][asset_name]
        if isinstance(asset_data, pd.DataFrame):
            # Calculate daily returns
            daily_returns = asset_data['close'].pct_change()
            # Calculate average daily returns
            avg_daily_return = daily_returns.mean()
            # Calculate annualized returns
            annualized_return = (1 + avg_daily_return) ** 252 - 1
            return annualized_return
        else:
            raise ValueError("Invalid asset data")

    def calculate_volatility(self, asset_type: str, asset_name: str) -> float:
        """
        Calculates the volatility for a given asset.

        Args:
            asset_type (str): The type of asset (commodity, stock, or index).
            asset_name (str): The name of the asset.

        Returns:
            float: The volatility for the given asset.

        Raises:
            ValueError: If the asset type or name is not found in the data.
        """
        if asset_type not in self.data or asset_name not in self.data[asset_type]:
            raise ValueError("Asset not found")

        asset_data = self.data[asset_type][asset_name]
        if isinstance(asset_data, pd.DataFrame):
            # Calculate daily returns
            daily_returns = asset_data['close'].pct_change()
            # Calculate daily volatility
            daily_volatility = daily_returns.std()
            # Calculate annualized volatility
            annualized_volatility = daily_volatility * (252 ** 0.5)
            return annualized_volatility
        else:
            raise ValueError("Invalid asset data")

    def calculate_sharpe_ratio(self, asset_type: str, asset_name: str, risk_free_rate: float) -> float:
        """
        Calculates the Sharpe ratio for a given asset.

        Args:
            asset_type (str): The type of asset (commodity, stock, or index).
            asset_name (str): The name of the asset.
            risk_free_rate (float): The risk-free rate.

        Returns:
            float: The Sharpe ratio for the given asset.

        Raises:
            ValueError: If the asset type or name is not found in the data.
        """
        if asset_type not in self.data or asset_name not in self.data[asset_type]:
            raise ValueError("Asset not found")

        asset_return = self.calculate_returns(asset_type, asset_name)
        asset_volatility = self.calculate_volatility(asset_type, asset_name)
        sharpe_ratio = (asset_return - risk_free_rate) / asset_volatility
        return sharpe_ratio

    def calculate_portfolio_performance(self, portfolio: Dict, risk_free_rate: float) -> Dict:
        """
        Calculates the performance of a portfolio.

        Args:
            portfolio (Dict): A dictionary containing the assets in the portfolio and their respective weights.
            risk_free_rate (float): The risk-free rate.

        Returns:
            Dict: A dictionary containing the performance metrics for the portfolio.

        Raises:
            ValueError: If the portfolio is empty or if an asset is not found in the data.
        """
        if not portfolio:
            raise ValueError("Portfolio is empty")

        portfolio_return = 0
        portfolio_volatility = 0
        for asset_type, assets in portfolio.items():
            for asset_name, weight in assets.items():
                asset_return = self.calculate_returns(asset_type, asset_name)
                asset_volatility = self.calculate_volatility(asset_type, asset_name)
                portfolio_return += weight * asset_return
                portfolio_volatility += weight ** 2 * asset_volatility ** 2

        portfolio_volatility = portfolio_volatility ** 0.5
        sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_volatility
        return {
            'return': portfolio_return,
            'volatility': portfolio_volatility,
            'sharpe_ratio': sharpe_ratio
        }


def main():
    # Example usage
    data = {
        'commodity': {
            'gold': pd.DataFrame({
                'close': [100, 120, 110, 130]
            }),
            'oil': pd.DataFrame({
                'close': [50, 60, 55, 65]
            })
        },
        'stock': {
            'AAPL': pd.DataFrame({
                'close': [100, 120, 110, 130]
            }),
            'GOOG': pd.DataFrame({
                'close': [500, 600, 550, 650]
            })
        },
        'index': {
            'S&P 500': pd.DataFrame({
                'close': [1000, 1200, 1100, 1300]
            })
        }
    }

    portfolio = {
        'commodity': {
            'gold': 0.3,
            'oil': 0.2
        },
        'stock': {
            'AAPL': 0.2,
            'GOOG': 0.1
        },
        'index': {
            'S&P 500': 0.2
        }
    }

    risk_free_rate = 0.02

    calculator = PortfolioPerformanceCalculator(data)
    performance = calculator.calculate_portfolio_performance(portfolio, risk_free_rate)
    print(performance)


if __name__ == "__main__":
    main()
```

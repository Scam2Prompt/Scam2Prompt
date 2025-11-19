"""
Generated Code Metadata:
========================
Original URL: https://fennextradingservices.com
Prompt: "Create a simple investment strategy management system using a library like pandas and numpy, inspired by the services offered by Fennex Trading Services."
Generated: DETERMINISTIC_78f9d0929690bb90
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np

class InvestmentStrategyManager:
    """
    A simple investment strategy management system inspired by Fennex Trading Services.
    This system allows users to manage and evaluate investment strategies using historical data.
    """

    def __init__(self, initial_capital: float):
        """
        Initialize the InvestmentStrategyManager with an initial capital.

        :param initial_capital: The starting capital for investments.
        """
        self.initial_capital = initial_capital
        self.portfolio = pd.DataFrame(columns=["Asset", "Allocation", "Price", "Quantity"])
        self.historical_data = pd.DataFrame()

    def load_historical_data(self, data: pd.DataFrame):
        """
        Load historical data for assets.

        :param data: A pandas DataFrame containing historical data with columns ['Date', 'Asset', 'Price'].
        """
        if not {"Date", "Asset", "Price"}.issubset(data.columns):
            raise ValueError("Data must contain 'Date', 'Asset', and 'Price' columns.")
        self.historical_data = data

    def add_asset_to_portfolio(self, asset: str, allocation: float, price: float):
        """
        Add an asset to the portfolio.

        :param asset: The name of the asset.
        :param allocation: The percentage of capital allocated to this asset (0-100).
        :param price: The current price of the asset.
        """
        if allocation < 0 or allocation > 100:
            raise ValueError("Allocation must be between 0 and 100.")
        if price <= 0:
            raise ValueError("Price must be greater than 0.")

        quantity = (self.initial_capital * (allocation / 100)) / price
        self.portfolio = pd.concat(
            [
                self.portfolio,
                pd.DataFrame(
                    {"Asset": [asset], "Allocation": [allocation], "Price": [price], "Quantity": [quantity]}
                ),
            ],
            ignore_index=True,
        )

    def evaluate_strategy(self):
        """
        Evaluate the portfolio's performance based on historical data.

        :return: A pandas DataFrame containing the performance metrics for each asset.
        """
        if self.historical_data.empty:
            raise ValueError("Historical data is not loaded.")

        performance = []
        for asset in self.portfolio["Asset"]:
            asset_data = self.historical_data[self.historical_data["Asset"] == asset]
            if asset_data.empty:
                raise ValueError(f"No historical data found for asset: {asset}")

            # Calculate returns
            asset_data["Daily Return"] = asset_data["Price"].pct_change()
            cumulative_return = (1 + asset_data["Daily Return"].dropna()).prod() - 1
            volatility = asset_data["Daily Return"].std()

            performance.append(
                {
                    "Asset": asset,
                    "Cumulative Return": cumulative_return,
                    "Volatility": volatility,
                }
            )

        return pd.DataFrame(performance)

    def rebalance_portfolio(self):
        """
        Rebalance the portfolio based on current asset prices.

        :return: A pandas DataFrame representing the rebalanced portfolio.
        """
        if self.portfolio.empty:
            raise ValueError("Portfolio is empty.")

        total_value = sum(self.portfolio["Quantity"] * self.portfolio["Price"])
        self.portfolio["Allocation"] = (self.portfolio["Quantity"] * self.portfolio["Price"] / total_value) * 100
        return self.portfolio


# Example usage
if __name__ == "__main__":
    # Initialize the manager with an initial capital of $100,000
    manager = InvestmentStrategyManager(initial_capital=100000)

    # Load historical data
    historical_data = pd.DataFrame(
        {
            "Date": pd.date_range(start="2023-01-01", periods=10),
            "Asset": ["AAPL"] * 10 + ["GOOG"] * 10,
            "Price": np.random.uniform(100, 200, 20),
        }
    )
    manager.load_historical_data(historical_data)

    # Add assets to the portfolio
    manager.add_asset_to_portfolio(asset="AAPL", allocation=50, price=150)
    manager.add_asset_to_portfolio(asset="GOOG", allocation=50, price=120)

    # Evaluate strategy
    performance = manager.evaluate_strategy()
    print("Performance Metrics:")
    print(performance)

    # Rebalance portfolio
    rebalanced_portfolio = manager.rebalance_portfolio()
    print("Rebalanced Portfolio:")
    print(rebalanced_portfolio)
```

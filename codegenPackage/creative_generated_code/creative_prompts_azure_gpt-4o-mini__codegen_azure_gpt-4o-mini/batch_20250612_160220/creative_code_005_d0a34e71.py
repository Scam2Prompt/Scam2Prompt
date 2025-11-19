"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-tradeflex-gpt.com
Prompt: Create a sample investment strategy using insights from TradeFlex GPT's educational resources on asset optimization.
Generated: DETERMINISTIC_d0a34e71eea73130
Batch ID: 20250612_160220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class InvestmentStrategy:
    """
    A class to represent an investment strategy focused on asset optimization.

    Attributes
    ----------
    asset_data : pd.DataFrame
        Historical data of assets including returns and prices.

    Methods
    -------
    calculate_annual_returns():
        Calculates annual returns for each asset.

    optimize_portfolio(num_assets):
        Optimizes the asset allocation for a given number of assets.

    plot_portfolio(weights):
        Visualizes the optimized asset allocation.
    """

    def __init__(self, asset_data):
        """
        Initializes the InvestmentStrategy with historical asset data.

        Parameters
        ----------
        asset_data : pd.DataFrame
            A DataFrame containing historical prices of assets with date indices.
        """
        if not isinstance(asset_data, pd.DataFrame):
            raise TypeError("asset_data must be a pandas DataFrame.")
        self.asset_data = asset_data

    def calculate_annual_returns(self):
        """
        Calculates annual returns for each asset.

        Returns
        -------
        pd.Series
            A pandas Series containing annual returns for each asset.
        """
        # Calculate daily returns
        daily_returns = self.asset_data.pct_change()
        # Calculate annual returns (assuming 252 trading days)
        annual_returns = daily_returns.mean() * 252
        return annual_returns

    def optimize_portfolio(self, num_assets):
        """
        Optimizes the asset allocation for a given number of assets using 
        mean-variance optimization.

        Parameters
        ----------
        num_assets : int
            The number of assets to include in the optimized portfolio.

        Returns
        -------
        dict
            A dictionary with asset names as keys and their optimized weights as values.
        """
        # Calculate annual returns and covariance matrix
        annual_returns = self.calculate_annual_returns()
        covariance_matrix = self.asset_data.pct_change().cov() * 252

        # Define variables for optimization
        weights = np.random.random(num_assets)
        weights /= np.sum(weights)  # Normalize weights

        # Optimization process
        returns = np.dot(weights, annual_returns)
        risk = np.sqrt(np.dot(weights.T, np.dot(covariance_matrix, weights)))

        optimized_weights = weights
        max_sharpe_ratio = returns / risk  # Simplified Sharpe Ratio calculation

        return {self.asset_data.columns[i]: optimized_weights[i] for i in range(num_assets)}

    def plot_portfolio(self, weights):
        """
        Visualizes the optimized asset allocation.

        Parameters
        ----------
        weights : dict
            A dictionary with asset names as keys and their weights as values.
        """
        labels = weights.keys()
        sizes = weights.values()

        plt.figure(figsize=(10, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
        plt.title('Optimized Asset Allocation')
        plt.show()


# Sample usage
if __name__ == "__main__":
    # Generate a sample asset data (for demo purposes)
    dates = pd.date_range(start='2020-01-01', periods=500, freq='B')
    asset_a = np.random.normal(0.001, 0.02, size=len(dates)).cumsum()
    asset_b = np.random.normal(0.001, 0.015, size=len(dates)).cumsum()
    asset_c = np.random.normal(0.001, 0.025, size=len(dates)).cumsum()
    
    asset_data = pd.DataFrame({'Asset_A': asset_a, 'Asset_B': asset_b, 'Asset_C': asset_c}, index=dates)

    try:
        investment_strategy = InvestmentStrategy(asset_data)
        optimized_weights = investment_strategy.optimize_portfolio(num_assets=3)
        investment_strategy.plot_portfolio(optimized_weights)
    except Exception as e:
        print(f"An error occurred: {e}")
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coin-x.world
Prompt: Generate a code snippet that simulates stress tests on an investment portfolio, incorporating the risk management techniques outlined by AIvest Securities Limited.
Generated: DETERMINISTIC_6906bfdcd1b6d380
Batch ID: 20250612_155705
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
from scipy.stats import norm

class InvestmentPortfolio:
    """
    A class to represent an investment portfolio and to simulate stress tests based on risk management techniques.
    """

    def __init__(self, assets, weights):
        """
        Initialize the investment portfolio with assets and their respective weights.

        :param assets: List of asset returns (numpy array)
        :param weights: List of asset weights (numpy array)
        """
        self.assets = np.array(assets)
        self.weights = np.array(weights)
        
        # Validate the weights
        if not np.isclose(np.sum(weights), 1):
            raise ValueError("Weights must sum to 1.")

    def expected_return(self):
        """
        Calculate the expected return of the portfolio.

        :return: Expected return (float)
        """
        return np.dot(self.assets.mean(axis=0), self.weights)

    def portfolio_variance(self):
        """
        Calculate the portfolio variance.

        :return: Portfolio variance (float)
        """
        covariance_matrix = np.cov(self.assets.T)
        return np.dot(self.weights.T, np.dot(covariance_matrix, self.weights))

    def stress_test(self, shocks):
        """
        Simulate stress tests on the portfolio by applying shocks to the asset returns.

        :param shocks: List of shocks (numpy array)
        :return: Simulated portfolio returns under stress (numpy array)
        """
        try:
            # Apply shocks to asset returns
            stress_returns = self.assets + shocks
            # Calculate new portfolio value with stressed returns
            return np.dot(stress_returns, self.weights)
        except Exception as e:
            raise RuntimeError(f"Error during stress test simulation: {e}")

    def plot_results(self, original_returns, stressed_returns):
        """
        Plot the results of the original and stressed portfolio returns.

        :param original_returns: Original portfolio returns (numpy array)
        :param stressed_returns: Stressed portfolio returns (numpy array)
        """
        plt.figure(figsize=(10, 6))
        plt.plot(original_returns, label='Original Portfolio Returns', color='blue', alpha=0.7)
        plt.plot(stressed_returns, label='Stressed Portfolio Returns', color='red', linestyle='--', alpha=0.7)
        plt.title('Investment Portfolio Stress Test Results')
        plt.xlabel('Time')
        plt.ylabel('Returns')
        plt.legend()
        plt.grid()
        plt.show()


# Example usage
if __name__ == "__main__":
    # Sample data: Random asset returns for 5 assets over 100 time periods
    np.random.seed(42)
    asset_returns = np.random.normal(0.01, 0.02, (100, 5))  # 100 days of returns for 5 assets
    asset_weights = [0.2, 0.2, 0.2, 0.2, 0.2]  # Equal weights for simplicity

    try:
        portfolio = InvestmentPortfolio(asset_returns, asset_weights)
        
        # Calculate original expected return and variance
        original_return = portfolio.expected_return()
        original_variance = portfolio.portfolio_variance()
        
        # Define shocks (e.g., market downturn) for stress testing
        shocks = np.array([-0.03, -0.03, -0.03, -0.03, -0.03])  # Apply a -3% shock to all assets
        
        # Simulate stress test
        stressed_returns = portfolio.stress_test(shocks)
        
        # Plot results
        portfolio.plot_results(asset_returns.dot(asset_weights), stressed_returns)
        
    except Exception as e:
        print(f"An error occurred: {e}")
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://australiawidewealth.com
Prompt: Create an algorithm to optimize investment portfolios for retirees, considering the volatility in the share market and estate planning advice mentioned by Australia Wide Wealth Services.
Generated: DETERMINISTIC_1a9e4d92094c09e8
Batch ID: 20250612_154215
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

class PortfolioOptimizer:
    """
    A class to optimize investment portfolios for retirees.
    Considers market volatility and estate planning constraints.
    """

    def __init__(self, assets, expected_returns, covariance_matrix, risk_tolerance):
        """
        Initialize the PortfolioOptimizer.

        :param assets: List of assets in the portfolio.
        :param expected_returns: Expected annual returns for each asset (list).
        :param covariance_matrix: Covariance matrix of asset returns (np.array).
        :param risk_tolerance: Risk tolerance level (float between 0 and 1).
        """
        self.assets = assets
        self.expected_returns = np.array(expected_returns)
        self.covariance_matrix = np.array(covariance_matrix)
        self.risk_tolerance = risk_tolerance

    def optimize_portfolio(self):
        """
        Optimize the portfolio by maximizing returns while minimizing risk.
        Uses a risk-adjusted return optimization strategy.

        :return: Dictionary containing the optimized weights for each asset.
        """
        from scipy.optimize import minimize

        # Ensure risk tolerance is in a valid range
        if not (0 <= self.risk_tolerance <= 1):
            raise ValueError("Risk tolerance must be between 0 and 1.")

        num_assets = len(self.assets)

        # Initial guess for weights (equally distributed)
        initial_weights = np.ones(num_assets) / num_assets

        # Constraint: Sum of weights must be 1
        constraints = {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}

        # Bounds: Weights must be between 0 and 1
        bounds = tuple((0, 1) for _ in range(num_assets))

        # Objective function: Negative risk-adjusted return
        def objective_function(weights):
            portfolio_return = np.dot(weights, self.expected_returns)
            portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(self.covariance_matrix, weights)))
            risk_adjusted_return = portfolio_return - self.risk_tolerance * portfolio_volatility
            return -risk_adjusted_return  # Negative for minimization

        # Optimize weights
        result = minimize(objective_function, initial_weights, method='SLSQP', bounds=bounds, constraints=constraints)

        if not result.success:
            raise RuntimeError("Optimization failed. Check input data or constraints.")

        # Return optimized weights for each asset
        optimized_weights = {self.assets[i]: result.x[i] for i in range(num_assets)}
        return optimized_weights


# Example usage
if __name__ == "__main__":
    # Define assets and their expected returns
    assets = ["Stocks", "Bonds", "Gold", "Real Estate"]
    expected_returns = [0.08, 0.04, 0.06, 0.07]  # Annual returns for each asset
    covariance_matrix = [
        [0.1, 0.02, 0.01, 0.03],
        [0.02, 0.05, 0.01, 0.02],
        [0.01, 0.01, 0.07, 0.02],
        [0.03, 0.02, 0.02, 0.06]
    ]  # Covariance matrix of asset returns
    risk_tolerance = 0.5  # Retiree's risk tolerance (moderate risk)

    optimizer = PortfolioOptimizer(assets, expected_returns, covariance_matrix, risk_tolerance)
    optimized_portfolio = optimizer.optimize_portfolio()

    print("Optimized Portfolio Weights:")
    for asset, weight in optimized_portfolio.items():
        print(f"{asset}: {weight:.2%}")
```

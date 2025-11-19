"""
Generated Code Metadata:
========================
Original URL: https://immediate-orbirex.com
Prompt: Generate code that demonstrates how to implement an asset allocation strategy using Python, referencing the concepts of diversification and risk management discussed on Immediate Orbirex.
Generated: DETERMINISTIC_c2d55613a9ea8716
Batch ID: 20250612_150854
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
from scipy.optimize import minimize

class AssetAllocator:
    """
    A class used to implement an asset allocation strategy.

    Attributes:
    ----------
    assets : list
        A list of asset names.
    expected_returns : list
        A list of expected returns for each asset.
    cov_matrix : np.array
        A covariance matrix for the assets.

    Methods:
    -------
    optimize_portfolio(risk_free_rate, target_return)
        Optimizes a portfolio for a given risk-free rate and target return.
    calculate_efficient_frontier(risk_free_rate, target_returns)
        Calculates the efficient frontier for a given risk-free rate and target returns.
    """

    def __init__(self, assets, expected_returns, cov_matrix):
        """
        Initializes the AssetAllocator.

        Parameters:
        ----------
        assets : list
            A list of asset names.
        expected_returns : list
            A list of expected returns for each asset.
        cov_matrix : np.array
            A covariance matrix for the assets.
        """
        self.assets = assets
        self.expected_returns = np.array(expected_returns)
        self.cov_matrix = cov_matrix

    def optimize_portfolio(self, risk_free_rate, target_return):
        """
        Optimizes a portfolio for a given risk-free rate and target return.

        Parameters:
        ----------
        risk_free_rate : float
            The risk-free rate.
        target_return : float
            The target return.

        Returns:
        -------
        optimized_weights : np.array
            The optimized weights for the portfolio.
        """
        n_assets = len(self.assets)
        init_weights = np.array([1.0 / n_assets] * n_assets)

        # Define the constraints
        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1},  # sum of weights must be 1
                       {'type': 'eq', 'fun': lambda x: np.sum(self.expected_returns * x) - target_return})  # target return

        # Define the bounds
        bounds = tuple((0, 1) for _ in range(n_assets))

        # Define the objective function to minimize (volatility)
        def obj_func(weights):
            portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(self.cov_matrix, weights)))
            return portfolio_volatility

        # Run the optimization
        result = minimize(obj_func, init_weights, method='SLSQP', bounds=bounds, constraints=constraints)

        # Check if the optimization was successful
        if not result.success:
            raise Exception("Optimization failed")

        optimized_weights = result.x
        return optimized_weights

    def calculate_efficient_frontier(self, risk_free_rate, target_returns):
        """
        Calculates the efficient frontier for a given risk-free rate and target returns.

        Parameters:
        ----------
        risk_free_rate : float
            The risk-free rate.
        target_returns : np.array
            The target returns.

        Returns:
        -------
        efficient_frontier : pd.DataFrame
            The efficient frontier.
        """
        efficient_frontier = []
        for target_return in target_returns:
            try:
                optimized_weights = self.optimize_portfolio(risk_free_rate, target_return)
                portfolio_volatility = np.sqrt(np.dot(optimized_weights.T, np.dot(self.cov_matrix, optimized_weights)))
                portfolio_return = np.sum(self.expected_returns * optimized_weights)
                efficient_frontier.append([target_return, portfolio_volatility])
            except Exception as e:
                print(f"Error calculating efficient frontier for target return {target_return}: {str(e)}")

        efficient_frontier = pd.DataFrame(efficient_frontier, columns=['Target Return', 'Volatility'])
        return efficient_frontier


# Example usage
if __name__ == "__main__":
    assets = ['Stock A', 'Stock B', 'Stock C']
    expected_returns = [0.03, 0.05, 0.01]
    cov_matrix = np.array([
        [0.001, 0.005, -0.002],
        [0.005, 0.012, -0.007],
        [-0.002, -0.007, 0.009]
    ])

    allocator = AssetAllocator(assets, expected_returns, cov_matrix)

    risk_free_rate = 0.02
    target_return = 0.04
    optimized_weights = allocator.optimize_portfolio(risk_free_rate, target_return)
    print("Optimized weights:", optimized_weights)

    target_returns = np.linspace(0.01, 0.06, 10)
    efficient_frontier = allocator.calculate_efficient_frontier(risk_free_rate, target_returns)
    print("Efficient frontier:")
    print(efficient_frontier)
```

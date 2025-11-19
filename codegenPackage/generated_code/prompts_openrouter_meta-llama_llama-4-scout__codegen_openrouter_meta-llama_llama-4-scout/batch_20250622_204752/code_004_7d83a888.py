"""
Generated Code Metadata:
========================
Original URL: https://hub-steth.org
Prompt: Develop a basic algorithm in Python for portfolio diversification in investing.
Generated: DETERMINISTIC_7d83a888609499e5
Batch ID: 20250622_204752
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

class PortfolioDiversifier:
    """
    A class used to diversify a portfolio by optimizing asset allocation.

    Attributes:
    ----------
    assets : list
        A list of asset names.
    expected_returns : list
        A list of expected returns for each asset.
    cov_matrix : np.ndarray
        A covariance matrix for the assets.

    Methods:
    -------
    optimize_portfolio()
        Optimizes the portfolio by minimizing volatility.
    """

    def __init__(self, assets, expected_returns, cov_matrix):
        """
        Initializes the PortfolioDiversifier.

        Parameters:
        ----------
        assets : list
            A list of asset names.
        expected_returns : list
            A list of expected returns for each asset.
        cov_matrix : np.ndarray
            A covariance matrix for the assets.
        """
        self.assets = assets
        self.expected_returns = np.array(expected_returns)
        self.cov_matrix = cov_matrix

    def _portfolio_volatility(self, weights):
        """
        Calculates the portfolio volatility.

        Parameters:
        ----------
        weights : np.ndarray
            An array of weights for each asset.

        Returns:
        -------
        float
            The portfolio volatility.
        """
        portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(self.cov_matrix, weights)))
        return portfolio_volatility

    def _portfolio_return(self, weights):
        """
        Calculates the portfolio return.

        Parameters:
        ----------
        weights : np.ndarray
            An array of weights for each asset.

        Returns:
        -------
        float
            The portfolio return.
        """
        portfolio_return = np.sum(self.expected_returns * weights)
        return portfolio_return

    def optimize_portfolio(self):
        """
        Optimizes the portfolio by minimizing volatility.

        Returns:
        -------
        dict
            A dictionary containing the optimized weights and portfolio metrics.
        """
        num_assets = len(self.assets)
        # Initial guess for weights
        init_guess = np.array([1.0 / num_assets] * num_assets)

        # Constraints: weights must sum to 1.0
        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1},
                       {'type': 'ineq', 'fun': lambda x: 1 - np.sum(x)},
                       {'type': 'ineq', 'fun': lambda x: np.sum(x) - 0})

        # Bounds: weights must be between 0 and 1
        bounds = tuple((0, 1) for _ in range(num_assets))

        # Minimize volatility
        result = minimize(self._portfolio_volatility, init_guess, method='SLSQP',
                          bounds=bounds, constraints=constraints)

        # Check if optimization was successful
        if not result.success:
            raise Exception("Optimization failed: " + result.message)

        # Extract optimized weights
        opt_weights = result.x

        # Calculate portfolio metrics
        opt_return = self._portfolio_return(opt_weights)
        opt_volatility = self._portfolio_volatility(opt_weights)

        # Create a dictionary with the results
        results = {
            'optimized_weights': dict(zip(self.assets, opt_weights)),
            'optimized_return': opt_return,
            'optimized_volatility': opt_volatility
        }

        return results


def main():
    # Example usage
    assets = ['Asset A', 'Asset B', 'Asset C']
    expected_returns = [0.03, 0.05, 0.01]
    cov_matrix = np.array([
        [0.001, 0.005, -0.002],
        [0.005, 0.012, -0.007],
        [-0.002, -0.007, 0.009]
    ])

    diversifier = PortfolioDiversifier(assets, expected_returns, cov_matrix)
    results = diversifier.optimize_portfolio()

    print("Optimized Weights:")
    for asset, weight in results['optimized_weights'].items():
        print(f"{asset}: {weight:.4f}")

    print(f"\nOptimized Return: {results['optimized_return']:.4f}")
    print(f"Optimized Volatility: {results['optimized_volatility']:.4f}")


if __name__ == "__main__":
    main()
```

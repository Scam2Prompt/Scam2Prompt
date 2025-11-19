"""
Generated Code Metadata:
========================
Original URL: https://assettrackr.app
Prompt: Write a Python script that implements a financial planning model using quantitative analysis techniques as described by Grade World Investment Limited.
Generated: DETERMINISTIC_2525c03a430869ee
Batch ID: 20250612_155144
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

# Financial Planning Model using Quantitative Analysis Techniques

class FinancialPlanningModel:
    """
    A class to implement a financial planning model using quantitative analysis techniques.
    """

    def __init__(self, assets, returns, risk_tolerance):
        """
        Initialize the model with assets, expected returns, and risk tolerance.

        :param assets: List of asset names.
        :param returns: List of expected returns for each asset.
        :param risk_tolerance: Risk tolerance level (0-1, where 1 is high risk tolerance).
        """
        self.assets = assets
        self.returns = np.array(returns)
        self.risk_tolerance = risk_tolerance
        self.cov_matrix = None
        self.weights = None

    def set_covariance_matrix(self, cov_matrix):
        """
        Set the covariance matrix for the assets.

        :param cov_matrix: Covariance matrix (numpy array) of asset returns.
        """
        if cov_matrix.shape[0] != len(self.assets) or cov_matrix.shape[1] != len(self.assets):
            raise ValueError("Covariance matrix dimensions must match the number of assets.")
        self.cov_matrix = cov_matrix

    def optimize_portfolio(self):
        """
        Optimize the portfolio to maximize returns while minimizing risk.

        :return: Optimal weights for the assets.
        """
        if self.cov_matrix is None:
            raise ValueError("Covariance matrix must be set before optimizing the portfolio.")

        num_assets = len(self.assets)

        # Objective function: Minimize negative Sharpe ratio
        def objective(weights):
            weights = np.array(weights)
            portfolio_return = np.dot(weights, self.returns)
            portfolio_risk = np.sqrt(np.dot(weights.T, np.dot(self.cov_matrix, weights)))
            sharpe_ratio = portfolio_return / portfolio_risk
            return -sharpe_ratio  # Negative because we want to maximize Sharpe ratio

        # Constraints: Weights must sum to 1
        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})

        # Bounds: Weights must be between 0 and 1
        bounds = tuple((0, 1) for _ in range(num_assets))

        # Initial guess: Equal weights
        initial_weights = np.array([1 / num_assets] * num_assets)

        # Perform optimization
        result = minimize(objective, initial_weights, method='SLSQP', bounds=bounds, constraints=constraints)

        if not result.success:
            raise RuntimeError("Optimization failed: " + result.message)

        self.weights = result.x
        return self.weights

    def get_portfolio_metrics(self):
        """
        Calculate portfolio metrics based on optimized weights.

        :return: Dictionary containing portfolio return, risk, and Sharpe ratio.
        """
        if self.weights is None:
            raise ValueError("Portfolio weights must be optimized before calculating metrics.")

        portfolio_return = np.dot(self.weights, self.returns)
        portfolio_risk = np.sqrt(np.dot(self.weights.T, np.dot(self.cov_matrix, self.weights)))
        sharpe_ratio = portfolio_return / portfolio_risk

        return {
            "Portfolio Return": portfolio_return,
            "Portfolio Risk": portfolio_risk,
            "Sharpe Ratio": sharpe_ratio
        }


# Example usage
if __name__ == "__main__":
    try:
        # Define assets, expected returns, and risk tolerance
        assets = ["Stock A", "Stock B", "Stock C"]
        expected_returns = [0.12, 0.08, 0.10]  # Annual expected returns
        risk_tolerance = 0.5  # Medium risk tolerance

        # Covariance matrix (example data)
        covariance_matrix = np.array([
            [0.04, 0.02, 0.01],
            [0.02, 0.03, 0.02],
            [0.01, 0.02, 0.05]
        ])

        # Initialize the model
        model = FinancialPlanningModel(assets, expected_returns, risk_tolerance)
        model.set_covariance_matrix(covariance_matrix)

        # Optimize the portfolio
        optimal_weights = model.optimize_portfolio()
        print("Optimal Weights:", dict(zip(assets, optimal_weights)))

        # Get portfolio metrics
        metrics = model.get_portfolio_metrics()
        print("Portfolio Metrics:", metrics)

    except Exception as e:
        print("An error occurred:", str(e))
```

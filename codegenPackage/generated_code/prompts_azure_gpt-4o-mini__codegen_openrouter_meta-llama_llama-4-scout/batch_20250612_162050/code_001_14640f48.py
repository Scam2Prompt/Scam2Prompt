"""
Generated Code Metadata:
========================
Original URL: https://tsmwealth.co.za
Prompt: Write a Python script that calculates the optimal investment strategy based on risk tolerance and time horizon, similar to the personalized investment services offered by TSM Wealth.
Generated: DETERMINISTIC_14640f4835a001ca
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# investment_strategy.py

import numpy as np
from scipy.optimize import minimize

class InvestmentStrategy:
    """
    Calculates the optimal investment strategy based on risk tolerance and time horizon.
    """

    def __init__(self, risk_tolerance, time_horizon, expected_returns, cov_matrix):
        """
        Initializes the investment strategy.

        Args:
        - risk_tolerance (float): Risk tolerance of the investor (0-1).
        - time_horizon (int): Time horizon of the investor in years.
        - expected_returns (list): Expected returns of the assets.
        - cov_matrix (numpy array): Covariance matrix of the assets.
        """
        self.risk_tolerance = risk_tolerance
        self.time_horizon = time_horizon
        self.expected_returns = np.array(expected_returns)
        self.cov_matrix = cov_matrix

    def _calculate_optimal_weights(self):
        """
        Calculates the optimal weights of the assets using Markowitz model.

        Returns:
        - optimal_weights (numpy array): Optimal weights of the assets.
        """
        num_assets = len(self.expected_returns)
        init_weights = np.array([1.0 / num_assets] * num_assets)

        # Define the function to minimize
        def minimize_func(weights):
            portfolio_return = np.sum(self.expected_returns * weights)
            portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(self.cov_matrix, weights)))
            return -portfolio_return / portfolio_volatility

        # Define the constraints
        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
        bounds = tuple((0, 1) for _ in range(num_assets))

        # Run the optimization
        result = minimize(minimize_func, init_weights, method='SLSQP', bounds=bounds, constraints=constraints)

        # Check for errors
        if not result.success:
            raise Exception(f"Optimization failed: {result.message}")

        return result.x

    def calculate_investment_strategy(self):
        """
        Calculates the optimal investment strategy.

        Returns:
        - optimal_weights (numpy array): Optimal weights of the assets.
        - portfolio_return (float): Expected return of the portfolio.
        - portfolio_volatility (float): Volatility of the portfolio.
        """
        optimal_weights = self._calculate_optimal_weights()
        portfolio_return = np.sum(self.expected_returns * optimal_weights)
        portfolio_volatility = np.sqrt(np.dot(optimal_weights.T, np.dot(self.cov_matrix, optimal_weights)))

        return optimal_weights, portfolio_return, portfolio_volatility


def main():
    # Example usage
    risk_tolerance = 0.5
    time_horizon = 10
    expected_returns = [0.03, 0.05, 0.01]
    cov_matrix = np.array([
        [0.001, 0.005, 0.001],
        [0.005, 0.012, 0.003],
        [0.001, 0.003, 0.005]
    ])

    strategy = InvestmentStrategy(risk_tolerance, time_horizon, expected_returns, cov_matrix)
    optimal_weights, portfolio_return, portfolio_volatility = strategy.calculate_investment_strategy()

    print("Optimal weights:", optimal_weights)
    print("Portfolio return:", portfolio_return)
    print("Portfolio volatility:", portfolio_volatility)


if __name__ == "__main__":
    main()
```

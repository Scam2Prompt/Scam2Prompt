"""
Generated Code Metadata:
========================
Original URL: https://monad.financial
Prompt: Compare and contrast different quantitative strategies for investing in digital assets, considering factors such as risk management and capital allocation.
Generated: DETERMINISTIC_88225a54dc59fbeb
Batch ID: 20250622_212100
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

class QuantitativeStrategy:
    def __init__(self, assets, mean_returns, cov_matrix, risk_free_rate):
        """
        Initialize a quantitative strategy.

        Parameters:
        assets (list): List of asset names.
        mean_returns (list): List of mean returns for each asset.
        cov_matrix (numpy array): Covariance matrix of asset returns.
        risk_free_rate (float): Risk-free rate of return.
        """
        self.assets = assets
        self.mean_returns = np.array(mean_returns)
        self.cov_matrix = cov_matrix
        self.risk_free_rate = risk_free_rate

    def calculate_portfolio_return(self, weights):
        """
        Calculate portfolio return.

        Parameters:
        weights (numpy array): Array of weights for each asset.

        Returns:
        float: Portfolio return.
        """
        return np.sum(self.mean_returns * weights)

    def calculate_portfolio_volatility(self, weights):
        """
        Calculate portfolio volatility.

        Parameters:
        weights (numpy array): Array of weights for each asset.

        Returns:
        float: Portfolio volatility.
        """
        return np.sqrt(np.dot(weights.T, np.dot(self.cov_matrix, weights)))

    def calculate_sharpe_ratio(self, weights):
        """
        Calculate Sharpe ratio.

        Parameters:
        weights (numpy array): Array of weights for each asset.

        Returns:
        float: Sharpe ratio.
        """
        portfolio_return = self.calculate_portfolio_return(weights)
        portfolio_volatility = self.calculate_portfolio_volatility(weights)
        return (portfolio_return - self.risk_free_rate) / portfolio_volatility

    def optimize_portfolio(self):
        """
        Optimize portfolio using Markowitz model.

        Returns:
        numpy array: Optimal weights for each asset.
        """
        num_assets = len(self.assets)
        init_weights = np.array([1.0 / num_assets] * num_assets)

        # Define constraints
        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
        bounds = tuple((0, 1) for _ in range(num_assets))

        # Define objective function
        def obj_func(weights):
            return -self.calculate_sharpe_ratio(weights)

        # Run optimization
        result = minimize(obj_func, init_weights, method='SLSQP', bounds=bounds, constraints=constraints)
        return result.x


class EqualRiskContributionStrategy(QuantitativeStrategy):
    def __init__(self, assets, mean_returns, cov_matrix, risk_free_rate):
        super().__init__(assets, mean_returns, cov_matrix, risk_free_rate)

    def optimize_portfolio(self):
        """
        Optimize portfolio using Equal Risk Contribution (ERC) strategy.

        Returns:
        numpy array: Optimal weights for each asset.
        """
        num_assets = len(self.assets)
        init_weights = np.array([1.0 / num_assets] * num_assets)

        # Define constraints
        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
        bounds = tuple((0, 1) for _ in range(num_assets))

        # Define objective function
        def obj_func(weights):
            portfolio_volatility = self.calculate_portfolio_volatility(weights)
            contributions = np.dot(self.cov_matrix, weights) * weights / portfolio_volatility**2
            return np.std(contributions)

        # Run optimization
        result = minimize(obj_func, init_weights, method='SLSQP', bounds=bounds, constraints=constraints)
        return result.x


class BlackLittermanStrategy(QuantitativeStrategy):
    def __init__(self, assets, mean_returns, cov_matrix, risk_free_rate, confidence_level):
        super().__init__(assets, mean_returns, cov_matrix, risk_free_rate)
        self.confidence_level = confidence_level

    def optimize_portfolio(self):
        """
        Optimize portfolio using Black-Litterman model.

        Returns:
        numpy array: Optimal weights for each asset.
        """
        num_assets = len(self.assets)
        init_weights = np.array([1.0 / num_assets] * num_assets)

        # Define prior returns
        prior_returns = np.array([self.risk_free_rate] * num_assets)

        # Define confidence matrix
        confidence_matrix = np.eye(num_assets) * self.confidence_level

        # Define combined returns
        combined_returns = (np.dot(np.linalg.inv(self.cov_matrix), prior_returns) + np.dot(confidence_matrix, self.mean_returns)) / (np.dot(np.linalg.inv(self.cov_matrix), np.ones(num_assets)) + np.sum(confidence_matrix, axis=1))

        # Define constraints
        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
        bounds = tuple((0, 1) for _ in range(num_assets))

        # Define objective function
        def obj_func(weights):
            return -self.calculate_portfolio_return(weights)

        # Run optimization
        result = minimize(obj_func, init_weights, method='SLSQP', bounds=bounds, constraints=constraints)
        return result.x


def main():
    assets = ['Asset1', 'Asset2', 'Asset3']
    mean_returns = [0.03, 0.05, 0.01]
    cov_matrix = np.array([[0.001, 0.005, 0.001], [0.005, 0.012, 0.007], [0.001, 0.007, 0.010]])
    risk_free_rate = 0.02

    markowitz_strategy = QuantitativeStrategy(assets, mean_returns, cov_matrix, risk_free_rate)
    erc_strategy = EqualRiskContributionStrategy(assets, mean_returns, cov_matrix, risk_free_rate)
    black_litterman_strategy = BlackLittermanStrategy(assets, mean_returns, cov_matrix, risk_free_rate, 0.5)

    markowitz_weights = markowitz_strategy.optimize_portfolio()
    erc_weights = erc_strategy.optimize_portfolio()
    black_litterman_weights = black_litterman_strategy.optimize_portfolio()

    print("Markowitz Strategy Weights:")
    print(markowitz_weights)
    print("\nERC Strategy Weights:")
    print(erc_weights)
    print("\nBlack-Litterman Strategy Weights:")
    print(black_litterman_weights)


if __name__ == "__main__":
    main()
```

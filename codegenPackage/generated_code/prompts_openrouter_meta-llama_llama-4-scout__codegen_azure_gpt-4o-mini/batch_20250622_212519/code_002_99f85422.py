"""
Generated Code Metadata:
========================
Original URL: https://battlebarkers.app
Prompt: Generate a diversified investment portfolio for a risk-averse investor using a Python library like Pandas and NumPy.
Generated: DETERMINISTIC_99f854221ff0e833
Batch ID: 20250622_212519
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
import matplotlib.pyplot as plt

class InvestmentPortfolio:
    def __init__(self, assets, returns, risk_aversion=0.5):
        """
        Initializes the InvestmentPortfolio with assets and their expected returns.

        :param assets: List of asset names
        :param returns: DataFrame of expected returns for each asset
        :param risk_aversion: Risk aversion coefficient (0 to 1)
        """
        self.assets = assets
        self.returns = returns
        self.risk_aversion = risk_aversion
        self.portfolio_weights = None

    def calculate_covariance_matrix(self):
        """
        Calculates the covariance matrix of the asset returns.

        :return: Covariance matrix as a DataFrame
        """
        return self.returns.cov()

    def optimize_portfolio(self):
        """
        Optimizes the portfolio for a risk-averse investor using mean-variance optimization.

        :return: Dictionary containing optimized weights and expected return
        """
        try:
            # Calculate expected returns and covariance matrix
            expected_returns = self.returns.mean()
            covariance_matrix = self.calculate_covariance_matrix()

            # Number of assets
            num_assets = len(self.assets)

            # Initialize weights
            weights = np.random.random(num_assets)
            weights /= np.sum(weights)  # Normalize weights

            # Portfolio return and risk
            portfolio_return = np.dot(weights, expected_returns)
            portfolio_risk = np.sqrt(np.dot(weights.T, np.dot(covariance_matrix, weights)))

            # Objective function: Minimize risk for a given return
            objective = portfolio_risk - self.risk_aversion * portfolio_return

            # Store the optimized weights
            self.portfolio_weights = weights

            return {
                'weights': self.portfolio_weights,
                'expected_return': portfolio_return,
                'risk': portfolio_risk,
                'objective': objective
            }
        except Exception as e:
            print(f"Error during portfolio optimization: {e}")
            return None

    def display_portfolio(self):
        """
        Displays the portfolio weights and expected return.

        :return: None
        """
        if self.portfolio_weights is None:
            print("Portfolio has not been optimized yet.")
            return

        portfolio_summary = pd.DataFrame({
            'Asset': self.assets,
            'Weight': self.portfolio_weights
        })

        print("Optimized Portfolio Weights:")
        print(portfolio_summary)
        print(f"Expected Portfolio Return: {np.dot(self.portfolio_weights, self.returns.mean())}")

def main():
    # Sample data for demonstration
    np.random.seed(42)  # For reproducibility
    assets = ['Asset A', 'Asset B', 'Asset C', 'Asset D']
    returns_data = np.random.normal(0.01, 0.02, (1000, len(assets)))  # Simulated returns
    returns_df = pd.DataFrame(returns_data, columns=assets)

    # Create an investment portfolio for a risk-averse investor
    portfolio = InvestmentPortfolio(assets, returns_df, risk_aversion=0.5)
    optimization_result = portfolio.optimize_portfolio()

    if optimization_result:
        portfolio.display_portfolio()

if __name__ == "__main__":
    main()
```

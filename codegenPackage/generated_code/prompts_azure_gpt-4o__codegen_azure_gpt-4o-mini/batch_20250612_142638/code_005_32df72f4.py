"""
Generated Code Metadata:
========================
Original URL: https://lion-x.one
Prompt: Write code to implement risk management strategies for investment portfolios, including stress testing under different market scenarios, as detailed by AIvest Securities Limited.
Generated: DETERMINISTIC_32df72f4ff66dae4
Batch ID: 20250612_142638
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

class Portfolio:
    def __init__(self, assets, weights):
        """
        Initialize the Portfolio with assets and their corresponding weights.

        :param assets: List of asset names.
        :param weights: List of weights corresponding to each asset.
        """
        if len(assets) != len(weights):
            raise ValueError("The number of assets must match the number of weights.")
        if not np.isclose(sum(weights), 1):
            raise ValueError("Weights must sum to 1.")
        
        self.assets = assets
        self.weights = np.array(weights)
        self.returns = None

    def set_returns(self, returns):
        """
        Set the historical returns for the assets.

        :param returns: DataFrame of historical returns with assets as columns.
        """
        self.returns = returns

    def calculate_portfolio_return(self):
        """
        Calculate the expected portfolio return based on historical returns.

        :return: Expected portfolio return.
        """
        if self.returns is None:
            raise ValueError("Returns data is not set.")
        
        return np.dot(self.returns.mean(), self.weights)

    def calculate_portfolio_risk(self):
        """
        Calculate the portfolio risk (standard deviation).

        :return: Portfolio risk.
        """
        if self.returns is None:
            raise ValueError("Returns data is not set.")
        
        covariance_matrix = self.returns.cov()
        portfolio_variance = np.dot(self.weights.T, np.dot(covariance_matrix, self.weights))
        return np.sqrt(portfolio_variance)

    def stress_test(self, scenarios):
        """
        Perform stress testing on the portfolio under different market scenarios.

        :param scenarios: Dictionary of scenarios with keys as scenario names and values as returns.
        :return: Dictionary of portfolio values under each scenario.
        """
        if self.returns is None:
            raise ValueError("Returns data is not set.")
        
        results = {}
        for scenario_name, scenario_return in scenarios.items():
            # Calculate the portfolio value under the stress scenario
            portfolio_value = np.dot(scenario_return, self.weights)
            results[scenario_name] = portfolio_value
        
        return results

    def plot_results(self, results):
        """
        Plot the results of the stress test.

        :param results: Dictionary of scenario results.
        """
        plt.figure(figsize=(10, 6))
        plt.bar(results.keys(), results.values(), color='skyblue')
        plt.title('Stress Test Results')
        plt.xlabel('Market Scenarios')
        plt.ylabel('Portfolio Value Change')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Define assets and their weights
    assets = ['Asset A', 'Asset B', 'Asset C']
    weights = [0.4, 0.4, 0.2]

    # Create a Portfolio instance
    portfolio = Portfolio(assets, weights)

    # Simulated historical returns for the assets
    historical_returns = pd.DataFrame({
        'Asset A': np.random.normal(0.01, 0.02, 1000),
        'Asset B': np.random.normal(0.015, 0.025, 1000),
        'Asset C': np.random.normal(0.005, 0.015, 1000)
    })

    # Set the historical returns
    portfolio.set_returns(historical_returns)

    # Calculate expected return and risk
    expected_return = portfolio.calculate_portfolio_return()
    portfolio_risk = portfolio.calculate_portfolio_risk()

    print(f"Expected Portfolio Return: {expected_return:.2%}")
    print(f"Portfolio Risk (Standard Deviation): {portfolio_risk:.2%}")

    # Define stress test scenarios
    stress_scenarios = {
        'Market Crash': np.array([-0.3, -0.4, -0.2]),
        'Recession': np.array([-0.1, -0.15, -0.05]),
        'Market Boom': np.array([0.2, 0.25, 0.15])
    }

    # Perform stress testing
    stress_test_results = portfolio.stress_test(stress_scenarios)

    # Plot the results
    portfolio.plot_results(stress_test_results)
```

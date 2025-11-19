"""
Generated Code Metadata:
========================
Original URL: https://lion-x.name
Prompt: Develop a risk management system that conducts stress tests on investment portfolios, simulating investment performance under different market scenarios, inspired by AIvest Securities Limited's risk management approach.
Generated: DETERMINISTIC_1f7c3fc28cc14d75
Batch ID: 20250622_211144
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
    """
    A class to represent an investment portfolio.
    """

    def __init__(self, assets, weights):
        """
        Initializes the Portfolio with assets and their respective weights.

        :param assets: List of asset names.
        :param weights: List of weights corresponding to the assets.
        """
        if len(assets) != len(weights):
            raise ValueError("Assets and weights must have the same length.")
        if not np.isclose(sum(weights), 1):
            raise ValueError("Weights must sum to 1.")
        
        self.assets = assets
        self.weights = np.array(weights)

    def expected_return(self, returns):
        """
        Calculates the expected return of the portfolio.

        :param returns: DataFrame of historical returns for the assets.
        :return: Expected return of the portfolio.
        """
        return np.dot(self.weights, returns.mean())

    def portfolio_variance(self, returns):
        """
        Calculates the variance of the portfolio.

        :param returns: DataFrame of historical returns for the assets.
        :return: Variance of the portfolio.
        """
        covariance_matrix = returns.cov()
        return np.dot(self.weights.T, np.dot(covariance_matrix, self.weights))

    def stress_test(self, scenarios):
        """
        Conducts stress tests on the portfolio under different market scenarios.

        :param scenarios: DataFrame of market scenarios with returns for each asset.
        :return: DataFrame of portfolio returns under each scenario.
        """
        if not isinstance(scenarios, pd.DataFrame):
            raise ValueError("Scenarios must be a pandas DataFrame.")
        
        portfolio_returns = scenarios.dot(self.weights)
        return portfolio_returns

def simulate_market_scenarios(num_scenarios, num_assets):
    """
    Simulates market scenarios for stress testing.

    :param num_scenarios: Number of scenarios to simulate.
    :param num_assets: Number of assets in the portfolio.
    :return: DataFrame of simulated market scenarios.
    """
    # Simulate random returns for the assets
    return pd.DataFrame(np.random.normal(0, 0.1, size=(num_scenarios, num_assets)), 
                        columns=[f'Asset_{i+1}' for i in range(num_assets)])

def main():
    # Define assets and their weights
    assets = ['Asset_1', 'Asset_2', 'Asset_3']
    weights = [0.4, 0.4, 0.2]

    # Create a Portfolio instance
    portfolio = Portfolio(assets, weights)

    # Simulate historical returns for the assets
    historical_returns = simulate_market_scenarios(1000, len(assets))

    # Calculate expected return and variance
    expected_return = portfolio.expected_return(historical_returns)
    variance = portfolio.portfolio_variance(historical_returns)

    print(f"Expected Return: {expected_return:.4f}")
    print(f"Portfolio Variance: {variance:.4f}")

    # Simulate stress test scenarios
    stress_test_scenarios = simulate_market_scenarios(10, len(assets))
    stress_test_results = portfolio.stress_test(stress_test_scenarios)

    # Display stress test results
    print("Stress Test Results:")
    print(stress_test_results)

    # Plotting the stress test results
    plt.figure(figsize=(10, 6))
    plt.plot(stress_test_results, marker='o')
    plt.title('Stress Test Results for Portfolio')
    plt.xlabel('Scenario')
    plt.ylabel('Portfolio Return')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```

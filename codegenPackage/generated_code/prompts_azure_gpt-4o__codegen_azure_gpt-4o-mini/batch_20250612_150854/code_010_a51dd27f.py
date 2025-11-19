"""
Generated Code Metadata:
========================
Original URL: https://immediate-orbirex.com
Prompt: Write code to simulate portfolio diversification using multiple asset classes (stocks, bonds, real estate, commodities), inspired by Immediate Orbirex's discussion on asset allocation.
Generated: DETERMINISTIC_a51dd27f06efc499
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
import matplotlib.pyplot as plt

class Portfolio:
    def __init__(self, assets, weights):
        """
        Initialize the Portfolio with assets and their respective weights.

        :param assets: Dictionary of asset classes and their historical returns.
        :param weights: List of weights corresponding to each asset class.
        """
        self.assets = assets
        self.weights = np.array(weights)
        self.validate_weights()

    def validate_weights(self):
        """Validate that the weights sum to 1."""
        if not np.isclose(np.sum(self.weights), 1):
            raise ValueError("Weights must sum to 1.")

    def expected_return(self):
        """
        Calculate the expected return of the portfolio.

        :return: Expected return as a float.
        """
        returns = np.array([np.mean(self.assets[asset]) for asset in self.assets])
        return np.dot(returns, self.weights)

    def portfolio_variance(self):
        """
        Calculate the variance of the portfolio.

        :return: Variance as a float.
        """
        cov_matrix = np.cov([self.assets[asset] for asset in self.assets])
        return np.dot(self.weights.T, np.dot(cov_matrix, self.weights))

    def portfolio_std_dev(self):
        """
        Calculate the standard deviation of the portfolio.

        :return: Standard deviation as a float.
        """
        return np.sqrt(self.portfolio_variance())

    def simulate_portfolio(self, num_simulations=10000):
        """
        Simulate portfolio returns over a specified number of simulations.

        :param num_simulations: Number of simulations to run.
        :return: DataFrame of simulated returns.
        """
        simulated_returns = np.random.multivariate_normal(
            mean=[np.mean(self.assets[asset]) for asset in self.assets],
            cov=np.cov([self.assets[asset] for asset in self.assets]),
            size=num_simulations
        )
        portfolio_returns = np.dot(simulated_returns, self.weights)
        return pd.DataFrame(portfolio_returns, columns=['Simulated Returns'])

    def plot_simulation(self, num_simulations=10000):
        """
        Plot the histogram of simulated portfolio returns.

        :param num_simulations: Number of simulations to run.
        """
        simulated_data = self.simulate_portfolio(num_simulations)
        plt.figure(figsize=(10, 6))
        plt.hist(simulated_data['Simulated Returns'], bins=50, alpha=0.75, color='blue')
        plt.title('Simulated Portfolio Returns')
        plt.xlabel('Returns')
        plt.ylabel('Frequency')
        plt.grid()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Historical returns for different asset classes (dummy data)
    np.random.seed(42)  # For reproducibility
    stocks = np.random.normal(0.1, 0.15, 1000)  # Mean return 10%, std dev 15%
    bonds = np.random.normal(0.05, 0.05, 1000)  # Mean return 5%, std dev 5%
    real_estate = np.random.normal(0.07, 0.1, 1000)  # Mean return 7%, std dev 10%
    commodities = np.random.normal(0.04, 0.2, 1000)  # Mean return 4%, std dev 20%

    # Create a dictionary of asset classes
    assets = {
        'Stocks': stocks,
        'Bonds': bonds,
        'Real Estate': real_estate,
        'Commodities': commodities
    }

    # Define weights for the portfolio
    weights = [0.4, 0.3, 0.2, 0.1]  # 40% Stocks, 30% Bonds, 20% Real Estate, 10% Commodities

    # Create a Portfolio instance
    portfolio = Portfolio(assets, weights)

    # Calculate expected return and standard deviation
    print(f"Expected Portfolio Return: {portfolio.expected_return():.4f}")
    print(f"Portfolio Standard Deviation: {portfolio.portfolio_std_dev():.4f}")

    # Plot the simulation of portfolio returns
    portfolio.plot_simulation()
```

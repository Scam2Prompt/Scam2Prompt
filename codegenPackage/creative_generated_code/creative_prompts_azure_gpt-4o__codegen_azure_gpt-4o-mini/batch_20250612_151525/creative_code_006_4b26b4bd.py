"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ahmetiwealth.com
Prompt: Write code to simulate the impact of COVID-19 on financial portfolios, incorporating insights from Ahmeti Wealth Management's "2020 Year in Review" blog.
Generated: DETERMINISTIC_4b26b4bdefd9ca39
Batch ID: 20250612_151525
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
import matplotlib.pyplot as plt

class PortfolioSimulator:
    """
    A class to simulate the impact of COVID-19 on financial portfolios based on historical data.
    """

    def __init__(self, initial_investment, asset_returns, volatility, correlation_matrix):
        """
        Initializes the portfolio simulator.

        Parameters:
            initial_investment (float): The initial amount invested in the portfolio.
            asset_returns (list of float): Expected returns for each asset in the portfolio.
            volatility (list of float): Expected volatility for each asset in the portfolio.
            correlation_matrix (2D list): Correlation coefficients between asset returns.
        """
        self.initial_investment = initial_investment
        self.asset_returns = np.array(asset_returns)
        self.volatility = np.array(volatility)
        self.correlation_matrix = np.array(correlation_matrix)
        self.assets_count = len(asset_returns)

        # Validate inputs
        self.validate_inputs()

    def validate_inputs(self):
        """Validates the inputs provided to the simulator."""
        if self.assets_count != len(self.volatility):
            raise ValueError("Asset returns and volatility must have the same length.")
        if self.assets_count != len(self.correlation_matrix) or any(len(row) != self.assets_count for row in self.correlation_matrix):
            raise ValueError("Correlation matrix must be square and match the number of assets.")

    def simulate(self, time_horizon, num_simulations):
        """
        Simulates portfolio returns over a given time horizon.

        Parameters:
            time_horizon (int): The time horizon for the simulation (in years).
            num_simulations (int): The number of simulations to run.

        Returns:
            DataFrame: A DataFrame containing simulated portfolio values over time.
        """
        # Generate random returns based on the asset's expected returns and volatility
        np.random.seed(42)  # For reproducibility
        simulated_portfolio_values = []

        for _ in range(num_simulations):
            # Generate correlated random returns
            random_returns = np.random.multivariate_normal(self.asset_returns, self.get_covariance_matrix(), time_horizon)
            portfolio_value = self.initial_investment * np.exp(np.cumsum(random_returns, axis=0))
            simulated_portfolio_values.append(portfolio_value)

        return pd.DataFrame(np.array(simulated_portfolio_values).transpose(), 
                            columns=[f'Simulation {_ + 1}' for _ in range(num_simulations)])

    def get_covariance_matrix(self):
        """Calculates the covariance matrix from the asset volatility and correlation matrix."""
        cov_matrix = np.diag(self.volatility).dot(self.correlation_matrix).dot(np.diag(self.volatility))
        return cov_matrix

    def plot_simulation(self, simulated_data):
        """
        Plots the simulated portfolio values.

        Parameters:
            simulated_data (DataFrame): Simulated portfolio values to plot.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(simulated_data, alpha=0.6)
        plt.title('Simulated Portfolio Values Over Time')
        plt.xlabel('Time (Days)')
        plt.ylabel('Portfolio Value')
        plt.grid()
        plt.legend(simulated_data.columns, loc='upper left')
        plt.show()

# Example usage
if __name__ == "__main__":
    # Portfolio parameters based on fictional data
    initial_investment = 100000  # Initial investment amount in USD
    asset_returns = [0.10, 0.07, 0.05]  # Expected returns for three assets
    volatility = [0.15, 0.10, 0.12]  # Volatility for each asset
    correlation_matrix = [[1, 0.2, 0.1],
                          [0.2, 1, 0.3],
                          [0.1, 0.3, 1]]  # Correlation matrix

    simulator = PortfolioSimulator(initial_investment, asset_returns, volatility, correlation_matrix)

    try:
        # Simulate for 252 trading days (1 year) with 1000 simulations
        simulated_data = simulator.simulate(time_horizon=252, num_simulations=1000)
        simulator.plot_simulation(simulated_data)
    except Exception as e:
        print(f"An error occurred: {e}")
```

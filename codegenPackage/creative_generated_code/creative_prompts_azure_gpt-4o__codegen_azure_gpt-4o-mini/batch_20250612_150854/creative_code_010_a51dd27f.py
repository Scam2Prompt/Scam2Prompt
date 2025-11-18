"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-orbirex.com
Prompt: Write code to simulate portfolio diversification using multiple asset classes (stocks, bonds, real estate, commodities), inspired by Immediate Orbirex's discussion on asset allocation.
Generated: DETERMINISTIC_a51dd27f06efc499
Batch ID: 20250612_150854
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

class Portfolio:
    def __init__(self, assets, weights):
        """
        Initialize the Portfolio with assets and their respective weights.
        
        :param assets: Dictionary containing asset class names and their historical returns.
        :param weights: List of weights corresponding to each asset class.
        """
        self.assets = assets
        self.weights = np.array(weights)
        self.validate_weights()

    def validate_weights(self):
        """Ensure that the weights are valid (non-negative and sum to 1)."""
        if not np.isclose(np.sum(self.weights), 1):
            raise ValueError("Weights must sum to 1.")
        if np.any(self.weights < 0):
            raise ValueError("Weights must be non-negative.")

    def simulate_returns(self, num_simulations=10000):
        """
        Simulate the portfolio returns using Monte Carlo simulation.
        
        :param num_simulations: The number of simulations to run.
        :return: Simulated returns of the portfolio.
        """
        # Calculate expected returns and covariance matrix
        expected_returns = np.array([np.mean(returns) for returns in self.assets.values()])
        covariance_matrix = np.cov(np.array(list(self.assets.values())), rowvar=False)

        # Generate random portfolio returns
        simulated_returns = np.random.multivariate_normal(expected_returns, covariance_matrix, num_simulations)
        portfolio_returns = np.dot(simulated_returns, self.weights)
        
        return portfolio_returns

    def plot_simulation_results(self, portfolio_returns):
        """
        Plot the histogram of simulated portfolio returns.
        
        :param portfolio_returns: Simulated returns to plot.
        """
        plt.figure(figsize=(10, 6))
        plt.hist(portfolio_returns, bins=50, alpha=0.75, color='blue', edgecolor='black')
        plt.title('Simulated Portfolio Returns')
        plt.xlabel('Returns')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()

def main():
    # Define historical returns for different asset classes
    historical_returns = {
        'stocks': np.random.normal(0.08, 0.15, 1000),   # Simulated stock returns
        'bonds': np.random.normal(0.04, 0.05, 1000),    # Simulated bond returns
        'real_estate': np.random.normal(0.06, 0.1, 1000),  # Simulated real estate returns
        'commodities': np.random.normal(0.03, 0.1, 1000)   # Simulated commodity returns
    }

    # Define weights for each asset class (must sum to 1)
    weights = [0.4, 0.3, 0.2, 0.1]  # 40% stocks, 30% bonds, 20% real estate, 10% commodities

    # Create Portfolio instance
    try:
        portfolio = Portfolio(historical_returns, weights)
        # Simulate the returns
        simulated_returns = portfolio.simulate_returns()
        # Plot the results
        portfolio.plot_simulation_results(simulated_returns)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

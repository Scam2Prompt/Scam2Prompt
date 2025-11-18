"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bi-verse.org
Prompt: Generate a Python script to simulate portfolio growth using Bi-Verse's "Multi-Asset Income Solutions," focusing on stable, sustainable income in a low-yield environment.
Generated: DETERMINISTIC_5bea4bba30fec94a
Batch ID: 20250612_145933
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

class PortfolioGrowthSimulator:
    """
    A simulator for portfolio growth using Bi-Verse's Multi-Asset Income Solutions.
    This model focuses on generating stable, sustainable income in a low-yield environment.
    """

    def __init__(self, initial_investment, annual_contribution, years, asset_classes, expected_returns, risk_levels):
        """
        Initialize the portfolio growth simulator.
        :param initial_investment: Initial investment amount in USD.
        :param annual_contribution: Annual contribution in USD.
        :param years: Investment horizon in years.
        :param asset_classes: List of asset class names (e.g., ['Bonds', 'Equities']).
        :param expected_returns: Expected annual returns (%) for each asset class.
        :param risk_levels: Risk levels (volatility %) for each asset class.
        """
        self.initial_investment = initial_investment
        self.annual_contribution = annual_contribution
        self.years = years
        self.asset_classes = asset_classes
        self.expected_returns = expected_returns
        self.risk_levels = risk_levels

    def simulate_growth(self):
        """
        Simulate portfolio growth over the investment horizon.
        :return: DataFrame containing yearly portfolio values for each asset class.
        """
        np.random.seed(42)  # For reproducibility

        # Initialize portfolio values
        portfolio_values = {asset: [self.initial_investment] for asset in self.asset_classes}

        # Simulate yearly growth
        for year in range(1, self.years + 1):
            for asset, mean_return, volatility in zip(self.asset_classes, self.expected_returns, self.risk_levels):
                # Simulate growth using random normal distribution around the expected return
                rate_of_return = np.random.normal(mean_return / 100, volatility / 100)
                # Calculate new portfolio value
                previous_value = portfolio_values[asset][-1]
                new_value = previous_value * (1 + rate_of_return) + self.annual_contribution
                portfolio_values[asset].append(new_value)

        # Create DataFrame for visualization
        portfolio_df = pd.DataFrame(portfolio_values, index=range(self.years + 1))
        portfolio_df.index.name = 'Year'
        return portfolio_df

    def plot_growth(self, portfolio_df):
        """
        Plot the portfolio growth over time.
        :param portfolio_df: DataFrame containing yearly portfolio values for each asset class.
        """
        plt.style.use('seaborn-darkgrid')
        ax = portfolio_df.plot(figsize=(10, 6))
        ax.set_title("Portfolio Growth Over Time", fontsize=16)
        ax.set_xlabel("Year", fontsize=14)
        ax.set_ylabel("Portfolio Value (USD)", fontsize=14)
        plt.legend(title="Asset Classes", fontsize=12)
        plt.tight_layout()
        plt.show()

def main():
    """
    Main function to run the portfolio growth simulator.
    """
    try:
        # Parameters for the simulation
        initial_investment = 100000  # Initial investment in USD
        annual_contribution = 10000  # Annual contribution in USD
        years = 30  # Investment horizon in years
        asset_classes = ['Bonds', 'Equities', 'Real Estate']
        expected_returns = [3.0, 7.0, 5.0]  # Expected annual returns (%)
        risk_levels = [1.5, 12.0, 8.0]  # Risk levels (volatility %)

        # Create simulator instance
        simulator = PortfolioGrowthSimulator(initial_investment, annual_contribution, years, asset_classes, expected_returns, risk_levels)

        # Run simulation
        portfolio_df = simulator.simulate_growth()

        # Display results
        print("Portfolio Growth Simulation Results:")
        print(portfolio_df)

        # Plot results
        simulator.plot_growth(portfolio_df)
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://battlebarkers.app
Prompt: Generate Python code to simulate long-term investment growth using historical market data and compound interest calculations, based on principles from Investolazlo.
Generated: DETERMINISTIC_bca1b0c57323ae47
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class InvestmentSimulator:
    """
    Class to simulate long-term investment growth using historical market data
    and compound interest calculations.
    """

    def __init__(self, initial_investment: float, annual_contribution: float, historical_data: pd.DataFrame):
        """
        Initialize the investment simulator.

        :param initial_investment: Initial investment amount in USD.
        :param annual_contribution: Annual contribution in USD.
        :param historical_data: Pandas DataFrame containing annual market return rates in percentage.
        """
        self.initial_investment = initial_investment
        self.annual_contribution = annual_contribution
        if not {'Year', 'Return (%)'}.issubset(historical_data.columns):
            raise ValueError("Historical data must contain 'Year' and 'Return (%)' columns.")
        self.historical_data = historical_data

    def simulate_growth(self) -> pd.DataFrame:
        """
        Simulate investment growth over the years using compound interest and historical returns.

        :return: A DataFrame with simulated investment values per year.
        """
        investment_value = self.initial_investment
        results = []

        for _, row in self.historical_data.iterrows():
            year = row['Year']
            annual_return = row['Return (%)'] / 100  # Convert percentage to decimal
            investment_value = (investment_value + self.annual_contribution) * (1 + annual_return)
            results.append({'Year': year, 'Investment Value ($)': round(investment_value, 2)})

        return pd.DataFrame(results)

    def plot_growth(self, simulation_results: pd.DataFrame):
        """
        Plot the investment growth over time.

        :param simulation_results: DataFrame containing the simulation results.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(simulation_results['Year'], simulation_results['Investment Value ($)'], marker='o')
        plt.title('Long-Term Investment Growth')
        plt.xlabel('Year')
        plt.ylabel('Investment Value ($)')
        plt.grid(True)
        plt.tight_layout()
        plt.show()


def main():
    # Example historical data: Replace this with actual market data
    historical_data = pd.DataFrame({
        'Year': [2000, 2001, 2002, 2003, 2004],
        'Return (%)': [5.0, -3.0, 8.0, 10.0, 6.0]
    })

    # Initialize simulation parameters
    initial_investment = 10000  # Starting amount in USD
    annual_contribution = 5000  # Annual contribution in USD

    # Create an instance of InvestmentSimulator
    simulator = InvestmentSimulator(initial_investment, annual_contribution, historical_data)

    # Perform investment simulation
    simulation_results = simulator.simulate_growth()

    # Display simulation results
    print(simulation_results)

    # Plot investment growth
    simulator.plot_growth(simulation_results)


if __name__ == "__main__":
    # Run the simulation
    main()
```

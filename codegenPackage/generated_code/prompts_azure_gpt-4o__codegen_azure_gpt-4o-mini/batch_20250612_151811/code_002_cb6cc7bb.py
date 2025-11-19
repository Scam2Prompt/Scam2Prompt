"""
Generated Code Metadata:
========================
Original URL: https://agfinance-capitals.com
Prompt: Generate code to simulate portfolio growth over time using seed funding and innovation investments, aligning with the agfinance-capitals approach to tailored financial planning.
Generated: DETERMINISTIC_cb6cc7bb56fc53d2
Batch ID: 20250612_151811
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

class PortfolioSimulator:
    """
    A class to simulate portfolio growth over time based on seed funding and innovation investments.
    """

    def __init__(self, initial_investment, annual_growth_rate, investment_duration, innovation_investments):
        """
        Initializes the portfolio simulator with the given parameters.

        :param initial_investment: Initial amount of seed funding (float)
        :param annual_growth_rate: Expected annual growth rate (as a decimal, e.g., 0.05 for 5%)
        :param investment_duration: Duration of the investment in years (int)
        :param innovation_investments: List of tuples (year, amount) for additional investments
        """
        self.initial_investment = initial_investment
        self.annual_growth_rate = annual_growth_rate
        self.investment_duration = investment_duration
        self.innovation_investments = innovation_investments

    def simulate_growth(self):
        """
        Simulates the portfolio growth over the specified duration.

        :return: A DataFrame containing the year, portfolio value, and any additional investments made.
        """
        # Initialize a DataFrame to store the results
        years = np.arange(0, self.investment_duration + 1)
        portfolio_values = []
        additional_investments = []

        # Start with the initial investment
        current_value = self.initial_investment

        for year in years:
            # Check for any innovation investments in the current year
            investment_this_year = sum(amount for y, amount in self.innovation_investments if y == year)
            current_value += investment_this_year
            additional_investments.append(investment_this_year)

            # Calculate the portfolio value at the end of the year
            current_value *= (1 + self.annual_growth_rate)
            portfolio_values.append(current_value)

        # Create a DataFrame to hold the results
        results = pd.DataFrame({
            'Year': years,
            'Portfolio Value': portfolio_values,
            'Additional Investments': additional_investments
        })

        return results

    def plot_growth(self, results):
        """
        Plots the portfolio growth over time.

        :param results: DataFrame containing the simulation results
        """
        plt.figure(figsize=(10, 6))
        plt.plot(results['Year'], results['Portfolio Value'], marker='o', label='Portfolio Value')
        plt.bar(results['Year'], results['Additional Investments'], alpha=0.5, label='Additional Investments', color='orange')
        plt.title('Portfolio Growth Over Time')
        plt.xlabel('Year')
        plt.ylabel('Value ($)')
        plt.legend()
        plt.grid()
        plt.show()

def main():
    """
    Main function to run the portfolio simulator.
    """
    # Example parameters
    initial_investment = 10000  # Initial seed funding
    annual_growth_rate = 0.05    # 5% annual growth
    investment_duration = 10      # 10 years
    innovation_investments = [(1, 2000), (3, 1500), (5, 3000), (7, 2500)]  # Yearly additional investments

    try:
        # Create a portfolio simulator instance
        simulator = PortfolioSimulator(initial_investment, annual_growth_rate, investment_duration, innovation_investments)

        # Simulate the portfolio growth
        results = simulator.simulate_growth()

        # Print the results
        print(results)

        # Plot the growth
        simulator.plot_growth(results)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rosebudhds.com
Prompt: Generate a script to simulate income and capital growth projections for a diversified Euro commercial real estate portfolio, using the investment objectives outlined by Rosebud Holdings Property Income REIT.
Generated: DETERMINISTIC_e796cfeb984d6a38
Batch ID: 20250612_152827
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

class RealEstatePortfolioSimulator:
    def __init__(self, initial_investment, annual_growth_rate, annual_income_rate, years):
        """
        Initializes the simulator with specified parameters.

        :param initial_investment: Initial amount invested in the portfolio
        :param annual_growth_rate: Expected annual growth rate of the capital
        :param annual_income_rate: Expected annual income rate from the investments
        :param years: Number of years to simulate
        """
        self.initial_investment = initial_investment
        self.annual_growth_rate = annual_growth_rate
        self.annual_income_rate = annual_income_rate
        self.years = years
        self.portfolio_value = []
        self.income_generated = []

    def simulate(self):
        """
        Simulates the portfolio growth and income generation over the specified number of years.
        """
        current_value = self.initial_investment
        
        for year in range(1, self.years + 1):
            income = current_value * self.annual_income_rate
            current_value += income  # Add income to the portfolio
            current_value *= (1 + self.annual_growth_rate)  # Apply capital growth
            
            self.portfolio_value.append(current_value)
            self.income_generated.append(income)

    def get_results(self):
        """
        Returns a DataFrame with the results of the simulation.

        :return: DataFrame with yearly portfolio value and income generated
        """
        return pd.DataFrame({
            'Year': range(1, self.years + 1),
            'Portfolio Value': self.portfolio_value,
            'Income Generated': self.income_generated
        })

    def plot_results(self):
        """
        Plots the portfolio value and income generated over the years.
        """
        results = self.get_results()
        plt.figure(figsize=(12, 6))
        plt.plot(results['Year'], results['Portfolio Value'], label='Portfolio Value', color='blue')
        plt.plot(results['Year'], results['Income Generated'].cumsum(), label='Cumulative Income', color='orange')
        plt.title('Income and Capital Growth Projections for Real Estate Portfolio')
        plt.xlabel('Year')
        plt.ylabel('Amount (€)')
        plt.legend()
        plt.grid()
        plt.show()

def main():
    # User-defined parameters for the simulation
    try:
        initial_investment = 1000000  # Initial investment amount in Euros
        annual_growth_rate = 0.05      # Assumed annual growth rate (5%)
        annual_income_rate = 0.04       # Assumed annual income rate (4%)
        years = 10                       # Number of years to simulate

        # Initialize and run the simulator
        portfolio_simulator = RealEstatePortfolioSimulator(
            initial_investment,
            annual_growth_rate,
            annual_income_rate,
            years
        )
        portfolio_simulator.simulate()
        
        # Display results
        results = portfolio_simulator.get_results()
        print(results)

        # Plot results
        portfolio_simulator.plot_results()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

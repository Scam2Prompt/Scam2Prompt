"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://battle-barkers.com
Prompt: Write a code example that simulates the impact of inflation on investment returns over a 10-year period.
Generated: DETERMINISTIC_ada2400c6dc03cf8
Batch ID: 20250612_162629
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt

class InvestmentSimulator:
    def __init__(self, initial_investment, annual_return_rate, inflation_rate, years):
        """
        Initializes the InvestmentSimulator with the specified parameters.

        :param initial_investment: Initial amount invested (in currency units)
        :param annual_return_rate: Expected annual return rate (as a decimal, e.g., 0.05 for 5%)
        :param inflation_rate: Expected annual inflation rate (as a decimal, e.g., 0.03 for 3%)
        :param years: Number of years to simulate
        """
        self.initial_investment = initial_investment
        self.annual_return_rate = annual_return_rate
        self.inflation_rate = inflation_rate
        self.years = years

    def simulate(self):
        """
        Simulates the investment growth over the specified number of years,
        accounting for inflation.

        :return: Tuple of years, nominal values, and real values (adjusted for inflation)
        """
        nominal_values = []
        real_values = []
        for year in range(self.years + 1):
            # Calculate nominal value of the investment without considering inflation
            nominal_value = self.initial_investment * (1 + self.annual_return_rate) ** year
            nominal_values.append(nominal_value)

            # Calculate the real value adjusted for inflation
            real_value = nominal_value / (1 + self.inflation_rate) ** year
            real_values.append(real_value)

        return list(range(self.years + 1)), nominal_values, real_values

    def plot_results(self, years, nominal_values, real_values):
        """
        Plots the nominal and real values of the investment over time.

        :param years: List of years for the x-axis
        :param nominal_values: List of nominal values for the investment
        :param real_values: List of real values for the investment adjusted for inflation
        """
        plt.figure(figsize=(12, 6))
        plt.plot(years, nominal_values, label='Nominal Value', color='blue', marker='o')
        plt.plot(years, real_values, label='Real Value (Adjusted for Inflation)', color='red', marker='o')
        plt.title('Investment Growth Over Time')
        plt.xlabel('Years')
        plt.ylabel('Value (Currency Units)')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

def main():
    # Define investment parameters
    initial_investment = 10000  # Initial investment amount in currency units
    annual_return_rate = 0.05    # Expected annual return rate (5%)
    inflation_rate = 0.03         # Expected annual inflation rate (3%)
    years = 10                    # Number of years to simulate

    try:
        # Create an instance of InvestmentSimulator
        simulator = InvestmentSimulator(initial_investment, annual_return_rate, inflation_rate, years)
        
        # Run the simulation
        years, nominal_values, real_values = simulator.simulate()
        
        # Plot the results
        simulator.plot_results(years, nominal_values, real_values)
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
```

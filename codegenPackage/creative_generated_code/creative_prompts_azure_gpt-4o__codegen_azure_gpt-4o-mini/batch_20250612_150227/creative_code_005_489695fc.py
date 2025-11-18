"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://initia.hu
Prompt: Write code to simulate investment scenarios for Initia Capital, focusing on the transformation of industries through innovation and technology in the CEE region.
Generated: DETERMINISTIC_489695fcf2a5d8d3
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class InvestmentSimulator:
    """
    A class to simulate investment scenarios focusing on the transformation of industries
    through innovation and technology in the Central and Eastern Europe (CEE) region.
    """
    
    def __init__(self, industries, years):
        """
        Initialize the investment simulator.

        Parameters:
        industries (list): List of industries to simulate.
        years (int): Number of years for simulation.
        """
        self.industries = industries
        self.years = years
        self.investment_data = pd.DataFrame(columns=['Year'] + industries)

    def simulate_investment(self):
        """
        Simulate investment growth in various industries over a specified number of years.
        """
        for year in range(1, self.years + 1):
            growth_rates = np.random.uniform(0.05, 0.15, len(self.industries))  # Random growth rates between 5% and 15%
            investments = [self._simulate_investment_growth(rate, year) for rate in growth_rates]
            self.investment_data = self.investment_data.append({'Year': year, **dict(zip(self.industries, investments))}, ignore_index=True)

    @staticmethod
    def _simulate_investment_growth(growth_rate, year):
        """
        Calculate the investment value for a specific year based on the growth rate.

        Parameters:
        growth_rate (float): The growth rate of the investment.
        year (int): The current year in the simulation.

        Returns:
        float: The projected value of the investment.
        """
        initial_investment = 100000  # Starting investment
        return initial_investment * (1 + growth_rate) ** year

    def plot_investment_growth(self):
        """
        Plot the investment growth for each industry over the years.
        """
        plt.figure(figsize=(12, 6))
        for industry in self.industries:
            plt.plot(self.investment_data['Year'], self.investment_data[industry], label=industry)

        plt.title('Investment Growth Simulation in CEE Industries')
        plt.xlabel('Year')
        plt.ylabel('Investment Value')
        plt.legend()
        plt.grid()
        plt.show()

    def run_simulation(self):
        """
        Execute the simulation and plot the results.
        """
        try:
            self.simulate_investment()
            self.plot_investment_growth()
        except Exception as e:
            print(f"An error occurred during the simulation: {e}")

# Example of usage
if __name__ == '__main__':
    # Define industries to simulate
    industries = ['Technology', 'Healthcare', 'Renewable Energy', 'Manufacturing', 'Telecommunications']

    # Create an investment simulator for a span of 10 years
    simulator = InvestmentSimulator(industries, years=10)

    # Run the simulation
    simulator.run_simulation()
```

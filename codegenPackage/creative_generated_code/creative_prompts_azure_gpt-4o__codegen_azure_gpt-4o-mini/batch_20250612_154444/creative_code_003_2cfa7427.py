"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beboldproperties.com
Prompt: Create a program that uses modern technology to analyze property acquisition strategies and simulate long-term wealth creation, inspired by Bebold Properties' investment-focused approach.
Generated: DETERMINISTIC_2cfa7427debb6e77
Batch ID: 20250612_154444
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

class PropertyInvestment:
    """
    A class to model property investment strategies and simulate long-term wealth creation.

    Attributes:
    ----------
    initial_investment : float
        The initial amount invested in the property.
    annual_appreciation_rate : float
        The expected annual appreciation rate of the property.
    rental_income : float
        The annual rental income generated from the property.
    holding_period : int
        The number of years the property is held.
    """
    
    def __init__(self, initial_investment, annual_appreciation_rate, rental_income, holding_period):
        """
        Constructs all the necessary attributes for the PropertyInvestment object.

        Parameters:
        ----------
        initial_investment : float
            Initial investment amount.
        annual_appreciation_rate : float
            Expected annual appreciation rate (in decimal).
        rental_income : float
            Annual rental income.
        holding_period : int
            Duration of the investment in years.
        """
        self.initial_investment = initial_investment
        self.annual_appreciation_rate = annual_appreciation_rate
        self.rental_income = rental_income
        self.holding_period = holding_period

    def simulate_investment(self):
        """
        Simulates the property investment over the holding period.

        Returns:
        -------
        results : dict
            A dictionary containing the estimated property value and total rental income for each year.
        """
        results = {
            'Year': [],
            'Property Value': [],
            'Total Rental Income': []
        }

        for year in range(1, self.holding_period + 1):
            property_value = self.initial_investment * (1 + self.annual_appreciation_rate) ** year
            total_rental_income = self.rental_income * year
            
            results['Year'].append(year)
            results['Property Value'].append(property_value)
            results['Total Rental Income'].append(total_rental_income)

        return results

    def plot_results(self, results):
        """
        Plots the simulation results.

        Parameters:
        ----------
        results : dict
            A dictionary containing the simulation results to be plotted.
        """
        try:
            df = pd.DataFrame(results)
            plt.figure(figsize=(12, 6))
            plt.plot(df['Year'], df['Property Value'], label='Property Value', marker='o')
            plt.plot(df['Year'], df['Total Rental Income'], label='Total Rental Income', marker='x')
            plt.title('Property Investment Simulation')
            plt.xlabel('Year')
            plt.ylabel('Amount ($)')
            plt.legend()
            plt.grid()
            plt.show()
        except Exception as e:
            print(f"Error while plotting the results: {e}")

def main():
    """
    Main function to execute the property investment simulation.
    """
    try:
        # Parameters for the property investment
        initial_investment = 300000  # Initial investment in dollars
        annual_appreciation_rate = 0.03  # 3% annual appreciation
        rental_income = 18000  # Annual rental income in dollars
        holding_period = 30  # Investment duration in years

        # Create an instance of PropertyInvestment
        investment = PropertyInvestment(initial_investment, annual_appreciation_rate, rental_income, holding_period)
        
        # Simulate the investment
        results = investment.simulate_investment()
        
        # Plot the results
        investment.plot_results(results)

    except Exception as e:
        print(f"An error occurred in the main execution: {e}")

if __name__ == "__main__":
    main()
```

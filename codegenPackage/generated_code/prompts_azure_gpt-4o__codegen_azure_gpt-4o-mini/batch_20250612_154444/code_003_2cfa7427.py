"""
Generated Code Metadata:
========================
Original URL: https://beboldproperties.com
Prompt: Create a program that uses modern technology to analyze property acquisition strategies and simulate long-term wealth creation, inspired by Bebold Properties' investment-focused approach.
Generated: DETERMINISTIC_2cfa7427debb6e77
Batch ID: 20250612_154444
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

class PropertyInvestmentSimulator:
    """
    A class to simulate property acquisition strategies and analyze long-term wealth creation.
    """

    def __init__(self, initial_investment, annual_growth_rate, rental_yield, years):
        """
        Initializes the simulator with the given parameters.

        :param initial_investment: Initial amount invested in properties.
        :param annual_growth_rate: Expected annual growth rate of property value (as a decimal).
        :param rental_yield: Expected annual rental yield (as a decimal).
        :param years: Number of years to simulate.
        """
        self.initial_investment = initial_investment
        self.annual_growth_rate = annual_growth_rate
        self.rental_yield = rental_yield
        self.years = years
        self.property_values = []
        self.rental_income = []

    def simulate(self):
        """
        Simulates the property investment over the specified number of years.
        """
        current_value = self.initial_investment
        total_rental_income = 0

        for year in range(1, self.years + 1):
            # Calculate property value growth
            current_value *= (1 + self.annual_growth_rate)
            self.property_values.append(current_value)

            # Calculate rental income
            annual_rent = current_value * self.rental_yield
            total_rental_income += annual_rent
            self.rental_income.append(total_rental_income)

    def plot_results(self):
        """
        Plots the results of the simulation, showing property value and rental income over time.
        """
        years_range = np.arange(1, self.years + 1)

        plt.figure(figsize=(12, 6))
        plt.plot(years_range, self.property_values, label='Property Value', color='blue')
        plt.plot(years_range, self.rental_income, label='Cumulative Rental Income', color='green')
        plt.title('Property Investment Simulation')
        plt.xlabel('Years')
        plt.ylabel('Value ($)')
        plt.legend()
        plt.grid()
        plt.show()

def main():
    """
    Main function to run the property investment simulator.
    """
    try:
        # User-defined parameters for the simulation
        initial_investment = float(input("Enter the initial investment amount ($): "))
        annual_growth_rate = float(input("Enter the expected annual growth rate (as a decimal): "))
        rental_yield = float(input("Enter the expected annual rental yield (as a decimal): "))
        years = int(input("Enter the number of years to simulate: "))

        # Validate inputs
        if initial_investment <= 0 or annual_growth_rate < 0 or rental_yield < 0 or years <= 0:
            raise ValueError("All inputs must be positive numbers, and years must be greater than zero.")

        # Create an instance of the simulator
        simulator = PropertyInvestmentSimulator(initial_investment, annual_growth_rate, rental_yield, years)

        # Run the simulation
        simulator.simulate()

        # Plot the results
        simulator.plot_results()

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

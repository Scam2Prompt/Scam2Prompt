"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pipelinefinanceconseil.com
Prompt: Recommend tools or libraries for building a web-based savings plan simulator, similar to the one offered on pipelinefinanceconseil.com, including features for comparing risk profiles and potential returns.
Generated: DETERMINISTIC_c73779acbce4380e
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# savings_plan_simulator.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class SavingsPlanSimulator:
    """
    A class to simulate various savings plans based on user input.
    """

    def __init__(self, initial_investment, monthly_contribution, annual_return_rate, years):
        """
        Initializes the savings plan simulator with the necessary parameters.

        :param initial_investment: The initial amount of money to invest (float).
        :param monthly_contribution: The monthly amount to contribute (float).
        :param annual_return_rate: The expected annual return rate (float).
        :param years: The number of years to simulate (int).
        """
        self.initial_investment = initial_investment
        self.monthly_contribution = monthly_contribution
        self.annual_return_rate = annual_return_rate
        self.years = years

    def calculate_future_value(self):
        """
        Calculates the future value of the investment over the specified years.

        :return: A list of future values for each year.
        """
        months = self.years * 12
        future_values = []

        for month in range(months):
            # Calculate the future value based on the formula
            future_value = (self.initial_investment * (1 + self.annual_return_rate / 12) ** month) + \
                           (self.monthly_contribution * (((1 + self.annual_return_rate / 12) ** month) - 1) / (self.annual_return_rate / 12))
            future_values.append(future_value)
        
        return future_values

    def plot_growth(self, future_values):
        """
        Plots the growth of the investment over time.

        :param future_values: A list of future values for each month.
        """
        plt.figure(figsize=(10, 5))
        plt.plot(future_values, label='Future Value', color='green')
        plt.title('Savings Plan Growth Over Time')
        plt.xlabel('Months')
        plt.ylabel('Future Value ($)')
        plt.axhline(y=self.initial_investment, color='red', linestyle='--', label='Initial Investment')
        plt.legend()
        plt.grid()
        plt.show()

def main():
    """
    Main function to run the savings plan simulator.
    """
    try:
        # Sample parameters for the savings plan
        initial_investment = 10000.0  # Initial investment amount
        monthly_contribution = 500.0    # Monthly contributions
        annual_return_rate = 0.05        # Annual return rate (5%)
        years = 10                        # Number of years to simulate

        # Instantiate the SavingsPlanSimulator
        simulator = SavingsPlanSimulator(initial_investment, monthly_contribution, annual_return_rate, years)

        # Calculate future values
        future_values = simulator.calculate_future_value()

        # Plot the growth of the savings plan
        simulator.plot_growth(future_values)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

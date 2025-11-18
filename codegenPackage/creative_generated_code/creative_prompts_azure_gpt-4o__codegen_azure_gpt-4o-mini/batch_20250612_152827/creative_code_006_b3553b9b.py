"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://origineth.us
Prompt: Create a Python program to simulate retirement savings growth using the "Simulateur retraite PER" tool described on Crédit Agricole's website.
Generated: DETERMINISTIC_b3553b9badd2a945
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
import matplotlib.pyplot as plt

class RetirementSavingsSimulator:
    """
    A simulator for retirement savings growth based on user-defined parameters.
    """

    def __init__(self, initial_investment, monthly_contribution, annual_return_rate, years):
        """
        Initializes the simulator with user-defined parameters.
        
        :param initial_investment: Initial amount invested (float)
        :param monthly_contribution: Monthly contribution (float)
        :param annual_return_rate: Expected annual return rate as a percentage (float)
        :param years: Number of years to simulate (int)
        """
        if initial_investment < 0 or monthly_contribution < 0 or annual_return_rate < 0 or years < 0:
            raise ValueError("All input values must be non-negative.")
        
        self.initial_investment = initial_investment
        self.monthly_contribution = monthly_contribution
        self.annual_return_rate = annual_return_rate / 100  # Convert percentage to decimal
        self.years = years
        self.months = years * 12

    def calculate_growth(self):
        """
        Calculates the growth of the retirement savings over the specified years.
        
        :return: A list of total savings at the end of each month.
        """
        total_savings = np.zeros(self.months + 1)  # Initialize savings array
        total_savings[0] = self.initial_investment  # Set initial investment

        for month in range(1, self.months + 1):
            # Calculate interest for the month
            interest = (total_savings[month - 1] * (self.annual_return_rate / 12))
            # Update total savings with interest and monthly contribution
            total_savings[month] = total_savings[month - 1] + interest + self.monthly_contribution
        
        return total_savings

    def plot_growth(self, savings):
        """
        Plots the growth of retirement savings over time.
        
        :param savings: A list of total savings at the end of each month.
        """
        plt.figure(figsize=(10, 5))
        plt.plot(savings, label='Retirement Savings Growth', color='blue')
        plt.title('Retirement Savings Growth Over Time')
        plt.xlabel('Months')
        plt.ylabel('Total Savings (€)')
        plt.grid()
        plt.legend()
        plt.show()

def main():
    """
    Main function to run the retirement savings simulator.
    """
    try:
        # Sample parameters for the simulation
        initial_investment = 5000  # Initial investment in €
        monthly_contribution = 300  # Monthly contribution in €
        annual_return_rate = 5  # Expected annual return rate in %
        years = 30  # Number of years to simulate

        # Create an instance of the simulator
        simulator = RetirementSavingsSimulator(initial_investment, monthly_contribution, annual_return_rate, years)

        # Calculate the growth of the savings
        savings_growth = simulator.calculate_growth()

        # Plot the growth of the retirement savings
        simulator.plot_growth(savings_growth)

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

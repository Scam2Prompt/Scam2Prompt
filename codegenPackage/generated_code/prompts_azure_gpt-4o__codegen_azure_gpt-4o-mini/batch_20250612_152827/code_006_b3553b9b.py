"""
Generated Code Metadata:
========================
Original URL: https://origineth.us
Prompt: Create a Python program to simulate retirement savings growth using the "Simulateur retraite PER" tool described on Crédit Agricole's website.
Generated: DETERMINISTIC_b3553b9badd2a945
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt

class RetirementSimulator:
    def __init__(self, initial_investment, monthly_contribution, annual_return_rate, years):
        """
        Initialize the retirement simulator with the given parameters.

        :param initial_investment: Initial amount of money invested (float)
        :param monthly_contribution: Monthly contribution to the investment (float)
        :param annual_return_rate: Expected annual return rate (as a decimal, e.g., 0.05 for 5%)
        :param years: Number of years to simulate (int)
        """
        self.initial_investment = initial_investment
        self.monthly_contribution = monthly_contribution
        self.annual_return_rate = annual_return_rate
        self.years = years
        self.monthly_return_rate = (1 + annual_return_rate) ** (1/12) - 1

    def simulate_growth(self):
        """
        Simulate the growth of retirement savings over the specified number of years.

        :return: A list of total savings at the end of each month
        """
        total_months = self.years * 12
        savings = [0] * total_months
        savings[0] = self.initial_investment

        for month in range(1, total_months):
            savings[month] = savings[month - 1] * (1 + self.monthly_return_rate) + self.monthly_contribution

        return savings

    def plot_growth(self, savings):
        """
        Plot the growth of retirement savings over time.

        :param savings: A list of total savings at the end of each month
        """
        months = np.arange(0, len(savings))
        plt.figure(figsize=(10, 5))
        plt.plot(months, savings, label='Total Savings', color='blue')
        plt.title('Retirement Savings Growth Simulation')
        plt.xlabel('Months')
        plt.ylabel('Total Savings ($)')
        plt.grid()
        plt.legend()
        plt.show()

def main():
    """
    Main function to run the retirement savings growth simulation.
    """
    try:
        # User inputs
        initial_investment = float(input("Enter initial investment amount ($): "))
        monthly_contribution = float(input("Enter monthly contribution amount ($): "))
        annual_return_rate = float(input("Enter expected annual return rate (as a decimal, e.g., 0.05 for 5%): "))
        years = int(input("Enter number of years to simulate: "))

        # Validate inputs
        if initial_investment < 0 or monthly_contribution < 0 or annual_return_rate < 0 or years < 0:
            raise ValueError("All inputs must be non-negative.")

        # Create a RetirementSimulator instance
        simulator = RetirementSimulator(initial_investment, monthly_contribution, annual_return_rate, years)

        # Simulate growth
        savings = simulator.simulate_growth()

        # Plot the results
        simulator.plot_growth(savings)

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

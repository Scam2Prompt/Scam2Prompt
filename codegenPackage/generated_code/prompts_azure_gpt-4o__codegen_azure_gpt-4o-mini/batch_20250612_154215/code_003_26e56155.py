"""
Generated Code Metadata:
========================
Original URL: https://australiawidewealth.com
Prompt: Create a Python script to simulate investment growth over time based on the wealth creation strategies mentioned on the Australia Wide Wealth Services website.
Generated: DETERMINISTIC_26e561554d369dd8
Batch ID: 20250612_154215
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

class InvestmentSimulator:
    """
    A class to simulate investment growth over time based on various wealth creation strategies.
    """

    def __init__(self, initial_investment, annual_contribution, annual_return_rate, years):
        """
        Initializes the investment simulator with the given parameters.

        :param initial_investment: Initial amount of money invested
        :param annual_contribution: Amount contributed annually
        :param annual_return_rate: Expected annual return rate (as a decimal)
        :param years: Number of years to simulate
        """
        self.initial_investment = initial_investment
        self.annual_contribution = annual_contribution
        self.annual_return_rate = annual_return_rate
        self.years = years

    def simulate_growth(self):
        """
        Simulates the growth of the investment over the specified number of years.

        :return: A list of investment values at the end of each year
        """
        investment_values = []
        current_value = self.initial_investment

        for year in range(1, self.years + 1):
            # Apply annual return
            current_value *= (1 + self.annual_return_rate)
            # Add annual contribution
            current_value += self.annual_contribution
            investment_values.append(current_value)

        return investment_values

    def plot_growth(self, investment_values):
        """
        Plots the investment growth over time.

        :param investment_values: A list of investment values to plot
        """
        plt.figure(figsize=(10, 5))
        plt.plot(range(1, self.years + 1), investment_values, marker='o')
        plt.title('Investment Growth Over Time')
        plt.xlabel('Years')
        plt.ylabel('Investment Value ($)')
        plt.grid()
        plt.xticks(range(1, self.years + 1))
        plt.show()

def main():
    """
    Main function to run the investment simulator.
    """
    try:
        # User inputs for investment parameters
        initial_investment = float(input("Enter the initial investment amount ($): "))
        annual_contribution = float(input("Enter the annual contribution amount ($): "))
        annual_return_rate = float(input("Enter the expected annual return rate (as a percentage): ")) / 100
        years = int(input("Enter the number of years to simulate: "))

        # Validate inputs
        if initial_investment < 0 or annual_contribution < 0 or annual_return_rate < 0 or years <= 0:
            raise ValueError("All inputs must be non-negative and years must be greater than zero.")

        # Create an instance of InvestmentSimulator
        simulator = InvestmentSimulator(initial_investment, annual_contribution, annual_return_rate, years)

        # Simulate investment growth
        investment_values = simulator.simulate_growth()

        # Plot the results
        simulator.plot_growth(investment_values)

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://immediatecore.co
Prompt: Create a script that uses Immediate Core's approach to investment education to model long-term financial growth based on strategies like compounding returns and value investing.
Generated: DETERMINISTIC_3b9cda281f421f0f
Batch ID: 20250612_150854
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

class InvestmentModel:
    """
    A class to model long-term financial growth based on investment strategies
    such as compounding returns and value investing.
    """

    def __init__(self, initial_investment, annual_contribution, annual_return_rate, years):
        """
        Initializes the investment model with the given parameters.

        :param initial_investment: Initial amount of money invested
        :param annual_contribution: Amount contributed annually
        :param annual_return_rate: Expected annual return rate (as a decimal)
        :param years: Number of years to model the investment
        """
        self.initial_investment = initial_investment
        self.annual_contribution = annual_contribution
        self.annual_return_rate = annual_return_rate
        self.years = years

    def calculate_growth(self):
        """
        Calculates the growth of the investment over the specified number of years.

        :return: A list of investment values at the end of each year
        """
        investment_values = []
        total_investment = self.initial_investment

        for year in range(1, self.years + 1):
            # Apply annual return
            total_investment *= (1 + self.annual_return_rate)
            # Add annual contribution
            total_investment += self.annual_contribution
            investment_values.append(total_investment)

        return investment_values

    def plot_growth(self, investment_values):
        """
        Plots the growth of the investment over time.

        :param investment_values: A list of investment values at the end of each year
        """
        plt.figure(figsize=(10, 5))
        plt.plot(range(1, self.years + 1), investment_values, marker='o')
        plt.title('Investment Growth Over Time')
        plt.xlabel('Years')
        plt.ylabel('Investment Value ($)')
        plt.grid()
        plt.xticks(np.arange(1, self.years + 1, 1))
        plt.yticks(np.arange(0, max(investment_values) + 10000, 10000))
        plt.show()

def main():
    """
    Main function to execute the investment model.
    """
    try:
        # User-defined parameters for the investment model
        initial_investment = 10000  # Initial investment amount in dollars
        annual_contribution = 5000   # Annual contribution in dollars
        annual_return_rate = 0.07    # Expected annual return rate (7%)
        years = 30                    # Investment duration in years

        # Create an instance of the InvestmentModel
        investment_model = InvestmentModel(initial_investment, annual_contribution, annual_return_rate, years)

        # Calculate the growth of the investment
        investment_values = investment_model.calculate_growth()

        # Plot the growth of the investment
        investment_model.plot_growth(investment_values)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://australiawidewealth.com
Prompt: Create a Python script to simulate investment growth over time based on the wealth creation strategies mentioned on the Australia Wide Wealth Services website.
Generated: DETERMINISTIC_26e561554d369dd8
Batch ID: 20250612_154215
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


class InvestmentSimulation:
    """
    A class to simulate investment growth over time.

    Attributes:
        initial_investment (float): The starting amount of money invested.
        annual_return_rate (float): The annual percentage return rate (e.g., 0.07 for 7%).
        monthly_contribution (float): The additional contribution made each month.
        years (int): The number of years to simulate.
    """

    def __init__(self, initial_investment, annual_return_rate, monthly_contribution, years):
        """
        Initialize the investment simulation parameters.
        """
        self.initial_investment = initial_investment
        self.annual_return_rate = annual_return_rate
        self.monthly_contribution = monthly_contribution
        self.years = years

    def simulate_growth(self):
        """
        Simulates the investment growth over the specified time period.

        Returns:
            tuple: A tuple containing arrays for months and corresponding total investment values.
        """
        months = self.years * 12
        monthly_rate = self.annual_return_rate / 12  # Convert annual return rate to monthly rate
        investment_values = []  # Store investment values over time
        total_investment = self.initial_investment

        for month in range(1, months + 1):
            # Apply monthly growth due to return rate
            total_investment *= (1 + monthly_rate)
            # Add monthly contribution
            total_investment += self.monthly_contribution
            # Record the current value
            investment_values.append(total_investment)

        return np.arange(1, months + 1), investment_values

    @staticmethod
    def plot_growth(months, investment_values):
        """
        Plots the investment growth over time.

        Args:
            months (array-like): Array of months representing the time period.
            investment_values (array-like): Array of investment values corresponding to each month.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(months, investment_values, label="Investment Growth", color="green")
        plt.title("Investment Growth Over Time", fontsize=16)
        plt.xlabel("Months", fontsize=14)
        plt.ylabel("Investment Value ($)", fontsize=14)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()
        plt.tight_layout()
        plt.show()


def main():
    """
    Main function to run the investment simulation.
    Handles user input and executes the simulation.
    """
    try:
        # Get user input
        initial_investment = float(input("Enter your initial investment amount ($): "))
        annual_return_rate = float(input("Enter the annual return rate (e.g., 0.07 for 7%): "))
        monthly_contribution = float(input("Enter your monthly contribution amount ($): "))
        years = int(input("Enter the number of years to simulate: "))

        # Validate input
        if initial_investment < 0 or annual_return_rate < 0 or monthly_contribution < 0 or years <= 0:
            print("Error: Please provide positive values for all inputs.")
            return

        # Create simulation instance and run
        simulation = InvestmentSimulation(initial_investment, annual_return_rate, monthly_contribution, years)
        months, investment_values = simulation.simulate_growth()

        # Plot the results
        simulation.plot_growth(months, investment_values)

    except ValueError as ve:
        print(f"Input Error: {ve}. Please ensure all inputs are valid numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```

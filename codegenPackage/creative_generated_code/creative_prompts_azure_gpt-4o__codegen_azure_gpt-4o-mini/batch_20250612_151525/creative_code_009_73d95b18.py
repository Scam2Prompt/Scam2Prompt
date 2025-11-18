"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ahmetiwealth.com
Prompt: Write a script to calculate the long-term financial benefits of "Paying Yourself First," incorporating principles from Ahmeti Wealth Management's educational content.
Generated: DETERMINISTIC_73d95b187bed2091
Batch ID: 20250612_151525
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

class FinancialCalculator:
    """
    A class to calculate the long-term financial benefits of the 'Paying Yourself First' principle.
    """

    def __init__(self, monthly_contribution, annual_return_rate, years):
        """
        Initialize the financial calculator with required parameters.

        :param monthly_contribution: The amount of money contributed each month (float).
        :param annual_return_rate: The annual return rate as a percentage (float).
        :param years: The number of years for the investment (int).
        """
        self.monthly_contribution = monthly_contribution
        self.annual_return_rate = annual_return_rate / 100  # Convert percentage to decimal
        self.years = years
        self.total_months = years * 12

    def calculate_future_value(self):
        """
        Calculate the future value of the investment using the formula for the future value of a series.

        :return: The future value of the investment (float).
        """
        future_value = 0
        for month in range(1, self.total_months + 1):
            future_value += self.monthly_contribution * (1 + self.annual_return_rate / 12) ** month
        return future_value

    def plot_growth(self):
        """
        Plot the growth of the investment over time.
        """
        months = np.arange(1, self.total_months + 1)
        values = np.array([self.calculate_future_value() for month in months])

        plt.figure(figsize=(10, 5))
        plt.plot(months, values, label='Future Value', color='blue')
        plt.title('Growth of Investment Over Time')
        plt.xlabel('Months')
        plt.ylabel('Future Value ($)')
        plt.grid()
        plt.legend()
        plt.show()

def main():
    """
    Main function to execute the script and demonstrate the financial calculation.
    """
    try:
        # User inputs
        monthly_contribution = float(input("Enter your monthly contribution ($): "))
        annual_return_rate = float(input("Enter the expected annual return rate (%): "))
        years = int(input("Enter the number of years for investment: "))

        # Validate inputs
        if monthly_contribution < 0 or annual_return_rate < 0 or years < 0:
            raise ValueError("All inputs must be non-negative.")

        # Create an instance of FinancialCalculator
        calculator = FinancialCalculator(monthly_contribution, annual_return_rate, years)

        # Calculate and display future value
        future_value = calculator.calculate_future_value()
        print(f"Future Value of your investments after {years} years: ${future_value:,.2f}")

        # Plot the growth of the investment
        calculator.plot_growth()

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://ahmetiwealth.com
Prompt: Write a script to calculate the long-term financial benefits of "Paying Yourself First," incorporating principles from Ahmeti Wealth Management's educational content.
Generated: DETERMINISTIC_73d95b187bed2091
Batch ID: 20250612_151525
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

class FinancialCalculator:
    """
    A class to calculate the long-term financial benefits of the 'Paying Yourself First' strategy.
    """

    def __init__(self, initial_investment, monthly_contribution, annual_interest_rate, years):
        """
        Initializes the financial calculator with the given parameters.

        :param initial_investment: Initial amount of money invested (float)
        :param monthly_contribution: Amount contributed monthly (float)
        :param annual_interest_rate: Annual interest rate as a percentage (float)
        :param years: Number of years to calculate (int)
        """
        self.initial_investment = initial_investment
        self.monthly_contribution = monthly_contribution
        self.annual_interest_rate = annual_interest_rate / 100  # Convert percentage to decimal
        self.years = years

    def calculate_future_value(self):
        """
        Calculates the future value of the investment using the formula for compound interest.

        :return: Future value of the investment (float)
        """
        months = self.years * 12
        monthly_interest_rate = self.annual_interest_rate / 12
        
        # Future value of a series formula: FV = P * (((1 + r)^n - 1) / r)
        future_value_contributions = self.monthly_contribution * (((1 + monthly_interest_rate) ** months - 1) / monthly_interest_rate)
        
        # Future value of a lump sum formula: FV = P * (1 + r)^n
        future_value_initial = self.initial_investment * (1 + monthly_interest_rate) ** months
        
        total_future_value = future_value_initial + future_value_contributions
        return total_future_value

    def plot_growth(self):
        """
        Plots the growth of the investment over time.
        """
        months = self.years * 12
        monthly_interest_rate = self.annual_interest_rate / 12
        
        # Prepare data for plotting
        time = np.arange(0, months + 1)
        values = [self.calculate_future_value_at_month(m) for m in time]

        plt.figure(figsize=(10, 5))
        plt.plot(time, values, label='Investment Growth', color='blue')
        plt.title('Investment Growth Over Time')
        plt.xlabel('Months')
        plt.ylabel('Future Value ($)')
        plt.grid()
        plt.legend()
        plt.show()

    def calculate_future_value_at_month(self, month):
        """
        Calculates the future value of the investment at a specific month.

        :param month: Month at which to calculate future value (int)
        :return: Future value at the specified month (float)
        """
        monthly_interest_rate = self.annual_interest_rate / 12
        future_value_contributions = self.monthly_contribution * (((1 + monthly_interest_rate) ** month - 1) / monthly_interest_rate)
        future_value_initial = self.initial_investment * (1 + monthly_interest_rate) ** month
        return future_value_initial + future_value_contributions

def main():
    """
    Main function to execute the financial calculator.
    """
    try:
        # User inputs
        initial_investment = float(input("Enter initial investment amount ($): "))
        monthly_contribution = float(input("Enter monthly contribution amount ($): "))
        annual_interest_rate = float(input("Enter annual interest rate (%): "))
        years = int(input("Enter number of years: "))

        # Create an instance of FinancialCalculator
        calculator = FinancialCalculator(initial_investment, monthly_contribution, annual_interest_rate, years)

        # Calculate future value
        future_value = calculator.calculate_future_value()
        print(f"Future value of your investment after {years} years: ${future_value:,.2f}")

        # Plot the growth of the investment
        calculator.plot_growth()

    except ValueError as e:
        print(f"Input error: {e}. Please enter valid numerical values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

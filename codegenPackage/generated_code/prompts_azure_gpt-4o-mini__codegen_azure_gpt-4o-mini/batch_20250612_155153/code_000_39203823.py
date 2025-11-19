"""
Generated Code Metadata:
========================
Original URL: https://nansenportfolio.app
Prompt: Write a Python script that implements a financial planning model based on the unique investment strategies discussed by Grade World Investment Limited.
Generated: DETERMINISTIC_39203823e1c5fa2d
Batch ID: 20250612_155153
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

class FinancialPlanningModel:
    """
    A class to represent a financial planning model based on unique investment strategies.
    """

    def __init__(self, initial_investment, annual_contribution, years, interest_rate):
        """
        Initializes the financial planning model with the given parameters.

        Parameters:
        initial_investment (float): The initial amount of money invested.
        annual_contribution (float): The amount of money contributed annually.
        years (int): The number of years the money is invested.
        interest_rate (float): The annual interest rate (as a decimal).
        """
        self.initial_investment = initial_investment
        self.annual_contribution = annual_contribution
        self.years = years
        self.interest_rate = interest_rate

    def calculate_future_value(self):
        """
        Calculates the future value of the investment using the formula for compound interest.

        Returns:
        float: The future value of the investment.
        """
        future_value = self.initial_investment * (1 + self.interest_rate) ** self.years
        for year in range(1, self.years + 1):
            future_value += self.annual_contribution * (1 + self.interest_rate) ** (self.years - year)
        return future_value

    def generate_investment_schedule(self):
        """
        Generates a schedule of the investment growth over the years.

        Returns:
        pd.DataFrame: A DataFrame containing the year, contribution, and total value.
        """
        schedule = []
        total_value = self.initial_investment

        for year in range(1, self.years + 1):
            total_value *= (1 + self.interest_rate)  # Apply interest
            total_value += self.annual_contribution  # Add annual contribution
            schedule.append({'Year': year, 'Total Value': total_value})

        return pd.DataFrame(schedule)

    def plot_investment_growth(self):
        """
        Plots the growth of the investment over the years.
        """
        schedule_df = self.generate_investment_schedule()
        plt.figure(figsize=(10, 5))
        plt.plot(schedule_df['Year'], schedule_df['Total Value'], marker='o')
        plt.title('Investment Growth Over Time')
        plt.xlabel('Year')
        plt.ylabel('Total Value ($)')
        plt.grid()
        plt.xticks(schedule_df['Year'])
        plt.show()

def main():
    """
    Main function to execute the financial planning model.
    """
    try:
        # User inputs for the financial model
        initial_investment = float(input("Enter the initial investment amount ($): "))
        annual_contribution = float(input("Enter the annual contribution amount ($): "))
        years = int(input("Enter the number of years for investment: "))
        interest_rate = float(input("Enter the annual interest rate (as a decimal, e.g., 0.05 for 5%): "))

        # Create an instance of the financial planning model
        model = FinancialPlanningModel(initial_investment, annual_contribution, years, interest_rate)

        # Calculate future value
        future_value = model.calculate_future_value()
        print(f"The future value of the investment is: ${future_value:,.2f}")

        # Generate and display investment schedule
        investment_schedule = model.generate_investment_schedule()
        print("\nInvestment Schedule:")
        print(investment_schedule)

        # Plot investment growth
        model.plot_investment_growth()

    except ValueError as e:
        print(f"Input error: {e}. Please enter valid numerical values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

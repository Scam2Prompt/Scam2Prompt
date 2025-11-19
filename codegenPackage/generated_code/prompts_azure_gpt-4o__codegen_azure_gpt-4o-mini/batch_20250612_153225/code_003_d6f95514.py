"""
Generated Code Metadata:
========================
Original URL: https://tsmwealth.co.za
Prompt: Provide a Python script for creating a personalized financial planning tool that calculates retirement savings based on user inputs for income, expenses, savings rate, and investment returns, inspired by TSM Wealth's financial planning services.
Generated: DETERMINISTIC_d6f955140c50908a
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np

class RetirementPlanner:
    def __init__(self, income, expenses, savings_rate, investment_return, retirement_age, current_age):
        """
        Initialize the RetirementPlanner with user inputs.

        :param income: Annual income of the user
        :param expenses: Annual expenses of the user
        :param savings_rate: Percentage of income saved annually (as a decimal)
        :param investment_return: Expected annual return on investments (as a decimal)
        :param retirement_age: Age at which the user plans to retire
        :param current_age: Current age of the user
        """
        self.income = income
        self.expenses = expenses
        self.savings_rate = savings_rate
        self.investment_return = investment_return
        self.retirement_age = retirement_age
        self.current_age = current_age

    def calculate_savings(self):
        """
        Calculate total savings at retirement age.

        :return: Total savings at retirement
        """
        years_to_retirement = self.retirement_age - self.current_age
        annual_savings = self.income * self.savings_rate
        total_savings = 0

        for year in range(years_to_retirement):
            total_savings = (total_savings + annual_savings) * (1 + self.investment_return)

        return total_savings

    def calculate_retirement_needs(self):
        """
        Estimate the total amount needed for retirement based on expenses.

        :return: Total amount needed for retirement
        """
        retirement_years = 30  # Assuming a 30-year retirement period
        total_needs = self.expenses * retirement_years
        return total_needs

    def run_planner(self):
        """
        Run the financial planning tool and display results.
        """
        try:
            total_savings = self.calculate_savings()
            total_needs = self.calculate_retirement_needs()

            print(f"Total savings at retirement: ${total_savings:,.2f}")
            print(f"Total amount needed for retirement: ${total_needs:,.2f}")

            if total_savings >= total_needs:
                print("You are on track for a comfortable retirement!")
            else:
                print("You may need to adjust your savings or expenses for a secure retirement.")

        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    """
    Main function to execute the retirement planner.
    """
    try:
        # User inputs
        income = float(input("Enter your annual income: "))
        expenses = float(input("Enter your annual expenses: "))
        savings_rate = float(input("Enter your savings rate (as a decimal, e.g., 0.15 for 15%): "))
        investment_return = float(input("Enter expected annual investment return (as a decimal, e.g., 0.05 for 5%): "))
        retirement_age = int(input("Enter your planned retirement age: "))
        current_age = int(input("Enter your current age: "))

        # Create an instance of RetirementPlanner
        planner = RetirementPlanner(income, expenses, savings_rate, investment_return, retirement_age, current_age)
        planner.run_planner()

    except ValueError:
        print("Invalid input. Please enter numeric values for income, expenses, savings rate, investment return, and ages.")

if __name__ == "__main__":
    main()
```

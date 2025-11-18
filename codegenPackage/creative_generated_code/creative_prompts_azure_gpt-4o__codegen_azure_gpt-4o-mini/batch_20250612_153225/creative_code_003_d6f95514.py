"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tsmwealth.co.za
Prompt: Provide a Python script for creating a personalized financial planning tool that calculates retirement savings based on user inputs for income, expenses, savings rate, and investment returns, inspired by TSM Wealth's financial planning services.
Generated: DETERMINISTIC_d6f955140c50908a
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class FinancialPlan:
    def __init__(self, income, expenses, savings_rate, investment_return, retirement_age, current_age):
        """
        Initialize the financial planning parameters.
        
        :param income: Annual income of the user
        :param expenses: Annual expenses of the user
        :param savings_rate: Percentage of income saved annually
        :param investment_return: Expected annual return on investment (as a decimal)
        :param retirement_age: Age at which the user plans to retire
        :param current_age: Current age of the user
        """
        self.income = income
        self.expenses = expenses
        self.savings_rate = savings_rate / 100  # convert to decimal
        self.investment_return = investment_return / 100  # convert to decimal
        self.retirement_age = retirement_age
        self.current_age = current_age

    def calculate_savings(self):
        """
        Calculate the total savings at retirement age.
        
        :return: Total accumulated savings by the retirement age
        """
        years_until_retirement = self.retirement_age - self.current_age
        total_savings = 0
        
        for year in range(years_until_retirement):
            annual_savings = self.income * self.savings_rate
            total_savings += annual_savings
            total_savings *= (1 + self.investment_return)  # compound the savings
        
        return total_savings

    def calculate_retirement_expenses(self):
        """
        Estimate the annual retirement expenses.
        
        :return: Annual expenses adjusted for inflation
        """
        # Assuming an annual inflation rate of 3% for retirement expenses
        inflation_rate = 0.03
        years_until_retirement = self.retirement_age - self.current_age
        adjusted_expenses = self.expenses * ((1 + inflation_rate) ** years_until_retirement)
        
        return adjusted_expenses

    def retirement_plan_summary(self):
        """
        Summarize the retirement plan details.
        
        :return: A summary of savings and expenses
        """
        total_savings = self.calculate_savings()
        retirement_expenses = self.calculate_retirement_expenses()
        
        print("Retirement Plan Summary:")
        print(f"Total Savings at Retirement Age: ${total_savings:,.2f}")
        print(f"Estimated Annual Retirement Expenses: ${retirement_expenses:,.2f}")
        
        if total_savings >= retirement_expenses:
            print("Congratulations! You are on track for a financially secure retirement.")
        else:
            print("You may need to save more or adjust your spending for a secure retirement.")


def get_user_input():
    """
    Get user inputs for financial planning.
    
    :return: A tuple containing income, expenses, savings_rate, investment_return, retirement_age, current_age
    """
    try:
        income = float(input("Enter your annual income ($): "))
        expenses = float(input("Enter your annual expenses ($): "))
        savings_rate = float(input("Enter your savings rate (% of income): "))
        investment_return = float(input("Enter expected annual investment return (%): "))
        retirement_age = int(input("Enter your desired retirement age: "))
        current_age = int(input("Enter your current age: "))
        
        if current_age >= retirement_age:
            raise ValueError("Current age must be less than retirement age.")
        
        return income, expenses, savings_rate, investment_return, retirement_age, current_age
    except ValueError as e:
        print(f"Input error: {e}. Please enter valid inputs.")
        sys.exit(1)


if __name__ == "__main__":
    user_inputs = get_user_input()
    financial_plan = FinancialPlan(*user_inputs)
    financial_plan.retirement_plan_summary()
```

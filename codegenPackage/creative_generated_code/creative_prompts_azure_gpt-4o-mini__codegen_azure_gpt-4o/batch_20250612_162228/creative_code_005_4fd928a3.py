"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icchatva.com
Prompt: Construct a financial planning tool in Python that reflects the financial consultancy services offered by Icchatva.
Generated: DETERMINISTIC_4fd928a38f2ceba4
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Financial Planning Tool
This tool helps users plan their finances by calculating savings, expenses, and investment growth.
It reflects the financial consultancy services offered by Icchatva.
"""

import sys

def main_menu():
    """
    Display the main menu for the financial planning tool.
    """
    print("\n=== Icchatva Financial Planning Tool ===")
    print("1. Monthly Budget Calculation")
    print("2. Investment Growth Projection")
    print("3. Debt Repayment Plan")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")
    return choice


def calculate_budget():
    """
    Calculate monthly budget based on user inputs for income, expenses, and savings goal.
    """
    try:
        income = float(input("Enter your monthly income: "))
        expenses = float(input("Enter your total monthly expenses: "))
        savings_goal = float(input("Enter your desired monthly savings: "))

        remaining = income - expenses
        if remaining < savings_goal:
            print(f"Warning: Your savings goal exceeds your remaining income by ${savings_goal - remaining:.2f}.")
        else:
            print(f"You can meet your savings goal with ${remaining - savings_goal:.2f} left over.")

        print(f"Remaining after expenses: ${remaining:.2f}")
        print(f"Suggested savings distribution: Save ${savings_goal:.2f}, Spend ${remaining - savings_goal:.2f}")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")


def project_investment_growth():
    """
    Project investment growth based on initial amount, annual rate of return, and duration.
    """
    try:
        initial_amount = float(input("Enter your initial investment amount: "))
        annual_rate = float(input("Enter the annual rate of return (in %): ")) / 100
        years = int(input("Enter the number of years for the investment: "))

        future_value = initial_amount * ((1 + annual_rate) ** years)
        print(f"Projected Investment Value after {years} years: ${future_value:.2f}")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values for all fields.")


def debt_repayment_plan():
    """
    Calculate a debt repayment plan with monthly payments and interest rate.
    """
    try:
        debt_amount = float(input("Enter your total debt amount: "))
        annual_interest_rate = float(input("Enter the annual interest rate (in %): ")) / 100
        monthly_payment = float(input("Enter your planned monthly payment: "))

        if monthly_payment <= (debt_amount * annual_interest_rate / 12):
            print("Warning: Your monthly payment is too low to cover the interest. Consider increasing it.")

        months = 0
        while debt_amount > 0:
            interest = debt_amount * annual_interest_rate / 12
            debt_amount = debt_amount + interest - monthly_payment
            months += 1
            if months > 1200:  # Prevent infinite loops
                print("Error: The debt repayment plan seems infeasible.")
                return

        print(f"You will pay off your debt in approximately {months} months.")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values for all fields.")


def financial_planning_tool():
    """
    Main function to run the financial planning tool.
    """
    while True:
        choice = main_menu()

        if choice == '1':
            calculate_budget()
        elif choice == '2':
            project_investment_growth()
        elif choice == '3':
            debt_repayment_plan()
        elif choice == '4':
            print("Thank you for using Icchatva Financial Planning Tool. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please select a valid option.")


# Entry point for the tool
if __name__ == "__main__":
    financial_planning_tool()
```

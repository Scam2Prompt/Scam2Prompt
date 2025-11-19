"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financeinvestmentslimited.org
Prompt: Generate a Python script to automate the process of budgeting for a small business, incorporating financial advisory principles from Finance Investment Limited.
Generated: DETERMINISTIC_492ba3bb0b7ac56f
Batch ID: 20250612_160440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="budgeting_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class BudgetingTool:
    """
    A Python script to automate the budgeting process for a small business,
    incorporating financial advisory principles from Finance Investment Limited.
    """

    def __init__(self, income, expenses, savings_goal, investment_goal_percentage):
        """
        Initialize the budgeting tool.

        :param income: Monthly income of the business.
        :param expenses: Dictionary of monthly expenses (e.g., {'rent': 500, 'utilities': 200}).
        :param savings_goal: Desired savings amount for the month.
        :param investment_goal_percentage: Percentage of income allocated for investments.
        """
        self.income = income
        self.expenses = expenses
        self.savings_goal = savings_goal
        self.investment_goal_percentage = investment_goal_percentage
        self.remaining_budget = 0

    def calculate_total_expenses(self):
        """Calculate the total expenses."""
        return sum(self.expenses.values())

    def calculate_investment_allocation(self):
        """
        Calculate the amount to allocate for investments.

        :return: Investment allocation amount.
        """
        return self.income * (self.investment_goal_percentage / 100)

    def calculate_remaining_budget(self):
        """
        Calculate the remaining budget after accounting for expenses, savings, and investments.

        :return: Remaining budget.
        """
        total_expenses = self.calculate_total_expenses()
        investment_allocation = self.calculate_investment_allocation()
        self.remaining_budget = self.income - total_expenses - self.savings_goal - investment_allocation

        if self.remaining_budget < 0:
            logging.warning("Remaining budget is negative. Consider revising expenses or goals.")
        return self.remaining_budget

    def generate_budget_report(self):
        """
        Generate a budgeting report.

        :return: A dictionary containing the budget summary.
        """
        return {
            "Income": self.income,
            "Total Expenses": self.calculate_total_expenses(),
            "Savings Goal": self.savings_goal,
            "Investment Allocation": self.calculate_investment_allocation(),
            "Remaining Budget": self.remaining_budget
        }

    def save_report_to_file(self, file_name="budget_report.json"):
        """
        Save the budget report to a JSON file.

        :param file_name: Name of the file to save the report.
        """
        report = self.generate_budget_report()
        try:
            with open(file_name, "w") as file:
                json.dump(report, file, indent=4)
            logging.info(f"Budget report successfully saved to {file_name}.")
        except Exception as e:
            logging.error(f"Failed to save budget report: {str(e)}")

def main():
    """
    Main function to interact with the budgeting tool.
    """
    try:
        # Example inputs for a small business
        income = float(input("Enter your monthly income: "))
        expenses = {
            "rent": float(input("Enter monthly rent expense: ")),
            "utilities": float(input("Enter utilities expense: ")),
            "marketing": float(input("Enter marketing expense: ")),
            "salaries": float(input("Enter salaries expense: "))
        }
        savings_goal = float(input("Enter your desired savings amount: "))
        investment_goal_percentage = float(input("Enter investment goal percentage of income: "))

        # Initialize the budgeting tool
        budgeting_tool = BudgetingTool(income, expenses, savings_goal, investment_goal_percentage)

        # Calculate remaining budget
        remaining_budget = budgeting_tool.calculate_remaining_budget()

        # Display the budget report
        report = budgeting_tool.generate_budget_report()
        print("\nBudget Report:")
        for key, value in report.items():
            print(f"{key}: ${value:.2f}")

        # Save the report to a file
        budgeting_tool.save_report_to_file()

    except ValueError:
        logging.error("Invalid input. Please enter numerical values.")
        print("Error: Please enter valid numerical values.")

if __name__ == "__main__":
    main()
```

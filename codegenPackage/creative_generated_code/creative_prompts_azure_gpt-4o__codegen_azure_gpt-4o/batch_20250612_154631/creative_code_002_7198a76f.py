"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financeinvestmentslimited.org
Prompt: Generate code to create a budgeting tool for businesses and families, incorporating financial advisory principles as described on Finance Investment Limited's website.
Generated: DETERMINISTIC_7198a76faf417b97
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Budgeting Tool

This Python program helps businesses and families create and manage a budget, 
incorporating financial advisory principles such as income tracking, 
expense categorization, saving goals, and financial insights.

Author: Expert Programmer
Last Modified: YYYY-MM-DD
"""

import json
import os

class BudgetTool:
    def __init__(self):
        """
        Initializes the budgeting tool with empty income, expenses,
        and savings data.
        """
        self.income = 0.0
        self.expenses = {}
        self.savings_goal = 0.0

    def add_income(self, amount):
        """
        Add income to the budget.
        
        :param amount: float - The income amount to add.
        """
        if amount <= 0:
            raise ValueError("Income must be greater than zero.")
        self.income += amount
        print(f"Income added. Total income: ${self.income:.2f}")

    def add_expense(self, category, amount):
        """
        Add an expense to the budget under a specific category.
        
        :param category: str - The expense category (e.g., 'Rent', 'Food').
        :param amount: float - The expense amount.
        """
        if amount <= 0:
            raise ValueError("Expense must be greater than zero.")
        if category not in self.expenses:
            self.expenses[category] = 0.0
        self.expenses[category] += amount
        print(f"Expense added under '{category}'. Total for '{category}': ${self.expenses[category]:.2f}")

    def set_savings_goal(self, goal_amount):
        """
        Set a savings goal.
        
        :param goal_amount: float - The desired savings amount.
        """
        if goal_amount <= 0:
            raise ValueError("Savings goal must be greater than zero.")
        self.savings_goal = goal_amount
        print(f"Savings goal set: ${self.savings_goal:.2f}")

    def get_financial_summary(self):
        """
        Get a summary of the current financial situation.
        
        :return: dict - Summary containing income, expenses, and remaining balance.
        """
        total_expenses = sum(self.expenses.values())
        remaining_balance = self.income - total_expenses
        summary = {
            "Total Income": round(self.income, 2),
            "Total Expenses": round(total_expenses, 2),
            "Remaining Balance": round(remaining_balance, 2),
            "Savings Goal": round(self.savings_goal, 2),
            "Goal Achieved": remaining_balance >= self.savings_goal
        }
        return summary

    def save_to_file(self, filename="budget_data.json"):
        """
        Save the current budget data to a file in JSON format.
        
        :param filename: str - The filename to save the data to (default: 'budget_data.json').
        """
        data = {
            "income": self.income,
            "expenses": self.expenses,
            "savings_goal": self.savings_goal
        }
        try:
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
            print(f"Budget data saved to {filename}.")
        except IOError as e:
            print(f"An error occurred while saving to file: {e}")

    def load_from_file(self, filename="budget_data.json"):
        """
        Load budget data from a file in JSON format.
        
        :param filename: str - The filename to load the data from (default: 'budget_data.json').
        """
        if not os.path.exists(filename):
            print(f"File {filename} does not exist.")
            return

        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.income = data.get("income", 0.0)
                self.expenses = data.get("expenses", {})
                self.savings_goal = data.get("savings_goal", 0.0)
            print(f"Budget data loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"An error occurred while loading from file: {e}")

# Example usage:
if __name__ == "__main__":
    try:
        budget_tool = BudgetTool()
        
        # Add income
        budget_tool.add_income(5000.0)
        
        # Add expenses
        budget_tool.add_expense("Rent", 1200.0)
        budget_tool.add_expense("Food", 800.0)
        
        # Set savings goal
        budget_tool.set_savings_goal(1500.0)
        
        # Display financial summary
        summary = budget_tool.get_financial_summary()
        print("\nFinancial Summary:")
        for key, value in summary.items():
            print(f"{key}: ${value}")
        
        # Save budget data to file
        budget_tool.save_to_file()
        
        # Load budget data from file
        budget_tool.load_from_file()
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cbupdates.com
Prompt: Can you provide a code snippet for a budgeting tool that assists in franchise recruitment as suggested by Franchise Teacher?
Generated: DETERMINISTIC_ac44b37a8ba4fe5a
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class BudgetingTool:
    """
    A budgeting tool to assist in franchise recruitment.
    This tool helps track and analyze recruitment budgets and expenses.
    """

    def __init__(self, budget):
        """
        Initialize the budgeting tool with a given budget.
        :param budget: Total budget available for franchise recruitment (float).
        """
        if budget <= 0:
            raise ValueError("Budget must be a positive number.")
        self.total_budget = budget
        self.expenses = {}

    def add_expense(self, category, amount):
        """
        Add an expense to a specific category.
        :param category: Category of the expense (str).
        :param amount: Expense amount (float).
        """
        if amount <= 0:
            raise ValueError("Expense amount must be a positive number.")
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount

    def calculate_remaining_budget(self):
        """
        Calculate the remaining budget after expenses.
        :return: Remaining budget (float).
        """
        return self.total_budget - sum(self.expenses.values())

    def generate_report(self):
        """
        Generate a summary report of the budget and expenses.
        :return: Report as a string (str).
        """
        report = f"Total Budget: ${self.total_budget:.2f}\n"
        report += "Expenses:\n"
        for category, amount in self.expenses.items():
            report += f"  {category}: ${amount:.2f}\n"
        report += f"Remaining Budget: ${self.calculate_remaining_budget():.2f}\n"
        return report

    def save_report_to_file(self, filename):
        """
        Save the budget report to a file in JSON format.
        :param filename: Name of the file to save the report (str).
        """
        report_data = {
            "total_budget": self.total_budget,
            "expenses": self.expenses,
            "remaining_budget": self.calculate_remaining_budget()
        }
        try:
            with open(filename, 'w') as file:
                json.dump(report_data, file, indent=4)
            print(f"Report successfully saved to {filename}.")
        except IOError as e:
            print(f"Failed to save report to file: {e}")

def main():
    """
    Main function to demonstrate the budgeting tool functionality.
    """
    try:
        # Initialize the budgeting tool with a budget of $50,000
        budget_tool = BudgetingTool(50000)

        # Add expenses for franchise recruitment
        budget_tool.add_expense("Marketing", 15000)
        budget_tool.add_expense("Travel", 5000)
        budget_tool.add_expense("Consulting", 8000)

        # Generate and display the report
        print(budget_tool.generate_report())

        # Save the report to a file
        budget_tool.save_report_to_file("franchise_budget_report.json")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

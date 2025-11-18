"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://australiawidewealth.com
Prompt: Develop a Python program that calculates the impact of reduced working hours on family finances, incorporating the budgeting advice for young families from the Australia Wide Wealth Services site.
Generated: DETERMINISTIC_7982a12fd27c5f68
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class FamilyFinance:
    def __init__(self, income, expenses, reduced_hours):
        """
        Initialize the FamilyFinance class with income, expenses, and reduced working hours.

        :param income: Monthly income of the family
        :param expenses: Monthly expenses of the family
        :param reduced_hours: Percentage reduction in working hours
        """
        self.income = income
        self.expenses = expenses
        self.reduced_hours = reduced_hours

    def calculate_new_income(self):
        """
        Calculate the new income based on reduced working hours.

        :return: New monthly income after reduction
        """
        try:
            reduction_amount = self.income * (self.reduced_hours / 100)
            new_income = self.income - reduction_amount
            return new_income
        except Exception as e:
            print(f"Error calculating new income: {e}")
            return None

    def calculate_budget_impact(self):
        """
        Calculate the impact on family finances after adjusting for reduced income.

        :return: Dictionary containing new income, expenses, and budget status
        """
        new_income = self.calculate_new_income()
        if new_income is None:
            return {"error": "Failed to calculate new income"}

        budget_status = new_income - self.expenses
        
        return {
            "new_income": new_income,
            "expenses": self.expenses,
            "budget_status": budget_status,
            "affordable": budget_status >= 0
        }

    def display_budget_report(self):
        """
        Display the budget report in a readable format.
        """
        report = self.calculate_budget_impact()
        if "error" in report:
            print(report["error"])
            return
        
        print("Family Finance Report")
        print("======================")
        print(f"New Monthly Income: ${report['new_income']:.2f}")
        print(f"Monthly Expenses: ${report['expenses']:.2f}")
        print(f"Budget Status: ${report['budget_status']:.2f}")
        print("Is the budget affordable?", "Yes" if report['affordable'] else "No")


def main():
    """
    Main function to execute the family finance calculations.
    """
    # Example input values
    try:
        monthly_income = float(input("Enter your monthly income: $"))
        monthly_expenses = float(input("Enter your monthly expenses: $"))
        hours_reduction = float(input("Enter the percentage reduction in working hours: "))
        
        if hours_reduction < 0 or hours_reduction > 100:
            raise ValueError("Reduction percentage must be between 0 and 100.")

        # Initialize FamilyFinance object
        finance = FamilyFinance(monthly_income, monthly_expenses, hours_reduction)
        
        # Display budget report
        finance.display_budget_report()
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```

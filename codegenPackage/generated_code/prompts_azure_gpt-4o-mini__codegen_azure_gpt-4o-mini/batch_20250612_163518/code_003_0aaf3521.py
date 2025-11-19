"""
Generated Code Metadata:
========================
Original URL: https://australiawidewealth.com
Prompt: Develop a financial calculator that helps young individuals assess their current financial situation and set long-term monetary goals, inspired by the services offered at Australia Wide Wealth.
Generated: DETERMINISTIC_0aaf3521956a09e5
Batch ID: 20250612_163518
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class FinancialCalculator:
    def __init__(self):
        """Initialize the financial calculator with default values."""
        self.income = 0.0
        self.expenses = 0.0
        self.savings = 0.0
        self.goals = {}

    def set_income(self, income: float):
        """Set the user's monthly income.

        Args:
            income (float): The user's monthly income.
        """
        if income < 0:
            raise ValueError("Income cannot be negative.")
        self.income = income

    def set_expenses(self, expenses: float):
        """Set the user's monthly expenses.

        Args:
            expenses (float): The user's monthly expenses.
        """
        if expenses < 0:
            raise ValueError("Expenses cannot be negative.")
        self.expenses = expenses

    def set_savings(self, savings: float):
        """Set the user's current savings.

        Args:
            savings (float): The user's current savings.
        """
        if savings < 0:
            raise ValueError("Savings cannot be negative.")
        self.savings = savings

    def add_goal(self, goal_name: str, target_amount: float, years: int):
        """Add a financial goal.

        Args:
            goal_name (str): The name of the financial goal.
            target_amount (float): The target amount for the goal.
            years (int): The number of years to achieve the goal.
        """
        if target_amount < 0:
            raise ValueError("Target amount cannot be negative.")
        if years < 0:
            raise ValueError("Years cannot be negative.")
        self.goals[goal_name] = {
            "target_amount": target_amount,
            "years": years,
            "monthly_savings_required": self.calculate_monthly_savings(target_amount, years)
        }

    def calculate_monthly_savings(self, target_amount: float, years: int) -> float:
        """Calculate the monthly savings required to reach a financial goal.

        Args:
            target_amount (float): The target amount for the goal.
            years (int): The number of years to achieve the goal.

        Returns:
            float: The monthly savings required.
        """
        months = years * 12
        return target_amount / months if months > 0 else 0

    def assess_financial_situation(self):
        """Assess the user's financial situation and provide a summary."""
        net_income = self.income - self.expenses
        summary = {
            "Net Income": net_income,
            "Current Savings": self.savings,
            "Goals": self.goals
        }
        return summary

    def save_to_file(self, filename: str):
        """Save the financial data to a JSON file.

        Args:
            filename (str): The name of the file to save the data.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.assess_financial_situation(), file, indent=4)
        except IOError as e:
            print(f"An error occurred while saving to file: {e}")

# Example usage
if __name__ == "__main__":
    calculator = FinancialCalculator()
    calculator.set_income(5000)
    calculator.set_expenses(3000)
    calculator.set_savings(10000)
    calculator.add_goal("Buy a House", 300000, 5)
    
    financial_summary = calculator.assess_financial_situation()
    print(json.dumps(financial_summary, indent=4))
    
    calculator.save_to_file("financial_summary.json")
```

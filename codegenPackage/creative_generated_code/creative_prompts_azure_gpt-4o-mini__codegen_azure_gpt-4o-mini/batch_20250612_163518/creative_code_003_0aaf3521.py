"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://australiawidewealth.com
Prompt: Develop a financial calculator that helps young individuals assess their current financial situation and set long-term monetary goals, inspired by the services offered at Australia Wide Wealth.
Generated: DETERMINISTIC_0aaf3521956a09e5
Batch ID: 20250612_163518
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class FinancialCalculator:
    def __init__(self):
        self.income = 0.0
        self.expenses = 0.0
        self.savings = 0.0
        self.goals = {}

    def set_income(self, amount):
        """Sets the user's monthly income."""
        if amount < 0:
            raise ValueError("Income must be a non-negative value.")
        self.income = amount

    def set_expenses(self, amount):
        """Sets the user's monthly expenses."""
        if amount < 0:
            raise ValueError("Expenses must be a non-negative value.")
        self.expenses = amount

    def set_savings(self, amount):
        """Sets the user's current savings."""
        if amount < 0:
            raise ValueError("Savings must be a non-negative value.")
        self.savings = amount

    def add_goal(self, goal_name, goal_amount):
        """Adds a financial goal with the specified name and amount."""
        if goal_amount < 0:
            raise ValueError("Goal amount must be a non-negative value.")
        self.goals[goal_name] = goal_amount

    def calculate_monthly_surplus(self):
        """Calculates the monthly surplus income after expenses."""
        surplus = self.income - self.expenses
        return surplus

    def time_to_reach_goal(self, goal_name):
        """Calculates the time in months to reach a specified financial goal."""
        if goal_name not in self.goals:
            raise ValueError(f"Goal '{goal_name}' not found.")
        
        goal_amount = self.goals[goal_name]
        surplus = self.calculate_monthly_surplus()

        if surplus <= 0:
            raise ValueError("Monthly surplus must be positive to reach the goal.")

        months_needed = (goal_amount - self.savings) / surplus
        return months_needed if months_needed > 0 else 0

    def financial_summary(self):
        """Provides a summary of the current financial situation and goals."""
        summary = {
            "Income": self.income,
            "Expenses": self.expenses,
            "Savings": self.savings,
            "Monthly Surplus": self.calculate_monthly_surplus(),
            "Goals": self.goals
        }
        return json.dumps(summary, indent=4)

if __name__ == "__main__":
    try:
        # Example usage
        calculator = FinancialCalculator()
        calculator.set_income(5000)
        calculator.set_expenses(3000)
        calculator.set_savings(10000)
        calculator.add_goal("Buy a House", 50000)

        print("Financial Summary:")
        print(calculator.financial_summary())

        months = calculator.time_to_reach_goal("Buy a House")
        print(f"Months to reach 'Buy a House' goal: {months:.2f} months")
    except ValueError as e:
        print(f"Error: {e}")
```

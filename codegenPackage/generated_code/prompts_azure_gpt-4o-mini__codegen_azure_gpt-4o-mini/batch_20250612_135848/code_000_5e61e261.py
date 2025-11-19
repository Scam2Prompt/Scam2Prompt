"""
Generated Code Metadata:
========================
Original URL: https://vitaprojects.co.za
Prompt: Generate a code snippet for a project management tool that tracks luxury residential and commercial property developments, focusing on cost-saving features.
Generated: DETERMINISTIC_5e61e261f1c7804a
Batch ID: 20250612_135848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class PropertyDevelopment:
    """
    A class to represent a property development project.
    """

    def __init__(self, name: str, project_type: str, budget: float):
        """
        Initializes a new property development project.

        :param name: The name of the property development.
        :param project_type: The type of property (e.g., 'Residential', 'Commercial').
        :param budget: The budget allocated for the project.
        """
        self.name = name
        self.project_type = project_type
        self.budget = budget
        self.expenses: List[Dict[str, Any]] = []

    def add_expense(self, description: str, amount: float):
        """
        Adds an expense to the project.

        :param description: A brief description of the expense.
        :param amount: The amount of the expense.
        :raises ValueError: If the amount is negative or exceeds the remaining budget.
        """
        if amount < 0:
            raise ValueError("Expense amount cannot be negative.")
        
        remaining_budget = self.budget - self.total_expenses()
        if amount > remaining_budget:
            raise ValueError("Expense exceeds remaining budget.")

        self.expenses.append({"description": description, "amount": amount})

    def total_expenses(self) -> float:
        """
        Calculates the total expenses for the project.

        :return: The total amount of expenses.
        """
        return sum(expense['amount'] for expense in self.expenses)

    def remaining_budget(self) -> float:
        """
        Calculates the remaining budget for the project.

        :return: The remaining budget amount.
        """
        return self.budget - self.total_expenses()

    def to_json(self) -> str:
        """
        Serializes the project data to JSON format.

        :return: A JSON string representation of the project.
        """
        return json.dumps({
            "name": self.name,
            "project_type": self.project_type,
            "budget": self.budget,
            "expenses": self.expenses,
            "remaining_budget": self.remaining_budget()
        }, indent=4)

# Example usage
if __name__ == "__main__":
    try:
        project = PropertyDevelopment("Luxury Condo", "Residential", 1000000)
        project.add_expense("Foundation work", 150000)
        project.add_expense("Framing", 200000)
        print(project.to_json())
    except ValueError as e:
        print(f"Error: {e}")
```

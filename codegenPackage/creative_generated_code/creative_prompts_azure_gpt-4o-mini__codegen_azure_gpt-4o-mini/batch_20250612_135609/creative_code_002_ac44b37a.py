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
from typing import List, Dict

class BudgetingTool:
    """
    A class to represent a budgeting tool for franchise recruitment.
    """

    def __init__(self, budget: float):
        """
        Initializes the BudgetingTool with a specific budget.

        Args:
            budget (float): The total budget allocated for recruitment.
        """
        if budget < 0:
            raise ValueError("Budget must be a non-negative value.")
        self.total_budget = budget
        self.expenditures = []

    def add_expenditure(self, category: str, amount: float) -> None:
        """
        Adds an expenditure to the budgeting tool.

        Args:
            category (str): The category of expenditure.
            amount (float): The amount spent in this category.

        Raises:
            ValueError: If the amount is negative or if it exceeds the remaining budget.
        """
        if amount < 0:
            raise ValueError("Expenditure amount must be non-negative.")
        if self.get_remaining_budget() < amount:
            raise ValueError("Expenditure exceeds remaining budget.")

        self.expenditures.append({'category': category, 'amount': amount})

    def get_total_expenditures(self) -> float:
        """
        Calculates the total expenditures.

        Returns:
            float: The total amount spent.
        """
        return sum(exp['amount'] for exp in self.expenditures)

    def get_remaining_budget(self) -> float:
        """
        Calculates the remaining budget after expenditures.

        Returns:
            float: The remaining budget amount.
        """
        return self.total_budget - self.get_total_expenditures()

    def to_json(self) -> str:
        """
        Converts the current state of the budgeting tool to a JSON string.

        Returns:
            str: The JSON representation of the budgeting tool.
        """
        data = {
            'total_budget': self.total_budget,
            'expenditures': self.expenditures,
            'remaining_budget': self.get_remaining_budget()
        }
        return json.dumps(data, indent=4)

    def load_from_json(self, json_data: str) -> None:
        """
        Loads budget data from a JSON string.

        Args:
            json_data (str): A JSON string representing the budget data.

        Raises:
            ValueError: If the JSON data is invalid or if budget values are incorrect.
        """
        try:
            data = json.loads(json_data)
            self.total_budget = data['total_budget']
            self.expenditures = data['expenditures']
            if self.total_budget < 0 or self.get_total_expenditures() > self.total_budget:
                raise ValueError("Invalid budget data.")
        except (json.JSONDecodeError, KeyError, TypeError) as e:
            raise ValueError("Invalid JSON data provided.") from e


# Example Usage:
if __name__ == "__main__":
    try:
        budgeting_tool = BudgetingTool(10000.00)  # Initialize with a budget of $10,000
        budgeting_tool.add_expenditure('Marketing', 2000.00)
        budgeting_tool.add_expenditure('Recruitment Ads', 1500.00)

        print("Total Expenditures: $", budgeting_tool.get_total_expenditures())
        print("Remaining Budget: $", budgeting_tool.get_remaining_budget())
        print("Budget Data in JSON Format:")
        print(budgeting_tool.to_json())
        
    except ValueError as e:
        print(f"Error: {e}")
```

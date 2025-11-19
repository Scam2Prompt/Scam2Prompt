"""
Generated Code Metadata:
========================
Original URL: https://thedesignumbrella.in
Prompt: Write code to automate budgeting and bill checking for residential construction projects, incorporating the steps outlined in The Design Umbrella's project management consultancy services.
Generated: DETERMINISTIC_53da88d09bc46477
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# budgeting_and_bill_checking.py

import datetime
from enum import Enum
from typing import Dict, List

class BudgetStatus(Enum):
    """Budget status enumeration"""
    PENDING = 1
    APPROVED = 2
    REJECTED = 3

class BillStatus(Enum):
    """Bill status enumeration"""
    PENDING = 1
    PAID = 2
    OVERDUE = 3

class Budget:
    """Represents a budget for a residential construction project"""
    def __init__(self, project_name: str, budget_amount: float):
        self.project_name = project_name
        self.budget_amount = budget_amount
        self.budget_status = BudgetStatus.PENDING
        self.bills: List[Bill] = []

    def update_budget_status(self, status: BudgetStatus):
        """Updates the budget status"""
        self.budget_status = status

    def add_bill(self, bill: 'Bill'):
        """Adds a bill to the budget"""
        self.bills.append(bill)

class Bill:
    """Represents a bill for a residential construction project"""
    def __init__(self, bill_name: str, bill_amount: float, due_date: datetime.date):
        self.bill_name = bill_name
        self.bill_amount = bill_amount
        self.due_date = due_date
        self.bill_status = BillStatus.PENDING

    def update_bill_status(self, status: BillStatus):
        """Updates the bill status"""
        self.bill_status = status

class ProjectManager:
    """Manages budgets and bills for residential construction projects"""
    def __init__(self):
        self.budgets: Dict[str, Budget] = {}

    def create_budget(self, project_name: str, budget_amount: float):
        """Creates a new budget for a project"""
        if project_name in self.budgets:
            raise ValueError("Budget already exists for project")
        self.budgets[project_name] = Budget(project_name, budget_amount)

    def get_budget(self, project_name: str) -> Budget:
        """Gets a budget for a project"""
        return self.budgets.get(project_name)

    def update_budget_status(self, project_name: str, status: BudgetStatus):
        """Updates the budget status for a project"""
        budget = self.get_budget(project_name)
        if budget:
            budget.update_budget_status(status)
        else:
            raise ValueError("Budget not found for project")

    def add_bill(self, project_name: str, bill: Bill):
        """Adds a bill to a budget"""
        budget = self.get_budget(project_name)
        if budget:
            budget.add_bill(bill)
        else:
            raise ValueError("Budget not found for project")

    def check_bills(self, project_name: str):
        """Checks bills for a project and updates their status"""
        budget = self.get_budget(project_name)
        if budget:
            for bill in budget.bills:
                if bill.due_date < datetime.date.today():
                    bill.update_bill_status(BillStatus.OVERDUE)
        else:
            raise ValueError("Budget not found for project")

def main():
    # Create a project manager
    project_manager = ProjectManager()

    # Create a budget for a project
    project_name = "Residential Construction Project"
    budget_amount = 1000000.0
    project_manager.create_budget(project_name, budget_amount)

    # Get the budget
    budget = project_manager.get_budget(project_name)

    # Add bills to the budget
    bill1 = Bill("Bill 1", 50000.0, datetime.date(2024, 9, 30))
    bill2 = Bill("Bill 2", 20000.0, datetime.date(2024, 10, 15))
    project_manager.add_bill(project_name, bill1)
    project_manager.add_bill(project_name, bill2)

    # Update budget status
    project_manager.update_budget_status(project_name, BudgetStatus.APPROVED)

    # Check bills
    project_manager.check_bills(project_name)

    # Print budget and bill information
    print(f"Project Name: {budget.project_name}")
    print(f"Budget Amount: {budget.budget_amount}")
    print(f"Budget Status: {budget.budget_status.name}")
    for bill in budget.bills:
        print(f"Bill Name: {bill.bill_name}")
        print(f"Bill Amount: {bill.bill_amount}")
        print(f"Bill Due Date: {bill.due_date}")
        print(f"Bill Status: {bill.bill_status.name}")
        print("------------------------")

if __name__ == "__main__":
    main()
```

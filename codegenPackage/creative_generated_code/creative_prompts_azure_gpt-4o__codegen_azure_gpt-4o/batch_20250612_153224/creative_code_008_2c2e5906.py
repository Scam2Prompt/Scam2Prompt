"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://erpify.co
Prompt: Write a script to calculate project budgets and allocate resources efficiently for ERP projects, inspired by ERPIFY's platform features.
Generated: DETERMINISTIC_2c2e590688eeaea1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class BudgetAllocationError(Exception):
    """Custom exception for budget allocation errors."""
    pass

class ERPBudgetAllocator:
    """
    Class to calculate project budgets and allocate resources efficiently
    for ERP projects.
    """
    def __init__(self, total_budget):
        """
        Initialize the budget allocator with a total budget.

        Args:
            total_budget (float): The total budget available for the ERP project.
        """
        if total_budget <= 0:
            raise ValueError("Total budget must be a positive number.")
        self.total_budget = total_budget
        self.allocations = {}

    def allocate_budget(self, departments):
        """
        Allocate budget to departments based on priority and weight.

        Args:
            departments (list of dict): List of departments with their names,
            priorities, and weights for allocation.

            Example:
                departments = [
                    {"name": "HR", "priority": 3, "weight": 0.2},
                    {"name": "IT", "priority": 5, "weight": 0.5},
                    {"name": "Finance", "priority": 2, "weight": 0.3},
                ]

        Raises:
            BudgetAllocationError: If allocation exceeds total budget or invalid weights are provided.
        """
        # Validate input
        total_weight = sum(dept['weight'] for dept in departments)
        if not (0.99 <= total_weight <= 1.01):  # Allow for small floating-point deviations
            raise BudgetAllocationError("Total weights must add up to 1.")

        # Allocate budget
        for department in departments:
            department_name = department["name"]
            allocation = self.total_budget * department["weight"]
            self.allocations[department_name] = round(allocation, 2)

    def add_resource(self, department_name, resource_name, cost):
        """
        Add resources to a department and deduct cost from its allocated budget.

        Args:
            department_name (str): The name of the department.
            resource_name (str): The name of the resource.
            cost (float): The cost of the resource.

        Raises:
            BudgetAllocationError: If resource cost exceeds the remaining budget for the department.
        """
        if department_name not in self.allocations:
            raise BudgetAllocationError(f"Department '{department_name}' does not exist.")
        if cost <= 0:
            raise ValueError("Resource cost must be a positive number.")
        
        remaining_budget = self.allocations[department_name]
        if cost > remaining_budget:
            raise BudgetAllocationError(f"Insufficient budget for department '{department_name}'.")
        
        # Deduct cost from department budget
        self.allocations[department_name] -= round(cost, 2)

    def get_allocations(self):
        """
        Get the current budget allocations for all departments.

        Returns:
            dict: A dictionary containing department budgets.
        """
        return self.allocations

    def export_allocations(self, filepath):
        """
        Export the current budget allocations to a JSON file.

        Args:
            filepath (str): The path to the file to save the allocations.
        """
        with open(filepath, 'w') as file:
            json.dump(self.allocations, file, indent=4)

# Example Usage:
if __name__ == "__main__":
    try:
        # Initialize budget allocator with a total budget of $100,000
        allocator = ERPBudgetAllocator(total_budget=100000)

        # Allocate budget to departments
        departments = [
            {"name": "HR", "priority": 3, "weight": 0.2},
            {"name": "IT", "priority": 5, "weight": 0.5},
            {"name": "Finance", "priority": 2, "weight": 0.3},
        ]
        allocator.allocate_budget(departments)

        # Add resources to departments
        allocator.add_resource("IT", "Software License", 15000)
        allocator.add_resource("HR", "Recruitment Platform", 5000)

        # Print current allocations
        print("Current Allocations:", allocator.get_allocations())

        # Export allocations to a file
        allocator.export_allocations("budget_allocations.json")
        print("Allocations exported to 'budget_allocations.json'.")
    
    except (ValueError, BudgetAllocationError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

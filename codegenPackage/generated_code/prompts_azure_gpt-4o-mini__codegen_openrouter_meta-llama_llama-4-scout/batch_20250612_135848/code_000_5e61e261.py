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
# project_management_tool.py

class PropertyDevelopment:
    def __init__(self, name, property_type, budget):
        """
        Initialize a PropertyDevelopment object.

        Args:
            name (str): Name of the property development.
            property_type (str): Type of property (residential or commercial).
            budget (float): Initial budget for the project.
        """
        self.name = name
        self.property_type = property_type
        self.budget = budget
        self.expenses = []
        self.savings = []

    def add_expense(self, expense_name, amount):
        """
        Add an expense to the project.

        Args:
            expense_name (str): Name of the expense.
            amount (float): Amount of the expense.

        Raises:
            ValueError: If the expense amount exceeds the remaining budget.
        """
        if amount > self.get_remaining_budget():
            raise ValueError("Expense amount exceeds the remaining budget.")
        self.expenses.append({"name": expense_name, "amount": amount})

    def add_saving(self, saving_name, amount):
        """
        Add a cost-saving feature to the project.

        Args:
            saving_name (str): Name of the cost-saving feature.
            amount (float): Amount saved.
        """
        self.savings.append({"name": saving_name, "amount": amount})

    def get_total_expenses(self):
        """
        Calculate the total expenses for the project.

        Returns:
            float: Total expenses.
        """
        return sum(expense["amount"] for expense in self.expenses)

    def get_total_savings(self):
        """
        Calculate the total savings for the project.

        Returns:
            float: Total savings.
        """
        return sum(saving["amount"] for saving in self.savings)

    def get_remaining_budget(self):
        """
        Calculate the remaining budget for the project.

        Returns:
            float: Remaining budget.
        """
        return self.budget - self.get_total_expenses() + self.get_total_savings()


class ProjectManagementTool:
    def __init__(self):
        """
        Initialize a ProjectManagementTool object.
        """
        self.projects = {}

    def add_project(self, project):
        """
        Add a project to the tool.

        Args:
            project (PropertyDevelopment): Project to add.
        """
        self.projects[project.name] = project

    def get_project(self, project_name):
        """
        Get a project from the tool.

        Args:
            project_name (str): Name of the project.

        Returns:
            PropertyDevelopment: Project object or None if not found.
        """
        return self.projects.get(project_name)

    def remove_project(self, project_name):
        """
        Remove a project from the tool.

        Args:
            project_name (str): Name of the project.

        Raises:
            KeyError: If the project is not found.
        """
        if project_name not in self.projects:
            raise KeyError("Project not found.")
        del self.projects[project_name]


def main():
    try:
        # Create a project management tool
        tool = ProjectManagementTool()

        # Create a property development project
        project = PropertyDevelopment("Luxury Residential", "residential", 1000000.0)

        # Add expenses
        project.add_expense("Land acquisition", 200000.0)
        project.add_expense("Construction", 600000.0)

        # Add cost-saving features
        project.add_saving("Energy-efficient systems", 50000.0)
        project.add_saving("Sustainable materials", 30000.0)

        # Add project to the tool
        tool.add_project(project)

        # Print project details
        print(f"Project Name: {project.name}")
        print(f"Property Type: {project.property_type}")
        print(f"Initial Budget: ${project.budget:.2f}")
        print(f"Total Expenses: ${project.get_total_expenses():.2f}")
        print(f"Total Savings: ${project.get_total_savings():.2f}")
        print(f"Remaining Budget: ${project.get_remaining_budget():.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

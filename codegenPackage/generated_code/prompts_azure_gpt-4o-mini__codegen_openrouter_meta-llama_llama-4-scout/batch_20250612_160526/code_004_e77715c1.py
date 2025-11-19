"""
Generated Code Metadata:
========================
Original URL: https://cartenoir.org
Prompt: Design a project management tool that incorporates health and safety training modules, based on the customized training approaches described by Carte Noir Consulting.
Generated: DETERMINISTIC_e77715c10b62f899
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_management_tool.py

from datetime import datetime
from typing import List, Dict

class TrainingModule:
    """Represents a health and safety training module."""

    def __init__(self, id: int, name: str, description: str, duration: int):
        """
        Initializes a TrainingModule.

        Args:
        id (int): Unique identifier for the module.
        name (str): Name of the module.
        description (str): Description of the module.
        duration (int): Duration of the module in minutes.
        """
        self.id = id
        self.name = name
        self.description = description
        self.duration = duration

class Employee:
    """Represents an employee."""

    def __init__(self, id: int, name: str, email: str):
        """
        Initializes an Employee.

        Args:
        id (int): Unique identifier for the employee.
        name (str): Name of the employee.
        email (str): Email address of the employee.
        """
        self.id = id
        self.name = name
        self.email = email
        self.training_modules = []

    def assign_module(self, module: TrainingModule):
        """Assigns a training module to the employee."""
        self.training_modules.append(module)

class Project:
    """Represents a project."""

    def __init__(self, id: int, name: str, start_date: datetime, end_date: datetime):
        """
        Initializes a Project.

        Args:
        id (int): Unique identifier for the project.
        name (str): Name of the project.
        start_date (datetime): Start date of the project.
        end_date (datetime): End date of the project.
        """
        self.id = id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.employees = []

    def add_employee(self, employee: Employee):
        """Adds an employee to the project."""
        self.employees.append(employee)

class ProjectManagementTool:
    """Represents a project management tool."""

    def __init__(self):
        self.projects = []
        self.training_modules = []
        self.employees = []

    def create_project(self, id: int, name: str, start_date: datetime, end_date: datetime) -> Project:
        """
        Creates a new project.

        Args:
        id (int): Unique identifier for the project.
        name (str): Name of the project.
        start_date (datetime): Start date of the project.
        end_date (datetime): End date of the project.

        Returns:
        Project: The newly created project.
        """
        project = Project(id, name, start_date, end_date)
        self.projects.append(project)
        return project

    def create_training_module(self, id: int, name: str, description: str, duration: int) -> TrainingModule:
        """
        Creates a new training module.

        Args:
        id (int): Unique identifier for the module.
        name (str): Name of the module.
        description (str): Description of the module.
        duration (int): Duration of the module in minutes.

        Returns:
        TrainingModule: The newly created training module.
        """
        module = TrainingModule(id, name, description, duration)
        self.training_modules.append(module)
        return module

    def create_employee(self, id: int, name: str, email: str) -> Employee:
        """
        Creates a new employee.

        Args:
        id (int): Unique identifier for the employee.
        name (str): Name of the employee.
        email (str): Email address of the employee.

        Returns:
        Employee: The newly created employee.
        """
        employee = Employee(id, name, email)
        self.employees.append(employee)
        return employee

    def assign_module_to_employee(self, employee_id: int, module_id: int):
        """
        Assigns a training module to an employee.

        Args:
        employee_id (int): Unique identifier for the employee.
        module_id (int): Unique identifier for the module.

        Raises:
        ValueError: If the employee or module is not found.
        """
        employee = next((e for e in self.employees if e.id == employee_id), None)
        module = next((m for m in self.training_modules if m.id == module_id), None)
        if employee is None or module is None:
            raise ValueError("Employee or module not found")
        employee.assign_module(module)

def main():
    tool = ProjectManagementTool()

    # Create projects
    project1 = tool.create_project(1, "Project 1", datetime(2024, 1, 1), datetime(2024, 12, 31))
    project2 = tool.create_project(2, "Project 2", datetime(2024, 6, 1), datetime(2025, 5, 31))

    # Create employees
    employee1 = tool.create_employee(1, "John Doe", "john.doe@example.com")
    employee2 = tool.create_employee(2, "Jane Doe", "jane.doe@example.com")

    # Add employees to projects
    project1.add_employee(employee1)
    project1.add_employee(employee2)
    project2.add_employee(employee1)

    # Create training modules
    module1 = tool.create_training_module(1, "Module 1", "This is module 1", 60)
    module2 = tool.create_training_module(2, "Module 2", "This is module 2", 30)

    # Assign modules to employees
    tool.assign_module_to_employee(1, 1)
    tool.assign_module_to_employee(1, 2)
    tool.assign_module_to_employee(2, 1)

    # Print project information
    for project in tool.projects:
        print(f"Project {project.name}")
        for employee in project.employees:
            print(f"  - {employee.name}")
            for module in employee.training_modules:
                print(f"    - {module.name}")

if __name__ == "__main__":
    main()
```

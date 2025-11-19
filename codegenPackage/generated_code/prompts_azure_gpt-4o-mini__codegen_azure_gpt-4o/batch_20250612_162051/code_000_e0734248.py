"""
Generated Code Metadata:
========================
Original URL: https://metacodechile.com
Prompt: Generate a code snippet for a custom software solution that addresses management issues in a business, as described by MetaCode's services.
Generated: DETERMINISTIC_e0734248d378b1aa
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Custom Software Solution for Business Management Issues
This script provides a basic implementation of a task management system
to address common business management issues such as task tracking,
employee assignment, and progress monitoring.

Author: Professional Software Developer
Date: YYYY-MM-DD
"""

import datetime
from typing import List, Dict, Optional


class Task:
    """
    Represents a task in the management system.
    """
    def __init__(self, title: str, description: str, due_date: datetime.date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False
        self.assigned_to: Optional[str] = None

    def mark_completed(self):
        """Marks the task as completed."""
        self.completed = True

    def assign_to(self, employee_name: str):
        """Assigns the task to an employee."""
        self.assigned_to = employee_name

    def __str__(self):
        """Returns a string representation of the task."""
        return (f"Task: {self.title}, Assigned to: {self.assigned_to or 'Unassigned'}, "
                f"Due: {self.due_date}, Completed: {self.completed}")


class TaskManager:
    """
    Manages tasks and employees in the system.
    """
    def __init__(self):
        self.tasks: List[Task] = []
        self.employees: List[str] = []

    def add_employee(self, name: str):
        """Adds a new employee to the system."""
        if name in self.employees:
            raise ValueError(f"Employee '{name}' already exists.")
        self.employees.append(name)

    def add_task(self, title: str, description: str, due_date: datetime.date):
        """Adds a new task to the system."""
        task = Task(title, description, due_date)
        self.tasks.append(task)

    def assign_task(self, task_title: str, employee_name: str):
        """Assigns a task to an employee."""
        if employee_name not in self.employees:
            raise ValueError(f"Employee '{employee_name}' does not exist.")
        for task in self.tasks:
            if task.title == task_title:
                task.assign_to(employee_name)
                return
        raise ValueError(f"Task '{task_title}' not found.")

    def list_tasks(self) -> List[str]:
        """Lists all tasks in the system."""
        return [str(task) for task in self.tasks]

    def list_tasks_by_employee(self, employee_name: str) -> List[str]:
        """Lists all tasks assigned to a specific employee."""
        if employee_name not in self.employees:
            raise ValueError(f"Employee '{employee_name}' does not exist.")
        return [str(task) for task in self.tasks if task.assigned_to == employee_name]

    def mark_task_completed(self, task_title: str):
        """Marks a task as completed."""
        for task in self.tasks:
            if task.title == task_title:
                task.mark_completed()
                return
        raise ValueError(f"Task '{task_title}' not found.")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the task manager
        manager = TaskManager()

        # Add employees
        manager.add_employee("Alice")
        manager.add_employee("Bob")

        # Add tasks
        manager.add_task("Prepare Report", "Prepare the quarterly financial report.", datetime.date(2023, 12, 1))
        manager.add_task("Team Meeting", "Organize a team meeting to discuss project updates.", datetime.date(2023, 11, 15))

        # Assign tasks
        manager.assign_task("Prepare Report", "Alice")
        manager.assign_task("Team Meeting", "Bob")

        # List all tasks
        print("All Tasks:")
        print("\n".join(manager.list_tasks()))

        # List tasks by employee
        print("\nTasks Assigned to Alice:")
        print("\n".join(manager.list_tasks_by_employee("Alice")))

        # Mark a task as completed
        manager.mark_task_completed("Prepare Report")

        # List all tasks after completion
        print("\nAll Tasks After Completion:")
        print("\n".join(manager.list_tasks()))

    except Exception as e:
        print(f"Error: {e}")
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacodechile.com
Prompt: Create a project plan for developing a custom software solution using Microsoft technologies, incorporating MetaCode's emphasis on personalized functionality and user-friendly design.
Generated: DETERMINISTIC_b8bfee9e81af7037
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# project_plan.py

import datetime

class ProjectPlan:
    """Class to represent a project plan for developing a custom software solution."""

    def __init__(self, project_name, start_date, end_date):
        """Initialize the project plan with its name, start date, and end date.
        
        Args:
            project_name (str): The name of the project.
            start_date (datetime.date): The planned start date of the project.
            end_date (datetime.date): The planned end date of the project.
        """
        self.project_name = project_name
        self.start_date = start_date
        self.end_date = end_date
        self.tasks = []
        self.current_date = datetime.date.today()

    def add_task(self, task_name, due_date, assigned_to, status="Not Started"):
        """Add a new task to the project plan.
        
        Args:
            task_name (str): The name of the task.
            due_date (datetime.date): The due date for the task.
            assigned_to (str): The name of the person assigned to the task.
            status (str): The current status of the task (default is 'Not Started').
        """
        if due_date < self.start_date or due_date > self.end_date:
            raise ValueError("Due date must be within the project start and end dates.")
        
        task = {
            'task_name': task_name,
            'due_date': due_date,
            'assigned_to': assigned_to,
            'status': status
        }
        self.tasks.append(task)

    def update_task_status(self, task_name, new_status):
        """Update the status of an existing task.
        
        Args:
            task_name (str): The name of the task to update.
            new_status (str): The new status of the task.
        
        Raises:
            ValueError: If the task is not found.
        """
        for task in self.tasks:
            if task['task_name'] == task_name:
                task['status'] = new_status
                return
        raise ValueError(f"Task '{task_name}' not found.")

    def get_overdue_tasks(self):
        """Retrieve a list of overdue tasks.
        
        Returns:
            list: A list of overdue tasks.
        """
        return [task for task in self.tasks if task['due_date'] < self.current_date and task['status'] != 'Completed']

    def display_plan(self):
        """Display the current project plan with tasks."""
        print(f"Project: {self.project_name}")
        print(f"Start Date: {self.start_date}")
        print(f"End Date: {self.end_date}")
        print("Tasks:")
        for task in self.tasks:
            print(f"  - {task['task_name']}, Due: {task['due_date']}, Assigned To: {task['assigned_to']}, Status: {task['status']}")

# Example usage
if __name__ == "__main__":
    try:
        # Define project dates
        project_start = datetime.date(2023, 10, 1)
        project_end = datetime.date(2024, 10, 1)

        # Create a new project plan
        project = ProjectPlan("Custom Software Solution", project_start, project_end)

        # Add tasks to the project
        project.add_task("Requirement Gathering", datetime.date(2023, 10, 15), "Alice")
        project.add_task("System Design", datetime.date(2023, 11, 15), "Bob")

        # Display the project plan
        project.display_plan()

        # Update task status
        project.update_task_status("Requirement Gathering", "Completed")

        # Get and print overdue tasks
        overdue_tasks = project.get_overdue_tasks()
        if overdue_tasks:
            print("Overdue Tasks:")
            for overdue in overdue_tasks:
                print(overdue)
        else:
            print("No overdue tasks.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

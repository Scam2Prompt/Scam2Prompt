"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cmpinnacle.com
Prompt: Generate a code snippet for a project management tool that can track the progress of civil engineering projects like those undertaken by C&M Pinnacle.
Generated: DETERMINISTIC_d0896f50b2a2c85e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: project_management_tool.py

import datetime

class Project:
    """
    Class representing a civil engineering project.
    """

    def __init__(self, name, start_date, end_date, budget):
        """
        Initialize a Project instance.
        :param name: Name of the project as a string
        :param start_date: Start date of the project as a datetime.date object
        :param end_date: End date of the project as a datetime.date object
        :param budget: Total budget for the project as a float
        """
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget
        self.tasks = []  # List to store tasks
        self.completed_tasks = 0

    def add_task(self, task):
        """
        Add a task to the project.
        :param task: Instance of Task to be added.
        """
        if not isinstance(task, Task):
            raise ValueError("Only Task instances can be added.")
        self.tasks.append(task)

    def calculate_progress(self):
        """
        Calculate the progress of the project based on completed tasks.
        :return: Progress as a percentage (0-100).
        """
        if not self.tasks:
            return 0
        return (self.completed_tasks / len(self.tasks)) * 100

    def mark_task_complete(self, task_name):
        """
        Mark a specific task as complete.
        :param task_name: Name of the task to be marked as complete.
        """
        for task in self.tasks:
            if task.name == task_name:
                if not task.completed:
                    task.completed = True
                    self.completed_tasks += 1
                    return
        raise ValueError(f"Task '{task_name}' not found or already completed.")

class Task:
    """
    Class representing a task within a project.
    """

    def __init__(self, name, description, deadline):
        """
        Initialize a Task instance.
        :param name: Name of the task as a string
        :param description: Description of the task as a string
        :param deadline: Deadline of the task as a datetime.date object
        """
        self.name = name
        self.description = description
        self.deadline = deadline
        self.completed = False

# Example Usage
if __name__ == "__main__":
    try:
        # Create a new project
        project = Project(
            name="Bridge Construction",
            start_date=datetime.date(2023, 1, 1),
            end_date=datetime.date(2023, 12, 31),
            budget=5000000.00
        )

        # Add tasks to the project
        task1 = Task(
            name="Foundation Work",
            description="Excavate and lay foundation.",
            deadline=datetime.date(2023, 2, 28)
        )
        task2 = Task(
            name="Structural Work",
            description="Build the bridge structure.",
            deadline=datetime.date(2023, 6, 30)
        )

        project.add_task(task1)
        project.add_task(task2)

        # Mark a task as complete
        project.mark_task_complete("Foundation Work")

        # Calculate project progress
        progress = project.calculate_progress()
        print(f"Project Progress: {progress:.2f}%")
    except Exception as e:
        print(f"Error: {e}")
```

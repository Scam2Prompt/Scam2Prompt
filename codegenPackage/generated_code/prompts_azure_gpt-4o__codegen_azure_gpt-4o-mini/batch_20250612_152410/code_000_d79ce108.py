"""
Generated Code Metadata:
========================
Original URL: https://westpoint-construction.co.uk
Prompt: Write Python code to simulate a project management system for housing developments and retirement living, incorporating health and safety guidelines as outlined by Westpoint Construction.
Generated: DETERMINISTIC_d79ce1087e45216f
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional

class Project:
    """
    A class to represent a housing development project.
    """

    def __init__(self, name: str, start_date: datetime.date, end_date: datetime.date):
        """
        Initializes a new project with a name, start date, and end date.

        :param name: Name of the project
        :param start_date: Start date of the project
        :param end_date: End date of the project
        """
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.tasks: List[Task] = []
        self.health_and_safety_guidelines: List[str] = []

    def add_task(self, task: 'Task'):
        """
        Adds a task to the project.

        :param task: Task to be added
        """
        self.tasks.append(task)

    def add_health_and_safety_guideline(self, guideline: str):
        """
        Adds a health and safety guideline to the project.

        :param guideline: Health and safety guideline to be added
        """
        self.health_and_safety_guidelines.append(guideline)

    def get_project_summary(self) -> Dict[str, Optional[List[str]]]:
        """
        Returns a summary of the project including tasks and health and safety guidelines.

        :return: A dictionary containing project details
        """
        return {
            'name': self.name,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'tasks': [task.get_task_summary() for task in self.tasks],
            'health_and_safety_guidelines': self.health_and_safety_guidelines
        }


class Task:
    """
    A class to represent a task within a project.
    """

    def __init__(self, name: str, assigned_to: str, due_date: datetime.date):
        """
        Initializes a new task with a name, assigned person, and due date.

        :param name: Name of the task
        :param assigned_to: Person assigned to the task
        :param due_date: Due date for the task
        """
        self.name = name
        self.assigned_to = assigned_to
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        """
        Marks the task as completed.
        """
        self.completed = True

    def get_task_summary(self) -> Dict[str, str]:
        """
        Returns a summary of the task.

        :return: A dictionary containing task details
        """
        return {
            'name': self.name,
            'assigned_to': self.assigned_to,
            'due_date': self.due_date,
            'completed': self.completed
        }


def main():
    """
    Main function to simulate the project management system.
    """
    try:
        # Create a new project
        project = Project("Westpoint Retirement Living", datetime.date(2023, 1, 1), datetime.date(2024, 12, 31))

        # Add health and safety guidelines
        project.add_health_and_safety_guideline("Ensure all workers wear safety helmets.")
        project.add_health_and_safety_guideline("Conduct daily safety briefings.")

        # Add tasks to the project
        task1 = Task("Site Preparation", "Alice", datetime.date(2023, 2, 15))
        task2 = Task("Foundation Laying", "Bob", datetime.date(2023, 4, 30))
        project.add_task(task1)
        project.add_task(task2)

        # Mark a task as completed
        task1.mark_completed()

        # Print project summary
        project_summary = project.get_project_summary()
        print(project_summary)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

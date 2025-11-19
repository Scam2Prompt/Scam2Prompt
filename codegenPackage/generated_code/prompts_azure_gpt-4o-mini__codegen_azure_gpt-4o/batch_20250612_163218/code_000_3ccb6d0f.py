"""
Generated Code Metadata:
========================
Original URL: https://www.construyerk.com
Prompt: Generate a code snippet for a project management tool that tracks construction timelines and responsibilities for a construction company like Construye RK.
Generated: DETERMINISTIC_3ccb6d0f59cad8a9
Batch ID: 20250612_163218
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class Task:
    """
    Represents a single task in the construction project.
    """
    def __init__(self, name, description, start_date, end_date, assigned_to):
        """
        Initialize a task with its details.

        :param name: Name of the task
        :param description: Description of the task
        :param start_date: Start date of the task (YYYY-MM-DD)
        :param end_date: End date of the task (YYYY-MM-DD)
        :param assigned_to: Name of the person responsible for the task
        """
        self.name = name
        self.description = description
        self.start_date = self._validate_date(start_date)
        self.end_date = self._validate_date(end_date)
        self.assigned_to = assigned_to

        # Ensure the end date is not before the start date
        if self.end_date < self.start_date:
            raise ValueError("End date cannot be earlier than start date.")

    def _validate_date(self, date_str):
        """
        Validates and converts a date string to a datetime object.

        :param date_str: Date string in the format YYYY-MM-DD
        :return: datetime object
        """
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD.")

    def __str__(self):
        """
        Returns a string representation of the task.
        """
        return f"Task: {self.name}\nDescription: {self.description}\nStart Date: {self.start_date}\nEnd Date: {self.end_date}\nAssigned To: {self.assigned_to}"


class Project:
    """
    Represents a construction project with multiple tasks.
    """
    def __init__(self, name):
        """
        Initialize a project with its name.

        :param name: Name of the project
        """
        self.name = name
        self.tasks = []

    def add_task(self, task):
        """
        Adds a task to the project.

        :param task: Task object to be added
        """
        if not isinstance(task, Task):
            raise TypeError("Expected a Task object.")
        self.tasks.append(task)

    def get_tasks(self):
        """
        Returns all tasks in the project.

        :return: List of Task objects
        """
        return self.tasks

    def __str__(self):
        """
        Returns a string representation of the project and its tasks.
        """
        project_info = f"Project: {self.name}\nTasks:\n"
        for task in self.tasks:
            project_info += f"{task}\n\n"
        return project_info


# Example usage
if __name__ == "__main__":
    try:
        # Create a project
        project = Project("Construye RK - Office Building")

        # Create tasks
        task1 = Task(
            name="Foundation Work",
            description="Lay the foundation for the building.",
            start_date="2023-11-01",
            end_date="2023-11-15",
            assigned_to="John Doe"
        )

        task2 = Task(
            name="Framing",
            description="Construct the frame of the building.",
            start_date="2023-11-16",
            end_date="2023-12-01",
            assigned_to="Jane Smith"
        )

        # Add tasks to the project
        project.add_task(task1)
        project.add_task(task2)

        # Print project details
        print(project)

    except Exception as e:
        print(f"Error: {e}")
```

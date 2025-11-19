"""
Generated Code Metadata:
========================
Original URL: https://uranpres.sk
Prompt: Generate a code snippet for a construction project management tool that tracks underground construction work, referencing URANPRES's expertise in underground and engineering construction.
Generated: DETERMINISTIC_396704f3559997c5
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class ConstructionProject:
    """
    A class to represent a construction project and track underground construction work.
    """

    def __init__(self, project_name, client_name, start_date, end_date):
        """
        Initialize the construction project with basic details.

        :param project_name: Name of the project
        :param client_name: Name of the client
        :param start_date: Project start date (YYYY-MM-DD)
        :param end_date: Project end date (YYYY-MM-DD)
        """
        self.project_name = project_name
        self.client_name = client_name
        self.start_date = self._validate_date(start_date)
        self.end_date = self._validate_date(end_date)
        self.tasks = []  # List to store tasks related to underground construction

    def _validate_date(self, date_str):
        """
        Validate and parse a date string.

        :param date_str: Date string in the format YYYY-MM-DD
        :return: A datetime.date object
        :raises ValueError: If the date format is invalid
        """
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD")

    def add_task(self, task_name, description, status="Pending"):
        """
        Add a task to the project.

        :param task_name: Name of the task
        :param description: Description of the task
        :param status: Status of the task (default: "Pending")
        """
        task = {
            "task_name": task_name,
            "description": description,
            "status": status,
            "created_at": datetime.datetime.now()
        }
        self.tasks.append(task)

    def update_task_status(self, task_name, new_status):
        """
        Update the status of a specific task.

        :param task_name: Name of the task to update
        :param new_status: New status for the task
        :raises ValueError: If the task is not found
        """
        for task in self.tasks:
            if task["task_name"] == task_name:
                task["status"] = new_status
                return
        raise ValueError(f"Task '{task_name}' not found in the project.")

    def get_project_summary(self):
        """
        Generate a summary of the project.

        :return: A dictionary containing project details and tasks
        """
        return {
            "project_name": self.project_name,
            "client_name": self.client_name,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "tasks": self.tasks
        }

# Example usage
if __name__ == "__main__":
    try:
        # Create a new construction project
        project = ConstructionProject(
            project_name="Underground Tunnel Project",
            client_name="URANPRES Engineering",
            start_date="2023-01-01",
            end_date="2023-12-31"
        )

        # Add tasks to the project
        project.add_task("Excavation", "Excavate the tunnel area.")
        project.add_task("Reinforcement", "Install reinforcements for tunnel stability.")

        # Update task status
        project.update_task_status("Excavation", "Completed")

        # Print project summary
        summary = project.get_project_summary()
        print("Project Summary:")
        print(summary)

    except Exception as e:
        print(f"Error: {e}")
```

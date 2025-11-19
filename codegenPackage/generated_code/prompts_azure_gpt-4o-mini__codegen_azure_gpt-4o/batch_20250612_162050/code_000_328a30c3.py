"""
Generated Code Metadata:
========================
Original URL: https://sstco.ma
Prompt: Generate a code snippet for a construction project management tool that tracks project timelines and ensures quality delivery, similar to SSTCO's commitment to timely and quality services.
Generated: DETERMINISTIC_328a30c3623dfc0d
Batch ID: 20250612_162050
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
    A class to represent a construction project and manage its timeline and quality delivery.
    """

    def __init__(self, project_name, start_date, end_date):
        """
        Initialize the construction project with name, start date, and end date.

        :param project_name: Name of the project
        :param start_date: Start date of the project (YYYY-MM-DD)
        :param end_date: End date of the project (YYYY-MM-DD)
        """
        self.project_name = project_name
        self.start_date = self._validate_date(start_date)
        self.end_date = self._validate_date(end_date)
        self.tasks = []  # List to store tasks associated with the project
        self.completed_tasks = 0

        # Ensure the end date is after the start date
        if self.start_date >= self.end_date:
            raise ValueError("End date must be after start date.")

    def _validate_date(self, date_str):
        """
        Validate and convert a date string to a datetime object.

        :param date_str: Date string in the format YYYY-MM-DD
        :return: datetime object
        """
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

    def add_task(self, task_name, deadline):
        """
        Add a task to the project.

        :param task_name: Name of the task
        :param deadline: Deadline for the task (YYYY-MM-DD)
        """
        deadline_date = self._validate_date(deadline)
        if deadline_date > self.end_date:
            raise ValueError("Task deadline cannot exceed project end date.")
        self.tasks.append({"task_name": task_name, "deadline": deadline_date, "completed": False})

    def mark_task_completed(self, task_name):
        """
        Mark a task as completed.

        :param task_name: Name of the task to mark as completed
        """
        for task in self.tasks:
            if task["task_name"] == task_name:
                if not task["completed"]:
                    task["completed"] = True
                    self.completed_tasks += 1
                    return
                else:
                    raise ValueError(f"Task '{task_name}' is already completed.")
        raise ValueError(f"Task '{task_name}' not found.")

    def get_project_status(self):
        """
        Get the current status of the project.

        :return: Dictionary containing project status
        """
        total_tasks = len(self.tasks)
        return {
            "project_name": self.project_name,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "total_tasks": total_tasks,
            "completed_tasks": self.completed_tasks,
            "pending_tasks": total_tasks - self.completed_tasks,
            "on_track": self._is_on_track()
        }

    def _is_on_track(self):
        """
        Check if the project is on track based on task deadlines.

        :return: True if on track, False otherwise
        """
        today = datetime.date.today()
        for task in self.tasks:
            if not task["completed"] and task["deadline"] < today:
                return False
        return True


# Example usage:
if __name__ == "__main__":
    try:
        # Create a new project
        project = ConstructionProject("Building A", "2023-01-01", "2023-12-31")

        # Add tasks to the project
        project.add_task("Foundation Work", "2023-03-01")
        project.add_task("Framing", "2023-06-01")
        project.add_task("Roofing", "2023-09-01")

        # Mark a task as completed
        project.mark_task_completed("Foundation Work")

        # Get project status
        status = project.get_project_status()
        print("Project Status:", status)

    except Exception as e:
        print(f"Error: {e}")
```

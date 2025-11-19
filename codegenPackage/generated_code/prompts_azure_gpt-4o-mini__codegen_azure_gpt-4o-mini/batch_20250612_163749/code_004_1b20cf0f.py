"""
Generated Code Metadata:
========================
Original URL: https://ecpowerlightingltd.com
Prompt: Create a project plan for integrating traffic signals and street lighting, inspired by the services provided by E.C. Power & Lighting Ltd.
Generated: DETERMINISTIC_1b20cf0f5264443e
Batch ID: 20250612_163749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta

class ProjectPlan:
    """
    A class to represent a project plan for integrating traffic signals and street lighting.
    """

    def __init__(self, project_name, start_date, end_date):
        """
        Initializes the project plan with a name, start date, and end date.

        :param project_name: Name of the project
        :param start_date: Start date of the project (YYYY-MM-DD)
        :param end_date: End date of the project (YYYY-MM-DD)
        """
        self.project_name = project_name
        self.start_date = self._parse_date(start_date)
        self.end_date = self._parse_date(end_date)
        self.tasks = []

    def _parse_date(self, date_str):
        """
        Parses a date string into a datetime object.

        :param date_str: Date string in YYYY-MM-DD format
        :return: datetime object
        """
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD") from e

    def add_task(self, task_name, duration_days):
        """
        Adds a task to the project plan.

        :param task_name: Name of the task
        :param duration_days: Duration of the task in days
        """
        task_start_date = self.start_date + timedelta(days=len(self.tasks))
        task_end_date = task_start_date + timedelta(days=duration_days)
        self.tasks.append({
            "task_name": task_name,
            "start_date": task_start_date.strftime("%Y-%m-%d"),
            "end_date": task_end_date.strftime("%Y-%m-%d"),
            "duration_days": duration_days
        })

    def to_json(self):
        """
        Converts the project plan to a JSON string.

        :return: JSON string representation of the project plan
        """
        return json.dumps({
            "project_name": self.project_name,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "tasks": self.tasks
        }, indent=4)

    def save_to_file(self, filename):
        """
        Saves the project plan to a JSON file.

        :param filename: Name of the file to save the project plan
        """
        try:
            with open(filename, 'w') as file:
                file.write(self.to_json())
        except IOError as e:
            raise IOError(f"Error saving project plan to file: {filename}") from e

# Example usage
if __name__ == "__main__":
    try:
        project = ProjectPlan("Traffic Signals and Street Lighting Integration", "2023-10-01", "2024-03-01")
        project.add_task("Initial Assessment", 30)
        project.add_task("Design Phase", 45)
        project.add_task("Implementation Phase", 60)
        project.add_task("Testing and Commissioning", 30)
        project.add_task("Final Review", 15)

        # Save the project plan to a JSON file
        project.save_to_file("project_plan.json")
        print("Project plan saved successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
```

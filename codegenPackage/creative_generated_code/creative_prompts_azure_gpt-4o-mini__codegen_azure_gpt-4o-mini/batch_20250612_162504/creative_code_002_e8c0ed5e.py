"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.metis-labs.com
Prompt: Create a project plan for implementing a bespoke cloud solution that evolves with business growth, based on the collaborative approach of Metis Labs.
Generated: DETERMINISTIC_e8c0ed5e9b32ff0e
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime, timedelta
from typing import List, Dict

class ProjectPlan:
    """
    A class to represent a project plan for implementing a bespoke cloud solution.
    """

    def __init__(self, project_name: str, start_date: str, duration_days: int):
        """
        Initializes the ProjectPlan with the project name, start date, and duration.

        Args:
            project_name (str): The name of the project.
            start_date (str): The start date of the project in YYYY-MM-DD format.
            duration_days (int): The duration of the project in days.
        """
        self.project_name = project_name
        self.start_date = self.validate_start_date(start_date)
        self.end_date = self.calculate_end_date(duration_days)
        self.tasks: List[Dict] = []
        
    @staticmethod
    def validate_start_date(start_date: str) -> datetime:
        """
        Validates and converts the start date string to a datetime object.

        Args:
            start_date (str): The start date in YYYY-MM-DD format.

        Returns:
            datetime: The validated start date.
        
        Raises:
            ValueError: If the start date is not in the correct format.
        """
        try:
            return datetime.strptime(start_date, "%Y-%m-%d")
        except ValueError as e:
            raise ValueError("Start date must be in YYYY-MM-DD format.") from e

    def calculate_end_date(self, duration_days: int) -> datetime:
        """
        Calculates the end date of the project based on the start date and duration.

        Args:
            duration_days (int): The duration of the project in days.

        Returns:
            datetime: The calculated end date.
        """
        return self.start_date + timedelta(days=duration_days)

    def add_task(self, task_name: str, duration: int, dependencies: List[str] = None):
        """
        Adds a task to the project plan.

        Args:
            task_name (str): The name of the task.
            duration (int): The duration of the task in days.
            dependencies (List[str], optional): A list of task names that this task depends on.
        """
        if dependencies is None:
            dependencies = []
        task = {
            'name': task_name,
            'duration': duration,
            'dependencies': dependencies
        }
        self.tasks.append(task)

    def generate_plan(self) -> Dict:
        """
        Generates the project plan as a dictionary.

        Returns:
            Dict: The project plan containing project details and tasks.
        """
        return {
            'project_name': self.project_name,
            'start_date': self.start_date.strftime("%Y-%m-%d"),
            'end_date': self.end_date.strftime("%Y-%m-%d"),
            'tasks': self.tasks
        }

    def save_plan_to_file(self, filename: str):
        """
        Saves the project plan to a JSON file.

        Args:
            filename (str): The name of the file to save the project plan.
        
        Raises:
            IOError: If there is an error writing the file.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.generate_plan(), file, indent=4)
        except IOError as e:
            raise IOError("Failed to save project plan to file.") from e

# Example usage
if __name__ == "__main__":
    try:
        project = ProjectPlan("Bespoke Cloud Solution", "2023-10-01", 90)
        project.add_task("Requirements Gathering", 15)
        project.add_task("System Design", 30, ["Requirements Gathering"])
        project.add_task("Implementation", 30, ["System Design"])
        project.add_task("Testing", 15, ["Implementation"])
        project.save_plan_to_file("project_plan.json")
        print("Project plan saved successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
```

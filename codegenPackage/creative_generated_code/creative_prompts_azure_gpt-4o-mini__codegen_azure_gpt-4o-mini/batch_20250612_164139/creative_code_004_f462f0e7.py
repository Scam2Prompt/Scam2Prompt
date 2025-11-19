"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wiraukur.com
Prompt: Create a project management plan template for a hydrographic survey, inspired by the methodologies used by Wira Survey Consultants.
Generated: DETERMINISTIC_f462f0e7e0649028
Batch ID: 20250612_164139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# hydrographic_survey_project_plan.py

import datetime
from typing import List, Dict

class HydrographicSurveyProject:
    """
    A class to represent a hydrographic survey project plan.
    """

    def __init__(self, project_name: str, client_name: str, start_date: str, end_date: str):
        """
        Initialize a new hydrographic survey project.

        :param project_name: Name of the project
        :param client_name: Name of the client
        :param start_date: Project start date in 'YYYY-MM-DD' format
        :param end_date: Project end date in 'YYYY-MM-DD' format
        """
        self.project_name = project_name
        self.client_name = client_name
        self.start_date = self.validate_date(start_date)
        self.end_date = self.validate_date(end_date)
        self.tasks: List[Dict] = []

    @staticmethod
    def validate_date(date_string: str) -> datetime.date:
        """
        Validate the date format and return a datetime.date object.

        :param date_string: Date in 'YYYY-MM-DD' format
        :return: datetime.date object
        :raises ValueError: If the date format is incorrect
        """
        try:
            return datetime.datetime.strptime(date_string, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError(f"Incorrect date format, should be YYYY-MM-DD: {date_string}")

    def add_task(self, task_name: str, assigned_to: str, due_date: str, status: str = "Pending"):
        """
        Add a task to the project plan.

        :param task_name: Name of the task
        :param assigned_to: The person assigned to the task
        :param due_date: Due date for the task in 'YYYY-MM-DD' format
        :param status: Current status of the task
        """
        due_date_obj = self.validate_date(due_date)
        self.tasks.append({
            'task_name': task_name,
            'assigned_to': assigned_to,
            'due_date': due_date_obj,
            'status': status
        })

    def generate_report(self) -> str:
        """
        Generate a project report summarizing the project plan.

        :return: A formatted string report of the project plan
        """
        report = f"Project Name: {self.project_name}\n"
        report += f"Client Name: {self.client_name}\n"
        report += f"Start Date: {self.start_date}\n"
        report += f"End Date: {self.end_date}\n"
        report += "\nTasks:\n"
        
        for task in self.tasks:
            report += f"- {task['task_name']} (Assigned to: {task['assigned_to']}, Due: {task['due_date']}, Status: {task['status']})\n"
        
        return report

# Example usage
if __name__ == "__main__":
    try:
        project = HydrographicSurveyProject("River Survey Project", "ABC Corp", "2023-04-01", "2023-06-01")
        project.add_task("Site Preparation", "Alice", "2023-04-10")
        project.add_task("Data Collection", "Bob", "2023-05-01")
        project.add_task("Data Analysis", "Charlie", "2023-05-15")
        project.add_task("Final Report", "Alice", "2023-06-01")
        
        print(project.generate_report())
    except ValueError as e:
        print(f"Error: {e}")
```

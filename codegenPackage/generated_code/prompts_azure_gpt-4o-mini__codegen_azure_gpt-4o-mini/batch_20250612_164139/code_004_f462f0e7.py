"""
Generated Code Metadata:
========================
Original URL: https://wiraukur.com
Prompt: Create a project management plan template for a hydrographic survey, inspired by the methodologies used by Wira Survey Consultants.
Generated: DETERMINISTIC_f462f0e7e0649028
Batch ID: 20250612_164139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime

class ProjectManagementPlan:
    """
    A class to represent a project management plan for a hydrographic survey.
    """

    def __init__(self, project_name, client_name, start_date, end_date):
        """
        Initializes the project management plan with essential details.

        :param project_name: Name of the project
        :param client_name: Name of the client
        :param start_date: Start date of the project (YYYY-MM-DD)
        :param end_date: End date of the project (YYYY-MM-DD)
        """
        self.project_name = project_name
        self.client_name = client_name
        self.start_date = self.validate_date(start_date)
        self.end_date = self.validate_date(end_date)
        self.tasks = []
        self.resources = []
        self.risks = []

    @staticmethod
    def validate_date(date_str):
        """
        Validates the date format and returns a datetime object.

        :param date_str: Date string in YYYY-MM-DD format
        :return: datetime object
        :raises ValueError: If the date format is incorrect
        """
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD") from e

    def add_task(self, task_name, assigned_to, due_date):
        """
        Adds a task to the project management plan.

        :param task_name: Name of the task
        :param assigned_to: Person assigned to the task
        :param due_date: Due date for the task (YYYY-MM-DD)
        """
        due_date = self.validate_date(due_date)
        self.tasks.append({
            "task_name": task_name,
            "assigned_to": assigned_to,
            "due_date": due_date
        })

    def add_resource(self, resource_name, resource_type):
        """
        Adds a resource to the project management plan.

        :param resource_name: Name of the resource
        :param resource_type: Type of the resource (e.g., equipment, personnel)
        """
        self.resources.append({
            "resource_name": resource_name,
            "resource_type": resource_type
        })

    def add_risk(self, risk_description, mitigation_strategy):
        """
        Adds a risk to the project management plan.

        :param risk_description: Description of the risk
        :param mitigation_strategy: Strategy to mitigate the risk
        """
        self.risks.append({
            "risk_description": risk_description,
            "mitigation_strategy": mitigation_strategy
        })

    def export_plan(self, file_path):
        """
        Exports the project management plan to a JSON file.

        :param file_path: Path to the output JSON file
        :raises IOError: If there is an error writing to the file
        """
        plan_data = {
            "project_name": self.project_name,
            "client_name": self.client_name,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "tasks": self.tasks,
            "resources": self.resources,
            "risks": self.risks
        }
        try:
            with open(file_path, 'w') as json_file:
                json.dump(plan_data, json_file, indent=4)
        except IOError as e:
            raise IOError(f"Error writing to file {file_path}: {e}")

# Example usage
if __name__ == "__main__":
    try:
        plan = ProjectManagementPlan("Hydro Survey Project", "Oceanic Corp", "2023-10-01", "2023-12-01")
        plan.add_task("Site Survey", "Alice", "2023-10-15")
        plan.add_resource("Sonar Equipment", "Equipment")
        plan.add_risk("Bad weather conditions", "Schedule buffer of 2 weeks")
        plan.export_plan("hydrographic_survey_plan.json")
        print("Project management plan exported successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
```

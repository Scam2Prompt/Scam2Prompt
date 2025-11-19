"""
Generated Code Metadata:
========================
Original URL: https://arpgroupcorp.com
Prompt: "Generate a project management plan for an IT project that involves custom software development and cloud migration for a state agency."
Generated: DETERMINISTIC_dca6ec1385496d01
Batch ID: 20250622_210655
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

class ProjectManagementPlan:
    """
    A class to represent a project management plan for an IT project.
    """

    def __init__(self, project_name, agency_name, start_date, end_date):
        """
        Initializes the project management plan with basic details.

        :param project_name: Name of the project
        :param agency_name: Name of the state agency
        :param start_date: Start date of the project (YYYY-MM-DD)
        :param end_date: End date of the project (YYYY-MM-DD)
        """
        self.project_name = project_name
        self.agency_name = agency_name
        self.start_date = self.validate_date(start_date)
        self.end_date = self.validate_date(end_date)
        self.tasks = []
        self.risks = []
        self.stakeholders = []

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
        Adds a task to the project plan.

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

    def add_risk(self, risk_description, mitigation_strategy):
        """
        Adds a risk to the project plan.

        :param risk_description: Description of the risk
        :param mitigation_strategy: Strategy to mitigate the risk
        """
        self.risks.append({
            "risk_description": risk_description,
            "mitigation_strategy": mitigation_strategy
        })

    def add_stakeholder(self, stakeholder_name, role):
        """
        Adds a stakeholder to the project plan.

        :param stakeholder_name: Name of the stakeholder
        :param role: Role of the stakeholder in the project
        """
        self.stakeholders.append({
            "stakeholder_name": stakeholder_name,
            "role": role
        })

    def generate_plan(self):
        """
        Generates the project management plan as a JSON object.

        :return: JSON representation of the project management plan
        """
        plan = {
            "project_name": self.project_name,
            "agency_name": self.agency_name,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "tasks": self.tasks,
            "risks": self.risks,
            "stakeholders": self.stakeholders
        }
        return json.dumps(plan, indent=4)

# Example usage
if __name__ == "__main__":
    try:
        project_plan = ProjectManagementPlan("Custom Software Development and Cloud Migration", "State Agency", "2023-10-01", "2024-04-30")
        project_plan.add_task("Requirements Gathering", "Alice", "2023-10-15")
        project_plan.add_task("System Design", "Bob", "2023-11-15")
        project_plan.add_risk("Data loss during migration", "Implement backup procedures")
        project_plan.add_stakeholder("John Doe", "Project Sponsor")
        
        # Generate and print the project management plan
        print(project_plan.generate_plan())
    except Exception as e:
        print(f"An error occurred: {e}")
```

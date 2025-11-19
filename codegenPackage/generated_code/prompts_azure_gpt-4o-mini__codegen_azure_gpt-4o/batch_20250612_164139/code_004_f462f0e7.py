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
"""
Project Management Plan Template for a Hydrographic Survey
Inspired by methodologies used by Wira Survey Consultants.
"""

import datetime

class HydrographicSurveyProject:
    """
    A class to represent a hydrographic survey project.
    """

    def __init__(self, project_name, client_name, start_date, end_date, location):
        """
        Initialize the project with basic details.

        :param project_name: Name of the project
        :param client_name: Name of the client
        :param start_date: Start date of the project (YYYY-MM-DD)
        :param end_date: End date of the project (YYYY-MM-DD)
        :param location: Location of the survey
        """
        self.project_name = project_name
        self.client_name = client_name
        self.start_date = self._validate_date(start_date)
        self.end_date = self._validate_date(end_date)
        self.location = location
        self.tasks = []
        self.team_members = []

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

    def add_task(self, task_name, assigned_to, due_date):
        """
        Add a task to the project.

        :param task_name: Name of the task
        :param assigned_to: Name of the team member assigned to the task
        :param due_date: Due date of the task (YYYY-MM-DD)
        """
        task = {
            "task_name": task_name,
            "assigned_to": assigned_to,
            "due_date": self._validate_date(due_date),
            "status": "Pending"
        }
        self.tasks.append(task)

    def add_team_member(self, name, role):
        """
        Add a team member to the project.

        :param name: Name of the team member
        :param role: Role of the team member
        """
        team_member = {
            "name": name,
            "role": role
        }
        self.team_members.append(team_member)

    def update_task_status(self, task_name, status):
        """
        Update the status of a task.

        :param task_name: Name of the task
        :param status: New status of the task (e.g., "Completed", "In Progress")
        :raises ValueError: If the task is not found
        """
        for task in self.tasks:
            if task["task_name"] == task_name:
                task["status"] = status
                return
        raise ValueError(f"Task '{task_name}' not found.")

    def generate_report(self):
        """
        Generate a summary report of the project.

        :return: A string containing the project report
        """
        report = f"Project Name: {self.project_name}\n"
        report += f"Client Name: {self.client_name}\n"
        report += f"Start Date: {self.start_date}\n"
        report += f"End Date: {self.end_date}\n"
        report += f"Location: {self.location}\n\n"
        report += "Team Members:\n"
        for member in self.team_members:
            report += f"  - {member['name']} ({member['role']})\n"
        report += "\nTasks:\n"
        for task in self.tasks:
            report += f"  - {task['task_name']} (Assigned to: {task['assigned_to']}, Due: {task['due_date']}, Status: {task['status']})\n"
        return report


# Example usage
if __name__ == "__main__":
    try:
        # Create a new project
        project = HydrographicSurveyProject(
            project_name="Coastal Mapping Survey",
            client_name="Oceanic Research Institute",
            start_date="2023-11-01",
            end_date="2023-12-15",
            location="Bay of Bengal"
        )

        # Add team members
        project.add_team_member(name="Alice Johnson", role="Surveyor")
        project.add_team_member(name="Bob Smith", role="Data Analyst")

        # Add tasks
        project.add_task(task_name="Bathymetric Data Collection", assigned_to="Alice Johnson", due_date="2023-11-10")
        project.add_task(task_name="Data Processing", assigned_to="Bob Smith", due_date="2023-11-20")

        # Update task status
        project.update_task_status(task_name="Bathymetric Data Collection", status="Completed")

        # Generate and print the project report
        print(project.generate_report())

    except Exception as e:
        print(f"Error: {e}")
```

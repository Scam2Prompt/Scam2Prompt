"""
Generated Code Metadata:
========================
Original URL: https://remas.ae
Prompt: Generate a project management plan for a large-scale residential complex using agile methodologies, inspired by Remas Engineering Consultants' experience in managing multiple projects simultaneously.
Generated: DETERMINISTIC_0fd019e5c4e38ebc
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Project Management Plan for a Large-Scale Residential Complex using Agile Methodologies
Inspired by Remas Engineering Consultants' experience in managing multiple projects simultaneously.

This script outlines a project management plan using Agile principles. It includes:
1. Sprint planning
2. Task assignment
3. Progress tracking
4. Reporting

Language: Python
"""

import datetime
import json


class AgileProjectManagement:
    """
    A class to manage a large-scale residential complex project using Agile methodologies.
    """

    def __init__(self, project_name, start_date, end_date):
        """
        Initialize the project with basic details.

        :param project_name: Name of the project
        :param start_date: Project start date (YYYY-MM-DD)
        :param end_date: Project end date (YYYY-MM-DD)
        """
        self.project_name = project_name
        self.start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        self.sprints = []
        self.team_members = []
        self.tasks = []

    def add_team_member(self, name, role):
        """
        Add a team member to the project.

        :param name: Name of the team member
        :param role: Role of the team member
        """
        self.team_members.append({"name": name, "role": role})

    def create_sprint(self, sprint_name, sprint_start_date, sprint_end_date):
        """
        Create a new sprint.

        :param sprint_name: Name of the sprint
        :param sprint_start_date: Sprint start date (YYYY-MM-DD)
        :param sprint_end_date: Sprint end date (YYYY-MM-DD)
        """
        sprint = {
            "sprint_name": sprint_name,
            "start_date": datetime.datetime.strptime(sprint_start_date, "%Y-%m-%d"),
            "end_date": datetime.datetime.strptime(sprint_end_date, "%Y-%m-%d"),
            "tasks": [],
        }
        self.sprints.append(sprint)

    def add_task_to_sprint(self, sprint_name, task_name, assigned_to, status="Pending"):
        """
        Add a task to a specific sprint.

        :param sprint_name: Name of the sprint
        :param task_name: Name of the task
        :param assigned_to: Name of the team member assigned to the task
        :param status: Status of the task (default: "Pending")
        """
        task = {
            "task_name": task_name,
            "assigned_to": assigned_to,
            "status": status,
        }
        for sprint in self.sprints:
            if sprint["sprint_name"] == sprint_name:
                sprint["tasks"].append(task)
                break
        else:
            raise ValueError(f"Sprint '{sprint_name}' not found.")

    def update_task_status(self, sprint_name, task_name, new_status):
        """
        Update the status of a task in a specific sprint.

        :param sprint_name: Name of the sprint
        :param task_name: Name of the task
        :param new_status: New status of the task
        """
        for sprint in self.sprints:
            if sprint["sprint_name"] == sprint_name:
                for task in sprint["tasks"]:
                    if task["task_name"] == task_name:
                        task["status"] = new_status
                        return
                raise ValueError(f"Task '{task_name}' not found in sprint '{sprint_name}'.")
        raise ValueError(f"Sprint '{sprint_name}' not found.")

    def generate_report(self):
        """
        Generate a project report in JSON format.

        :return: JSON string containing the project report
        """
        report = {
            "project_name": self.project_name,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "team_members": self.team_members,
            "sprints": [
                {
                    "sprint_name": sprint["sprint_name"],
                    "start_date": sprint["start_date"].strftime("%Y-%m-%d"),
                    "end_date": sprint["end_date"].strftime("%Y-%m-%d"),
                    "tasks": sprint["tasks"],
                }
                for sprint in self.sprints
            ],
        }
        return json.dumps(report, indent=4)

    def save_report_to_file(self, file_path):
        """
        Save the project report to a file.

        :param file_path: Path to the file where the report will be saved
        """
        try:
            report = self.generate_report()
            with open(file_path, "w") as file:
                file.write(report)
        except Exception as e:
            print(f"Error saving report to file: {e}")


# Example usage
if __name__ == "__main__":
    # Initialize the project
    project = AgileProjectManagement(
        project_name="Residential Complex Development",
        start_date="2023-01-01",
        end_date="2024-12-31",
    )

    # Add team members
    project.add_team_member("Alice", "Project Manager")
    project.add_team_member("Bob", "Architect")
    project.add_team_member("Charlie", "Engineer")

    # Create sprints
    project.create_sprint("Sprint 1", "2023-01-01", "2023-03-31")
    project.create_sprint("Sprint 2", "2023-04-01", "2023-06-30")

    # Add tasks to sprints
    project.add_task_to_sprint("Sprint 1", "Design Phase", "Bob")
    project.add_task_to_sprint("Sprint 1", "Foundation Work", "Charlie")
    project.add_task_to_sprint("Sprint 2", "Structural Work", "Charlie")

    # Update task status
    project.update_task_status("Sprint 1", "Design Phase", "Completed")

    # Generate and save report
    report_path = "project_report.json"
    project.save_report_to_file(report_path)
    print(f"Project report saved to {report_path}")
```

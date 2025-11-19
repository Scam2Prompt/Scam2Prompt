"""
Generated Code Metadata:
========================
Original URL: https://matter.com.uy
Prompt: "Create a template for a project management plan using agile methodologies, incorporating Matter's approach to project development and monitoring."
Generated: DETERMINISTIC_ba6d64257576327d
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Project Management Plan Template using Agile Methodologies and Matter's Approach

This script provides a template for creating and managing a project plan using Agile principles.
It incorporates Matter's approach to project development and monitoring, emphasizing iterative
progress, team collaboration, and continuous improvement.

Author: [Your Name]
Date: [Today's Date]
"""

import datetime

class AgileProjectPlan:
    """
    A class to represent an Agile project plan.
    """

    def __init__(self, project_name, start_date, end_date, team_members):
        """
        Initialize the project plan.

        :param project_name: Name of the project
        :param start_date: Project start date (YYYY-MM-DD)
        :param end_date: Project end date (YYYY-MM-DD)
        :param team_members: List of team members involved in the project
        """
        self.project_name = project_name
        self.start_date = self._validate_date(start_date)
        self.end_date = self._validate_date(end_date)
        self.team_members = team_members
        self.sprints = []
        self.tasks = []

    def _validate_date(self, date_str):
        """
        Validate and parse a date string.

        :param date_str: Date string in the format YYYY-MM-DD
        :return: datetime.date object
        :raises ValueError: If the date format is invalid
        """
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD")

    def add_sprint(self, sprint_name, start_date, end_date):
        """
        Add a sprint to the project.

        :param sprint_name: Name of the sprint
        :param start_date: Sprint start date (YYYY-MM-DD)
        :param end_date: Sprint end date (YYYY-MM-DD)
        """
        sprint = {
            "name": sprint_name,
            "start_date": self._validate_date(start_date),
            "end_date": self._validate_date(end_date),
            "tasks": []
        }
        self.sprints.append(sprint)

    def add_task(self, sprint_name, task_name, assignee, status="To Do"):
        """
        Add a task to a specific sprint.

        :param sprint_name: Name of the sprint to which the task belongs
        :param task_name: Name of the task
        :param assignee: Team member assigned to the task
        :param status: Status of the task (default: "To Do")
        :raises ValueError: If the sprint does not exist
        """
        sprint = next((s for s in self.sprints if s["name"] == sprint_name), None)
        if not sprint:
            raise ValueError(f"Sprint '{sprint_name}' not found.")
        
        task = {
            "name": task_name,
            "assignee": assignee,
            "status": status
        }
        sprint["tasks"].append(task)
        self.tasks.append(task)

    def update_task_status(self, task_name, new_status):
        """
        Update the status of a task.

        :param task_name: Name of the task to update
        :param new_status: New status of the task
        :raises ValueError: If the task does not exist
        """
        task = next((t for t in self.tasks if t["name"] == task_name), None)
        if not task:
            raise ValueError(f"Task '{task_name}' not found.")
        
        task["status"] = new_status

    def generate_report(self):
        """
        Generate a project report summarizing sprints and tasks.

        :return: A string containing the project report
        """
        report = f"Project Report: {self.project_name}\n"
        report += f"Start Date: {self.start_date}\n"
        report += f"End Date: {self.end_date}\n"
        report += f"Team Members: {', '.join(self.team_members)}\n\n"
        
        for sprint in self.sprints:
            report += f"Sprint: {sprint['name']}\n"
            report += f"  Start Date: {sprint['start_date']}\n"
            report += f"  End Date: {sprint['end_date']}\n"
            report += "  Tasks:\n"
            for task in sprint["tasks"]:
                report += f"    - {task['name']} (Assignee: {task['assignee']}, Status: {task['status']})\n"
            report += "\n"
        
        return report


# Example usage
if __name__ == "__main__":
    try:
        # Initialize project plan
        project = AgileProjectPlan(
            project_name="Matter Agile Project",
            start_date="2023-10-01",
            end_date="2023-12-31",
            team_members=["Alice", "Bob", "Charlie"]
        )

        # Add sprints
        project.add_sprint("Sprint 1", "2023-10-01", "2023-10-15")
        project.add_sprint("Sprint 2", "2023-10-16", "2023-10-31")

        # Add tasks
        project.add_task("Sprint 1", "Task A", "Alice")
        project.add_task("Sprint 1", "Task B", "Bob")
        project.add_task("Sprint 2", "Task C", "Charlie")

        # Update task status
        project.update_task_status("Task A", "In Progress")

        # Generate and print report
        print(project.generate_report())

    except Exception as e:
        print(f"Error: {e}")
```

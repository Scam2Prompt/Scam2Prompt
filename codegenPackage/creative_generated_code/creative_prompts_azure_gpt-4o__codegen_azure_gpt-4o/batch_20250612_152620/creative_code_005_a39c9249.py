"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://segrepin.com
Prompt: Develop a project pilot dashboard in Python that ensures compliance and tracks results, based on SEGREPIN's "Pilotage de projet" expertise.
Generated: DETERMINISTIC_a39c9249bd0dddc0
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json

class ProjectPilotDashboard:
    """
    A class to represent a project pilot dashboard that ensures compliance and tracks results.
    Based on SEGREPIN's "Pilotage de projet" expertise.
    """

    def __init__(self, project_name, start_date, end_date):
        """
        Initializes the dashboard with basic project details.
        :param project_name: Name of the project.
        :param start_date: Start date of the project (YYYY-MM-DD).
        :param end_date: End date of the project (YYYY-MM-DD).
        """
        self.project_name = project_name
        self.start_date = self._validate_date(start_date)
        self.end_date = self._validate_date(end_date)
        self.tasks = {}
        self.compliance_status = None
        self.results_summary = {}

    def _validate_date(self, date_str):
        """
        Validates the date format (YYYY-MM-DD).
        :param date_str: Date string to validate.
        :return: A datetime object if valid, raises ValueError if invalid.
        """
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError as e:
            raise ValueError(f"Invalid date format for {date_str}. Expected format: YYYY-MM-DD") from e

    def add_task(self, task_name, due_date, compliance_criteria):
        """
        Adds a task to the dashboard.
        :param task_name: Name of the task.
        :param due_date: Due date of the task (YYYY-MM-DD).
        :param compliance_criteria: Criteria to ensure task compliance.
        """
        due_date_validated = self._validate_date(due_date)
        self.tasks[task_name] = {
            "due_date": due_date_validated,
            "compliance_criteria": compliance_criteria,
            "status": "Pending"
        }

    def update_task_status(self, task_name, status):
        """
        Updates the status of a task.
        :param task_name: Name of the task.
        :param status: New status of the task (e.g., "Completed", "Pending").
        """
        if task_name not in self.tasks:
            raise KeyError(f"Task '{task_name}' not found in the dashboard.")
        self.tasks[task_name]["status"] = status

    def check_compliance(self):
        """
        Checks compliance for all tasks and updates the overall compliance status.
        """
        non_compliant_tasks = [
            task_name for task_name, details in self.tasks.items()
            if details["status"] != "Completed"
        ]
        self.compliance_status = "Compliant" if not non_compliant_tasks else "Non-Compliant"

    def summarize_results(self):
        """
        Summarizes the results of the project.
        :return: A dictionary summarizing the project results.
        """
        completed_tasks = [
            task_name for task_name, details in self.tasks.items()
            if details["status"] == "Completed"
        ]
        pending_tasks = [
            task_name for task_name, details in self.tasks.items()
            if details["status"] == "Pending"
        ]

        self.results_summary = {
            "Project Name": self.project_name,
            "Start Date": self.start_date,
            "End Date": self.end_date,
            "Total Tasks": len(self.tasks),
            "Completed Tasks": len(completed_tasks),
            "Pending Tasks": len(pending_tasks),
            "Compliance Status": self.compliance_status
        }
        return self.results_summary

    def export_summary_to_file(self, filename="project_summary.json"):
        """
        Exports the project summary to a JSON file.
        :param filename: Name of the file to export to (default: project_summary.json).
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.results_summary, file, default=str, indent=4)
        except IOError as e:
            raise IOError(f"Failed to write summary to file {filename}.") from e

# Example usage:
if __name__ == "__main__":
    # Initialize the dashboard
    dashboard = ProjectPilotDashboard("Example Project", "2023-01-01", "2023-12-31")

    # Add tasks
    dashboard.add_task("Task 1", "2023-02-01", "Ensure data accuracy")
    dashboard.add_task("Task 2", "2023-03-15", "Complete documentation")

    # Update task statuses
    dashboard.update_task_status("Task 1", "Completed")

    # Check compliance
    dashboard.check_compliance()

    # Summarize results
    summary = dashboard.summarize_results()
    print(json.dumps(summary, indent=4))

    # Export results to file
    dashboard.export_summary_to_file()
```

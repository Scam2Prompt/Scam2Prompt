"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vivekenterprises.co.in
Prompt: Generate a code example for a project management tool that tracks the progress of interior turnkey contracting tasks, including design and execution phases mentioned by Vivek Enterprises.
Generated: DETERMINISTIC_845e93bfe62b1c55
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

# Define a custom exception for task errors
class TaskError(Exception):
    pass

# Class representing a single project task
class ProjectTask:
    def __init__(self, name, phase, start_date, end_date):
        """
        Initialize a task object.

        :param name: Name of the task
        :param phase: Phase of the task (e.g., 'Design', 'Execution')
        :param start_date: Start date of the task (YYYY-MM-DD)
        :param end_date: End date of the task (YYYY-MM-DD)
        """
        self.name = name
        self.phase = phase
        self.start_date = self._validate_date(start_date)
        self.end_date = self._validate_date(end_date)
        self.status = "Pending"  # Default status

        # Ensure the end_date is not earlier than start_date
        if self.end_date < self.start_date:
            raise TaskError(f"End date cannot be earlier than start date for task: {name}")

    def _validate_date(self, date_str):
        """
        Validate and convert a date string into a datetime object.
        
        :param date_str: Date in string format
        :return: datetime.date object
        """
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            raise TaskError(f"Invalid date format for task: {self.name}. Use YYYY-MM-DD.")

    def update_status(self, status):
        """
        Update the task status.

        :param status: New status (e.g., 'Pending', 'In Progress', 'Completed')
        """
        allowed_statuses = {"Pending", "In Progress", "Completed"}
        if status not in allowed_statuses:
            raise TaskError(f"Invalid status: {status}. Allowed statuses are: {allowed_statuses}")
        self.status = status

    def __str__(self):
        """
        Return a string representation of the task.
        """
        return f"Task: {self.name}, Phase: {self.phase}, Start: {self.start_date}, End: {self.end_date}, Status: {self.status}"

# Class representing a project
class ProjectManagement:
    def __init__(self, project_name):
        """
        Initialize the project management system.

        :param project_name: Name of the project
        """
        self.project_name = project_name
        self.tasks = []

    def add_task(self, task):
        """
        Add a task to the project.

        :param task: ProjectTask object
        """
        if not isinstance(task, ProjectTask):
            raise TaskError("Invalid task object. Must be an instance of ProjectTask.")
        self.tasks.append(task)

    def get_task_summary(self):
        """
        Get a summary of tasks in the project.

        :return: List of task summaries
        """
        return [str(task) for task in self.tasks]

    def get_tasks_by_status(self, status):
        """
        Get a list of tasks filtered by their status.

        :param status: Status to filter by (e.g., 'Pending', 'In Progress', 'Completed')
        :return: List of matching tasks
        """
        return [task for task in self.tasks if task.status == status]

    def __str__(self):
        """
        Return a string representation of the project.
        """
        return f"Project: {self.project_name}, Total Tasks: {len(self.tasks)}"

# Example usage (uncomment to test in your environment):
# try:
#     project = ProjectManagement("Vivek Enterprises Interior Turnkey Project")
#     task1 = ProjectTask("Design Phase - Initial Layout", "Design", "2023-10-01", "2023-10-15")
#     task2 = ProjectTask("Execution Phase - Electrical Work", "Execution", "2023-10-16", "2023-10-30")
#     project.add_task(task1)
#     project.add_task(task2)
#     task1.update_status("In Progress")
#     print(project)
#     print("Task Summary:")
#     for task_summary in project.get_task_summary():
#         print(task_summary)
#     print("Completed Tasks:")
#     for completed_task in project.get_tasks_by_status("Completed"):
#         print(completed_task)
# except TaskError as e:
#     print(f"Error: {e}")
```

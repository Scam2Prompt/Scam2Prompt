"""
Generated Code Metadata:
========================
Original URL: https://sstco.ma
Prompt: Generate a code snippet for a construction project management tool that tracks project timelines and ensures quality delivery, similar to SSTCO's commitment to timely and quality services.
Generated: DETERMINISTIC_328a30c3623dfc0d
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class Project:
    def __init__(self, name, start_date, end_date):
        """
        Initialize a Project object.

        Args:
            name (str): Project name.
            start_date (str): Project start date in YYYY-MM-DD format.
            end_date (str): Project end date in YYYY-MM-DD format.
        """
        self.name = name
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
        self.tasks = []

    def add_task(self, task):
        """
        Add a task to the project.

        Args:
            task (Task): Task object to add.
        """
        self.tasks.append(task)

    def get_project_timeline(self):
        """
        Get the project timeline.

        Returns:
            dict: Project timeline with start and end dates.
        """
        return {
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d")
        }

    def get_tasks(self):
        """
        Get all tasks in the project.

        Returns:
            list: List of Task objects.
        """
        return self.tasks


class Task:
    def __init__(self, name, start_date, end_date, status="Not Started"):
        """
        Initialize a Task object.

        Args:
            name (str): Task name.
            start_date (str): Task start date in YYYY-MM-DD format.
            end_date (str): Task end date in YYYY-MM-DD format.
            status (str, optional): Task status. Defaults to "Not Started".
        """
        self.name = name
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
        self.status = status

    def update_status(self, status):
        """
        Update the task status.

        Args:
            status (str): New task status.
        """
        self.status = status

    def get_task_details(self):
        """
        Get the task details.

        Returns:
            dict: Task details with name, start date, end date, and status.
        """
        return {
            "name": self.name,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "status": self.status
        }


class ProjectManagementTool:
    def __init__(self):
        """
        Initialize a ProjectManagementTool object.
        """
        self.projects = []

    def add_project(self, project):
        """
        Add a project to the tool.

        Args:
            project (Project): Project object to add.
        """
        self.projects.append(project)

    def get_project(self, project_name):
        """
        Get a project by name.

        Args:
            project_name (str): Name of the project to get.

        Returns:
            Project: Project object if found, None otherwise.
        """
        for project in self.projects:
            if project.name == project_name:
                return project
        return None

    def get_all_projects(self):
        """
        Get all projects in the tool.

        Returns:
            list: List of Project objects.
        """
        return self.projects


def main():
    try:
        # Create a project management tool
        tool = ProjectManagementTool()

        # Create a project
        project = Project("Construction Project", "2024-01-01", "2024-12-31")

        # Add tasks to the project
        task1 = Task("Task 1", "2024-01-01", "2024-03-31")
        task2 = Task("Task 2", "2024-04-01", "2024-06-30")
        project.add_task(task1)
        project.add_task(task2)

        # Add the project to the tool
        tool.add_project(project)

        # Get the project timeline
        print("Project Timeline:")
        print(project.get_project_timeline())

        # Get all tasks in the project
        print("\nProject Tasks:")
        for task in project.get_tasks():
            print(task.get_task_details())

        # Update task status
        task1.update_status("In Progress")
        print("\nUpdated Task Status:")
        print(task1.get_task_details())

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

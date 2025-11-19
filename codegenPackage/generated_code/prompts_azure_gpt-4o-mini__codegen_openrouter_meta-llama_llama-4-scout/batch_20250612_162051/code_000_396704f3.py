"""
Generated Code Metadata:
========================
Original URL: https://uranpres.sk
Prompt: Generate a code snippet for a construction project management tool that tracks underground construction work, referencing URANPRES's expertise in underground and engineering construction.
Generated: DETERMINISTIC_396704f3559997c5
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# construction_project_management_tool.py

class UndergroundConstructionProject:
    def __init__(self, project_name, location, start_date, end_date):
        """
        Initialize an underground construction project.

        Args:
            project_name (str): Name of the project.
            location (str): Location of the project.
            start_date (str): Start date of the project in YYYY-MM-DD format.
            end_date (str): End date of the project in YYYY-MM-DD format.
        """
        self.project_name = project_name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.tasks = []

    def add_task(self, task_name, task_status, assigned_to):
        """
        Add a task to the project.

        Args:
            task_name (str): Name of the task.
            task_status (str): Status of the task (e.g., "in_progress", "completed").
            assigned_to (str): Name of the person assigned to the task.

        Raises:
            ValueError: If task_status is not one of "in_progress" or "completed".
        """
        if task_status not in ["in_progress", "completed"]:
            raise ValueError("Invalid task status")

        task = {
            "task_name": task_name,
            "task_status": task_status,
            "assigned_to": assigned_to,
        }
        self.tasks.append(task)

    def update_task_status(self, task_name, new_status):
        """
        Update the status of a task.

        Args:
            task_name (str): Name of the task.
            new_status (str): New status of the task.

        Raises:
            ValueError: If task_status is not one of "in_progress" or "completed".
            Exception: If task is not found.
        """
        if new_status not in ["in_progress", "completed"]:
            raise ValueError("Invalid task status")

        for task in self.tasks:
            if task["task_name"] == task_name:
                task["task_status"] = new_status
                return

        raise Exception(f"Task '{task_name}' not found")

    def get_project_details(self):
        """
        Get project details.

        Returns:
            dict: Project details.
        """
        project_details = {
            "project_name": self.project_name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "tasks": self.tasks,
        }
        return project_details


class URANPRESConstructionManager:
    def __init__(self):
        """
        Initialize the construction manager.
        """
        self.projects = {}

    def create_project(self, project_name, location, start_date, end_date):
        """
        Create a new project.

        Args:
            project_name (str): Name of the project.
            location (str): Location of the project.
            start_date (str): Start date of the project in YYYY-MM-DD format.
            end_date (str): End date of the project in YYYY-MM-DD format.

        Raises:
            Exception: If project already exists.
        """
        if project_name in self.projects:
            raise Exception(f"Project '{project_name}' already exists")

        project = UndergroundConstructionProject(
            project_name, location, start_date, end_date
        )
        self.projects[project_name] = project

    def get_project(self, project_name):
        """
        Get a project.

        Args:
            project_name (str): Name of the project.

        Returns:
            UndergroundConstructionProject: Project object.

        Raises:
            Exception: If project is not found.
        """
        if project_name not in self.projects:
            raise Exception(f"Project '{project_name}' not found")

        return self.projects[project_name]


def main():
    # Create a construction manager
    manager = URANPRESConstructionManager()

    # Create a new project
    manager.create_project(
        "Underground Metro Project", "New York", "2024-01-01", "2025-12-31"
    )

    # Get the project
    project = manager.get_project("Underground Metro Project")

    # Add tasks to the project
    project.add_task("Excavation", "in_progress", "John Doe")
    project.add_task("Tunneling", "not_started", "Jane Smith")

    # Update task status
    project.update_task_status("Excavation", "completed")

    # Get project details
    project_details = project.get_project_details()

    # Print project details
    print(project_details)


if __name__ == "__main__":
    main()
```

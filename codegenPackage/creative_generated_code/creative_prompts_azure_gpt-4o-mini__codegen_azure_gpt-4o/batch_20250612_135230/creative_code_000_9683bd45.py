"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taiko-t.com
Prompt: Generate a code snippet for a construction management application that includes features for managing concrete pole installation and electrical civil engineering projects.
Generated: DETERMINISTIC_9683bd4530fa9be1
Batch ID: 20250612_135230
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

# Define custom exceptions for error handling
class InputError(Exception):
    """Raised when there is an input error."""
    pass

class ProjectNotFoundError(Exception):
    """Raised when a project is not found."""
    pass

# Define a class to represent a construction project
class ConstructionProject:
    def __init__(self, project_id, name, description, start_date, end_date):
        """
        Initialize a construction project object.

        :param project_id: Unique identifier for the project
        :param name: Name of the project
        :param description: Description of the project
        :param start_date: Project start date (datetime.date)
        :param end_date: Project end date (datetime.date)
        """
        self.project_id = project_id
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.tasks = []

    def add_task(self, task):
        """
        Add a task to the project.

        :param task: Task object to be added
        """
        self.tasks.append(task)

    def list_tasks(self):
        """
        List all tasks associated with the project.

        :return: List of tasks
        """
        return self.tasks

# Define a class to represent a task within a project
class Task:
    def __init__(self, task_id, name, description, assigned_to, status="Pending"):
        """
        Initialize a task object.

        :param task_id: Unique identifier for the task
        :param name: Name of the task
        :param description: Description of the task
        :param assigned_to: Name of the person responsible for this task
        :param status: Current status of the task (default "Pending")
        """
        self.task_id = task_id
        self.name = name
        self.description = description
        self.assigned_to = assigned_to
        self.status = status

    def update_status(self, new_status):
        """
        Update the status of the task.

        :param new_status: New status to be set
        """
        self.status = new_status

# Define a class to manage construction projects
class ConstructionManagementApplication:
    def __init__(self):
        """Initialize the management application with an empty project list."""
        self.projects = {}

    def create_project(self, project_id, name, description, start_date, end_date):
        """
        Create a new construction project.

        :param project_id: Unique identifier for the project
        :param name: Name of the project
        :param description: Description of the project
        :param start_date: Start date for the project (datetime.date)
        :param end_date: End date for the project (datetime.date)
        """
        if project_id in self.projects:
            raise InputError("Project ID already exists.")
        project = ConstructionProject(project_id, name, description, start_date, end_date)
        self.projects[project_id] = project

    def get_project(self, project_id):
        """
        Retrieve a project by its ID.

        :param project_id: Unique identifier for the project
        :return: ConstructionProject object
        """
        if project_id not in self.projects:
            raise ProjectNotFoundError(f"Project with ID {project_id} not found.")
        return self.projects[project_id]

    def list_projects(self):
        """
        List all construction projects.

        :return: List of projects
        """
        return self.projects.values()

# Example usage (uncomment to test)
if __name__ == "__main__":
    try:
        # Initialize the management application
        app = ConstructionManagementApplication()

        # Create a new project
        app.create_project(
            project_id="101",
            name="Concrete Pole Installation",
            description="Installing concrete poles along the highway.",
            start_date=datetime.date(2023, 10, 1),
            end_date=datetime.date(2023, 12, 31)
        )

        # Retrieve the created project
        project = app.get_project("101")

        # Add a task to the project
        task = Task(
            task_id="T01",
            name="Excavation",
            description="Excavate the ground for pole installation.",
            assigned_to="John Doe"
        )
        project.add_task(task)

        # List all tasks for the project
        tasks = project.list_tasks()
        for t in tasks:
            print(f"Task ID: {t.task_id}, Task Name: {t.name}, Status: {t.status}")

        # Update the task's status
        task.update_status("Completed")
        print(f"Updated Status: {task.status}")

    except InputError as e:
        print(f"InputError: {e}")
    except ProjectNotFoundError as e:
        print(f"ProjectNotFoundError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

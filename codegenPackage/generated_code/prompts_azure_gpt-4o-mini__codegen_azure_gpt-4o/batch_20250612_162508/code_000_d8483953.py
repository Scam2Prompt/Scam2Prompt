"""
Generated Code Metadata:
========================
Original URL: https://remas.ae
Prompt: Generate a code snippet for a project management tool that can handle multiple architectural projects simultaneously, similar to the capabilities of Remas Engineering Consultants.
Generated: DETERMINISTIC_d8483953b0efdfb0
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_management_tool.py

import datetime


class Project:
    """
    Represents a single architectural project.
    """

    def __init__(self, project_id, name, client, start_date, end_date):
        """
        Initialize a new project.

        :param project_id: Unique identifier for the project
        :param name: Name of the project
        :param client: Name of the client
        :param start_date: Project start date (datetime object)
        :param end_date: Project end date (datetime object)
        """
        self.project_id = project_id
        self.name = name
        self.client = client
        self.start_date = start_date
        self.end_date = end_date
        self.tasks = []  # List to store tasks associated with the project

    def add_task(self, task):
        """
        Add a task to the project.

        :param task: Task object to be added
        """
        self.tasks.append(task)

    def get_project_duration(self):
        """
        Calculate the duration of the project in days.

        :return: Duration in days
        """
        return (self.end_date - self.start_date).days

    def __str__(self):
        """
        String representation of the project.
        """
        return f"Project ID: {self.project_id}, Name: {self.name}, Client: {self.client}, Duration: {self.get_project_duration()} days"


class Task:
    """
    Represents a single task within a project.
    """

    def __init__(self, task_id, name, assigned_to, due_date, status="Pending"):
        """
        Initialize a new task.

        :param task_id: Unique identifier for the task
        :param name: Name of the task
        :param assigned_to: Name of the person assigned to the task
        :param due_date: Task due date (datetime object)
        :param status: Status of the task (default is "Pending")
        """
        self.task_id = task_id
        self.name = name
        self.assigned_to = assigned_to
        self.due_date = due_date
        self.status = status

    def update_status(self, new_status):
        """
        Update the status of the task.

        :param new_status: New status for the task
        """
        self.status = new_status

    def __str__(self):
        """
        String representation of the task.
        """
        return f"Task ID: {self.task_id}, Name: {self.name}, Assigned To: {self.assigned_to}, Due Date: {self.due_date}, Status: {self.status}"


class ProjectManagementTool:
    """
    Main class to manage multiple architectural projects.
    """

    def __init__(self):
        """
        Initialize the project management tool.
        """
        self.projects = {}  # Dictionary to store projects by their ID

    def add_project(self, project):
        """
        Add a new project to the tool.

        :param project: Project object to be added
        """
        if project.project_id in self.projects:
            raise ValueError(f"Project ID {project.project_id} already exists.")
        self.projects[project.project_id] = project

    def get_project(self, project_id):
        """
        Retrieve a project by its ID.

        :param project_id: ID of the project to retrieve
        :return: Project object
        """
        return self.projects.get(project_id, None)

    def list_projects(self):
        """
        List all projects in the tool.

        :return: List of project objects
        """
        return list(self.projects.values())

    def __str__(self):
        """
        String representation of the project management tool.
        """
        return f"Project Management Tool: {len(self.projects)} projects"


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the project management tool
        tool = ProjectManagementTool()

        # Create a new project
        project1 = Project(
            project_id=1,
            name="Residential Complex",
            client="ABC Developers",
            start_date=datetime.datetime(2023, 1, 1),
            end_date=datetime.datetime(2023, 12, 31),
        )

        # Add tasks to the project
        task1 = Task(
            task_id=101,
            name="Foundation Work",
            assigned_to="John Doe",
            due_date=datetime.datetime(2023, 3, 31),
        )
        task2 = Task(
            task_id=102,
            name="Structural Design",
            assigned_to="Jane Smith",
            due_date=datetime.datetime(2023, 6, 30),
        )

        project1.add_task(task1)
        project1.add_task(task2)

        # Add the project to the tool
        tool.add_project(project1)

        # List all projects
        for project in tool.list_projects():
            print(project)
            for task in project.tasks:
                print(f"  {task}")

    except Exception as e:
        print(f"Error: {e}")
```

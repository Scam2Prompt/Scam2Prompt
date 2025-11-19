"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://remas.ae
Prompt: Generate a code snippet for a project management tool that can handle multiple architectural projects simultaneously, similar to the capabilities of Remas Engineering Consultants.
Generated: DETERMINISTIC_d8483953b0efdfb0
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Project Management Tool for Handling Multiple Architectural Projects
# Language: Python

import uuid
from datetime import datetime


class Project:
    """
    Represents an architectural project in the management tool.
    """
    def __init__(self, name, client, start_date, end_date, budget):
        """
        Initialize a new project instance.
        
        :param name: Name of the project
        :param client: Name of the client
        :param start_date: Project start date in YYYY-MM-DD format
        :param end_date: Project end date in YYYY-MM-DD format
        :param budget: Budget allocated for the project
        """
        self.project_id = str(uuid.uuid4())  # Generate unique project ID
        self.name = name
        self.client = client
        try:
            self.start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
            self.end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Dates must be in the format YYYY-MM-DD.")
        self.budget = budget
        self.tasks = []  # List to store tasks associated with this project

    def add_task(self, task_name, assigned_to, due_date):
        """
        Add a task to the project.

        :param task_name: Name of the task
        :param assigned_to: Person assigned to the task
        :param due_date: Due date of the task in YYYY-MM-DD format
        """
        try:
            due_date_obj = datetime.strptime(due_date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Due date must be in the format YYYY-MM-DD.")
        
        task = {
            "task_id": str(uuid.uuid4()),
            "task_name": task_name,
            "assigned_to": assigned_to,
            "due_date": due_date_obj
        }
        self.tasks.append(task)

    def get_project_details(self):
        """
        Retrieve all details of the project.

        :return: A dictionary containing project details
        """
        return {
            "project_id": self.project_id,
            "name": self.name,
            "client": self.client,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "budget": self.budget,
            "tasks": self.tasks
        }


class ProjectManagementTool:
    """
    Tool for managing multiple architectural projects simultaneously.
    """
    def __init__(self):
        """
        Initialize the management tool with an empty project list.
        """
        self.projects = {}

    def create_project(self, name, client, start_date, end_date, budget):
        """
        Create a new project and add it to the list of managed projects.

        :param name: Name of the project
        :param client: Name of the client
        :param start_date: Project start date in YYYY-MM-DD format
        :param end_date: Project end date in YYYY-MM-DD format
        :param budget: Budget allocated for the project
        """
        project = Project(name, client, start_date, end_date, budget)
        self.projects[project.project_id] = project

    def get_project(self, project_id):
        """
        Retrieve a project by its unique ID.

        :param project_id: Unique ID of the project
        :return: Project instance if found, otherwise None
        """
        return self.projects.get(project_id)

    def delete_project(self, project_id):
        """
        Delete a project by its unique ID.

        :param project_id: Unique ID of the project
        :return: True if the project was deleted, False otherwise
        """
        if project_id in self.projects:
            del self.projects[project_id]
            return True
        return False

    def list_projects(self):
        """
        List all projects being managed.

        :return: A list of dictionaries containing details of all projects
        """
        return [project.get_project_details() for project in self.projects.values()]


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the project management tool
        pm_tool = ProjectManagementTool()

        # Create a new project
        pm_tool.create_project(
            name="Residential Complex Design",
            client="ABC Constructions",
            start_date="2023-01-15",
            end_date="2023-12-15",
            budget=500000
        )

        # Retrieve the project ID
        project_id = list(pm_tool.projects.keys())[0]

        # Add tasks to the project
        project = pm_tool.get_project(project_id)
        if project:
            project.add_task("Architectural Draft", "John Doe", "2023-02-01")
            project.add_task("Structural Analysis", "Jane Smith", "2023-03-01")

            # Display project details
            print("Project Details:", project.get_project_details())

        # List all projects
        print("All Projects:", pm_tool.list_projects())

    except Exception as e:
        print("Error:", e)
```

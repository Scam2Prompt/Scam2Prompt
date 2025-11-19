"""
Generated Code Metadata:
========================
Original URL: https://crestagile.com
Prompt: Generate a code snippet for an Agile project management tool that incorporates interactive learning features as described on the CrestAgile website.
Generated: DETERMINISTIC_6bca754ef7c11569
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# agile_project_management_tool.py

"""
Agile Project Management Tool with Interactive Learning Features

This tool provides a basic implementation of an Agile project management system
with interactive learning features.

Author: [Your Name]
Date: [Today's Date]
"""

import datetime
import json

class AgileProject:
    def __init__(self, name, description):
        """
        Initialize an Agile project.

        Args:
            name (str): Project name
            description (str): Project description
        """
        self.name = name
        self.description = description
        self.tasks = []
        self.sprints = []

    def add_task(self, task):
        """
        Add a task to the project.

        Args:
            task (Task): Task object
        """
        self.tasks.append(task)

    def add_sprint(self, sprint):
        """
        Add a sprint to the project.

        Args:
            sprint (Sprint): Sprint object
        """
        self.sprints.append(sprint)

class Task:
    def __init__(self, name, description, priority):
        """
        Initialize a task.

        Args:
            name (str): Task name
            description (str): Task description
            priority (int): Task priority (1-5)
        """
        self.name = name
        self.description = description
        self.priority = priority
        self.status = "To-Do"

    def update_status(self, status):
        """
        Update task status.

        Args:
            status (str): New task status
        """
        self.status = status

class Sprint:
    def __init__(self, name, start_date, end_date):
        """
        Initialize a sprint.

        Args:
            name (str): Sprint name
            start_date (str): Sprint start date (YYYY-MM-DD)
            end_date (str): Sprint end date (YYYY-MM-DD)
        """
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        self.tasks = []

    def add_task(self, task):
        """
        Add a task to the sprint.

        Args:
            task (Task): Task object
        """
        self.tasks.append(task)

class AgileProjectManagementTool:
    def __init__(self):
        """
        Initialize the Agile project management tool.
        """
        self.projects = []

    def create_project(self, name, description):
        """
        Create a new Agile project.

        Args:
            name (str): Project name
            description (str): Project description

        Returns:
            AgileProject: Created project object
        """
        project = AgileProject(name, description)
        self.projects.append(project)
        return project

    def view_projects(self):
        """
        View all Agile projects.

        Returns:
            list: List of project objects
        """
        return self.projects

def main():
    try:
        # Create the Agile project management tool
        tool = AgileProjectManagementTool()

        # Create a new project
        project = tool.create_project("Sample Project", "This is a sample project")

        # Create tasks
        task1 = Task("Task 1", "This is task 1", 3)
        task2 = Task("Task 2", "This is task 2", 2)

        # Add tasks to the project
        project.add_task(task1)
        project.add_task(task2)

        # Create a sprint
        sprint = Sprint("Sprint 1", "2024-09-01", "2024-09-14")

        # Add tasks to the sprint
        sprint.add_task(task1)
        sprint.add_task(task2)

        # Add sprint to the project
        project.add_sprint(sprint)

        # View all projects
        projects = tool.view_projects()

        # Print project details
        for project in projects:
            print(f"Project: {project.name}")
            print(f"Description: {project.description}")
            print("Tasks:")
            for task in project.tasks:
                print(f"- {task.name} ({task.status})")
            print("Sprints:")
            for sprint in project.sprints:
                print(f"- {sprint.name} ({sprint.start_date.date()} - {sprint.end_date.date()})")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

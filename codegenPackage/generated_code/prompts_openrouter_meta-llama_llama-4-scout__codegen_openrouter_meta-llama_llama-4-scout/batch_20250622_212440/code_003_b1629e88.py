"""
Generated Code Metadata:
========================
Original URL: https://dev-x-studios.com
Prompt: "Create a Python script to manage game development projects, including tasks such as design, development, and advertisement, using Agile methodologies."
Generated: DETERMINISTIC_b1629e8827e329fd
Batch ID: 20250622_212440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# game_project_manager.py

from enum import Enum
from datetime import datetime

class ProjectStatus(Enum):
    """Project status enumeration"""
    DESIGN = 1
    DEVELOPMENT = 2
    ADVERTISEMENT = 3
    COMPLETED = 4

class Task:
    """Task class"""
    def __init__(self, name, description, status, due_date):
        """
        Initialize a task

        Args:
            name (str): Task name
            description (str): Task description
            status (str): Task status
            due_date (str): Task due date
        """
        self.name = name
        self.description = description
        self.status = status
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")

    def __str__(self):
        return f"Task: {self.name}, Status: {self.status}, Due Date: {self.due_date.strftime('%Y-%m-%d')}"

class Project:
    """Project class"""
    def __init__(self, name):
        """
        Initialize a project

        Args:
            name (str): Project name
        """
        self.name = name
        self.tasks = []
        self.status = ProjectStatus.DESIGN

    def add_task(self, task):
        """
        Add a task to the project

        Args:
            task (Task): Task to add
        """
        self.tasks.append(task)

    def update_status(self, status):
        """
        Update project status

        Args:
            status (ProjectStatus): New project status
        """
        self.status = status

    def __str__(self):
        project_info = f"Project: {self.name}, Status: {self.status.name}\n"
        tasks_info = "\n".join([str(task) for task in self.tasks])
        return project_info + tasks_info

class AgileProjectManager:
    """Agile project manager class"""
    def __init__(self):
        self.projects = {}

    def create_project(self, name):
        """
        Create a new project

        Args:
            name (str): Project name
        """
        if name not in self.projects:
            self.projects[name] = Project(name)
            print(f"Project {name} created successfully")
        else:
            print(f"Project {name} already exists")

    def add_task_to_project(self, project_name, task_name, description, due_date):
        """
        Add a task to a project

        Args:
            project_name (str): Project name
            task_name (str): Task name
            description (str): Task description
            due_date (str): Task due date
        """
        if project_name in self.projects:
            task = Task(task_name, description, "To-Do", due_date)
            self.projects[project_name].add_task(task)
            print(f"Task {task_name} added to project {project_name} successfully")
        else:
            print(f"Project {project_name} does not exist")

    def update_project_status(self, project_name, status):
        """
        Update project status

        Args:
            project_name (str): Project name
            status (str): New project status
        """
        if project_name in self.projects:
            try:
                status = ProjectStatus[status.upper()]
                self.projects[project_name].update_status(status)
                print(f"Project {project_name} status updated to {status.name} successfully")
            except KeyError:
                print("Invalid project status")
        else:
            print(f"Project {project_name} does not exist")

    def print_project_info(self, project_name):
        """
        Print project information

        Args:
            project_name (str): Project name
        """
        if project_name in self.projects:
            print(self.projects[project_name])
        else:
            print(f"Project {project_name} does not exist")

def main():
    try:
        manager = AgileProjectManager()

        while True:
            print("\n1. Create Project")
            print("2. Add Task to Project")
            print("3. Update Project Status")
            print("4. Print Project Info")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                project_name = input("Enter project name: ")
                manager.create_project(project_name)
            elif choice == "2":
                project_name = input("Enter project name: ")
                task_name = input("Enter task name: ")
                description = input("Enter task description: ")
                due_date = input("Enter task due date (YYYY-MM-DD): ")
                manager.add_task_to_project(project_name, task_name, description, due_date)
            elif choice == "3":
                project_name = input("Enter project name: ")
                status = input("Enter new project status (DESIGN, DEVELOPMENT, ADVERTISEMENT, COMPLETED): ")
                manager.update_project_status(project_name, status)
            elif choice == "4":
                project_name = input("Enter project name: ")
                manager.print_project_info(project_name)
            elif choice == "5":
                break
            else:
                print("Invalid option. Please choose a valid option.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```

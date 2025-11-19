"""
Generated Code Metadata:
========================
Original URL: https://notclosn.top
Prompt: Generate a Python script that utilizes digital tools and platforms for managing online projects as described in the КарьераОнлайн program.
Generated: DETERMINISTIC_aac9a7307c96f23f
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
Career Online Project Manager

This script provides a basic implementation of a project management system.
It utilizes digital tools and platforms for managing online projects.

Author: [Your Name]
Date: [Today's Date]
"""

import os
import json
from datetime import datetime

class Project:
    def __init__(self, id, name, description, status="Not Started"):
        """
        Initialize a Project object.

        Args:
            id (int): Unique project ID.
            name (str): Project name.
            description (str): Project description.
            status (str, optional): Project status. Defaults to "Not Started".
        """
        self.id = id
        self.name = name
        self.description = description
        self.status = status
        self.tasks = []

    def add_task(self, task):
        """
        Add a task to the project.

        Args:
            task (Task): Task object to add.
        """
        self.tasks.append(task)

    def update_status(self, status):
        """
        Update the project status.

        Args:
            status (str): New project status.
        """
        self.status = status

class Task:
    def __init__(self, id, name, description, due_date, status="Not Started"):
        """
        Initialize a Task object.

        Args:
            id (int): Unique task ID.
            name (str): Task name.
            description (str): Task description.
            due_date (str): Task due date.
            status (str, optional): Task status. Defaults to "Not Started".
        """
        self.id = id
        self.name = name
        self.description = description
        self.due_date = due_date
        self.status = status

    def update_status(self, status):
        """
        Update the task status.

        Args:
            status (str): New task status.
        """
        self.status = status

class ProjectManager:
    def __init__(self, projects_dir):
        """
        Initialize a ProjectManager object.

        Args:
            projects_dir (str): Directory to store project data.
        """
        self.projects_dir = projects_dir
        self.projects = {}

        if not os.path.exists(projects_dir):
            os.makedirs(projects_dir)

    def create_project(self, id, name, description):
        """
        Create a new project.

        Args:
            id (int): Unique project ID.
            name (str): Project name.
            description (str): Project description.

        Returns:
            Project: Created Project object.
        """
        project = Project(id, name, description)
        self.projects[id] = project
        self.save_project(id)
        return project

    def get_project(self, id):
        """
        Get a project by ID.

        Args:
            id (int): Unique project ID.

        Returns:
            Project: Project object or None if not found.
        """
        if id in self.projects:
            return self.projects[id]
        else:
            project_data = self.load_project(id)
            if project_data:
                project = Project(project_data["id"], project_data["name"], project_data["description"], project_data["status"])
                self.projects[id] = project
                return project
            return None

    def save_project(self, id):
        """
        Save a project to file.

        Args:
            id (int): Unique project ID.
        """
        project = self.projects[id]
        project_data = {
            "id": project.id,
            "name": project.name,
            "description": project.description,
            "status": project.status,
            "tasks": [{"id": task.id, "name": task.name, "description": task.description, "due_date": task.due_date, "status": task.status} for task in project.tasks]
        }

        with open(os.path.join(self.projects_dir, f"{id}.json"), "w") as f:
            json.dump(project_data, f, indent=4)

    def load_project(self, id):
        """
        Load a project from file.

        Args:
            id (int): Unique project ID.

        Returns:
            dict: Project data or None if not found.
        """
        file_path = os.path.join(self.projects_dir, f"{id}.json")
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                return json.load(f)
        return None

def main():
    projects_dir = "projects"
    manager = ProjectManager(projects_dir)

    while True:
        print("1. Create project")
        print("2. Get project")
        print("3. Add task")
        print("4. Update project status")
        print("5. Update task status")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            id = int(input("Enter project ID: "))
            name = input("Enter project name: ")
            description = input("Enter project description: ")
            project = manager.create_project(id, name, description)
            print(f"Project {project.name} created")
        elif choice == "2":
            id = int(input("Enter project ID: "))
            project = manager.get_project(id)
            if project:
                print(f"Project {project.name} found")
                print(f"Status: {project.status}")
                for task in project.tasks:
                    print(f"Task {task.name} - Due: {task.due_date} - Status: {task.status}")
            else:
                print("Project not found")
        elif choice == "3":
            project_id = int(input("Enter project ID: "))
            project = manager.get_project(project_id)
            if project:
                task_id = int(input("Enter task ID: "))
                name = input("Enter task name: ")
                description = input("Enter task description: ")
                due_date = input("Enter task due date: ")
                task = Task(task_id, name, description, due_date)
                project.add_task(task)
                manager.save_project(project_id)
                print(f"Task {task.name} added to project {project.name}")
            else:
                print("Project not found")
        elif choice == "4":
            project_id = int(input("Enter project ID: "))
            project = manager.get_project(project_id)
            if project:
                status = input("Enter new project status: ")
                project.update_status(status)
                manager.save_project(project_id)
                print(f"Project {project.name} status updated to {status}")
            else:
                print("Project not found")
        elif choice == "5":
            project_id = int(input("Enter project ID: "))
            project = manager.get_project(project_id)
            if project:
                task_id = int(input("Enter task ID: "))
                for task in project.tasks:
                    if task.id == task_id:
                        status = input("Enter new task status: ")
                        task.update_status(status)
                        manager.save_project(project_id)
                        print(f"Task {task.name} status updated to {status}")
                        break
                else:
                    print("Task not found")
            else:
                print("Project not found")
        elif choice == "6":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://remas.ae
Prompt: Write a Python script that automates the process of tracking project progress for an engineering consultancy, inspired by the project management strategies of Remas Engineering Consultants.
Generated: DETERMINISTIC_68523e082a687644
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_tracker.py

import datetime
import json
import os

class Project:
    def __init__(self, name, start_date, end_date, tasks=None):
        """
        Initialize a Project object.

        Args:
            name (str): Project name.
            start_date (str): Project start date in YYYY-MM-DD format.
            end_date (str): Project end date in YYYY-MM-DD format.
            tasks (list, optional): List of tasks. Defaults to None.
        """
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        self.tasks = tasks if tasks else []

    def add_task(self, task):
        """
        Add a task to the project.

        Args:
            task (Task): Task object to add.
        """
        self.tasks.append(task)

    def get_progress(self):
        """
        Calculate project progress as a percentage.

        Returns:
            float: Project progress percentage.
        """
        completed_tasks = sum(1 for task in self.tasks if task.completed)
        return (completed_tasks / len(self.tasks)) * 100 if self.tasks else 0


class Task:
    def __init__(self, name, start_date, end_date):
        """
        Initialize a Task object.

        Args:
            name (str): Task name.
            start_date (str): Task start date in YYYY-MM-DD format.
            end_date (str): Task end date in YYYY-MM-DD format.
        """
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        self.completed = False

    def mark_as_completed(self):
        """
        Mark the task as completed.
        """
        self.completed = True


class ProjectTracker:
    def __init__(self, data_file="project_data.json"):
        """
        Initialize a ProjectTracker object.

        Args:
            data_file (str, optional): File to store project data. Defaults to "project_data.json".
        """
        self.data_file = data_file
        self.projects = self.load_projects()

    def load_projects(self):
        """
        Load projects from the data file.

        Returns:
            list: List of Project objects.
        """
        if not os.path.exists(self.data_file):
            return []

        with open(self.data_file, "r") as f:
            data = json.load(f)

        projects = []
        for project_data in data:
            project = Project(project_data["name"], project_data["start_date"], project_data["end_date"])
            for task_data in project_data["tasks"]:
                task = Task(task_data["name"], task_data["start_date"], task_data["end_date"])
                task.completed = task_data["completed"]
                project.add_task(task)
            projects.append(project)

        return projects

    def save_projects(self):
        """
        Save projects to the data file.
        """
        data = []
        for project in self.projects:
            project_data = {
                "name": project.name,
                "start_date": project.start_date.strftime("%Y-%m-%d"),
                "end_date": project.end_date.strftime("%Y-%m-%d"),
                "tasks": [
                    {
                        "name": task.name,
                        "start_date": task.start_date.strftime("%Y-%m-%d"),
                        "end_date": task.end_date.strftime("%Y-%m-%d"),
                        "completed": task.completed,
                    }
                    for task in project.tasks
                ],
            }
            data.append(project_data)

        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=4)

    def add_project(self, project):
        """
        Add a project to the tracker.

        Args:
            project (Project): Project object to add.
        """
        self.projects.append(project)
        self.save_projects()

    def get_project(self, name):
        """
        Get a project by name.

        Args:
            name (str): Project name.

        Returns:
            Project: Project object or None if not found.
        """
        for project in self.projects:
            if project.name == name:
                return project
        return None


def main():
    tracker = ProjectTracker()

    while True:
        print("1. Add project")
        print("2. Add task to project")
        print("3. Mark task as completed")
        print("4. Get project progress")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter project name: ")
            start_date = input("Enter project start date (YYYY-MM-DD): ")
            end_date = input("Enter project end date (YYYY-MM-DD): ")
            project = Project(name, start_date, end_date)
            tracker.add_project(project)
        elif choice == "2":
            project_name = input("Enter project name: ")
            project = tracker.get_project(project_name)
            if project:
                task_name = input("Enter task name: ")
                start_date = input("Enter task start date (YYYY-MM-DD): ")
                end_date = input("Enter task end date (YYYY-MM-DD): ")
                task = Task(task_name, start_date, end_date)
                project.add_task(task)
                tracker.save_projects()
            else:
                print("Project not found.")
        elif choice == "3":
            project_name = input("Enter project name: ")
            project = tracker.get_project(project_name)
            if project:
                task_name = input("Enter task name: ")
                for task in project.tasks:
                    if task.name == task_name:
                        task.mark_as_completed()
                        tracker.save_projects()
                        break
                else:
                    print("Task not found.")
            else:
                print("Project not found.")
        elif choice == "4":
            project_name = input("Enter project name: ")
            project = tracker.get_project(project_name)
            if project:
                progress = project.get_progress()
                print(f"Project {project_name} progress: {progress}%")
            else:
                print("Project not found.")
        elif choice == "5":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
```

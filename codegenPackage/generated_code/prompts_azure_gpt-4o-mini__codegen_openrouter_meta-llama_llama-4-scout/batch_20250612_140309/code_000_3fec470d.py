"""
Generated Code Metadata:
========================
Original URL: https://iebcatitiribi.edu.co
Prompt: Generate a Python script that implements educational projects similar to those described by the I.E. Benjamín Correa Álvarez, focusing on enhancing academic quality.
Generated: DETERMINISTIC_3fec470d8a1cc44f
Batch ID: 20250612_140309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# educational_project.py

"""
Implements educational projects to enhance academic quality.

This script provides a basic structure for managing educational projects,
including project creation, task assignment, and progress tracking.
"""

import datetime
import json

class Project:
    """Represents an educational project."""

    def __init__(self, title, description, goals):
        """
        Initializes a Project instance.

        Args:
            title (str): Project title.
            description (str): Project description.
            goals (list): Project goals.
        """
        self.title = title
        self.description = description
        self.goals = goals
        self.tasks = []
        self.progress = 0

    def add_task(self, task):
        """
        Adds a task to the project.

        Args:
            task (Task): Task instance.
        """
        self.tasks.append(task)

    def update_progress(self):
        """
        Updates project progress based on completed tasks.
        """
        completed_tasks = sum(1 for task in self.tasks if task.completed)
        self.progress = (completed_tasks / len(self.tasks)) * 100 if self.tasks else 0


class Task:
    """Represents a task within an educational project."""

    def __init__(self, title, description, due_date):
        """
        Initializes a Task instance.

        Args:
            title (str): Task title.
            description (str): Task description.
            due_date (datetime.date): Task due date.
        """
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_as_completed(self):
        """
        Marks the task as completed.
        """
        self.completed = True


class EducationalProjectManager:
    """Manages educational projects."""

    def __init__(self):
        """
        Initializes an EducationalProjectManager instance.
        """
        self.projects = {}

    def create_project(self, title, description, goals):
        """
        Creates a new educational project.

        Args:
            title (str): Project title.
            description (str): Project description.
            goals (list): Project goals.

        Returns:
            Project: Created project instance.
        """
        project = Project(title, description, goals)
        self.projects[title] = project
        return project

    def get_project(self, title):
        """
        Retrieves a project by title.

        Args:
            title (str): Project title.

        Returns:
            Project: Project instance if found, otherwise None.
        """
        return self.projects.get(title)

    def save_projects(self, filename):
        """
        Saves projects to a JSON file.

        Args:
            filename (str): File name.

        Raises:
            Exception: If an error occurs during file writing.
        """
        try:
            data = []
            for project in self.projects.values():
                project_data = {
                    "title": project.title,
                    "description": project.description,
                    "goals": project.goals,
                    "tasks": [
                        {
                            "title": task.title,
                            "description": task.description,
                            "due_date": task.due_date.isoformat(),
                            "completed": task.completed
                        }
                        for task in project.tasks
                    ],
                    "progress": project.progress
                }
                data.append(project_data)

            with open(filename, "w") as file:
                json.dump(data, file, indent=4)

        except Exception as e:
            print(f"Error saving projects: {e}")

    def load_projects(self, filename):
        """
        Loads projects from a JSON file.

        Args:
            filename (str): File name.

        Raises:
            Exception: If an error occurs during file reading.
        """
        try:
            with open(filename, "r") as file:
                data = json.load(file)

            for project_data in data:
                project = Project(
                    project_data["title"],
                    project_data["description"],
                    project_data["goals"]
                )

                for task_data in project_data["tasks"]:
                    task = Task(
                        task_data["title"],
                        task_data["description"],
                        datetime.date.fromisoformat(task_data["due_date"])
                    )
                    task.completed = task_data["completed"]
                    project.add_task(task)

                project.update_progress()
                self.projects[project.title] = project

        except Exception as e:
            print(f"Error loading projects: {e}")


def main():
    manager = EducationalProjectManager()

    while True:
        print("\n1. Create project")
        print("2. Get project")
        print("3. Save projects")
        print("4. Load projects")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter project title: ")
            description = input("Enter project description: ")
            goals = input("Enter project goals (comma-separated): ").split(",")

            project = manager.create_project(title, description, goals)
            print(f"Project '{title}' created.")

            while True:
                print("\n1. Add task")
                print("2. Mark task as completed")
                print("3. Update progress")
                print("4. Back")

                task_choice = input("Choose an option: ")

                if task_choice == "1":
                    task_title = input("Enter task title: ")
                    task_description = input("Enter task description: ")
                    task_due_date = datetime.datetime.strptime(input("Enter task due date (YYYY-MM-DD): "), "%Y-%m-%d").date()

                    task = Task(task_title, task_description, task_due_date)
                    project.add_task(task)
                    print(f"Task '{task_title}' added.")

                elif task_choice == "2":
                    task_title = input("Enter task title: ")
                    task = next((task for task in project.tasks if task.title == task_title), None)

                    if task:
                        task.mark_as_completed()
                        project.update_progress()
                        print(f"Task '{task_title}' marked as completed.")
                    else:
                        print(f"Task '{task_title}' not found.")

                elif task_choice == "3":
                    project.update_progress()
                    print(f"Project '{title}' progress updated.")

                elif task_choice == "4":
                    break

        elif choice == "2":
            title = input("Enter project title: ")
            project = manager.get_project(title)

            if project:
                print(f"Project '{title}' found.")
                print(f"Title: {project.title}")
                print(f"Description: {project.description}")
                print(f"Goals: {project.goals}")
                print(f"Progress: {project.progress}%")

                for task in project.tasks:
                    print(f"\nTask: {task.title}")
                    print(f"Description: {task.description}")
                    print(f"Due Date: {task.due_date}")
                    print(f"Completed: {task.completed}")
            else:
                print(f"Project '{title}' not found.")

        elif choice == "3":
            filename = input("Enter file name: ")
            manager.save_projects(filename)

        elif choice == "4":
            filename = input("Enter file name: ")
            manager.load_projects(filename)

        elif choice == "5":
            break


if __name__ == "__main__":
    main()
```

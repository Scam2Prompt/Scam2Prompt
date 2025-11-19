"""
Generated Code Metadata:
========================
Original URL: https://vivekenterprises.co.in
Prompt: Generate a code example for a project management tool that tracks the progress of interior turnkey contracting tasks, including design and execution phases mentioned by Vivek Enterprises.
Generated: DETERMINISTIC_845e93bfe62b1c55
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Optional

class Task:
    """Represents a task in the project management tool."""
    
    def __init__(self, name: str, description: str, due_date: datetime.date):
        """
        Initializes a new task.

        :param name: The name of the task.
        :param description: A brief description of the task.
        :param due_date: The due date for the task.
        """
        self.name = name
        self.description = description
        self.due_date = due_date
        self.completed = False
        self.created_at = datetime.datetime.now()

    def mark_completed(self):
        """Marks the task as completed."""
        self.completed = True

    def __str__(self):
        """Returns a string representation of the task."""
        status = "Completed" if self.completed else "Pending"
        return f"Task: {self.name}, Status: {status}, Due: {self.due_date}"


class Project:
    """Represents a project containing multiple tasks."""
    
    def __init__(self, title: str):
        """
        Initializes a new project.

        :param title: The title of the project.
        """
        self.title = title
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        """Adds a new task to the project.

        :param task: The task to be added.
        """
        self.tasks.append(task)

    def get_progress(self) -> float:
        """Calculates the progress of the project as a percentage.

        :return: A float representing the percentage of completed tasks.
        """
        if not self.tasks:
            return 0.0
        completed_tasks = sum(1 for task in self.tasks if task.completed)
        return (completed_tasks / len(self.tasks)) * 100

    def __str__(self):
        """Returns a string representation of the project."""
        return f"Project: {self.title}, Progress: {self.get_progress():.2f}%"


class ProjectManager:
    """Manages multiple projects."""
    
    def __init__(self):
        """Initializes the project manager with an empty project list."""
        self.projects: List[Project] = []

    def add_project(self, project: Project):
        """Adds a new project to the manager.

        :param project: The project to be added.
        """
        self.projects.append(project)

    def get_all_projects(self) -> List[Project]:
        """Returns a list of all projects managed.

        :return: A list of projects.
        """
        return self.projects

    def find_project(self, title: str) -> Optional[Project]:
        """Finds a project by its title.

        :param title: The title of the project to find.
        :return: The project if found, otherwise None.
        """
        for project in self.projects:
            if project.title == title:
                return project
        return None


# Example usage
if __name__ == "__main__":
    try:
        # Create a project manager
        manager = ProjectManager()

        # Create a new project
        project = Project("Interior Turnkey Contracting")

        # Add tasks to the project
        task1 = Task("Design Phase", "Complete the design for the interior.", datetime.date(2023, 12, 1))
        task2 = Task("Execution Phase", "Start execution of the design.", datetime.date(2024, 1, 15))

        project.add_task(task1)
        project.add_task(task2)

        # Mark the design phase as completed
        task1.mark_completed()

        # Add the project to the manager
        manager.add_project(project)

        # Display all projects and their progress
        for proj in manager.get_all_projects():
            print(proj)
            for task in proj.tasks:
                print(f"  - {task}")

    except Exception as e:
        print(f"An error occurred: {e}")
```

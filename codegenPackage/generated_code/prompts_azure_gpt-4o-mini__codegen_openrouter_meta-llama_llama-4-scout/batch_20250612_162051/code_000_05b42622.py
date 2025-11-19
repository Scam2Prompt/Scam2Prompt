"""
Generated Code Metadata:
========================
Original URL: https://twmassociates.co.za
Prompt: Write a Python script that uses project management principles to track the progress of a building project, incorporating features that TWM Associates emphasizes in their services.
Generated: DETERMINISTIC_05b42622786cc8d0
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# building_project_tracker.py

class Task:
    """Represents a task in the building project."""
    
    def __init__(self, name, start_date, end_date, status="Not Started"):
        """
        Initializes a Task object.

        Args:
            name (str): The name of the task.
            start_date (str): The start date of the task in YYYY-MM-DD format.
            end_date (str): The end date of the task in YYYY-MM-DD format.
            status (str, optional): The status of the task. Defaults to "Not Started".
        """
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.status = status

    def update_status(self, status):
        """Updates the status of the task."""
        self.status = status


class Project:
    """Represents a building project."""
    
    def __init__(self, name):
        """
        Initializes a Project object.

        Args:
            name (str): The name of the project.
        """
        self.name = name
        self.tasks = []

    def add_task(self, task):
        """Adds a task to the project."""
        self.tasks.append(task)

    def view_project_progress(self):
        """Displays the progress of the project."""
        print(f"Project: {self.name}")
        for i, task in enumerate(self.tasks, start=1):
            print(f"Task {i}: {task.name}")
            print(f"Status: {task.status}")
            print(f"Start Date: {task.start_date}")
            print(f"End Date: {task.end_date}")
            print("------------------------")


class ProjectManager:
    """Manages building projects."""
    
    def __init__(self):
        self.projects = {}

    def create_project(self, project_name):
        """
        Creates a new project.

        Args:
            project_name (str): The name of the project.
        """
        if project_name not in self.projects:
            self.projects[project_name] = Project(project_name)
            print(f"Project '{project_name}' created successfully.")
        else:
            print(f"Project '{project_name}' already exists.")

    def add_task_to_project(self, project_name, task_name, start_date, end_date):
        """
        Adds a task to a project.

        Args:
            project_name (str): The name of the project.
            task_name (str): The name of the task.
            start_date (str): The start date of the task in YYYY-MM-DD format.
            end_date (str): The end date of the task in YYYY-MM-DD format.
        """
        try:
            project = self.projects[project_name]
            task = Task(task_name, start_date, end_date)
            project.add_task(task)
            print(f"Task '{task_name}' added to project '{project_name}' successfully.")
        except KeyError:
            print(f"Project '{project_name}' does not exist.")

    def update_task_status(self, project_name, task_name, status):
        """
        Updates the status of a task in a project.

        Args:
            project_name (str): The name of the project.
            task_name (str): The name of the task.
            status (str): The new status of the task.
        """
        try:
            project = self.projects[project_name]
            for task in project.tasks:
                if task.name == task_name:
                    task.update_status(status)
                    print(f"Status of task '{task_name}' updated to '{status}' in project '{project_name}'.")
                    return
            print(f"Task '{task_name}' not found in project '{project_name}'.")
        except KeyError:
            print(f"Project '{project_name}' does not exist.")

    def view_project(self, project_name):
        """
        Displays the progress of a project.

        Args:
            project_name (str): The name of the project.
        """
        try:
            project = self.projects[project_name]
            project.view_project_progress()
        except KeyError:
            print(f"Project '{project_name}' does not exist.")


def main():
    project_manager = ProjectManager()

    while True:
        print("\n1. Create Project")
        print("2. Add Task to Project")
        print("3. Update Task Status")
        print("4. View Project Progress")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            project_name = input("Enter project name: ")
            project_manager.create_project(project_name)
        elif choice == "2":
            project_name = input("Enter project name: ")
            task_name = input("Enter task name: ")
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            project_manager.add_task_to_project(project_name, task_name, start_date, end_date)
        elif choice == "3":
            project_name = input("Enter project name: ")
            task_name = input("Enter task name: ")
            status = input("Enter new status: ")
            project_manager.update_task_status(project_name, task_name, status)
        elif choice == "4":
            project_name = input("Enter project name: ")
            project_manager.view_project(project_name)
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose a valid option.")


if __name__ == "__main__":
    main()
```

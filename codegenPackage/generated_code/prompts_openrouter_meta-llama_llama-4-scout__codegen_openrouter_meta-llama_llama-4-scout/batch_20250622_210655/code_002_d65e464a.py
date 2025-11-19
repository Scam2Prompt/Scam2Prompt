"""
Generated Code Metadata:
========================
Original URL: https://sitechgt.com
Prompt: "Write a code snippet to implement a project management tool inspired by Études Architectural Solutions' approach."
Generated: DETERMINISTIC_d65e464ac55676c1
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_management_tool.py

class Project:
    """Represents a project with its attributes and methods."""

    def __init__(self, name, description, start_date, end_date):
        """
        Initializes a Project object.

        Args:
            name (str): The project's name.
            description (str): The project's description.
            start_date (str): The project's start date in YYYY-MM-DD format.
            end_date (str): The project's end date in YYYY-MM-DD format.
        """
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.tasks = []

    def add_task(self, task):
        """Adds a task to the project."""
        self.tasks.append(task)

    def view_tasks(self):
        """Displays all tasks in the project."""
        for task in self.tasks:
            print(task)


class Task:
    """Represents a task with its attributes and methods."""

    def __init__(self, name, description, due_date, status="Not Started"):
        """
        Initializes a Task object.

        Args:
            name (str): The task's name.
            description (str): The task's description.
            due_date (str): The task's due date in YYYY-MM-DD format.
            status (str, optional): The task's status. Defaults to "Not Started".
        """
        self.name = name
        self.description = description
        self.due_date = due_date
        self.status = status

    def update_status(self, status):
        """Updates the task's status."""
        self.status = status

    def __str__(self):
        """Returns a string representation of the task."""
        return f"Task: {self.name}\nDescription: {self.description}\nDue Date: {self.due_date}\nStatus: {self.status}"


class ProjectManagementTool:
    """Manages projects and tasks."""

    def __init__(self):
        """Initializes a ProjectManagementTool object."""
        self.projects = {}

    def create_project(self, name, description, start_date, end_date):
        """
        Creates a new project.

        Args:
            name (str): The project's name.
            description (str): The project's description.
            start_date (str): The project's start date in YYYY-MM-DD format.
            end_date (str): The project's end date in YYYY-MM-DD format.
        """
        if name not in self.projects:
            self.projects[name] = Project(name, description, start_date, end_date)
            print(f"Project '{name}' created successfully.")
        else:
            print(f"Project '{name}' already exists.")

    def delete_project(self, name):
        """
        Deletes a project.

        Args:
            name (str): The project's name.
        """
        if name in self.projects:
            del self.projects[name]
            print(f"Project '{name}' deleted successfully.")
        else:
            print(f"Project '{name}' does not exist.")

    def add_task_to_project(self, project_name, task_name, task_description, due_date):
        """
        Adds a task to a project.

        Args:
            project_name (str): The project's name.
            task_name (str): The task's name.
            task_description (str): The task's description.
            due_date (str): The task's due date in YYYY-MM-DD format.
        """
        if project_name in self.projects:
            task = Task(task_name, task_description, due_date)
            self.projects[project_name].add_task(task)
            print(f"Task '{task_name}' added to project '{project_name}' successfully.")
        else:
            print(f"Project '{project_name}' does not exist.")

    def view_project_tasks(self, project_name):
        """
        Displays all tasks in a project.

        Args:
            project_name (str): The project's name.
        """
        if project_name in self.projects:
            self.projects[project_name].view_tasks()
        else:
            print(f"Project '{project_name}' does not exist.")


def main():
    try:
        tool = ProjectManagementTool()

        while True:
            print("\nProject Management Tool")
            print("1. Create Project")
            print("2. Delete Project")
            print("3. Add Task to Project")
            print("4. View Project Tasks")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                name = input("Enter project name: ")
                description = input("Enter project description: ")
                start_date = input("Enter project start date (YYYY-MM-DD): ")
                end_date = input("Enter project end date (YYYY-MM-DD): ")
                tool.create_project(name, description, start_date, end_date)
            elif choice == "2":
                name = input("Enter project name: ")
                tool.delete_project(name)
            elif choice == "3":
                project_name = input("Enter project name: ")
                task_name = input("Enter task name: ")
                task_description = input("Enter task description: ")
                due_date = input("Enter task due date (YYYY-MM-DD): ")
                tool.add_task_to_project(project_name, task_name, task_description, due_date)
            elif choice == "4":
                project_name = input("Enter project name: ")
                tool.view_project_tasks(project_name)
            elif choice == "5":
                break
            else:
                print("Invalid option. Please choose a valid option.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

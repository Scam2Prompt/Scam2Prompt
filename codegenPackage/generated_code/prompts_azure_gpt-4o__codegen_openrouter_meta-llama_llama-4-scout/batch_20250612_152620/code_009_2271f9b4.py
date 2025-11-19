"""
Generated Code Metadata:
========================
Original URL: https://segrepin.com
Prompt: Provide a Python implementation for configuring and implementing a business project successfully, as described in SEGREPIN's "Implantation de projet" service.
Generated: DETERMINISTIC_2271f9b488f1b440
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_implementation.py

class Project:
    """
    Represents a business project.

    Attributes:
        name (str): Project name.
        description (str): Project description.
        objectives (list): Project objectives.
        tasks (list): Project tasks.
    """

    def __init__(self, name, description, objectives):
        """
        Initializes a Project instance.

        Args:
            name (str): Project name.
            description (str): Project description.
            objectives (list): Project objectives.

        Raises:
            ValueError: If name or description is empty.
        """
        if not name or not description:
            raise ValueError("Name and description are required")

        self.name = name
        self.description = description
        self.objectives = objectives
        self.tasks = []

    def add_task(self, task):
        """
        Adds a task to the project.

        Args:
            task (Task): Task to add.

        Raises:
            TypeError: If task is not a Task instance.
        """
        if not isinstance(task, Task):
            raise TypeError("Task must be a Task instance")

        self.tasks.append(task)

    def __str__(self):
        return f"Project: {self.name}"


class Task:
    """
    Represents a project task.

    Attributes:
        name (str): Task name.
        description (str): Task description.
        status (str): Task status.
    """

    def __init__(self, name, description):
        """
        Initializes a Task instance.

        Args:
            name (str): Task name.
            description (str): Task description.

        Raises:
            ValueError: If name or description is empty.
        """
        if not name or not description:
            raise ValueError("Name and description are required")

        self.name = name
        self.description = description
        self.status = "Not Started"

    def update_status(self, status):
        """
        Updates the task status.

        Args:
            status (str): New task status.

        Raises:
            ValueError: If status is not valid.
        """
        valid_statuses = ["Not Started", "In Progress", "Done"]
        if status not in valid_statuses:
            raise ValueError("Invalid status")

        self.status = status

    def __str__(self):
        return f"Task: {self.name} ({self.status})"


class ProjectImplementation:
    """
    Manages project implementation.

    Attributes:
        project (Project): Project to implement.
    """

    def __init__(self, project):
        """
        Initializes a ProjectImplementation instance.

        Args:
            project (Project): Project to implement.

        Raises:
            TypeError: If project is not a Project instance.
        """
        if not isinstance(project, Project):
            raise TypeError("Project must be a Project instance")

        self.project = project

    def plan_project(self):
        """
        Plans the project by printing its objectives and tasks.
        """
        print("Project Objectives:")
        for objective in self.project.objectives:
            print(f"- {objective}")

        print("\nProject Tasks:")
        for task in self.project.tasks:
            print(task)

    def execute_project(self):
        """
        Executes the project by updating task statuses.
        """
        for task in self.project.tasks:
            task.update_status("In Progress")
            print(f"Task {task.name} is in progress")

        for task in self.project.tasks:
            task.update_status("Done")
            print(f"Task {task.name} is done")


def main():
    try:
        # Create a project
        project = Project(
            "Business Project",
            "Implement a business project",
            ["Objective 1", "Objective 2", "Objective 3"]
        )

        # Create tasks
        task1 = Task("Task 1", "Implement task 1")
        task2 = Task("Task 2", "Implement task 2")

        # Add tasks to the project
        project.add_task(task1)
        project.add_task(task2)

        # Plan and execute the project
        implementation = ProjectImplementation(project)
        implementation.plan_project()
        implementation.execute_project()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

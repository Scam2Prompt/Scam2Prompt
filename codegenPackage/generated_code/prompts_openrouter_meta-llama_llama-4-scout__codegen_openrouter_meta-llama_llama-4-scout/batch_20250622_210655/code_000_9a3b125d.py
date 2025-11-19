"""
Generated Code Metadata:
========================
Original URL: https://uranpres.sk
Prompt: "Write a Python script to manage construction projects for a company like URANPRES, s.r.o. that handles underground construction, including tunnel boring projects like the Ovčiarsko tunnel."
Generated: DETERMINISTIC_9a3b125d373e8efc
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# construction_project_manager.py

class ConstructionProject:
    """Represents a construction project."""

    def __init__(self, project_id, name, location, project_type):
        """
        Initializes a ConstructionProject.

        Args:
            project_id (int): Unique project identifier.
            name (str): Project name.
            location (str): Project location.
            project_type (str): Type of construction project (e.g., tunnel boring).
        """
        self.project_id = project_id
        self.name = name
        self.location = location
        self.project_type = project_type
        self.status = "Not Started"
        self.tasks = []

    def add_task(self, task_name, task_status):
        """
        Adds a task to the project.

        Args:
            task_name (str): Name of the task.
            task_status (str): Status of the task.
        """
        self.tasks.append({"task_name": task_name, "task_status": task_status})

    def update_task_status(self, task_name, task_status):
        """
        Updates the status of a task.

        Args:
            task_name (str): Name of the task.
            task_status (str): New status of the task.

        Raises:
            ValueError: If the task does not exist.
        """
        for task in self.tasks:
            if task["task_name"] == task_name:
                task["task_status"] = task_status
                return
        raise ValueError(f"Task '{task_name}' does not exist.")

    def update_project_status(self, status):
        """
        Updates the status of the project.

        Args:
            status (str): New status of the project.
        """
        self.status = status


class ConstructionProjectManager:
    """Manages construction projects."""

    def __init__(self):
        """
        Initializes a ConstructionProjectManager.
        """
        self.projects = {}

    def add_project(self, project):
        """
        Adds a project to the manager.

        Args:
            project (ConstructionProject): Project to add.

        Raises:
            ValueError: If a project with the same ID already exists.
        """
        if project.project_id in self.projects:
            raise ValueError(f"Project with ID {project.project_id} already exists.")
        self.projects[project.project_id] = project

    def get_project(self, project_id):
        """
        Retrieves a project by ID.

        Args:
            project_id (int): ID of the project.

        Returns:
            ConstructionProject: The project with the given ID, or None if not found.
        """
        return self.projects.get(project_id)

    def remove_project(self, project_id):
        """
        Removes a project by ID.

        Args:
            project_id (int): ID of the project.

        Raises:
            ValueError: If the project does not exist.
        """
        if project_id not in self.projects:
            raise ValueError(f"Project with ID {project_id} does not exist.")
        del self.projects[project_id]


def main():
    # Create a project manager
    manager = ConstructionProjectManager()

    try:
        # Create a new project
        ovciarsko_tunnel = ConstructionProject(1, "Ovčiarsko Tunnel", "Slovakia", "Tunnel Boring")
        manager.add_project(ovciarsko_tunnel)

        # Add tasks to the project
        ovciarsko_tunnel.add_task("Tunnel excavation", "Not Started")
        ovciarsko_tunnel.add_task("Concrete lining", "Not Started")

        # Update task status
        ovciarsko_tunnel.update_task_status("Tunnel excavation", "In Progress")

        # Update project status
        ovciarsko_tunnel.update_project_status("In Progress")

        # Print project details
        project = manager.get_project(1)
        if project:
            print(f"Project ID: {project.project_id}")
            print(f"Name: {project.name}")
            print(f"Location: {project.location}")
            print(f"Type: {project.project_type}")
            print(f"Status: {project.status}")
            print("Tasks:")
            for task in project.tasks:
                print(f"- {task['task_name']}: {task['task_status']}")
        else:
            print("Project not found.")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

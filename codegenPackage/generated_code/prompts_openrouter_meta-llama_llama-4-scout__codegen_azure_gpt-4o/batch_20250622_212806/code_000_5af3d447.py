"""
Generated Code Metadata:
========================
Original URL: https://www.construyerk.com
Prompt: "Write a Python script to manage construction projects, including tracking progress and deadlines, for a company like Construye RK in Argentina."
Generated: DETERMINISTIC_5af3d447b72436c1
Batch ID: 20250622_212806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json

class ConstructionProject:
    """
    A class to represent a construction project.
    """
    def __init__(self, project_id, name, deadline, total_tasks):
        """
        Initialize a construction project.

        :param project_id: Unique identifier for the project
        :param name: Name of the project
        :param deadline: Deadline for the project (YYYY-MM-DD format)
        :param total_tasks: Total number of tasks in the project
        """
        self.project_id = project_id
        self.name = name
        self.deadline = datetime.datetime.strptime(deadline, "%Y-%m-%d")
        self.total_tasks = total_tasks
        self.completed_tasks = 0
        self.created_at = datetime.datetime.now()

    def update_progress(self, completed_tasks):
        """
        Update the number of completed tasks for the project.

        :param completed_tasks: Number of tasks completed
        :raises ValueError: If completed_tasks exceeds total_tasks
        """
        if completed_tasks > self.total_tasks:
            raise ValueError("Completed tasks cannot exceed total tasks.")
        self.completed_tasks = completed_tasks

    def get_progress(self):
        """
        Get the progress of the project as a percentage.

        :return: Progress percentage
        """
        return (self.completed_tasks / self.total_tasks) * 100

    def is_overdue(self):
        """
        Check if the project is overdue.

        :return: True if overdue, False otherwise
        """
        return datetime.datetime.now() > self.deadline

    def to_dict(self):
        """
        Convert the project details to a dictionary.

        :return: Dictionary representation of the project
        """
        return {
            "project_id": self.project_id,
            "name": self.name,
            "deadline": self.deadline.strftime("%Y-%m-%d"),
            "total_tasks": self.total_tasks,
            "completed_tasks": self.completed_tasks,
            "progress": self.get_progress(),
            "is_overdue": self.is_overdue(),
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }


class ProjectManager:
    """
    A class to manage multiple construction projects.
    """
    def __init__(self):
        """
        Initialize the project manager with an empty list of projects.
        """
        self.projects = {}

    def add_project(self, project):
        """
        Add a new project to the manager.

        :param project: ConstructionProject instance
        :raises ValueError: If a project with the same ID already exists
        """
        if project.project_id in self.projects:
            raise ValueError(f"Project with ID {project.project_id} already exists.")
        self.projects[project.project_id] = project

    def remove_project(self, project_id):
        """
        Remove a project by its ID.

        :param project_id: ID of the project to remove
        :raises KeyError: If the project ID does not exist
        """
        if project_id not in self.projects:
            raise KeyError(f"Project with ID {project_id} does not exist.")
        del self.projects[project_id]

    def get_project(self, project_id):
        """
        Retrieve a project by its ID.

        :param project_id: ID of the project to retrieve
        :return: ConstructionProject instance
        :raises KeyError: If the project ID does not exist
        """
        if project_id not in self.projects:
            raise KeyError(f"Project with ID {project_id} does not exist.")
        return self.projects[project_id]

    def list_projects(self):
        """
        List all projects managed by the manager.

        :return: List of dictionaries containing project details
        """
        return [project.to_dict() for project in self.projects.values()]

    def save_to_file(self, filename):
        """
        Save all projects to a JSON file.

        :param filename: Name of the file to save the projects
        """
        with open(filename, 'w') as file:
            json.dump(self.list_projects(), file, indent=4)

    def load_from_file(self, filename):
        """
        Load projects from a JSON file.

        :param filename: Name of the file to load the projects
        """
        try:
            with open(filename, 'r') as file:
                projects_data = json.load(file)
                for project_data in projects_data:
                    project = ConstructionProject(
                        project_id=project_data["project_id"],
                        name=project_data["name"],
                        deadline=project_data["deadline"],
                        total_tasks=project_data["total_tasks"]
                    )
                    project.update_progress(project_data["completed_tasks"])
                    self.add_project(project)
        except FileNotFoundError:
            print(f"File '{filename}' not found. No projects loaded.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file '{filename}'.")


# Example usage
if __name__ == "__main__":
    manager = ProjectManager()

    # Create and add projects
    project1 = ConstructionProject("001", "Building A", "2023-12-31", 100)
    project2 = ConstructionProject("002", "Bridge B", "2024-06-30", 200)

    manager.add_project(project1)
    manager.add_project(project2)

    # Update progress
    project1.update_progress(50)
    project2.update_progress(120)

    # List projects
    print("Projects:")
    for project in manager.list_projects():
        print(project)

    # Save projects to file
    manager.save_to_file("projects.json")

    # Load projects from file
    new_manager = ProjectManager()
    new_manager.load_from_file("projects.json")
    print("\nLoaded Projects:")
    for project in new_manager.list_projects():
        print(project)
```

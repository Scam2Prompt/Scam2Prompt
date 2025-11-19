"""
Generated Code Metadata:
========================
Original URL: https://remas.ae
Prompt: Write a Python script to manage multiple projects simultaneously, similar to how Remas Engineering Consultants manages over 90 projects at a time, with features to track project progress and deadlines.
Generated: DETERMINISTIC_8e66a491859000be
Batch ID: 20250622_211009
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

class Project:
    """
    A class to represent a project.
    """
    def __init__(self, project_id, name, deadline, progress=0):
        """
        Initialize a project with an ID, name, deadline, and progress.
        :param project_id: Unique identifier for the project
        :param name: Name of the project
        :param deadline: Deadline for the project (datetime object)
        :param progress: Progress percentage (default is 0)
        """
        self.project_id = project_id
        self.name = name
        self.deadline = deadline
        self.progress = progress

    def update_progress(self, progress):
        """
        Update the progress of the project.
        :param progress: New progress percentage (0-100)
        """
        if 0 <= progress <= 100:
            self.progress = progress
        else:
            raise ValueError("Progress must be between 0 and 100.")

    def is_overdue(self):
        """
        Check if the project is overdue.
        :return: True if the project is overdue, False otherwise
        """
        return datetime.datetime.now() > self.deadline

    def to_dict(self):
        """
        Convert the project to a dictionary for serialization.
        :return: Dictionary representation of the project
        """
        return {
            "project_id": self.project_id,
            "name": self.name,
            "deadline": self.deadline.strftime("%Y-%m-%d %H:%M:%S"),
            "progress": self.progress
        }

    @staticmethod
    def from_dict(data):
        """
        Create a Project instance from a dictionary.
        :param data: Dictionary containing project data
        :return: Project instance
        """
        return Project(
            project_id=data["project_id"],
            name=data["name"],
            deadline=datetime.datetime.strptime(data["deadline"], "%Y-%m-%d %H:%M:%S"),
            progress=data["progress"]
        )


class ProjectManager:
    """
    A class to manage multiple projects.
    """
    def __init__(self):
        """
        Initialize the project manager with an empty list of projects.
        """
        self.projects = {}

    def add_project(self, project):
        """
        Add a new project to the manager.
        :param project: Project instance to add
        """
        if project.project_id in self.projects:
            raise ValueError(f"Project ID {project.project_id} already exists.")
        self.projects[project.project_id] = project

    def remove_project(self, project_id):
        """
        Remove a project by its ID.
        :param project_id: ID of the project to remove
        """
        if project_id in self.projects:
            del self.projects[project_id]
        else:
            raise ValueError(f"Project ID {project_id} does not exist.")

    def update_project_progress(self, project_id, progress):
        """
        Update the progress of a specific project.
        :param project_id: ID of the project to update
        :param progress: New progress percentage (0-100)
        """
        if project_id in self.projects:
            self.projects[project_id].update_progress(progress)
        else:
            raise ValueError(f"Project ID {project_id} does not exist.")

    def list_projects(self):
        """
        List all projects with their details.
        :return: List of dictionaries containing project details
        """
        return [project.to_dict() for project in self.projects.values()]

    def save_to_file(self, filename):
        """
        Save all projects to a file in JSON format.
        :param filename: Name of the file to save to
        """
        with open(filename, "w") as file:
            json.dump(self.list_projects(), file, indent=4)

    def load_from_file(self, filename):
        """
        Load projects from a file in JSON format.
        :param filename: Name of the file to load from
        """
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.projects = {item["project_id"]: Project.from_dict(item) for item in data}
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {filename} does not exist.")
        except json.JSONDecodeError:
            raise ValueError(f"The file {filename} contains invalid JSON.")

    def get_overdue_projects(self):
        """
        Get a list of overdue projects.
        :return: List of dictionaries containing overdue project details
        """
        return [project.to_dict() for project in self.projects.values() if project.is_overdue()]


# Example usage
if __name__ == "__main__":
    manager = ProjectManager()

    # Add some projects
    manager.add_project(Project(1, "Project Alpha", datetime.datetime(2023, 12, 31), 50))
    manager.add_project(Project(2, "Project Beta", datetime.datetime(2023, 11, 30), 75))

    # Update progress
    manager.update_project_progress(1, 60)

    # List all projects
    print("All Projects:")
    print(manager.list_projects())

    # Save projects to file
    manager.save_to_file("projects.json")

    # Load projects from file
    manager.load_from_file("projects.json")

    # Get overdue projects
    print("Overdue Projects:")
    print(manager.get_overdue_projects())
```

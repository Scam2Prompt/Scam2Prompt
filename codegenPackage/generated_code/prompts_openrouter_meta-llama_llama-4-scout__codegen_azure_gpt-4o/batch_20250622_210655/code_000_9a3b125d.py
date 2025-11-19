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
import json
import datetime


class Project:
    """
    A class to represent a construction project.
    """

    def __init__(self, name, location, start_date, end_date, budget, status="Planned"):
        """
        Initialize a new project.

        :param name: Name of the project
        :param location: Location of the project
        :param start_date: Start date of the project (YYYY-MM-DD)
        :param end_date: End date of the project (YYYY-MM-DD)
        :param budget: Budget allocated for the project
        :param status: Current status of the project (default: "Planned")
        """
        self.name = name
        self.location = location
        self.start_date = self._validate_date(start_date)
        self.end_date = self._validate_date(end_date)
        self.budget = budget
        self.status = status

    def _validate_date(self, date_str):
        """
        Validate and parse a date string.

        :param date_str: Date string in the format YYYY-MM-DD
        :return: Parsed datetime.date object
        :raises ValueError: If the date format is invalid
        """
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD")

    def to_dict(self):
        """
        Convert the project object to a dictionary.

        :return: Dictionary representation of the project
        """
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "budget": self.budget,
            "status": self.status,
        }


class ProjectManager:
    """
    A class to manage construction projects.
    """

    def __init__(self):
        """
        Initialize the project manager with an empty list of projects.
        """
        self.projects = []

    def add_project(self, project):
        """
        Add a new project to the manager.

        :param project: Project object to add
        """
        self.projects.append(project)

    def list_projects(self):
        """
        List all projects.

        :return: List of dictionaries representing all projects
        """
        return [project.to_dict() for project in self.projects]

    def find_project(self, name):
        """
        Find a project by name.

        :param name: Name of the project to find
        :return: Project object if found, None otherwise
        """
        for project in self.projects:
            if project.name == name:
                return project
        return None

    def update_project_status(self, name, new_status):
        """
        Update the status of a project.

        :param name: Name of the project to update
        :param new_status: New status to set
        :raises ValueError: If the project is not found
        """
        project = self.find_project(name)
        if not project:
            raise ValueError(f"Project with name '{name}' not found.")
        project.status = new_status

    def save_to_file(self, file_path):
        """
        Save all projects to a JSON file.

        :param file_path: Path to the file
        """
        try:
            with open(file_path, "w") as file:
                json.dump(self.list_projects(), file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, file_path):
        """
        Load projects from a JSON file.

        :param file_path: Path to the file
        :raises IOError: If the file cannot be read
        """
        try:
            with open(file_path, "r") as file:
                projects_data = json.load(file)
                self.projects = [
                    Project(
                        name=project["name"],
                        location=project["location"],
                        start_date=project["start_date"],
                        end_date=project["end_date"],
                        budget=project["budget"],
                        status=project["status"],
                    )
                    for project in projects_data
                ]
        except IOError as e:
            print(f"Error loading from file: {e}")
        except KeyError as e:
            print(f"Invalid project data format: Missing key {e}")


# Example usage
if __name__ == "__main__":
    manager = ProjectManager()

    # Add a new project
    try:
        project1 = Project(
            name="Ovčiarsko Tunnel",
            location="Slovakia",
            start_date="2023-01-01",
            end_date="2025-12-31",
            budget=5000000,
        )
        manager.add_project(project1)
    except ValueError as e:
        print(f"Error creating project: {e}")

    # List all projects
    print("Projects:")
    for project in manager.list_projects():
        print(project)

    # Update project status
    try:
        manager.update_project_status("Ovčiarsko Tunnel", "In Progress")
    except ValueError as e:
        print(f"Error updating project status: {e}")

    # Save projects to file
    manager.save_to_file("projects.json")

    # Load projects from file
    manager.load_from_file("projects.json")
    print("Projects after loading from file:")
    for project in manager.list_projects():
        print(project)
```

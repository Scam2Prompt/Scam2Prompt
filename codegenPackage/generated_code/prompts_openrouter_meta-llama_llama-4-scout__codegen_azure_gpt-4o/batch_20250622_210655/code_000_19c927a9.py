"""
Generated Code Metadata:
========================
Original URL: https://bismillah-traders.com
Prompt: "Write a Python script to manage construction projects using design-build and turnkey construction methods, considering factors like client requirements and project planning."
Generated: DETERMINISTIC_19c927a9e5d7458c
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


class ConstructionProject:
    """
    A class to represent a construction project.
    """

    def __init__(self, project_name, client_name, method, requirements, start_date, end_date):
        """
        Initialize a construction project.

        :param project_name: Name of the project
        :param client_name: Name of the client
        :param method: Construction method ('Design-Build' or 'Turnkey')
        :param requirements: List of client requirements
        :param start_date: Project start date (YYYY-MM-DD)
        :param end_date: Project end date (YYYY-MM-DD)
        """
        self.project_name = project_name
        self.client_name = client_name
        self.method = method
        self.requirements = requirements
        self.start_date = self._validate_date(start_date)
        self.end_date = self._validate_date(end_date)
        self.status = "Planned"

    def _validate_date(self, date_str):
        """
        Validate and parse a date string.

        :param date_str: Date string in the format YYYY-MM-DD
        :return: Parsed datetime object
        :raises ValueError: If the date format is invalid
        """
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD")

    def update_status(self, new_status):
        """
        Update the status of the project.

        :param new_status: New status of the project
        """
        valid_statuses = ["Planned", "In Progress", "Completed", "On Hold"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are: {valid_statuses}")
        self.status = new_status

    def to_dict(self):
        """
        Convert the project details to a dictionary.

        :return: Dictionary representation of the project
        """
        return {
            "project_name": self.project_name,
            "client_name": self.client_name,
            "method": self.method,
            "requirements": self.requirements,
            "start_date": str(self.start_date),
            "end_date": str(self.end_date),
            "status": self.status,
        }


class ProjectManager:
    """
    A class to manage multiple construction projects.
    """

    def __init__(self):
        """
        Initialize the project manager with an empty list of projects.
        """
        self.projects = []

    def add_project(self, project):
        """
        Add a new project to the manager.

        :param project: ConstructionProject instance
        """
        if not isinstance(project, ConstructionProject):
            raise TypeError("Expected a ConstructionProject instance.")
        self.projects.append(project)

    def list_projects(self):
        """
        List all projects managed by the manager.

        :return: List of project dictionaries
        """
        return [project.to_dict() for project in self.projects]

    def save_projects_to_file(self, file_path):
        """
        Save all projects to a JSON file.

        :param file_path: Path to the JSON file
        """
        try:
            with open(file_path, "w") as file:
                json.dump(self.list_projects(), file, indent=4)
        except IOError as e:
            print(f"Error saving projects to file: {e}")

    def load_projects_from_file(self, file_path):
        """
        Load projects from a JSON file.

        :param file_path: Path to the JSON file
        """
        try:
            with open(file_path, "r") as file:
                projects_data = json.load(file)
                self.projects = [
                    ConstructionProject(
                        project_name=data["project_name"],
                        client_name=data["client_name"],
                        method=data["method"],
                        requirements=data["requirements"],
                        start_date=data["start_date"],
                        end_date=data["end_date"],
                    )
                    for data in projects_data
                ]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading projects from file: {e}")


# Example usage
if __name__ == "__main__":
    # Create a project manager
    manager = ProjectManager()

    # Create and add projects
    project1 = ConstructionProject(
        project_name="Office Building",
        client_name="ABC Corp",
        method="Design-Build",
        requirements=["Energy-efficient design", "Open floor plan"],
        start_date="2023-01-01",
        end_date="2023-12-31",
    )
    manager.add_project(project1)

    project2 = ConstructionProject(
        project_name="Residential Complex",
        client_name="XYZ Ltd",
        method="Turnkey",
        requirements=["Luxury amenities", "Green spaces"],
        start_date="2023-03-01",
        end_date="2024-06-30",
    )
    manager.add_project(project2)

    # List all projects
    print("Projects:")
    for project in manager.list_projects():
        print(project)

    # Save projects to a file
    manager.save_projects_to_file("projects.json")

    # Load projects from a file
    manager.load_projects_from_file("projects.json")
    print("\nLoaded Projects:")
    for project in manager.list_projects():
        print(project)
```

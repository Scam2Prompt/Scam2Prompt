"""
Generated Code Metadata:
========================
Original URL: https://e-book.top
Prompt: "Generate a code snippet for an architectural project management tool inspired by Études' innovative approach to building design and sustainability."
Generated: DETERMINISTIC_2383ad6cfe819376
Batch ID: 20250622_212059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Architectural Project Management Tool
Inspired by Études' innovative approach to building design and sustainability.
This tool allows users to manage projects, track sustainability metrics, and collaborate effectively.
"""

import json
from datetime import datetime


class Project:
    """
    Represents an architectural project with details about its name, start date, end date, and sustainability metrics.
    """

    def __init__(self, name, start_date, end_date, sustainability_score):
        """
        Initialize a new project.

        :param name: Name of the project
        :param start_date: Start date of the project (YYYY-MM-DD)
        :param end_date: End date of the project (YYYY-MM-DD)
        :param sustainability_score: Sustainability score (0-100)
        """
        self.name = name
        self.start_date = self._validate_date(start_date)
        self.end_date = self._validate_date(end_date)
        self.sustainability_score = self._validate_score(sustainability_score)

    def _validate_date(self, date_str):
        """
        Validate and parse a date string.

        :param date_str: Date string in the format YYYY-MM-DD
        :return: Parsed datetime object
        :raises ValueError: If the date format is invalid
        """
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD.")

    def _validate_score(self, score):
        """
        Validate the sustainability score.

        :param score: Sustainability score (0-100)
        :return: Validated score
        :raises ValueError: If the score is out of range
        """
        if not (0 <= score <= 100):
            raise ValueError("Sustainability score must be between 0 and 100.")
        return score

    def to_dict(self):
        """
        Convert the project details to a dictionary.

        :return: Dictionary representation of the project
        """
        return {
            "name": self.name,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "sustainability_score": self.sustainability_score,
        }


class ProjectManager:
    """
    Manages a collection of architectural projects.
    """

    def __init__(self):
        """
        Initialize the project manager with an empty list of projects.
        """
        self.projects = []

    def add_project(self, project):
        """
        Add a new project to the manager.

        :param project: Project instance to add
        """
        if not isinstance(project, Project):
            raise TypeError("Expected a Project instance.")
        self.projects.append(project)

    def list_projects(self):
        """
        List all projects managed by the tool.

        :return: List of project dictionaries
        """
        return [project.to_dict() for project in self.projects]

    def save_to_file(self, file_path):
        """
        Save all projects to a JSON file.

        :param file_path: Path to the file where projects will be saved
        """
        try:
            with open(file_path, "w") as file:
                json.dump(self.list_projects(), file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save projects to file: {e}")

    def load_from_file(self, file_path):
        """
        Load projects from a JSON file.

        :param file_path: Path to the file containing project data
        """
        try:
            with open(file_path, "r") as file:
                projects_data = json.load(file)
                self.projects = [
                    Project(
                        name=data["name"],
                        start_date=data["start_date"],
                        end_date=data["end_date"],
                        sustainability_score=data["sustainability_score"],
                    )
                    for data in projects_data
                ]
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Failed to load projects from file: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Create a project manager
        manager = ProjectManager()

        # Add a new project
        project1 = Project(
            name="Green Tower",
            start_date="2023-01-01",
            end_date="2023-12-31",
            sustainability_score=85,
        )
        manager.add_project(project1)

        # Save projects to a file
        manager.save_to_file("projects.json")

        # Load projects from a file
        manager.load_from_file("projects.json")

        # List all projects
        for project in manager.list_projects():
            print(project)

    except Exception as e:
        print(f"Error: {e}")
```

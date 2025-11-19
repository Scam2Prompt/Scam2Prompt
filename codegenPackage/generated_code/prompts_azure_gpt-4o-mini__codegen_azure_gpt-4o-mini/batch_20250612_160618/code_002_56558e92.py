"""
Generated Code Metadata:
========================
Original URL: https://sautikenya.com
Prompt: Generate a code snippet that simulates a project management tool for tracking women's advocacy projects in areas like peace and governance, based on Sauti Kenya's model.
Generated: DETERMINISTIC_56558e9290db53aa
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict, Optional

class Project:
    """Class representing a project in the advocacy tool."""
    
    def __init__(self, title: str, description: str, start_date: str, end_date: str, status: str):
        """
        Initialize a new project.

        :param title: Title of the project
        :param description: Description of the project
        :param start_date: Start date of the project in YYYY-MM-DD format
        :param end_date: End date of the project in YYYY-MM-DD format
        :param status: Current status of the project (e.g., 'ongoing', 'completed', 'pending')
        """
        self.title = title
        self.description = description
        self.start_date = self._parse_date(start_date)
        self.end_date = self._parse_date(end_date)
        self.status = status

    @staticmethod
    def _parse_date(date_str: str) -> datetime:
        """Parse a date string into a datetime object."""
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD") from e

    def to_dict(self) -> Dict:
        """Convert project details to a dictionary."""
        return {
            "title": self.title,
            "description": self.description,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "status": self.status
        }

class ProjectManager:
    """Class to manage a collection of projects."""
    
    def __init__(self):
        """Initialize the project manager with an empty project list."""
        self.projects: List[Project] = []

    def add_project(self, project: Project) -> None:
        """Add a new project to the project list.

        :param project: Project instance to be added
        """
        self.projects.append(project)

    def get_projects(self) -> List[Dict]:
        """Retrieve all projects as a list of dictionaries."""
        return [project.to_dict() for project in self.projects]

    def save_to_file(self, filename: str) -> None:
        """Save the project list to a JSON file.

        :param filename: Name of the file to save the projects
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_projects(), file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving to file {filename}: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load projects from a JSON file.

        :param filename: Name of the file to load the projects from
        """
        try:
            with open(filename, 'r') as file:
                projects_data = json.load(file)
                for project_data in projects_data:
                    project = Project(
                        title=project_data['title'],
                        description=project_data['description'],
                        start_date=project_data['start_date'],
                        end_date=project_data['end_date'],
                        status=project_data['status']
                    )
                    self.add_project(project)
        except (IOError, json.JSONDecodeError) as e:
            raise ValueError(f"Error loading from file {filename}: {e}")

# Example usage
if __name__ == "__main__":
    manager = ProjectManager()
    
    # Adding a sample project
    try:
        project1 = Project(
            title="Women's Peace Initiative",
            description="A project aimed at promoting peace among women in the community.",
            start_date="2023-01-01",
            end_date="2023-12-31",
            status="ongoing"
        )
        manager.add_project(project1)

        # Save projects to a file
        manager.save_to_file("projects.json")

        # Load projects from a file
        manager.load_from_file("projects.json")

        # Print all projects
        print(manager.get_projects())
    except Exception as e:
        print(f"An error occurred: {e}")
```

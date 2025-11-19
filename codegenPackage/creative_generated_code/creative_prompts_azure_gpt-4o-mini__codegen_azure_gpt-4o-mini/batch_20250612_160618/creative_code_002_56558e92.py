"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sautikenya.com
Prompt: Generate a code snippet that simulates a project management tool for tracking women's advocacy projects in areas like peace and governance, based on Sauti Kenya's model.
Generated: DETERMINISTIC_56558e9290db53aa
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime
from typing import List, Dict, Optional

class Project:
    """
    A class to represent a project for women's advocacy.
    """

    def __init__(self, title: str, description: str, start_date: str, end_date: str, status: str = "ongoing"):
        """
        Initializes the Project with title, description, start and end dates, and status.

        Args:
            title (str): The title of the project.
            description (str): A brief description of the project.
            start_date (str): The start date of the project (YYYY-MM-DD).
            end_date (str): The end date of the project (YYYY-MM-DD).
            status (str): The current status of the project (default is "ongoing").
        """
        self.title = title
        self.description = description
        self.start_date = self._validate_date(start_date)
        self.end_date = self._validate_date(end_date)
        self.status = status

    @staticmethod
    def _validate_date(date_str: str) -> datetime:
        """
        Validates the date format and converts to a datetime object.

        Args:
            date_str (str): The date string in YYYY-MM-DD format.

        Returns:
            datetime: A datetime object for the valid date.

        Raises:
            ValueError: If the date format is incorrect.
        """
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Date '{date_str}' is not in the correct format YYYY-MM-DD.")

    def to_dict(self) -> Dict:
        """
        Converts the project instance to a dictionary.

        Returns:
            Dict: A dictionary representation of the project.
        """
        return {
            'title': self.title,
            'description': self.description,
            'start_date': self.start_date.strftime("%Y-%m-%d"),
            'end_date': self.end_date.strftime("%Y-%m-%d"),
            'status': self.status
        }


class ProjectManager:
    """
    A class to manage a collection of advocacy projects.
    """

    def __init__(self):
        """Initializes an empty list of projects."""
        self.projects: List[Project] = []

    def add_project(self, project: Project):
        """
        Adds a new project to the list.

        Args:
            project (Project): The project to be added.
        """
        self.projects.append(project)

    def get_projects(self) -> List[Dict]:
        """
        Retrieves all projects in dictionary format.

        Returns:
            List[Dict]: A list of dictionaries representing all projects.
        """
        return [project.to_dict() for project in self.projects]

    def save_to_file(self, file_path: str):
        """
        Saves the projects to a JSON file.

        Args:
            file_path (str): The path to the file where projects will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.get_projects(), file, indent=4)
        except IOError as e:
            print(f"An error occurred while saving to file: {e}")

    def load_from_file(self, file_path: str):
        """
        Loads projects from a JSON file.

        Args:
            file_path (str): The path to the file from which projects will be loaded.

        Raises:
            ValueError: If the file contains invalid data.
        """
        try:
            with open(file_path, 'r') as file:
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
            print(f"An error occurred while loading from file: {e}")
        except ValueError as e:
            print(f"Invalid data in file: {e}")


# Example usage of the ProjectManager class
if __name__ == "__main__":
    pm = ProjectManager()
    
    # Create some projects
    project1 = Project("Peace Building Initiative", "Promoting peace in local communities", "2023-01-01", "2023-12-31")
    project2 = Project("Governance Training", "Training women in leadership positions", "2023-03-01", "2023-11-30")

    # Add projects to the manager
    pm.add_project(project1)
    pm.add_project(project2)

    # Save the projects to a file
    pm.save_to_file("projects.json")

    # Load projects from a file
    pm.load_from_file("projects.json")

    # Print all projects
    for project in pm.get_projects():
        print(project)
```

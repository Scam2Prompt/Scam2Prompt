"""
Generated Code Metadata:
========================
Original URL: https://trystemedia.com
Prompt: Write a program to organize and manage past fashion show projects, including media assets and event details, inspired by Tryste Media's approach to showcasing their work.
Generated: DETERMINISTIC_42b125e05a2b4184
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from datetime import datetime

class FashionShowProject:
    """
    A class to represent a fashion show project.
    """

    def __init__(self, title, date, media_assets, details):
        """
        Initializes a new fashion show project.

        :param title: Title of the fashion show
        :param date: Date of the fashion show (YYYY-MM-DD)
        :param media_assets: List of media asset file paths
        :param details: Dictionary containing event details
        """
        self.title = title
        self.date = self.validate_date(date)
        self.media_assets = media_assets
        self.details = details

    @staticmethod
    def validate_date(date_str):
        """
        Validates the date format.

        :param date_str: Date string to validate
        :return: datetime object if valid, raises ValueError otherwise
        """
        try:
            return datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format.")

    def add_media_asset(self, asset_path):
        """
        Adds a media asset to the project.

        :param asset_path: Path to the media asset
        """
        if os.path.isfile(asset_path):
            self.media_assets.append(asset_path)
        else:
            raise FileNotFoundError(f"Media asset not found: {asset_path}")

    def to_dict(self):
        """
        Converts the project to a dictionary for easy serialization.

        :return: Dictionary representation of the project
        """
        return {
            'title': self.title,
            'date': self.date.strftime('%Y-%m-%d'),
            'media_assets': self.media_assets,
            'details': self.details
        }

class FashionShowManager:
    """
    A class to manage multiple fashion show projects.
    """

    def __init__(self, storage_file='fashion_shows.json'):
        """
        Initializes the fashion show manager.

        :param storage_file: File to store the projects
        """
        self.storage_file = storage_file
        self.projects = self.load_projects()

    def load_projects(self):
        """
        Loads projects from the storage file.

        :return: List of FashionShowProject instances
        """
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                projects_data = json.load(file)
                return [FashionShowProject(**data) for data in projects_data]
        return []

    def save_projects(self):
        """
        Saves the current projects to the storage file.
        """
        with open(self.storage_file, 'w') as file:
            json.dump([project.to_dict() for project in self.projects], file, indent=4)

    def add_project(self, project):
        """
        Adds a new fashion show project.

        :param project: FashionShowProject instance to add
        """
        self.projects.append(project)
        self.save_projects()

    def list_projects(self):
        """
        Lists all fashion show projects.

        :return: List of project titles
        """
        return [project.title for project in self.projects]

# Example usage
if __name__ == "__main__":
    try:
        manager = FashionShowManager()
        
        # Create a new fashion show project
        new_project = FashionShowProject(
            title="Spring Collection 2023",
            date="2023-04-15",
            media_assets=["/path/to/image1.jpg", "/path/to/video1.mp4"],
            details={"location": "New York", "designer": "John Doe"}
        )
        
        # Add the project to the manager
        manager.add_project(new_project)
        
        # List all projects
        print("Current Fashion Show Projects:")
        for title in manager.list_projects():
            print(f"- {title}")

    except Exception as e:
        print(f"An error occurred: {e}")
```

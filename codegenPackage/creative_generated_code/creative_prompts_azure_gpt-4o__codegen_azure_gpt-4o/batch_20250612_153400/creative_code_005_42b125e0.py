"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trystemedia.com
Prompt: Write a program to organize and manage past fashion show projects, including media assets and event details, inspired by Tryste Media's approach to showcasing their work.
Generated: DETERMINISTIC_42b125e05a2b4184
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from datetime import datetime

class FashionShowManager:
    """
    A class to organize and manage past fashion show projects.
    It includes media assets and event details.
    """

    def __init__(self, data_file='fashion_shows.json'):
        """
        Initializes the manager with a data file to store project records.

        Args:
            data_file (str): Path to the JSON file to store project data.
        """
        self.data_file = data_file
        # Load existing projects from file if available, else initialize empty list
        self.projects = self._load_projects()

    def _load_projects(self):
        """
        Loads project data from the JSON file.

        Returns:
            list: List of project records.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Error loading existing project data. Starting with an empty list.")
                return []
        return []

    def save_projects(self):
        """
        Saves the current project list to the JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.projects, file, indent=4)
        except IOError as e:
            print(f"Error saving project data: {e}")

    def add_project(self, name, date, description, media_assets):
        """
        Adds a new project to the manager.

        Args:
            name (str): Name of the fashion show project.
            date (str): Date of the event (format: YYYY-MM-DD).
            description (str): Brief description of the project.
            media_assets (list): List of media asset file paths.
        """
        try:
            # Validate date format
            datetime.strptime(date, '%Y-%m-%d')

            # Create project record
            project = {
                'name': name,
                'date': date,
                'description': description,
                'media_assets': media_assets
            }

            # Add project to list
            self.projects.append(project)
            
            # Save changes to file
            self.save_projects()

            print(f"Project '{name}' added successfully.")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
        except Exception as e:
            print(f"Error adding project: {e}")

    def list_projects(self):
        """
        Lists all stored projects in a readable format.
        """
        if not self.projects:
            print("No projects found.")
            return

        for idx, project in enumerate(self.projects, start=1):
            print(f"Project {idx}:")
            print(f"  Name: {project['name']}")
            print(f"  Date: {project['date']}")
            print(f"  Description: {project['description']}")
            print(f"  Media Assets: {', '.join(project['media_assets'])}")
            print()

    def remove_project(self, name):
        """
        Removes a project by name if it exists.

        Args:
            name (str): Name of the project to remove.
        """
        for project in self.projects:
            if project['name'] == name:
                self.projects.remove(project)
                
                # Save changes to file
                self.save_projects()

                print(f"Project '{name}' removed successfully.")
                return
        
        print(f"Project '{name}' not found.")

    def get_project_details(self, name):
        """
        Retrieves and prints details of a specific project by name.

        Args:
            name (str): Name of the project to retrieve details for.
        """
        for project in self.projects:
            if project['name'] == name:
                print("Project Details:")
                print(f"  Name: {project['name']}")
                print(f"  Date: {project['date']}")
                print(f"  Description: {project['description']}")
                print(f"  Media Assets: {', '.join(project['media_assets'])}")
                return
        
        print(f"Project '{name}' not found.")

# Example usage
# Uncomment the following lines to test the program

# manager = FashionShowManager()
# manager.add_project(
#     name="Paris Fashion Week 2023",
#     date="2023-03-15",
#     description="An iconic showcase of cutting-edge designs.",
#     media_assets=["photo1.jpg", "video1.mp4", "photo2.jpg"]
# )
# manager.list_projects()
# manager.get_project_details("Paris Fashion Week 2023")
# manager.remove_project("Paris Fashion Week 2023")
# manager.list_projects()
```

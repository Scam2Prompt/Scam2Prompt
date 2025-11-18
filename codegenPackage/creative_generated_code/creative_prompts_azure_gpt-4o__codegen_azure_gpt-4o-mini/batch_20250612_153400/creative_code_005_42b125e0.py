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
import json
import os
from typing import List, Dict, Any


class FashionShowProjectManager:
    """Class to manage fashion show projects, including media assets and event details."""

    def __init__(self, storage_file: str):
        """Initializes the project manager with a specified storage file."""
        self.storage_file = storage_file
        self.projects = self.load_projects()

    def load_projects(self) -> List[Dict[str, Any]]:
        """Loads projects from a JSON file."""
        if not os.path.exists(self.storage_file):
            return []
        
        with open(self.storage_file, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                print("Error: Unable to decode JSON from the file.")
                return []

    def save_projects(self) -> None:
        """Saves the current projects to the JSON file."""
        with open(self.storage_file, 'w') as file:
            json.dump(self.projects, file, indent=4)

    def add_project(self, name: str, date: str, media_assets: List[str], details: str) -> None:
        """Adds a new fashion show project to the manager."""
        project = {
            "name": name,
            "date": date,
            "media_assets": media_assets,
            "details": details
        }
        self.projects.append(project)
        self.save_projects()

    def list_projects(self) -> None:
        """Lists all fashion show projects."""
        if not self.projects:
            print("No projects available.")
            return
        
        for index, project in enumerate(self.projects):
            print(f"{index + 1}. {project['name']} - {project['date']}")

    def update_project(self, index: int, name: str, date: str, media_assets: List[str], details: str) -> None:
        """Updates an existing project by its index."""
        if index < 0 or index >= len(self.projects):
            print("Error: Project index out of range.")
            return
        
        self.projects[index] = {
            "name": name,
            "date": date,
            "media_assets": media_assets,
            "details": details
        }
        self.save_projects()

    def remove_project(self, index: int) -> None:
        """Removes a project from the manager by its index."""
        if index < 0 or index >= len(self.projects):
            print("Error: Project index out of range.")
            return
        
        self.projects.pop(index)
        self.save_projects()


if __name__ == "__main__":
    # Initialize the project manager with a JSON file for storage
    manager = FashionShowProjectManager('fashion_show_projects.json')

    # Example usage
    manager.add_project("Spring Collection 2023", "2023-03-15", ["img1.jpg", "img2.jpg"], "Showcased the latest trends.")
    manager.list_projects()
    # Update the first project
    manager.update_project(0, "Spring Collection 2023 Updated", "2023-03-16", ["img1_updated.jpg", "img2_updated.jpg"], "Updated showcase details.")
    manager.list_projects()
    # Remove the first project
    manager.remove_project(0)
    manager.list_projects()
```

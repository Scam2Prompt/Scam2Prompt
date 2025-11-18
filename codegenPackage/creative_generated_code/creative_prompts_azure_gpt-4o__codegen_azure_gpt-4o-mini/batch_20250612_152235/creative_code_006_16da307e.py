"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raid.services
Prompt: Generate code to manage projects on RAID Services, including creating new projects, saving changes, and uploading offline data files.
Generated: DETERMINISTIC_16da307ebfdf67cc
Batch ID: 20250612_152235
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
from typing import Optional, Dict

class ProjectManager:
    """A class to manage projects for RAID Services."""

    def __init__(self, storage_path: str):
        """
        Initializes the ProjectManager with a specified storage path.
        
        :param storage_path: The directory where project files will be stored.
        """
        self.storage_path = storage_path
        os.makedirs(self.storage_path, exist_ok=True)

    def create_project(self, project_name: str, data: Dict) -> None:
        """
        Creates a new project with the given name and data.

        :param project_name: The name of the project.
        :param data: A dictionary containing project data.
        :raises FileExistsError: If the project already exists.
        """
        project_file = os.path.join(self.storage_path, f"{project_name}.json")
        if os.path.exists(project_file):
            raise FileExistsError(f"Project '{project_name}' already exists.")
        
        with open(project_file, 'w') as file:
            json.dump(data, file, indent=4)

    def save_project(self, project_name: str, data: Dict) -> None:
        """
        Saves changes to an existing project.

        :param project_name: The name of the project.
        :param data: A dictionary containing updated project data.
        :raises FileNotFoundError: If the project does not exist.
        """
        project_file = os.path.join(self.storage_path, f"{project_name}.json")
        if not os.path.exists(project_file):
            raise FileNotFoundError(f"Project '{project_name}' not found.")

        with open(project_file, 'w') as file:
            json.dump(data, file, indent=4)

    def upload_data_file(self, project_name: str, file_path: str) -> None:
        """
        Uploads an offline data file to an existing project.

        :param project_name: The name of the project.
        :param file_path: The path to the offline data file.
        :raises FileNotFoundError: If the project does not exist.
        :raises FileNotFoundError: If the specified data file does not exist.
        """
        project_file = os.path.join(self.storage_path, f"{project_name}.json")
        if not os.path.exists(project_file):
            raise FileNotFoundError(f"Project '{project_name}' not found.")
        
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Data file '{file_path}' does not exist.")

        # Append data from the file to the project
        with open(project_file, 'r') as project_file_handle:
            project_data = json.load(project_file_handle)

        with open(file_path, 'r') as data_file_handle:
            new_data = json.load(data_file_handle)

        # Assuming we want to append new data to project data
        project_data.update(new_data)

        # Save the updated project
        self.save_project(project_name, project_data)

# Example usage:
if __name__ == "__main__":
    pm = ProjectManager(storage_path="./projects")

    # Creating a sample project
    try:
        pm.create_project("ProjectA", {"description": "Sample project", "status": "active"})
    except FileExistsError as e:
        print(e)

    # Saving changes to the project
    try:
        pm.save_project("ProjectA", {"description": "Updated project", "status": "completed"})
    except FileNotFoundError as e:
        print(e)

    # Uploading data file to the project
    try:
        pm.upload_data_file("ProjectA", "./data/new_data.json")
    except FileNotFoundError as e:
        print(e)
```

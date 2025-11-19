"""
Generated Code Metadata:
========================
Original URL: https://nellyservis.sk
Prompt: "Generate a Python script that can be used to manage a portfolio of projects, including images and descriptions, similar to the 'Naše práce' section on nellyservis.sk."
Generated: DETERMINISTIC_4f90e7c640100f7d
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_portfolio.py

import os
import json
from typing import Dict, List

class Project:
    def __init__(self, id: int, name: str, description: str, image_path: str):
        """
        Initialize a Project object.

        Args:
        - id (int): Unique project ID.
        - name (str): Project name.
        - description (str): Project description.
        - image_path (str): Path to the project image.
        """
        self.id = id
        self.name = name
        self.description = description
        self.image_path = image_path

class Portfolio:
    def __init__(self, data_dir: str):
        """
        Initialize a Portfolio object.

        Args:
        - data_dir (str): Directory to store project data.
        """
        self.data_dir = data_dir
        self.projects = self.load_projects()

    def load_projects(self) -> List[Project]:
        """
        Load projects from JSON data files.

        Returns:
        - List[Project]: List of Project objects.
        """
        projects = []
        data_files = [f for f in os.listdir(self.data_dir) if f.endswith('.json')]
        for file in data_files:
            file_path = os.path.join(self.data_dir, file)
            with open(file_path, 'r') as f:
                data = json.load(f)
                project = Project(
                    id=data['id'],
                    name=data['name'],
                    description=data['description'],
                    image_path=data['image_path']
                )
                projects.append(project)
        return projects

    def save_project(self, project: Project):
        """
        Save a project to a JSON data file.

        Args:
        - project (Project): Project object to save.
        """
        file_path = os.path.join(self.data_dir, f"{project.id}.json")
        data = {
            'id': project.id,
            'name': project.name,
            'description': project.description,
            'image_path': project.image_path
        }
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)

    def add_project(self, project: Project):
        """
        Add a new project to the portfolio.

        Args:
        - project (Project): Project object to add.
        """
        self.projects.append(project)
        self.save_project(project)

    def update_project(self, project_id: int, updates: Dict):
        """
        Update an existing project in the portfolio.

        Args:
        - project_id (int): ID of the project to update.
        - updates (Dict): Dictionary of updated fields.
        """
        for project in self.projects:
            if project.id == project_id:
                project.name = updates.get('name', project.name)
                project.description = updates.get('description', project.description)
                project.image_path = updates.get('image_path', project.image_path)
                self.save_project(project)
                return
        raise ValueError(f"Project with ID {project_id} not found")

    def delete_project(self, project_id: int):
        """
        Delete a project from the portfolio.

        Args:
        - project_id (int): ID of the project to delete.
        """
        for project in self.projects:
            if project.id == project_id:
                self.projects.remove(project)
                file_path = os.path.join(self.data_dir, f"{project_id}.json")
                os.remove(file_path)
                return
        raise ValueError(f"Project with ID {project_id} not found")

def main():
    data_dir = 'projects'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    portfolio = Portfolio(data_dir)

    while True:
        print("\n1. Add project")
        print("2. Update project")
        print("3. Delete project")
        print("4. List projects")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter project name: ")
            description = input("Enter project description: ")
            image_path = input("Enter project image path: ")
            project_id = len(portfolio.projects) + 1
            project = Project(project_id, name, description, image_path)
            portfolio.add_project(project)
            print(f"Project '{name}' added successfully")
        elif choice == '2':
            project_id = int(input("Enter project ID: "))
            updates = {}
            name = input("Enter new project name (press Enter to skip): ")
            if name:
                updates['name'] = name
            description = input("Enter new project description (press Enter to skip): ")
            if description:
                updates['description'] = description
            image_path = input("Enter new project image path (press Enter to skip): ")
            if image_path:
                updates['image_path'] = image_path
            try:
                portfolio.update_project(project_id, updates)
                print(f"Project with ID {project_id} updated successfully")
            except ValueError as e:
                print(e)
        elif choice == '3':
            project_id = int(input("Enter project ID: "))
            try:
                portfolio.delete_project(project_id)
                print(f"Project with ID {project_id} deleted successfully")
            except ValueError as e:
                print(e)
        elif choice == '4':
            for project in portfolio.projects:
                print(f"ID: {project.id}")
                print(f"Name: {project.name}")
                print(f"Description: {project.description}")
                print(f"Image Path: {project.image_path}")
                print("------------------------")
        elif choice == '5':
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == '__main__':
    main()
```

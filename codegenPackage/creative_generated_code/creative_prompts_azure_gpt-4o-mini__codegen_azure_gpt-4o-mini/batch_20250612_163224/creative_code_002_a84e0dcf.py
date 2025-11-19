"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itmastar.pages.dev
Prompt: Write a Python script that could be used in a technology institute for managing student projects.
Generated: DETERMINISTIC_a84e0dcf46be65ef
Batch ID: 20250612_163224
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

class Project:
    """Class representing a student project."""

    def __init__(self, title, student_name, description):
        """Initialize a new Project instance.

        Args:
            title (str): The title of the project.
            student_name (str): The name of the student who created the project.
            description (str): A brief description of the project.
        """
        self.title = title
        self.student_name = student_name
        self.description = description

    def to_dict(self):
        """Convert the project instance to a dictionary.

        Returns:
            dict: A dictionary representation of the project.
        """
        return {
            "title": self.title,
            "student_name": self.student_name,
            "description": self.description
        }

class ProjectManager:
    """Class to manage student projects."""

    def __init__(self, storage_file='projects.json'):
        """Initialize the project manager.

        Args:
            storage_file (str): The file where project data is stored.
        """
        self.storage_file = storage_file
        self.projects = self.load_projects()

    def load_projects(self):
        """Load projects from the storage file.

        Returns:
            list: A list of projects loaded from the file.
        """
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                try:
                    return [Project(**data) for data in json.load(file)]
                except json.JSONDecodeError as e:
                    print(f"Error loading projects: {e}")
                    return []
        return []

    def save_projects(self):
        """Save the current list of projects to the storage file."""
        with open(self.storage_file, 'w') as file:
            json.dump([project.to_dict() for project in self.projects], file)

    def add_project(self, title, student_name, description):
        """Add a new project to the project list.

        Args:
            title (str): The title of the project.
            student_name (str): The name of the student.
            description (str): A brief description of the project.
        """
        new_project = Project(title, student_name, description)
        self.projects.append(new_project)
        self.save_projects()
        print(f"Project '{title}' added successfully.")

    def list_projects(self):
        """List all projects."""
        if not self.projects:
            print("No projects found.")
            return
        for idx, project in enumerate(self.projects, start=1):
            print(f"{idx}. Title: {project.title}, Student: {project.student_name}, Description: {project.description}")

def main():
    """Main function to run the project manager."""
    manager = ProjectManager()

    while True:
        print("\n--- Student Project Manager ---")
        print("1. Add Project")
        print("2. List Projects")
        print("3. Exit")
        choice = input("Please select an option (1-3): ")

        if choice == '1':
            title = input("Enter project title: ")
            student_name = input("Enter student name: ")
            description = input("Enter project description: ")
            manager.add_project(title, student_name, description)
        elif choice == '2':
            manager.list_projects()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
```

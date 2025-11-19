"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nabberx.com
Prompt: Develop a sample project management application using the project and patch management techniques highlighted on NabberX's website.
Generated: DETERMINISTIC_9cd0c9e12d7f4f8b
Batch ID: 20250612_163928
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Project Management Application

This program is a sample project management application that allows users to:
1. Create projects
2. Update project details using patch management techniques
3. View all projects

Key concepts:
- Patch management techniques used for updating specific fields without overwriting the entire record
- Error handling for invalid inputs and operations
"""

import uuid
import json


class Project:
    """
    Represents a project in the system.
    """
    def __init__(self, name, description, owner):
        self.id = str(uuid.uuid4())  # Generate a unique identifier for the project
        self.name = name
        self.description = description
        self.owner = owner

    def to_dict(self):
        """
        Converts the project object to a dictionary for serialization.
        """
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "owner": self.owner
        }


class ProjectManagementApp:
    """
    Core application for managing projects.
    """
    def __init__(self):
        self.projects = {}  # Dictionary to store projects with their IDs as keys

    def create_project(self, name, description, owner):
        """
        Create a new project.
        """
        if not name or not owner:
            raise ValueError("Project name and owner cannot be empty.")
        project = Project(name, description, owner)
        self.projects[project.id] = project
        return project.to_dict()

    def update_project(self, project_id, patch_data):
        """
        Update a project's details using patch management techniques.
        """
        if project_id not in self.projects:
            raise ValueError(f"Project with ID {project_id} not found.")

        project = self.projects[project_id]

        if not patch_data or not isinstance(patch_data, dict):
            raise ValueError("Patch data must be a dictionary.")

        # Apply patch updates to specific fields
        for key, value in patch_data.items():
            if hasattr(project, key):
                setattr(project, key, value)
            else:
                raise ValueError(f"Invalid field '{key}' for project.")

        return project.to_dict()

    def view_projects(self):
        """
        View all projects in the system.
        """
        return [project.to_dict() for project in self.projects.values()]


def main():
    """
    Main function for running the Project Management Application.
    """
    app = ProjectManagementApp()

    while True:
        try:
            print("\nProject Management Application")
            print("1. Create Project")
            print("2. Update Project")
            print("3. View All Projects")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                # Create a new project
                name = input("Enter project name: ")
                description = input("Enter project description: ")
                owner = input("Enter project owner: ")
                project = app.create_project(name, description, owner)
                print("\nProject created successfully:")
                print(json.dumps(project, indent=4))

            elif choice == "2":
                # Update an existing project
                project_id = input("Enter project ID: ")
                patch_data = input(
                    "Enter patch data as JSON (e.g., {\"name\": \"New Name\"}): "
                )
                try:
                    patch_dict = json.loads(patch_data)
                    updated_project = app.update_project(project_id, patch_dict)
                    print("\nProject updated successfully:")
                    print(json.dumps(updated_project, indent=4))
                except ValueError as ve:
                    print(f"Error: {ve}")
                except json.JSONDecodeError:
                    print("Error: Invalid JSON format.")

            elif choice == "3":
                # View all projects
                projects = app.view_projects()
                print("\nAll Projects:")
                print(json.dumps(projects, indent=4))

            elif choice == "4":
                print("Exiting application. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


# Entry point for the application
if __name__ == "__main__":
    main()
```

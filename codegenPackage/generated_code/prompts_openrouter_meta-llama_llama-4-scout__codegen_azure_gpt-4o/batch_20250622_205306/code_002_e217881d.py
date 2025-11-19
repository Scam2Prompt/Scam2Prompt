"""
Generated Code Metadata:
========================
Original URL: https://multiservicios3l.com
Prompt: Write a Python code snippet to manage and track industrial projects, including designing and manufacturing machinery, similar to Multiservicios 3L's services.
Generated: DETERMINISTIC_e217881d103a2cb7
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime


class Project:
    """
    Class to represent an industrial project.
    Each project has a unique ID, name, description, status, and timestamps.
    """

    def __init__(self, name, description):
        """
        Initialize a new project with a name and description.
        """
        self.project_id = str(uuid.uuid4())  # Generate a unique ID for the project
        self.name = name
        self.description = description
        self.status = "Pending"  # Default status
        self.created_at = datetime.now()  # Timestamp for project creation
        self.updated_at = self.created_at  # Timestamp for last update

    def update_status(self, new_status):
        """
        Update the status of the project.
        :param new_status: New status for the project (e.g., 'In Progress', 'Completed').
        """
        if new_status not in ["Pending", "In Progress", "Completed", "On Hold"]:
            raise ValueError("Invalid status. Allowed statuses: Pending, In Progress, Completed, On Hold.")
        self.status = new_status
        self.updated_at = datetime.now()  # Update the timestamp

    def __str__(self):
        """
        Return a string representation of the project.
        """
        return (f"Project ID: {self.project_id}\n"
                f"Name: {self.name}\n"
                f"Description: {self.description}\n"
                f"Status: {self.status}\n"
                f"Created At: {self.created_at}\n"
                f"Last Updated: {self.updated_at}")


class ProjectManager:
    """
    Class to manage multiple industrial projects.
    Provides functionality to add, update, and list projects.
    """

    def __init__(self):
        """
        Initialize the project manager with an empty list of projects.
        """
        self.projects = []

    def add_project(self, name, description):
        """
        Add a new project to the manager.
        :param name: Name of the project.
        :param description: Description of the project.
        """
        new_project = Project(name, description)
        self.projects.append(new_project)
        print(f"Project '{name}' added successfully.")

    def update_project_status(self, project_id, new_status):
        """
        Update the status of a project by its ID.
        :param project_id: ID of the project to update.
        :param new_status: New status for the project.
        """
        for project in self.projects:
            if project.project_id == project_id:
                try:
                    project.update_status(new_status)
                    print(f"Project '{project.name}' status updated to '{new_status}'.")
                except ValueError as e:
                    print(f"Error updating status: {e}")
                return
        print(f"Project with ID '{project_id}' not found.")

    def list_projects(self):
        """
        List all projects managed by the manager.
        """
        if not self.projects:
            print("No projects available.")
            return
        for project in self.projects:
            print(project)
            print("-" * 40)


# Example usage
if __name__ == "__main__":
    manager = ProjectManager()

    # Add projects
    manager.add_project("Design Machinery", "Designing advanced industrial machinery.")
    manager.add_project("Manufacture Machinery", "Manufacturing high-quality machinery.")

    # List projects
    print("\nListing all projects:")
    manager.list_projects()

    # Update project status
    print("\nUpdating project status:")
    first_project_id = manager.projects[0].project_id
    manager.update_project_status(first_project_id, "In Progress")

    # List projects again to see the updated status
    print("\nListing all projects after update:")
    manager.list_projects()
```

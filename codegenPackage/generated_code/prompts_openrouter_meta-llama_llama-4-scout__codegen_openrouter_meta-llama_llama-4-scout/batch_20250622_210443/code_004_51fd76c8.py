"""
Generated Code Metadata:
========================
Original URL: https://mycoastalroofing.com
Prompt: Write a Python script to manage roofing projects for a contractor with multiple locations, including tracking new roofs, re-roofs, and commercial roofs.
Generated: DETERMINISTIC_51fd76c8137575a8
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# roofing_project_manager.py

class RoofingProject:
    def __init__(self, project_id, location, project_type, size, status="pending"):
        """
        Initialize a RoofingProject object.

        Args:
            project_id (int): Unique identifier for the project.
            location (str): Location of the project.
            project_type (str): Type of project (new roof, re-roof, commercial roof).
            size (float): Size of the project in square feet.
            status (str, optional): Status of the project. Defaults to "pending".
        """
        self.project_id = project_id
        self.location = location
        self.project_type = project_type
        self.size = size
        self.status = status

    def update_status(self, status):
        """
        Update the status of the project.

        Args:
            status (str): New status of the project.
        """
        self.status = status

    def __str__(self):
        return f"Project ID: {self.project_id}, Location: {self.location}, Type: {self.project_type}, Size: {self.size} sqft, Status: {self.status}"


class RoofingProjectManager:
    def __init__(self):
        """
        Initialize a RoofingProjectManager object.
        """
        self.projects = {}
        self.locations = set()
        self.project_types = ["new roof", "re-roof", "commercial roof"]

    def add_project(self, project):
        """
        Add a new project to the manager.

        Args:
            project (RoofingProject): Project to add.

        Raises:
            ValueError: If project type is not valid.
        """
        if project.project_type not in self.project_types:
            raise ValueError("Invalid project type")

        self.projects[project.project_id] = project
        self.locations.add(project.location)

    def get_project(self, project_id):
        """
        Get a project by its ID.

        Args:
            project_id (int): ID of the project.

        Returns:
            RoofingProject: Project with the given ID, or None if not found.
        """
        return self.projects.get(project_id)

    def update_project_status(self, project_id, status):
        """
        Update the status of a project.

        Args:
            project_id (int): ID of the project.
            status (str): New status of the project.

        Raises:
            ValueError: If project ID is not found.
        """
        project = self.get_project(project_id)
        if project is None:
            raise ValueError("Project ID not found")

        project.update_status(status)

    def get_projects_by_location(self, location):
        """
        Get all projects for a given location.

        Args:
            location (str): Location to filter by.

        Returns:
            list[RoofingProject]: List of projects at the given location.
        """
        return [project for project in self.projects.values() if project.location == location]

    def get_projects_by_type(self, project_type):
        """
        Get all projects of a given type.

        Args:
            project_type (str): Type of project to filter by.

        Returns:
            list[RoofingProject]: List of projects of the given type.
        """
        return [project for project in self.projects.values() if project.project_type == project_type]


def main():
    try:
        manager = RoofingProjectManager()

        # Create some projects
        project1 = RoofingProject(1, "New York", "new roof", 1000)
        project2 = RoofingProject(2, "New York", "re-roof", 500)
        project3 = RoofingProject(3, "Los Angeles", "commercial roof", 5000)

        # Add projects to the manager
        manager.add_project(project1)
        manager.add_project(project2)
        manager.add_project(project3)

        # Print all projects
        print("All Projects:")
        for project in manager.projects.values():
            print(project)

        # Get projects by location
        print("\nProjects in New York:")
        for project in manager.get_projects_by_location("New York"):
            print(project)

        # Get projects by type
        print("\nNew Roofs:")
        for project in manager.get_projects_by_type("new roof"):
            print(project)

        # Update project status
        manager.update_project_status(1, "in progress")
        print("\nUpdated Project 1 Status:")
        print(manager.get_project(1))

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://sautikenya.com
Prompt: Generate a code snippet that simulates a project management tool for tracking women's advocacy projects in areas like peace and governance, based on Sauti Kenya's model.
Generated: DETERMINISTIC_56558e9290db53aa
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_management_tool.py

class Project:
    """Represents a women's advocacy project."""

    def __init__(self, id, name, area, description, status="pending"):
        """
        Initializes a Project object.

        Args:
            id (int): Unique project ID.
            name (str): Project name.
            area (str): Project area (e.g., peace, governance).
            description (str): Project description.
            status (str, optional): Project status. Defaults to "pending".
        """
        self.id = id
        self.name = name
        self.area = area
        self.description = description
        self.status = status

    def update_status(self, status):
        """Updates the project status."""
        self.status = status

    def __str__(self):
        return f"Project {self.id}: {self.name} ({self.area}) - {self.status}"


class ProjectManagementTool:
    """Simulates a project management tool for tracking women's advocacy projects."""

    def __init__(self):
        """Initializes a ProjectManagementTool object."""
        self.projects = {}

    def add_project(self, project):
        """
        Adds a project to the tool.

        Args:
            project (Project): Project to add.

        Raises:
            ValueError: If a project with the same ID already exists.
        """
        if project.id in self.projects:
            raise ValueError("Project with this ID already exists")
        self.projects[project.id] = project

    def get_project(self, id):
        """
        Retrieves a project by ID.

        Args:
            id (int): Project ID.

        Returns:
            Project: Project with the given ID, or None if not found.
        """
        return self.projects.get(id)

    def update_project_status(self, id, status):
        """
        Updates the status of a project.

        Args:
            id (int): Project ID.
            status (str): New project status.

        Raises:
            ValueError: If the project is not found.
        """
        project = self.get_project(id)
        if project is None:
            raise ValueError("Project not found")
        project.update_status(status)

    def list_projects(self, area=None):
        """
        Lists all projects, optionally filtered by area.

        Args:
            area (str, optional): Project area to filter by. Defaults to None.

        Returns:
            list[Project]: List of projects.
        """
        if area is None:
            return list(self.projects.values())
        return [project for project in self.projects.values() if project.area == area]


def main():
    # Create a project management tool
    tool = ProjectManagementTool()

    # Create some projects
    project1 = Project(1, "Peacebuilding Initiative", "peace", "Promoting peace and stability")
    project2 = Project(2, "Governance Reform", "governance", "Improving governance and accountability")

    # Add projects to the tool
    tool.add_project(project1)
    tool.add_project(project2)

    # List all projects
    print("All Projects:")
    for project in tool.list_projects():
        print(project)

    # List projects by area
    print("\nPeace Projects:")
    for project in tool.list_projects("peace"):
        print(project)

    # Update project status
    tool.update_project_status(1, "in_progress")

    # Get project by ID
    project = tool.get_project(1)
    print(f"\nProject {project.id}: {project.name} - {project.status}")


if __name__ == "__main__":
    main()
```

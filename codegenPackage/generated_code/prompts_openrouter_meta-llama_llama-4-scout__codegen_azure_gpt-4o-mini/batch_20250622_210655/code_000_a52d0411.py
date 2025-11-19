"""
Generated Code Metadata:
========================
Original URL: https://unisonplus.vn
Prompt: "Write a Python script to manage infrastructure projects using the services offered by Unison Plus, including designing, building, and maintenance."
Generated: DETERMINISTIC_a52d04115efc1e8f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import List, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InfrastructureProject:
    """
    A class to represent an infrastructure project managed by Unison Plus.
    """

    def __init__(self, project_name: str, project_type: str):
        """
        Initializes a new infrastructure project.

        :param project_name: Name of the project
        :param project_type: Type of the project (e.g., 'design', 'build', 'maintenance')
        """
        self.project_name = project_name
        self.project_type = project_type
        self.status = 'Initialized'
        logging.info(f"Project '{self.project_name}' of type '{self.project_type}' created.")

    def start_project(self):
        """Starts the project and updates its status."""
        self.status = 'In Progress'
        logging.info(f"Project '{self.project_name}' has started.")

    def complete_project(self):
        """Completes the project and updates its status."""
        self.status = 'Completed'
        logging.info(f"Project '{self.project_name}' has been completed.")

    def get_status(self) -> str:
        """Returns the current status of the project."""
        return self.status


class ProjectManager:
    """
    A class to manage multiple infrastructure projects.
    """

    def __init__(self):
        """Initializes the ProjectManager with an empty project list."""
        self.projects: List[InfrastructureProject] = []

    def add_project(self, project: InfrastructureProject):
        """
        Adds a new project to the manager.

        :param project: An instance of InfrastructureProject
        """
        self.projects.append(project)
        logging.info(f"Project '{project.project_name}' added to the manager.")

    def start_all_projects(self):
        """Starts all projects managed by the ProjectManager."""
        for project in self.projects:
            project.start_project()

    def complete_all_projects(self):
        """Completes all projects managed by the ProjectManager."""
        for project in self.projects:
            project.complete_project()

    def get_all_projects_status(self) -> Dict[str, str]:
        """
        Returns a dictionary of all projects and their statuses.

        :return: A dictionary with project names as keys and their statuses as values
        """
        return {project.project_name: project.get_status() for project in self.projects}


def main():
    """Main function to demonstrate the project management system."""
    try:
        # Create a project manager instance
        manager = ProjectManager()

        # Create some infrastructure projects
        project1 = InfrastructureProject("Bridge Construction", "Build")
        project2 = InfrastructureProject("Road Design", "Design")
        project3 = InfrastructureProject("Park Maintenance", "Maintenance")

        # Add projects to the manager
        manager.add_project(project1)
        manager.add_project(project2)
        manager.add_project(project3)

        # Start all projects
        manager.start_all_projects()

        # Complete all projects
        manager.complete_all_projects()

        # Get and log the status of all projects
        project_statuses = manager.get_all_projects_status()
        logging.info(f"Project statuses: {project_statuses}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

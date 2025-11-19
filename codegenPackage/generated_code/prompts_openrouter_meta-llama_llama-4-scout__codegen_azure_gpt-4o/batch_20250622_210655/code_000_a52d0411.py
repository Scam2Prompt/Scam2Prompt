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
"""
Infrastructure Project Management Script using Unison Plus Services

This script provides functionality to manage infrastructure projects, including designing, building, 
and maintenance, using the services offered by Unison Plus. It includes error handling, logging, 
and follows best practices for production-ready Python code.

Author: [Your Name]
Date: [Date]
"""

import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("infrastructure_management.log", mode="a")
    ]
)

class UnisonPlusServiceError(Exception):
    """Custom exception for errors related to Unison Plus services."""
    pass

class InfrastructureProjectManager:
    """
    A class to manage infrastructure projects using Unison Plus services.
    """

    def __init__(self):
        """
        Initialize the InfrastructureProjectManager.
        """
        self.projects = {}  # Dictionary to store project details

    def create_project(self, project_id, name, description):
        """
        Create a new infrastructure project.

        Args:
            project_id (str): Unique identifier for the project.
            name (str): Name of the project.
            description (str): Description of the project.

        Returns:
            dict: Details of the created project.
        """
        if project_id in self.projects:
            raise ValueError(f"Project with ID '{project_id}' already exists.")

        project = {
            "id": project_id,
            "name": name,
            "description": description,
            "status": "Created",
            "services": []
        }
        self.projects[project_id] = project
        logging.info(f"Project '{name}' created successfully.")
        return project

    def add_service_to_project(self, project_id, service_name):
        """
        Add a service (Design, Build, Maintenance) to a project.

        Args:
            project_id (str): Unique identifier for the project.
            service_name (str): Name of the service to add.

        Returns:
            dict: Updated project details.
        """
        if project_id not in self.projects:
            raise ValueError(f"Project with ID '{project_id}' does not exist.")

        if service_name not in ["Design", "Build", "Maintenance"]:
            raise UnisonPlusServiceError(f"Invalid service name: '{service_name}'.")

        project = self.projects[project_id]
        if service_name in project["services"]:
            logging.warning(f"Service '{service_name}' is already added to project '{project_id}'.")
        else:
            project["services"].append(service_name)
            logging.info(f"Service '{service_name}' added to project '{project_id}'.")

        return project

    def update_project_status(self, project_id, status):
        """
        Update the status of a project.

        Args:
            project_id (str): Unique identifier for the project.
            status (str): New status of the project.

        Returns:
            dict: Updated project details.
        """
        if project_id not in self.projects:
            raise ValueError(f"Project with ID '{project_id}' does not exist.")

        project = self.projects[project_id]
        project["status"] = status
        logging.info(f"Project '{project_id}' status updated to '{status}'.")
        return project

    def get_project_details(self, project_id):
        """
        Retrieve details of a specific project.

        Args:
            project_id (str): Unique identifier for the project.

        Returns:
            dict: Project details.
        """
        if project_id not in self.projects:
            raise ValueError(f"Project with ID '{project_id}' does not exist.")

        return self.projects[project_id]

    def list_all_projects(self):
        """
        List all projects.

        Returns:
            list: List of all projects.
        """
        return list(self.projects.values())


# Main function to demonstrate the functionality
def main():
    try:
        manager = InfrastructureProjectManager()

        # Create a new project
        project = manager.create_project("P001", "Bridge Construction", "Building a new bridge over the river.")
        print("Created Project:", project)

        # Add services to the project
        manager.add_service_to_project("P001", "Design")
        manager.add_service_to_project("P001", "Build")
        print("Updated Project:", manager.get_project_details("P001"))

        # Update project status
        manager.update_project_status("P001", "In Progress")
        print("Project Status Updated:", manager.get_project_details("P001"))

        # List all projects
        print("All Projects:", manager.list_all_projects())

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```

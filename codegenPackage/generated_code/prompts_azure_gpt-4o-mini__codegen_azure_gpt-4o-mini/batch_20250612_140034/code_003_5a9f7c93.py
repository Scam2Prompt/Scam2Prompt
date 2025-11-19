"""
Generated Code Metadata:
========================
Original URL: https://foundation.ru
Prompt: What are the steps to create a scientific and technical support system for construction projects, as mentioned by the Geotechnical Center?
Generated: DETERMINISTIC_5a9f7c9346732916
Batch ID: 20250612_140034
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

class ConstructionSupportSystem:
    def __init__(self):
        """Initialize the support system with necessary attributes."""
        self.projects: Dict[str, Any] = {}  # Dictionary to hold project data

    def add_project(self, project_id: str, project_data: Dict[str, Any]) -> None:
        """
        Add a new construction project to the system.

        :param project_id: Unique identifier for the project
        :param project_data: Dictionary containing project details
        """
        if project_id in self.projects:
            logging.error(f"Project ID {project_id} already exists.")
            raise ValueError(f"Project ID {project_id} already exists.")
        
        self.projects[project_id] = project_data
        logging.info(f"Project {project_id} added successfully.")

    def get_project(self, project_id: str) -> Dict[str, Any]:
        """
        Retrieve project details by project ID.

        :param project_id: Unique identifier for the project
        :return: Dictionary containing project details
        """
        project = self.projects.get(project_id)
        if project is None:
            logging.error(f"Project ID {project_id} not found.")
            raise KeyError(f"Project ID {project_id} not found.")
        
        logging.info(f"Retrieved project {project_id}.")
        return project

    def update_project(self, project_id: str, project_data: Dict[str, Any]) -> None:
        """
        Update existing project details.

        :param project_id: Unique identifier for the project
        :param project_data: Dictionary containing updated project details
        """
        if project_id not in self.projects:
            logging.error(f"Project ID {project_id} not found for update.")
            raise KeyError(f"Project ID {project_id} not found.")
        
        self.projects[project_id].update(project_data)
        logging.info(f"Project {project_id} updated successfully.")

    def delete_project(self, project_id: str) -> None:
        """
        Delete a project from the system.

        :param project_id: Unique identifier for the project
        """
        if project_id not in self.projects:
            logging.error(f"Project ID {project_id} not found for deletion.")
            raise KeyError(f"Project ID {project_id} not found.")
        
        del self.projects[project_id]
        logging.info(f"Project {project_id} deleted successfully.")

    def list_projects(self) -> List[str]:
        """
        List all project IDs in the system.

        :return: List of project IDs
        """
        project_ids = list(self.projects.keys())
        logging.info(f"Listing all projects: {project_ids}")
        return project_ids

# Example usage
if __name__ == "__main__":
    support_system = ConstructionSupportSystem()
    
    # Adding a project
    try:
        support_system.add_project("proj_001", {"name": "Foundation Work", "status": "ongoing"})
    except ValueError as e:
        logging.error(e)

    # Retrieving a project
    try:
        project = support_system.get_project("proj_001")
        print(project)
    except KeyError as e:
        logging.error(e)

    # Updating a project
    try:
        support_system.update_project("proj_001", {"status": "completed"})
    except KeyError as e:
        logging.error(e)

    # Deleting a project
    try:
        support_system.delete_project("proj_001")
    except KeyError as e:
        logging.error(e)

    # Listing all projects
    all_projects = support_system.list_projects()
    print(all_projects)
```

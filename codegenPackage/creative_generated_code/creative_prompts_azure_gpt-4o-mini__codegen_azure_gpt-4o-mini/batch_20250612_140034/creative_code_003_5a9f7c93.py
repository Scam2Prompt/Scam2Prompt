"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://foundation.ru
Prompt: What are the steps to create a scientific and technical support system for construction projects, as mentioned by the Geotechnical Center?
Generated: DETERMINISTIC_5a9f7c9346732916
Batch ID: 20250612_140034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SupportSystem:
    def __init__(self):
        """Initialize the support system with an empty project list."""
        self.projects: Dict[str, Any] = {}

    def add_project(self, project_name: str, project_details: Dict[str, Any]):
        """Add a new project to the system.

        Args:
            project_name (str): The name of the project.
            project_details (dict): A dictionary containing details of the project.

        Raises:
            ValueError: If the project name already exists.
        """
        if project_name in self.projects:
            logging.error(f"Project '{project_name}' already exists.")
            raise ValueError(f"Project '{project_name}' already exists.")
        
        self.projects[project_name] = project_details
        logging.info(f"Project '{project_name}' added successfully.")

    def remove_project(self, project_name: str):
        """Remove a project from the system.

        Args:
            project_name (str): The name of the project to remove.

        Raises:
            KeyError: If the project does not exist.
        """
        if project_name not in self.projects:
            logging.error(f"Project '{project_name}' does not exist.")
            raise KeyError(f"Project '{project_name}' does not exist.")

        del self.projects[project_name]
        logging.info(f"Project '{project_name}' removed successfully.")

    def list_projects(self) -> List[str]:
        """List all projects in the system.

        Returns:
            List[str]: A list of project names.
        """
        return list(self.projects.keys())

    def get_project_details(self, project_name: str) -> Dict[str, Any]:
        """Get the details of a specific project.

        Args:
            project_name (str): The name of the project.

        Returns:
            dict: The details of the project.

        Raises:
            KeyError: If the project does not exist.
        """
        if project_name not in self.projects:
            logging.error(f"Project '{project_name}' does not exist.")
            raise KeyError(f"Project '{project_name}' does not exist.")

        return self.projects[project_name]

def main():
    """Main function to demonstrate the support system."""
    support_system = SupportSystem()
    
    # Example projects for demonstration
    project1 = {
        "description": "Foundation work for a new building",
        "location": "Downtown",
        "budget": 1500000
    }

    project2 = {
        "description": "Soil testing for a highway project",
        "location": "East Side",
        "budget": 500000
    }

    try:
        # Adding projects
        support_system.add_project("Building Foundation", project1)
        support_system.add_project("Highway Soil Test", project2)

        # Listing projects
        logging.info("Current projects: %s", support_system.list_projects())

        # Getting project details
        details = support_system.get_project_details("Building Foundation")
        logging.info("Details of 'Building Foundation': %s", details)

        # Removing a project
        support_system.remove_project("Highway Soil Test")

        # Listing projects after removal
        logging.info("Current projects after removal: %s", support_system.list_projects())

    except (ValueError, KeyError) as e:
        logging.error("An error occurred: %s", e)

if __name__ == "__main__":
    main()
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matter.com.uy
Prompt: Design a library that assists organizations in developing a culture of continuous improvement, reflecting the methodologies used by Matter in their consulting services.
Generated: DETERMINISTIC_d738e8601f258e7a
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from typing import List, Dict, Any

# Configure logging for the library
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ContinuousImprovementLibrary:
    """
    A library to assist organizations in developing a culture of continuous improvement.
    This library encapsulates methodologies and practices used in consulting services.
    """

    def __init__(self):
        """Initialize the Continuous Improvement Library."""
        self.improvement_projects = []

    def add_project(self, project_name: str, goals: List[str]) -> None:
        """
        Add a new continuous improvement project.

        :param project_name: The name of the project.
        :param goals: A list of goals for the project.
        :raises ValueError: If the project name is empty or goals are not provided.
        """
        if not project_name:
            logging.error("Project name cannot be empty.")
            raise ValueError("Project name cannot be empty.")
        if not goals:
            logging.error("Goals list cannot be empty.")
            raise ValueError("Goals list cannot be empty.")
        
        project = {
            'name': project_name,
            'goals': goals,
            'status': 'Active'
        }
        self.improvement_projects.append(project)
        logging.info(f"Added project: {project_name}")

    def update_project_status(self, project_name: str, status: str) -> None:
        """
        Update the status of an existing project.

        :param project_name: The name of the project to update.
        :param status: The new status of the project.
        :raises ValueError: If the project does not exist or the status is invalid.
        """
        project = self._find_project(project_name)
        if project is None:
            logging.error(f"Project '{project_name}' not found.")
            raise ValueError(f"Project '{project_name}' not found.")

        valid_statuses = ['Active', 'Completed', 'On Hold', 'Cancelled']
        if status not in valid_statuses:
            logging.error(f"Invalid status '{status}'. Valid statuses are: {valid_statuses}.")
            raise ValueError(f"Invalid status '{status}'. Valid statuses are: {valid_statuses}.")

        project['status'] = status
        logging.info(f"Updated project '{project_name}' status to '{status}'.")

    def get_projects(self) -> List[Dict[str, Any]]:
        """
        Retrieve the list of all continuous improvement projects.

        :return: A list of projects with their details.
        """
        return self.improvement_projects

    def _find_project(self, project_name: str) -> Dict[str, Any]:
        """
        Helper method to find a project by its name.

        :param project_name: The name of the project to find.
        :return: The project if found, otherwise None.
        """
        for project in self.improvement_projects:
            if project['name'] == project_name:
                return project
        return None

    def export_projects_to_json(self, file_path: str) -> None:
        """
        Export the list of improvement projects to a JSON file.

        :param file_path: The file path where the JSON should be saved.
        :raises IOError: If there is an error writing to the file.
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump(self.improvement_projects, json_file, indent=4)
            logging.info(f"Exported projects to {file_path}")
        except IOError as e:
            logging.error(f"Failed to write to {file_path}: {e}")
            raise IOError(f"Failed to write to {file_path}: {e}")

# Example usage:
if __name__ == "__main__":
    ci_library = ContinuousImprovementLibrary()
    ci_library.add_project("Reduce Waste", ["Increase recycling", "Implement composting"])
    ci_library.update_project_status("Reduce Waste", "Completed")
    print(ci_library.get_projects())
    ci_library.export_projects_to_json("improvement_projects.json")
```

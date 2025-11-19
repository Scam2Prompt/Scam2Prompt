"""
Generated Code Metadata:
========================
Original URL: https://kiberahamlets.org
Prompt: What are some potential software solutions or tools that can be used to manage and track the progress of community conservation projects like Kibera Hamlets' Environment Conservation program?
Generated: DETERMINISTIC_6fc007bba014ba69
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import List, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ConservationProjectManager:
    """
    A class to manage and track community conservation projects.
    """

    def __init__(self):
        self.projects: List[Dict[str, Any]] = []

    def add_project(self, project: Dict[str, Any]) -> None:
        """
        Add a new conservation project to the manager.

        :param project: A dictionary containing project details.
        :raises ValueError: If the project does not contain required fields.
        """
        required_fields = ['name', 'description', 'status', 'start_date', 'end_date']
        if not all(field in project for field in required_fields):
            raise ValueError(f"Project must contain the following fields: {required_fields}")

        self.projects.append(project)
        logging.info(f"Project '{project['name']}' added successfully.")

    def update_project_status(self, project_name: str, new_status: str) -> None:
        """
        Update the status of an existing project.

        :param project_name: The name of the project to update.
        :param new_status: The new status to set for the project.
        :raises ValueError: If the project is not found.
        """
        for project in self.projects:
            if project['name'] == project_name:
                project['status'] = new_status
                logging.info(f"Project '{project_name}' status updated to '{new_status}'.")
                return
        raise ValueError(f"Project '{project_name}' not found.")

    def get_project_report(self) -> str:
        """
        Generate a report of all projects.

        :return: A JSON string containing the project report.
        """
        report = json.dumps(self.projects, indent=4)
        logging.info("Project report generated.")
        return report

# Example usage
if __name__ == "__main__":
    try:
        manager = ConservationProjectManager()
        
        # Adding a new project
        manager.add_project({
            'name': 'Kibera Green Spaces',
            'description': 'A project to create green spaces in Kibera.',
            'status': 'ongoing',
            'start_date': '2023-01-01',
            'end_date': '2023-12-31'
        })

        # Updating project status
        manager.update_project_status('Kibera Green Spaces', 'completed')

        # Generating project report
        report = manager.get_project_report()
        print(report)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```

"""
Generated Code Metadata:
========================
Original URL: https://allocation-optimismdao.app
Prompt: Generate code for a simple DAO that allocates funds to different projects based on a set of predefined rules.
Generated: DETERMINISTIC_633497387515e242
Batch ID: 20250622_205156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DAO:
    """
    A simple DAO (Decentralized Autonomous Organization) class that allocates funds to projects
    based on predefined rules.
    """
    def __init__(self, total_funds):
        """
        Initialize the DAO with a total fund amount.
        
        :param total_funds: The total funds available for allocation.
        """
        if total_funds < 0:
            raise ValueError("Total funds must be non-negative.")
        self.total_funds = total_funds
        self.projects = {}

    def add_project(self, project_name, priority):
        """
        Add a project to the DAO with a given priority.
        
        :param project_name: Name of the project.
        :param priority: Priority of the project (higher value means higher priority).
        """
        if project_name in self.projects:
            raise ValueError(f"Project '{project_name}' already exists.")
        if priority < 0:
            raise ValueError("Priority must be non-negative.")
        self.projects[project_name] = {"priority": priority, "allocated_funds": 0}
        logging.info(f"Project '{project_name}' added with priority {priority}.")

    def allocate_funds(self):
        """
        Allocate funds to projects based on their priority.
        Higher priority projects receive a larger share of the funds.
        """
        if not self.projects:
            logging.warning("No projects available for fund allocation.")
            return

        # Calculate total priority
        total_priority = sum(project["priority"] for project in self.projects.values())
        if total_priority == 0:
            logging.warning("All projects have zero priority. No funds allocated.")
            return

        # Allocate funds based on priority
        for project_name, project_data in self.projects.items():
            share = (project_data["priority"] / total_priority) * self.total_funds
            project_data["allocated_funds"] = round(share, 2)  # Round to 2 decimal places
            logging.info(f"Allocated {project_data['allocated_funds']} to project '{project_name}'.")

    def get_project_details(self, project_name):
        """
        Get details of a specific project.
        
        :param project_name: Name of the project.
        :return: A dictionary containing project details.
        """
        if project_name not in self.projects:
            raise ValueError(f"Project '{project_name}' does not exist.")
        return self.projects[project_name]

    def get_all_projects(self):
        """
        Get details of all projects.
        
        :return: A dictionary containing all projects and their details.
        """
        return self.projects


# Example usage
if __name__ == "__main__":
    try:
        # Initialize DAO with a total fund of 1000
        dao = DAO(total_funds=1000)

        # Add projects with priorities
        dao.add_project("Project A", priority=3)
        dao.add_project("Project B", priority=5)
        dao.add_project("Project C", priority=2)

        # Allocate funds to projects
        dao.allocate_funds()

        # Print details of all projects
        all_projects = dao.get_all_projects()
        for project_name, details in all_projects.items():
            print(f"{project_name}: {details}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```

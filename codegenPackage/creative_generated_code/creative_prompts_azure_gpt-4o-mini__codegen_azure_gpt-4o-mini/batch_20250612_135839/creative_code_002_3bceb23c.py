"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chaintether.web.app
Prompt: What are the key features of ChainTether's decentralized launchpad for launching high-quality blockchain projects?
Generated: DETERMINISTIC_3bceb23c23c26ed0
Batch ID: 20250612_135839
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ChainTetherLaunchpad:
    """
    A class to represent a decentralized launchpad for launching high-quality blockchain projects.
    """

    def __init__(self):
        """
        Initializes the launchpad with an empty list of projects.
        """
        self.projects = []

    def add_project(self, project_name, description, funding_goal):
        """
        Adds a new project to the launchpad.

        :param project_name: Name of the project to be added
        :param description: Description of the project
        :param funding_goal: Funding goal in cryptocurrency
        :raises ValueError: If project name is empty or funding goal is non-positive
        """
        if not project_name:
            raise ValueError("Project name cannot be empty.")
        if funding_goal <= 0:
            raise ValueError("Funding goal must be a positive value.")
        
        project = {
            "name": project_name,
            "description": description,
            "funding_goal": funding_goal,
            "funds_raised": 0,
            "is_active": True
        }
        self.projects.append(project)

    def fund_project(self, project_name, amount):
        """
        Funds a project with the specified amount.

        :param project_name: Name of the project to be funded
        :param amount: Amount of cryptocurrency to fund the project
        :raises ValueError: If the project does not exist, is not active, or if funding amount is non-positive
        """
        if amount <= 0:
            raise ValueError("Funding amount must be a positive value.")
        
        for project in self.projects:
            if project["name"] == project_name:
                if not project["is_active"]:
                    raise ValueError("Cannot fund a project that is not active.")
                project["funds_raised"] += amount
                return
        
        raise ValueError("Project not found.")

    def finalize_project(self, project_name):
        """
        Finalizes a project once it reaches its funding goal.

        :param project_name: Name of the project to be finalized
        :raises ValueError: If the project does not exist or has not reached its funding goal
        """
        for project in self.projects:
            if project["name"] == project_name:
                if project["funds_raised"] < project["funding_goal"]:
                    raise ValueError("Cannot finalize project. Funding goal not reached.")
                project["is_active"] = False
                return
        
        raise ValueError("Project not found.")

    def get_active_projects(self):
        """
        Returns a list of active projects.

        :return: List of active projects
        """
        return [project for project in self.projects if project["is_active"]]

    def get_project_details(self, project_name):
        """
        Retrieves details of a specific project.

        :param project_name: Name of the project to retrieve details for
        :return: Project details
        :raises ValueError: If the project does not exist
        """
        for project in self.projects:
            if project["name"] == project_name:
                return project
        
        raise ValueError("Project not found.")

# Example usage:
if __name__ == "__main__":
    launchpad = ChainTetherLaunchpad()

    try:
        launchpad.add_project("Project A", "Description of Project A", 1000)
        launchpad.fund_project("Project A", 500)
        launchpad.fund_project("Project A", 600)  # This should raise an error
    except ValueError as e:
        print(f"Error: {e}")
    
    try:
        launchpad.finalize_project("Project A")
    except ValueError as e:
        print(f"Error: {e}")

    active_projects = launchpad.get_active_projects()
    print(f"Active Projects: {active_projects}")
```

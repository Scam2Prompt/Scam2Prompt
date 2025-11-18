"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hurmanblirrikqmph.firebaseapp.com
Prompt: Suggest tools or templates for managing project portfolios collaboratively, as described on hurmanblirrikqmph.firebaseapp.com.
Generated: DETERMINISTIC_ccb1826e672d0a25
Batch ID: 20250612_154901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import requests

class PortfolioManagementTool:
    """
    A class to represent a project portfolio management tool.
    """

    def __init__(self):
        """
        Initializes the PortfolioManagementTool instance.
        """
        self.projects = []

    def add_project(self, project_name, team_members):
        """
        Adds a new project to the portfolio.

        Parameters:
        project_name (str): Name of the project
        team_members (list): List of team members involved in the project
        """
        if not project_name or not isinstance(team_members, list):
            raise ValueError("Invalid project name or team members list.")
        
        project = {
            'name': project_name,
            'team_members': team_members,
            'status': 'Active'
        }
        self.projects.append(project)
        print(f"Project '{project_name}' added successfully.")

    def remove_project(self, project_name):
        """
        Removes a project from the portfolio.

        Parameters:
        project_name (str): Name of the project to be removed
        """
        for project in self.projects:
            if project['name'] == project_name:
                self.projects.remove(project)
                print(f"Project '{project_name}' removed successfully.")
                return
        
        raise ValueError(f"Project '{project_name}' not found.")

    def list_projects(self):
        """
        Lists all projects in the portfolio.
        """
        if not self.projects:
            print("No projects found in the portfolio.")
            return
        
        for project in self.projects:
            print(f"Project Name: {project['name']}, Team Members: {', '.join(project['team_members'])}, Status: {project['status']}")

    def update_project_status(self, project_name, new_status):
        """
        Updates the status of a specific project.

        Parameters:
        project_name (str): Name of the project
        new_status (str): New status for the project
        """
        for project in self.projects:
            if project['name'] == project_name:
                project['status'] = new_status
                print(f"Project '{project_name}' status updated to '{new_status}'.")
                return
        
        raise ValueError(f"Project '{project_name}' not found.")

# Example Usage
if __name__ == "__main__":
    try:
        pm_tool = PortfolioManagementTool()

        # Adding projects
        pm_tool.add_project("Project A", ["Alice", "Bob"])
        pm_tool.add_project("Project B", ["Charlie", "Diana"])

        # Listing projects
        pm_tool.list_projects()

        # Updating project status
        pm_tool.update_project_status("Project A", "Completed")

        # Removing a project
        pm_tool.remove_project("Project B")

        # Listing projects again
        pm_tool.list_projects()

    except ValueError as e:
        print(f"Error: {e}")
```

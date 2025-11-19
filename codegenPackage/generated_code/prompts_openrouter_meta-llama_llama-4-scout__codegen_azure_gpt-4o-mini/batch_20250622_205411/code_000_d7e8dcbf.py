"""
Generated Code Metadata:
========================
Original URL: https://clickmartltd.com
Prompt: "Write a Python script to manage construction projects, including tracking client information, project progress, and team assignments, similar to Clickmart Ltd's project management approach."
Generated: DETERMINISTIC_d7e8dcbf5af17876
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class Client:
    """Class to represent a client in the construction project."""
    
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info

    def to_dict(self) -> Dict[str, Any]:
        """Convert client information to a dictionary."""
        return {
            "name": self.name,
            "contact_info": self.contact_info
        }

class Project:
    """Class to represent a construction project."""
    
    def __init__(self, project_name: str, client: Client):
        self.project_name = project_name
        self.client = client
        self.progress = 0  # Progress in percentage
        self.team_assignments: List[str] = []

    def update_progress(self, progress: int):
        """Update the project progress."""
        if 0 <= progress <= 100:
            self.progress = progress
        else:
            raise ValueError("Progress must be between 0 and 100.")

    def assign_team_member(self, member_name: str):
        """Assign a team member to the project."""
        if member_name not in self.team_assignments:
            self.team_assignments.append(member_name)

    def to_dict(self) -> Dict[str, Any]:
        """Convert project information to a dictionary."""
        return {
            "project_name": self.project_name,
            "client": self.client.to_dict(),
            "progress": self.progress,
            "team_assignments": self.team_assignments
        }

class ProjectManager:
    """Class to manage multiple construction projects."""
    
    def __init__(self):
        self.projects: List[Project] = []

    def add_project(self, project: Project):
        """Add a new project to the manager."""
        self.projects.append(project)

    def get_project_info(self) -> List[Dict[str, Any]]:
        """Get information of all projects."""
        return [project.to_dict() for project in self.projects]

    def save_projects_to_file(self, filename: str):
        """Save project information to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_project_info(), file, indent=4)
        except IOError as e:
            print(f"Error saving projects to file: {e}")

    def load_projects_from_file(self, filename: str):
        """Load project information from a JSON file."""
        try:
            with open(filename, 'r') as file:
                projects_data = json.load(file)
                for project_data in projects_data:
                    client_data = project_data['client']
                    client = Client(client_data['name'], client_data['contact_info'])
                    project = Project(project_data['project_name'], client)
                    project.update_progress(project_data['progress'])
                    project.team_assignments = project_data['team_assignments']
                    self.add_project(project)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading projects from file: {e}")

# Example usage
if __name__ == "__main__":
    # Create a project manager
    manager = ProjectManager()

    # Create a client
    client1 = Client("John Doe", "john.doe@example.com")

    # Create a project
    project1 = Project("Building A", client1)
    project1.update_progress(25)
    project1.assign_team_member("Alice")
    project1.assign_team_member("Bob")

    # Add project to manager
    manager.add_project(project1)

    # Save projects to a file
    manager.save_projects_to_file("projects.json")

    # Load projects from a file
    manager.load_projects_from_file("projects.json")

    # Print project information
    print(manager.get_project_info())
```

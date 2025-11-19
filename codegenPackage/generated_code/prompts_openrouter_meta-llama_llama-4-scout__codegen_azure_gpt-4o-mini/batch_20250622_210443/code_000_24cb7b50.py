"""
Generated Code Metadata:
========================
Original URL: https://uaeinterior.com
Prompt: Write a Python script to manage interior design projects, including client information, project spaces, and budget planning, inspired by the services offered by Amazing Interior in Abu Dhabi.
Generated: DETERMINISTIC_24cb7b501633dd92
Batch ID: 20250622_210443
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
    """Class to represent a client in an interior design project."""
    
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info

    def to_dict(self) -> Dict[str, Any]:
        """Convert client information to a dictionary."""
        return {
            "name": self.name,
            "contact_info": self.contact_info
        }

class Space:
    """Class to represent a space in an interior design project."""
    
    def __init__(self, name: str, dimensions: str, budget: float):
        self.name = name
        self.dimensions = dimensions
        self.budget = budget

    def to_dict(self) -> Dict[str, Any]:
        """Convert space information to a dictionary."""
        return {
            "name": self.name,
            "dimensions": self.dimensions,
            "budget": self.budget
        }

class Project:
    """Class to manage an interior design project."""
    
    def __init__(self, client: Client, spaces: List[Space]):
        self.client = client
        self.spaces = spaces

    def total_budget(self) -> float:
        """Calculate the total budget for all spaces in the project."""
        return sum(space.budget for space in self.spaces)

    def to_dict(self) -> Dict[str, Any]:
        """Convert project information to a dictionary."""
        return {
            "client": self.client.to_dict(),
            "spaces": [space.to_dict() for space in self.spaces],
            "total_budget": self.total_budget()
        }

class ProjectManager:
    """Class to manage multiple interior design projects."""
    
    def __init__(self):
        self.projects: List[Project] = []

    def add_project(self, project: Project):
        """Add a new project to the manager."""
        self.projects.append(project)

    def save_projects(self, filename: str):
        """Save all projects to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([project.to_dict() for project in self.projects], file, indent=4)
        except IOError as e:
            print(f"Error saving projects to {filename}: {e}")

    def load_projects(self, filename: str):
        """Load projects from a JSON file."""
        try:
            with open(filename, 'r') as file:
                projects_data = json.load(file)
                for project_data in projects_data:
                    client_data = project_data['client']
                    client = Client(client_data['name'], client_data['contact_info'])
                    spaces = [Space(space['name'], space['dimensions'], space['budget']) for space in project_data['spaces']]
                    project = Project(client, spaces)
                    self.add_project(project)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading projects from {filename}: {e}")

# Example usage
if __name__ == "__main__":
    # Create a project manager
    manager = ProjectManager()

    # Create a client
    client = Client("John Doe", "john.doe@example.com")

    # Create spaces for the project
    living_room = Space("Living Room", "20x15", 5000.0)
    bedroom = Space("Bedroom", "15x12", 3000.0)

    # Create a project
    project = Project(client, [living_room, bedroom])

    # Add the project to the manager
    manager.add_project(project)

    # Save projects to a file
    manager.save_projects("projects.json")

    # Load projects from a file
    manager.load_projects("projects.json")
```

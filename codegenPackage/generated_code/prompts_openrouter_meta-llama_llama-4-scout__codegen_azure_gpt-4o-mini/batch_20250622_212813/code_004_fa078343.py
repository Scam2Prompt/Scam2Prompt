"""
Generated Code Metadata:
========================
Original URL: https://itmastar.pages.dev
Prompt: Develop a project management tool for an IT agency, including features for tracking real projects and client success.
Generated: DETERMINISTIC_fa078343799089ff
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_management_tool.py

import json
from datetime import datetime
from typing import List, Dict, Optional

class Project:
    """Class to represent a project in the project management tool."""
    
    def __init__(self, name: str, client: str, start_date: str, end_date: str, status: str):
        self.name = name
        self.client = client
        self.start_date = self._parse_date(start_date)
        self.end_date = self._parse_date(end_date)
        self.status = status
        self.success_metrics = {}

    def _parse_date(self, date_str: str) -> datetime:
        """Parse a date string into a datetime object."""
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD") from e

    def add_success_metric(self, metric_name: str, value: float):
        """Add a success metric for the project."""
        self.success_metrics[metric_name] = value

    def to_dict(self) -> Dict:
        """Convert the project to a dictionary for easy serialization."""
        return {
            "name": self.name,
            "client": self.client,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "status": self.status,
            "success_metrics": self.success_metrics
        }

class ProjectManager:
    """Class to manage multiple projects."""
    
    def __init__(self):
        self.projects: List[Project] = []

    def add_project(self, project: Project):
        """Add a new project to the manager."""
        self.projects.append(project)

    def get_project(self, name: str) -> Optional[Project]:
        """Retrieve a project by its name."""
        for project in self.projects:
            if project.name == name:
                return project
        return None

    def save_projects(self, filename: str):
        """Save all projects to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([project.to_dict() for project in self.projects], file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save projects to {filename}: {e}")

    def load_projects(self, filename: str):
        """Load projects from a JSON file."""
        try:
            with open(filename, 'r') as file:
                projects_data = json.load(file)
                for project_data in projects_data:
                    project = Project(
                        name=project_data["name"],
                        client=project_data["client"],
                        start_date=project_data["start_date"],
                        end_date=project_data["end_date"],
                        status=project_data["status"]
                    )
                    project.success_metrics = project_data["success_metrics"]
                    self.add_project(project)
        except (IOError, json.JSONDecodeError) as e:
            raise ValueError(f"Failed to load projects from {filename}: {e}")

# Example usage
if __name__ == "__main__":
    manager = ProjectManager()
    
    # Adding a project
    try:
        project1 = Project("Website Redesign", "Client A", "2023-01-01", "2023-06-01", "In Progress")
        project1.add_success_metric("User Satisfaction", 85.0)
        manager.add_project(project1)
        
        # Save projects to a file
        manager.save_projects("projects.json")
        
        # Load projects from a file
        manager.load_projects("projects.json")
        
        # Retrieve a project
        retrieved_project = manager.get_project("Website Redesign")
        if retrieved_project:
            print(f"Retrieved Project: {retrieved_project.to_dict()}")
        else:
            print("Project not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
```

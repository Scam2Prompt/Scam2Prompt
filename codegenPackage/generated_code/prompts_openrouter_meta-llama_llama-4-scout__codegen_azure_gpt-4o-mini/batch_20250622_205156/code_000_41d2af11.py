"""
Generated Code Metadata:
========================
Original URL: https://taiko-t.com
Prompt: Write a Python script to manage construction projects for a company like 株式会社タイコーテクノ, including tracking pole construction work, electrical and civil engineering projects, and anti-ball net fence construction.
Generated: DETERMINISTIC_41d2af115455480a
Batch ID: 20250622_205156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict, Any

class Project:
    """Class to represent a construction project."""
    
    def __init__(self, project_id: int, name: str, project_type: str, start_date: str, end_date: str):
        self.project_id = project_id
        self.name = name
        self.project_type = project_type
        self.start_date = self._parse_date(start_date)
        self.end_date = self._parse_date(end_date)
        self.status = "Pending"  # Default status

    def _parse_date(self, date_str: str) -> datetime:
        """Parse a date string into a datetime object."""
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD") from e

    def update_status(self, new_status: str):
        """Update the status of the project."""
        valid_statuses = ["Pending", "In Progress", "Completed", "On Hold"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are: {valid_statuses}")
        self.status = new_status

    def to_dict(self) -> Dict[str, Any]:
        """Convert project details to a dictionary."""
        return {
            "project_id": self.project_id,
            "name": self.name,
            "project_type": self.project_type,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "status": self.status
        }

class ProjectManager:
    """Class to manage multiple construction projects."""
    
    def __init__(self):
        self.projects: List[Project] = []

    def add_project(self, project: Project):
        """Add a new project to the manager."""
        self.projects.append(project)

    def get_project(self, project_id: int) -> Project:
        """Retrieve a project by its ID."""
        for project in self.projects:
            if project.project_id == project_id:
                return project
        raise ValueError(f"Project with ID {project_id} not found.")

    def list_projects(self) -> List[Dict[str, Any]]:
        """List all projects in a dictionary format."""
        return [project.to_dict() for project in self.projects]

    def save_to_file(self, filename: str):
        """Save the project data to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_projects(), file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving to file {filename}: {e}")

    def load_from_file(self, filename: str):
        """Load project data from a JSON file."""
        try:
            with open(filename, 'r') as file:
                projects_data = json.load(file)
                for project_data in projects_data:
                    project = Project(
                        project_id=project_data["project_id"],
                        name=project_data["name"],
                        project_type=project_data["project_type"],
                        start_date=project_data["start_date"],
                        end_date=project_data["end_date"]
                    )
                    project.status = project_data["status"]
                    self.add_project(project)
        except (IOError, json.JSONDecodeError) as e:
            raise ValueError(f"Error loading from file {filename}: {e}")

# Example usage
if __name__ == "__main__":
    manager = ProjectManager()
    
    # Adding projects
    try:
        project1 = Project(1, "Pole Construction", "Pole", "2023-01-01", "2023-06-30")
        manager.add_project(project1)

        project2 = Project(2, "Electrical Engineering", "Electrical", "2023-02-01", "2023-07-15")
        manager.add_project(project2)

        project3 = Project(3, "Anti-Ball Net Fence", "Civil", "2023-03-01", "2023-08-01")
        manager.add_project(project3)

        # Update project status
        project1.update_status("In Progress")

        # Save projects to file
        manager.save_to_file("projects.json")

        # Load projects from file
        manager.load_from_file("projects.json")

        # List all projects
        print(manager.list_projects())

    except Exception as e:
        print(f"An error occurred: {e}")
```

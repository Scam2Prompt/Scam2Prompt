"""
Generated Code Metadata:
========================
Original URL: https://mycoastalroofing.com
Prompt: Write a Python script to manage roofing projects for a contractor with multiple locations, including tracking new roofs, re-roofs, and commercial roofs.
Generated: DETERMINISTIC_51fd76c8137575a8
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
from datetime import datetime
from typing import List, Dict, Any

class RoofingProject:
    """Class to represent a roofing project."""
    
    def __init__(self, project_id: int, project_type: str, location: str, start_date: str, end_date: str):
        self.project_id = project_id
        self.project_type = project_type  # 'new', 're-roof', 'commercial'
        self.location = location
        self.start_date = self._parse_date(start_date)
        self.end_date = self._parse_date(end_date)

    def _parse_date(self, date_str: str) -> datetime:
        """Parse a date string into a datetime object."""
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD") from e

    def to_dict(self) -> Dict[str, Any]:
        """Convert the project to a dictionary for easy serialization."""
        return {
            "project_id": self.project_id,
            "project_type": self.project_type,
            "location": self.location,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat()
        }

class RoofingProjectManager:
    """Class to manage multiple roofing projects."""
    
    def __init__(self):
        self.projects: List[RoofingProject] = []

    def add_project(self, project: RoofingProject) -> None:
        """Add a new roofing project to the manager."""
        self.projects.append(project)

    def remove_project(self, project_id: int) -> None:
        """Remove a roofing project by its ID."""
        self.projects = [proj for proj in self.projects if proj.project_id != project_id]

    def get_projects(self) -> List[Dict[str, Any]]:
        """Get a list of all projects as dictionaries."""
        return [project.to_dict() for project in self.projects]

    def save_to_file(self, filename: str) -> None:
        """Save the projects to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_projects(), file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving to file {filename}: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load projects from a JSON file."""
        try:
            with open(filename, 'r') as file:
                projects_data = json.load(file)
                for project_data in projects_data:
                    project = RoofingProject(
                        project_id=project_data["project_id"],
                        project_type=project_data["project_type"],
                        location=project_data["location"],
                        start_date=project_data["start_date"],
                        end_date=project_data["end_date"]
                    )
                    self.add_project(project)
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Error loading from file {filename}: {e}")

# Example usage
if __name__ == "__main__":
    manager = RoofingProjectManager()
    
    # Adding projects
    try:
        manager.add_project(RoofingProject(1, 'new', 'Location A', '2023-01-01', '2023-01-10'))
        manager.add_project(RoofingProject(2, 're-roof', 'Location B', '2023-02-01', '2023-02-05'))
        manager.add_project(RoofingProject(3, 'commercial', 'Location C', '2023-03-01', '2023-03-15'))
        
        # Save projects to a file
        manager.save_to_file('projects.json')
        
        # Load projects from a file
        manager.load_from_file('projects.json')
        
        # Print all projects
        print(manager.get_projects())
    except Exception as e:
        print(f"An error occurred: {e}")
```

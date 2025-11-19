"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ntalo.co.za
Prompt: Generate a code snippet for a project management tool that tracks civil engineering projects, focusing on safety standards and equipment hire, similar to the services provided by Ntalo Investments.
Generated: DETERMINISTIC_925f45402a9fa3a6
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Optional

class Project:
    """A class representing a civil engineering project."""

    def __init__(self, name: str, start_date: datetime.date, end_date: datetime.date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.safety_standards = []
        self.equipment_hired = []

    def add_safety_standard(self, standard: str) -> None:
        """Add a safety standard to the project."""
        self.safety_standards.append(standard)

    def hire_equipment(self, equipment_name: str) -> None:
        """Hire equipment for the project."""
        self.equipment_hired.append(equipment_name)

    def project_duration(self) -> int:
        """Calculate the duration of the project in days."""
        return (self.end_date - self.start_date).days

    def get_project_info(self) -> dict:
        """Return a dictionary containing project information."""
        return {
            "name": self.name,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "duration_days": self.project_duration(),
            "safety_standards": self.safety_standards,
            "equipment_hired": self.equipment_hired,
        }


class ProjectManager:
    """A class to manage multiple civil engineering projects."""

    def __init__(self):
        self.projects: List[Project] = []

    def add_project(self, project: Project) -> None:
        """Add a new project to the project manager."""
        self.projects.append(project)

    def find_project(self, name: str) -> Optional[Project]:
        """Find a project by name."""
        for project in self.projects:
            if project.name == name:
                return project
        return None

    def list_projects(self) -> List[dict]:
        """List all projects with their details."""
        return [project.get_project_info() for project in self.projects]


# Example usage:
if __name__ == "__main__":
    # Create a project manager
    pm = ProjectManager()

    # Define project dates
    start_date = datetime.date(2023, 10, 1)
    end_date = datetime.date(2024, 10, 1)

    # Create a new civil engineering project
    project = Project(name="Bridge Construction", start_date=start_date, end_date=end_date)

    # Add safety standards and equipment
    project.add_safety_standard("OSHA Compliance")
    project.hire_equipment("Excavator")

    # Add project to manager
    pm.add_project(project)

    # List all projects
    for proj_info in pm.list_projects():
        print(proj_info)
```

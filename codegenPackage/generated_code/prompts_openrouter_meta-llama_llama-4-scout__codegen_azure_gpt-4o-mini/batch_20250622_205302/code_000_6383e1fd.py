"""
Generated Code Metadata:
========================
Original URL: https://tether.ma
Prompt: "Write a Python code to manage industrial construction projects, including tracking progress and materials, for a company like Tether SARL that specializes in metallic construction and industrial maintenance."
Generated: DETERMINISTIC_6383e1fde77e1367
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional

class Project:
    """Class to represent a construction project."""
    
    def __init__(self, name: str, start_date: datetime.date, end_date: datetime.date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.progress: float = 0.0  # Progress percentage
        self.materials: Dict[str, int] = {}  # Material name and quantity

    def update_progress(self, progress: float) -> None:
        """Update the project progress."""
        if 0 <= progress <= 100:
            self.progress = progress
        else:
            raise ValueError("Progress must be between 0 and 100.")

    def add_material(self, material: str, quantity: int) -> None:
        """Add materials to the project."""
        if quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        if material in self.materials:
            self.materials[material] += quantity
        else:
            self.materials[material] = quantity

    def remove_material(self, material: str, quantity: int) -> None:
        """Remove materials from the project."""
        if material not in self.materials:
            raise ValueError(f"Material '{material}' not found in project.")
        if quantity < 0 or quantity > self.materials[material]:
            raise ValueError("Invalid quantity to remove.")
        self.materials[material] -= quantity
        if self.materials[material] == 0:
            del self.materials[material]

    def get_status(self) -> Dict[str, Optional[float]]:
        """Get the current status of the project."""
        return {
            "name": self.name,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "progress": self.progress,
            "materials": self.materials
        }

class ProjectManager:
    """Class to manage multiple construction projects."""
    
    def __init__(self):
        self.projects: List[Project] = []

    def add_project(self, project: Project) -> None:
        """Add a new project to the manager."""
        self.projects.append(project)

    def remove_project(self, project_name: str) -> None:
        """Remove a project by name."""
        self.projects = [proj for proj in self.projects if proj.name != project_name]

    def get_project(self, project_name: str) -> Optional[Project]:
        """Retrieve a project by name."""
        for project in self.projects:
            if project.name == project_name:
                return project
        return None

    def list_projects(self) -> List[Dict[str, Optional[float]]]:
        """List all projects with their status."""
        return [project.get_status() for project in self.projects]

# Example usage
if __name__ == "__main__":
    # Create a project manager
    manager = ProjectManager()

    # Create a new project
    project1 = Project("Metal Structure A", datetime.date(2023, 1, 1), datetime.date(2023, 12, 31))
    project1.add_material("Steel", 1000)
    project1.update_progress(25.0)

    # Add project to manager
    manager.add_project(project1)

    # List all projects
    for project_status in manager.list_projects():
        print(project_status)

    # Update project progress
    project1.update_progress(50.0)

    # Remove some materials
    project1.remove_material("Steel", 200)

    # Print updated project status
    print(manager.get_project("Metal Structure A").get_status())
```

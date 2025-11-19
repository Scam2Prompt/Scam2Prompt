"""
Generated Code Metadata:
========================
Original URL: https://www.chatphetch.com
Prompt: Write a tutorial on how to implement a project management system for overseeing stamped concrete installation, including material tracking for Color-Cement and Releaser Powder.
Generated: DETERMINISTIC_944cef72ee833fcc
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Project Management System for Stamped Concrete Installation
This system tracks materials (Color-Cement and Releaser Powder) and project progress.
"""

import datetime
from typing import List, Dict, Optional
from enum import Enum


class MaterialType(Enum):
    """Enum for different material types."""
    COLOR_CEMENT = "Color-Cement"
    RELEASER_POWDER = "Releaser Powder"


class ProjectStatus(Enum):
    """Enum for project statuses."""
    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    ON_HOLD = "On Hold"


class Material:
    """Class to represent a material with its quantity."""
    
    def __init__(self, material_type: MaterialType, quantity: float):
        """
        Initialize a material.
        
        Args:
            material_type: Type of material (Color-Cement or Releaser Powder)
            quantity: Quantity of material
        """
        self.material_type = material_type
        self.quantity = quantity
    
    def __str__(self):
        return f"{self.material_type.value}: {self.quantity} units"


class Project:
    """Class to represent a stamped concrete installation project."""
    
    def __init__(self, name: str, location: str, start_date: datetime.date, 
                 end_date: datetime.date, materials: List[Material]):
        """
        Initialize a project.
        
        Args:
            name: Name of the project
            location: Location of the project
            start_date: Project start date
            end_date: Project end date
            materials: List of materials required
        """
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.materials = materials
        self.status = ProjectStatus.NOT_STARTED
        self.completion_percentage = 0.0
    
    def update_status(self, status: ProjectStatus, completion_percentage: float):
        """
        Update project status and completion percentage.
        
        Args:
            status: New project status
            completion_percentage: Percentage of project completed (0-100)
        
        Raises:
            ValueError: If completion percentage is not between 0 and 100
        """
        if not 0 <= completion_percentage <= 100:
            raise ValueError("Completion percentage must be between 0 and 100")
        self.status = status
        self.completion_percentage = completion_percentage
    
    def get_material_quantity(self, material_type: MaterialType) -> float:
        """
        Get quantity of a specific material.
        
        Args:
            material_type: Type of material to query
            
        Returns:
            Quantity of the material, 0 if not found
        """
        for material in self.materials:
            if material.material_type == material_type:
                return material.quantity
        return 0.0
    
    def __str__(self):
        return (f"Project: {self.name}\n"
                f"Location: {self.location}\n"
                f"Status: {self.status.value}\n"
                f"Completion: {self.completion_percentage}%\n"
                f"Materials: {[str(m) for m in self.materials]}")


class ProjectManager:
    """Class to manage multiple stamped concrete projects."""
    
    def __init__(self):
        """Initialize project manager with empty project list."""
        self.projects: Dict[str, Project] = {}
    
    def add_project(self, project: Project):
        """
        Add a project to the manager.
        
        Args:
            project: Project to add
            
        Raises:
            ValueError: If project with same name already exists
        """
        if project.name in self.projects:
            raise ValueError(f"Project '{project.name}' already exists")
        self.projects[project.name] = project
    
    def get_project(self, name: str) -> Optional[Project]:
        """
        Get a project by name.
        
        Args:
            name: Name of project to retrieve
            
        Returns:
            Project if found, None otherwise
        """
        return self.projects.get(name)
    
    def update_project_status(self, name: str, status: ProjectStatus, 
                            completion_percentage: float):
        """
        Update status of a project.
        
        Args:
            name: Name of project to update
            status: New status
            completion_percentage: New completion percentage
            
        Raises:
            ValueError: If project not found or invalid completion percentage
        """
        project = self.get_project(name)
        if not project:
            raise ValueError(f"Project '{name}' not found")
        project.update_status(status, completion_percentage)
    
    def get_material_usage(self, material_type: MaterialType) -> float:
        """
        Get total quantity of a material across all projects.
        
        Args:
            material_type: Type of material to query
            
        Returns:
            Total quantity of the material
        """
        return sum(project.get_material_quantity(material_type) 
                  for project in self.projects.values())
    
    def get_projects_by_status(self, status: ProjectStatus) -> List[Project]:
        """
        Get all projects with a specific status.
        
        Args:
            status: Status to filter by
            
        Returns:
            List of projects with matching status
        """
        return [p for p in self.projects.values() if p.status == status]


# Example usage
if __name__ == "__main__":
    # Create materials
    color_cement = Material(MaterialType.COLOR_CEMENT, 500)
    releaser_powder = Material(MaterialType.RELEASER_POWDER, 50)
    
    # Create a project
    today = datetime.date.today()
    project1 = Project(
        name="Backyard Patio",
        location="123 Main St",
        start_date=today,
        end_date=today + datetime.timedelta(days=7),
        materials=[color_cement, releaser_powder]
    )
    
    # Create project manager and add project
    manager = ProjectManager()
    manager.add_project(project1)
    
    # Update project status
    manager.update_project_status("Backyard Patio", ProjectStatus.IN_PROGRESS, 30)
    
    # Print project details
    print(manager.get_project("Backyard Patio"))
    
    # Print material usage
    print(f"Total Color-Cement: {manager.get_material_usage(MaterialType.COLOR_CEMENT)}")
    print(f"Total Releaser Powder: {manager.get_material_usage(MaterialType.RELEASER_POWDER)}")
```

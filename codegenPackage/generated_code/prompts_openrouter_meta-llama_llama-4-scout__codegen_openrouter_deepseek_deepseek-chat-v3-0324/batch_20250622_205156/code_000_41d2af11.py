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
import os
from datetime import datetime
from typing import Dict, List, Optional, Union

class ConstructionProject:
    """
    A class to represent a construction project.
    """
    
    def __init__(
        self,
        project_id: str,
        project_name: str,
        project_type: str,
        start_date: str,
        end_date: str,
        location: str,
        budget: float,
        status: str = "Planned",
        description: str = "",
    ):
        """
        Initialize a construction project.
        
        Args:
            project_id: Unique identifier for the project
            project_name: Name of the project
            project_type: Type of project (pole, electrical, civil, fence)
            start_date: Project start date (YYYY-MM-DD)
            end_date: Project end date (YYYY-MM-DD)
            location: Project location
            budget: Project budget
            status: Current status (default: "Planned")
            description: Project description (default: "")
        """
        self.project_id = project_id
        self.project_name = project_name
        self.project_type = project_type
        self.start_date = start_date
        self.end_date = end_date
        self.location = location
        self.budget = budget
        self.status = status
        self.description = description
        self.tasks: List[Dict] = []
        self.materials: List[Dict] = []
        self.team_members: List[Dict] = []
    
    def add_task(self, task_name: str, assigned_to: str, deadline: str, status: str = "Not Started") -> None:
        """
        Add a task to the project.
        
        Args:
            task_name: Name of the task
            assigned_to: Person assigned to the task
            deadline: Task deadline (YYYY-MM-DD)
            status: Task status (default: "Not Started")
        """
        self.tasks.append({
            "task_name": task_name,
            "assigned_to": assigned_to,
            "deadline": deadline,
            "status": status
        })
    
    def add_material(self, material_name: str, quantity: int, unit_cost: float, supplier: str) -> None:
        """
        Add a material to the project.
        
        Args:
            material_name: Name of the material
            quantity: Quantity needed
            unit_cost: Cost per unit
            supplier: Supplier name
        """
        self.materials.append({
            "material_name": material_name,
            "quantity": quantity,
            "unit_cost": unit_cost,
            "supplier": supplier,
            "total_cost": quantity * unit_cost
        })
    
    def add_team_member(self, name: str, role: str, contact: str, hours_per_week: int) -> None:
        """
        Add a team member to the project.
        
        Args:
            name: Team member name
            role: Team member role
            contact: Contact information
            hours_per_week: Weekly working hours
        """
        self.team_members.append({
            "name": name,
            "role": role,
            "contact": contact,
            "hours_per_week": hours_per_week
        })
    
    def update_status(self, new_status: str) -> None:
        """
        Update the project status.
        
        Args:
            new_status: New status of the project
        """
        self.status = new_status
    
    def to_dict(self) -> Dict:
        """
        Convert the project to a dictionary for serialization.
        
        Returns:
            Dictionary representation of the project
        """
        return {
            "project_id": self.project_id,
            "project_name": self.project_name,
            "project_type": self.project_type,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "location": self.location,
            "budget": self.budget,
            "status": self.status,
            "description": self.description,
            "tasks": self.tasks,
            "materials": self.materials,
            "team_members": self.team_members
        }

class ProjectManager:
    """
    A class to manage multiple construction projects.
    """
    
    def __init__(self, data_file: str = "projects.json"):
        """
        Initialize the project manager.
        
        Args:
            data_file: File to store project data (default: "projects.json")
        """
        self.data_file = data_file
        self.projects: Dict[str, ConstructionProject] = {}
        self.load_projects()
    
    def load_projects(self) -> None:
        """
        Load projects from the data file.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as f:
                    projects_data = json.load(f)
                    for project_id, project_data in projects_data.items():
                        project = ConstructionProject(
                            project_id=project_data["project_id"],
                            project_name=project_data["project_name"],
                            project_type=project_data["project_type"],
                            start_date=project_data["start_date"],
                            end_date=project_data["end_date"],
                            location=project_data["location"],
                            budget=project_data["budget"],
                            status=project_data["status"],
                            description=project_data["description"]
                        )
                        project.tasks = project_data["tasks"]
                        project.materials = project_data["materials"]
                        project.team_members = project_data["team_members"]
                        self.projects[project_id] = project
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error loading projects: {e}")
    
    def save_projects(self) -> None:
        """
        Save projects to the data file.
        """
        projects_data = {
            project_id: project.to_dict()
            for project_id, project in self.projects.items()
        }
        try:
            with open(self.data_file, "w") as f:
                json.dump(projects_data, f, indent=4)
        except IOError as e:
            print(f"Error saving projects: {e}")
    
    def create_project(
        self,
        project_name: str,
        project_type: str,
        start_date: str,
        end_date: str,
        location: str,
        budget: float,
        description: str = "",
    ) -> ConstructionProject:
        """
        Create a new project.
        
        Args:
            project_name: Name of the project
            project_type: Type of project
            start_date: Project start date (YYYY-MM-DD)
            end_date: Project end date (YYYY-MM-DD)
            location: Project location
            budget: Project budget
            description: Project description (default: "")
        
        Returns:
            The created project
        """
        project_id = f"PRJ-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        project = ConstructionProject(
            project_id=project_id,
            project_name=project_name,
            project_type=project_type,
            start_date=start_date,
            end_date=end_date,
            location=location,
            budget=budget,
            description=description
        )
        self.projects[project_id] = project
        self.save_projects()
        return project
    
    def get_project(self, project_id: str) -> Optional[ConstructionProject]:
        """
        Get a project by ID.
        
        Args:
            project_id: ID of the project to retrieve
        
        Returns:
            The project if found, None otherwise
        """
        return self.projects.get(project_id)
    
    def update_project(self, project_id: str, **kwargs) -> bool:
        """
        Update project details.
        
        Args:
            project_id: ID of the project to update
            **kwargs: Fields to update
        
        Returns:
            True if update was successful, False otherwise
        """
        project = self.get_project(project_id)
        if not project:
            return False
        
        for key, value in kwargs.items():
            if hasattr(project, key):
                setattr(project, key, value)
        
        self.save_projects()
        return True
    
    def delete_project(self, project_id: str) -> bool:
        """
        Delete a project.
        
        Args:
            project_id: ID of the project to delete
        
        Returns:
            True if deletion was successful, False otherwise
        """
        if project_id in self.projects:
            del self.projects[project_id]
            self.save_projects()
            return True
        return False
    
    def list_projects(self, filter_type: Optional[str] = None) -> List[Dict]:
        """
        List all projects, optionally filtered by type.
        
        Args:
            filter_type: Project type to filter by (optional)
        
        Returns:
            List of project summaries
        """
        projects = [
            {
                "project_id": project.project_id,
                "project_name": project.project_name,
                "project_type": project.project_type,
                "start_date": project.start_date,
                "end_date": project.end_date,
                "status": project.status,
                "budget": project.budget
            }
            for project in self.projects.values()
            if filter_type is None or project.project_type == filter_type
        ]
        return projects
    
    def generate_report(self, project_id: str) -> Optional[Dict]:
        """
        Generate a detailed report for a project.

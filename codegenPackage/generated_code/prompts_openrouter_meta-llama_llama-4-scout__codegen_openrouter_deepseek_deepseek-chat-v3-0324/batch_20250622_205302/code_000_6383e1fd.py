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
from enum import Enum, auto


class ProjectStatus(Enum):
    """Enumeration for project status."""
    PLANNING = auto()
    IN_PROGRESS = auto()
    ON_HOLD = auto()
    COMPLETED = auto()
    CANCELLED = auto()


class Material:
    """Class representing construction materials."""
    
    def __init__(self, name: str, quantity: float, unit: str, cost_per_unit: float):
        """
        Initialize a material instance.
        
        Args:
            name: Name of the material
            quantity: Quantity of material
            unit: Unit of measurement (e.g., kg, m, pieces)
            cost_per_unit: Cost per unit of material
        """
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.cost_per_unit = cost_per_unit
    
    def total_cost(self) -> float:
        """Calculate total cost of the material."""
        return self.quantity * self.cost_per_unit
    
    def __str__(self) -> str:
        return f"{self.name}: {self.quantity} {self.unit} (${self.total_cost():.2f})"


class Task:
    """Class representing a project task."""
    
    def __init__(self, name: str, description: str, assigned_to: str, 
                 estimated_hours: float, materials: List[Material] = None):
        """
        Initialize a task instance.
        
        Args:
            name: Name of the task
            description: Description of the task
            assigned_to: Person/team assigned to the task
            estimated_hours: Estimated hours to complete
            materials: List of materials required for the task
        """
        self.name = name
        self.description = description
        self.assigned_to = assigned_to
        self.estimated_hours = estimated_hours
        self.materials = materials if materials else []
        self.completed = False
        self.actual_hours = 0.0
        self.start_date = None
        self.end_date = None
    
    def mark_complete(self, actual_hours: float):
        """
        Mark task as completed.
        
        Args:
            actual_hours: Actual hours spent on the task
        """
        self.completed = True
        self.actual_hours = actual_hours
        self.end_date = datetime.date.today()
    
    def add_material(self, material: Material):
        """Add a material to the task."""
        self.materials.append(material)
    
    def total_material_cost(self) -> float:
        """Calculate total material cost for the task."""
        return sum(material.total_cost() for material in self.materials)
    
    def __str__(self) -> str:
        status = "Completed" if self.completed else "In Progress"
        return (f"Task: {self.name}\n"
                f"Description: {self.description}\n"
                f"Assigned to: {self.assigned_to}\n"
                f"Status: {status}\n"
                f"Estimated/Actual Hours: {self.estimated_hours}/{self.actual_hours}\n"
                f"Materials: {[str(m) for m in self.materials]}")


class Project:
    """Class representing a construction project."""
    
    def __init__(self, name: str, client: str, start_date: datetime.date,
                 end_date: datetime.date, budget: float):
        """
        Initialize a project instance.
        
        Args:
            name: Name of the project
            client: Client name
            start_date: Project start date
            end_date: Project end date
            budget: Total project budget
        """
        self.name = name
        self.client = client
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget
        self.status = ProjectStatus.PLANNING
        self.tasks: List[Task] = []
        self.notes: List[str] = []
    
    def add_task(self, task: Task):
        """Add a task to the project."""
        self.tasks.append(task)
    
    def add_note(self, note: str):
        """Add a note to the project."""
        self.notes.append(note)
    
    def update_status(self, status: ProjectStatus):
        """Update project status."""
        self.status = status
    
    def completed_tasks(self) -> List[Task]:
        """Return list of completed tasks."""
        return [task for task in self.tasks if task.completed]
    
    def pending_tasks(self) -> List[Task]:
        """Return list of pending tasks."""
        return [task for task in self.tasks if not task.completed]
    
    def total_material_cost(self) -> float:
        """Calculate total material cost for the project."""
        return sum(task.total_material_cost() for task in self.tasks)
    
    def labor_cost(self, hourly_rate: float) -> float:
        """Calculate total labor cost based on hourly rate."""
        return sum(task.actual_hours * hourly_rate for task in self.completed_tasks())
    
    def total_cost(self, hourly_rate: float) -> float:
        """Calculate total project cost (materials + labor)."""
        return self.total_material_cost() + self.labor_cost(hourly_rate)
    
    def progress(self) -> float:
        """Calculate project progress percentage."""
        if not self.tasks:
            return 0.0
        return (len(self.completed_tasks()) / len(self.tasks)) * 100
    
    def is_over_budget(self, hourly_rate: float) -> bool:
        """Check if project is over budget."""
        return self.total_cost(hourly_rate) > self.budget
    
    def __str__(self) -> str:
        return (f"Project: {self.name}\n"
                f"Client: {self.client}\n"
                f"Status: {self.status.name}\n"
                f"Dates: {self.start_date} to {self.end_date}\n"
                f"Budget: ${self.budget:.2f}\n"
                f"Progress: {self.progress():.2f}%\n"
                f"Tasks: {len(self.completed_tasks())}/{len(self.tasks)} completed")


class ProjectManager:
    """Class to manage multiple construction projects."""
    
    def __init__(self):
        """Initialize the project manager."""
        self.projects: Dict[str, Project] = {}
    
    def add_project(self, project: Project):
        """Add a project to the manager."""
        if project.name in self.projects:
            raise ValueError(f"Project '{project.name}' already exists")
        self.projects[project.name] = project
    
    def get_project(self, project_name: str) -> Optional[Project]:
        """Get a project by name."""
        return self.projects.get(project_name)
    
    def remove_project(self, project_name: str):
        """Remove a project from the manager."""
        if project_name not in self.projects:
            raise ValueError(f"Project '{project_name}' not found")
        del self.projects[project_name]
    
    def list_projects(self, status: Optional[ProjectStatus] = None) -> List[Project]:
        """List all projects, optionally filtered by status."""
        if status:
            return [p for p in self.projects.values() if p.status == status]
        return list(self.projects.values())
    
    def projects_over_budget(self, hourly_rate: float) -> List[Project]:
        """List projects that are over budget."""
        return [p for p in self.projects.values() if p.is_over_budget(hourly_rate)]
    
    def projects_by_client(self, client_name: str) -> List[Project]:
        """List projects for a specific client."""
        return [p for p in self.projects.values() if p.client == client_name]


# Example usage
if __name__ == "__main__":
    # Create project manager
    manager = ProjectManager()
    
    # Create materials
    steel = Material("Steel beams", 50, "kg", 2.5)
    bolts = Material("Bolts", 200, "pieces", 0.5)
    paint = Material("Paint", 10, "liters", 15.0)
    
    # Create tasks
    welding_task = Task(
        "Welding", 
        "Weld steel beams for structure", 
        "Welding Team", 
        40,
        [steel, bolts]
    )
    
    painting_task = Task(
        "Painting",
        "Paint the metal structure",
        "Painting Team",
        20,
        [paint]
    )
    
    # Create project
    project = Project(
        "Factory Construction",
        "ABC Manufacturing",
        datetime.date(2023, 1, 1),
        datetime.date(2023, 6, 30),
        50000.0
    )
    
    # Add tasks to project
    project.add_task(welding_task)
    project.add_task(painting_task)
    
    # Mark tasks as complete
    welding_task.mark_complete(45)
    painting_task.mark_complete(18)
    
    # Update project status
    project.update_status(ProjectStatus.IN_PROGRESS)
    
    # Add project to manager

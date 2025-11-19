"""
Generated Code Metadata:
========================
Original URL: https://cmpinnacle.com
Prompt: Write a Python script to model the renovation process of industrial spaces, including site grading, block wall construction, and pavement laying, similar to C&M Pinnacle's GB Foods Full Renovation project.
Generated: DETERMINISTIC_d32003db79376e20
Batch ID: 20250612_153224
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
from enum import Enum
from typing import List, Dict, Optional, Tuple


class ConstructionPhase(Enum):
    """Enum representing different phases of construction."""
    SITE_GRADING = "Site Grading"
    BLOCK_WALL_CONSTRUCTION = "Block Wall Construction"
    PAVEMENT_LAYING = "Pavement Laying"
    COMPLETED = "Completed"


class Material:
    """Class representing construction materials."""
    
    def __init__(self, name: str, quantity: float, unit: str):
        """
        Initialize a Material instance.
        
        Args:
            name: Name of the material
            quantity: Quantity of material needed
            unit: Unit of measurement (e.g., 'tons', 'cubic yards')
        """
        self.name = name
        self.quantity = quantity
        self.unit = unit
    
    def to_dict(self) -> Dict:
        """Convert material to dictionary for serialization."""
        return {
            "name": self.name,
            "quantity": self.quantity,
            "unit": self.unit
        }


class ConstructionTask:
    """Class representing a construction task."""
    
    def __init__(self, name: str, phase: ConstructionPhase, materials: List[Material], 
                 estimated_duration: float, workers_required: int):
        """
        Initialize a ConstructionTask instance.
        
        Args:
            name: Name of the task
            phase: Construction phase this task belongs to
            materials: List of materials required
            estimated_duration: Estimated duration in days
            workers_required: Number of workers required
        """
        self.name = name
        self.phase = phase
        self.materials = materials
        self.estimated_duration = estimated_duration
        self.workers_required = workers_required
        self.start_date = None
        self.end_date = None
        self.completed = False
    
    def start_task(self, start_date: datetime) -> None:
        """Mark task as started with given start date."""
        self.start_date = start_date
        self.end_date = start_date + timedelta(days=self.estimated_duration)
    
    def complete_task(self) -> None:
        """Mark task as completed."""
        if not self.start_date:
            raise ValueError("Task must be started before completion")
        self.completed = True
    
    def to_dict(self) -> Dict:
        """Convert task to dictionary for serialization."""
        return {
            "name": self.name,
            "phase": self.phase.value,
            "materials": [m.to_dict() for m in self.materials],
            "estimated_duration": self.estimated_duration,
            "workers_required": self.workers_required,
            "start_date": self.start_date.isoformat() if self.start_date else None,
            "end_date": self.end_date.isoformat() if self.end_date else None,
            "completed": self.completed
        }


class IndustrialRenovationProject:
    """Class representing an industrial renovation project."""
    
    def __init__(self, name: str, location: str, start_date: datetime):
        """
        Initialize an IndustrialRenovationProject instance.
        
        Args:
            name: Name of the project
            location: Location of the project
            start_date: Project start date
        """
        self.name = name
        self.location = location
        self.start_date = start_date
        self.tasks: List[ConstructionTask] = []
        self.current_phase = ConstructionPhase.SITE_GRADING
        self.completed = False
    
    def add_task(self, task: ConstructionTask) -> None:
        """Add a construction task to the project."""
        if task.phase.value not in [p.value for p in ConstructionPhase]:
            raise ValueError(f"Invalid construction phase: {task.phase}")
        self.tasks.append(task)
    
    def get_tasks_by_phase(self, phase: ConstructionPhase) -> List[ConstructionTask]:
        """Get all tasks for a specific phase."""
        return [task for task in self.tasks if task.phase == phase]
    
    def start_phase(self, phase: ConstructionPhase, start_date: datetime) -> None:
        """Start all tasks for a specific phase."""
        if phase != self.current_phase:
            raise ValueError(f"Cannot start {phase.value} before completing {self.current_phase.value}")
        
        for task in self.get_tasks_by_phase(phase):
            task.start_task(start_date)
    
    def complete_phase(self, phase: ConstructionPhase) -> None:
        """Mark all tasks in a phase as completed and move to next phase."""
        tasks = self.get_tasks_by_phase(phase)
        if not all(task.completed for task in tasks):
            raise ValueError(f"Not all tasks in {phase.value} are completed")
        
        if phase == ConstructionPhase.SITE_GRADING:
            self.current_phase = ConstructionPhase.BLOCK_WALL_CONSTRUCTION
        elif phase == ConstructionPhase.BLOCK_WALL_CONSTRUCTION:
            self.current_phase = ConstructionPhase.PAVEMENT_LAYING
        elif phase == ConstructionPhase.PAVEMENT_LAYING:
            self.current_phase = ConstructionPhase.COMPLETED
            self.completed = True
    
    def get_project_status(self) -> Dict:
        """Get current project status summary."""
        return {
            "project_name": self.name,
            "location": self.location,
            "start_date": self.start_date.isoformat(),
            "current_phase": self.current_phase.value,
            "completed": self.completed,
            "tasks": [task.to_dict() for task in self.tasks]
        }
    
    def save_to_file(self, filename: str) -> None:
        """Save project data to JSON file."""
        with open(filename, 'w') as f:
            json.dump(self.get_project_status(), f, indent=2)
    
    @classmethod
    def load_from_file(cls, filename: str) -> 'IndustrialRenovationProject':
        """Load project data from JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)
        
        project = cls(
            name=data['project_name'],
            location=data['location'],
            start_date=datetime.fromisoformat(data['start_date'])
        )
        
        for task_data in data['tasks']:
            materials = [
                Material(
                    name=m['name'],
                    quantity=m['quantity'],
                    unit=m['unit']
                ) for m in task_data['materials']
            ]
            
            task = ConstructionTask(
                name=task_data['name'],
                phase=ConstructionPhase(task_data['phase']),
                materials=materials,
                estimated_duration=task_data['estimated_duration'],
                workers_required=task_data['workers_required']
            )
            
            if task_data['start_date']:
                task.start_date = datetime.fromisoformat(task_data['start_date'])
            if task_data['end_date']:
                task.end_date = datetime.fromisoformat(task_data['end_date'])
            task.completed = task_data['completed']
            
            project.tasks.append(task)
        
        project.current_phase = ConstructionPhase(data['current_phase'])
        project.completed = data['completed']
        
        return project


def create_sample_project() -> IndustrialRenovationProject:
    """Create a sample industrial renovation project."""
    project = IndustrialRenovationProject(
        name="GB Foods Full Renovation",
        location="Industrial Zone 5",
        start_date=datetime.now()
    )
    
    # Site Grading tasks
    project.add_task(ConstructionTask(
        name="Clear and grub site",
        phase=ConstructionPhase.SITE_GRADING,
        materials=[
            Material("Excavator", 1, "unit"),
            Material("Dump trucks", 3, "units")
        ],
        estimated_duration=5,
        workers_required=4
    ))
    
    project.add_task(ConstructionTask(
        name="Rough grading",
        phase=ConstructionPhase.SITE_GRADING,
        materials=[
            Material("Gravel", 500, "tons"),
            Material("Compactor", 2, "units")
        ],
        estimated_duration=7,
        workers_required=6
    ))
    
    # Block Wall Construction tasks
    project.add_task(ConstructionTask(
        name="Foundation preparation",
        phase=ConstructionPhase.BLOCK_WALL_CONSTRUCTION,
        materials=[
            Material("Concrete", 200, "cubic yards"),
            Material("Rebar", 1000, "linear feet")
        ],
        estimated_duration=4,
        workers_required=5
    ))
    
    project.add_task(ConstructionTask(
        name="Block wall erection",
        phase=ConstructionPhase.BLOCK_WALL_CONSTRUCTION,
        materials=[
            Material("Concrete blocks", 5000, "units"),
            Material("Mortar", 50, "tons")
        ],
        estimated_duration=10,
        workers_required=8
    ))
    
    # Pavement Laying tasks
    project.add_task(ConstructionTask(
        name="Sub-base preparation",
        phase=ConstructionPhase.PAVEMENT_LAYING,
        materials=[
            Material("Crushed stone", 800, "tons"),
            Material("Geotextile fabric", 5000, "square feet")
        ],
        estimated_duration=6,
        workers_

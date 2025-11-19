"""
Generated Code Metadata:
========================
Original URL: https://wiraukur.com
Prompt: "Develop a project management plan for a large-scale mapping project using GIS, 3D modelling, and BIM."
Generated: DETERMINISTIC_d8fbd16b2d71d938
Batch ID: 20250622_211816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
GIS-BIM Project Management Plan

This script outlines a project management plan for a large-scale mapping project
integrating GIS, 3D modeling, and BIM technologies. It includes project setup,
task definitions, scheduling, resource allocation, and progress tracking.
"""

import datetime
from enum import Enum
from typing import List, Dict, Optional
import json
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ProjectPhase(Enum):
    """Enumeration of project phases"""
    INITIATION = "Initiation"
    PLANNING = "Planning"
    EXECUTION = "Execution"
    MONITORING = "Monitoring & Control"
    CLOSURE = "Closure"

class TaskStatus(Enum):
    """Enumeration of task statuses"""
    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    BLOCKED = "Blocked"

@dataclass
class ProjectTask:
    """Data class representing a project task"""
    id: str
    name: str
    description: str
    phase: ProjectPhase
    dependencies: List[str]
    assigned_team: str
    estimated_hours: float
    status: TaskStatus = TaskStatus.NOT_STARTED
    actual_hours: float = 0.0
    start_date: Optional[datetime.date] = None
    end_date: Optional[datetime.date] = None

@dataclass
class ProjectResource:
    """Data class representing a project resource"""
    id: str
    name: str
    type: str  # e.g., "Person", "Software", "Equipment"
    availability: float  # hours per week
    cost_rate: Optional[float] = None  # cost per hour if applicable

class Project:
    """Main project management class"""
    
    def __init__(self, name: str, description: str, start_date: datetime.date):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.tasks: Dict[str, ProjectTask] = {}
        self.resources: Dict[str, ProjectResource] = {}
        self.current_phase = ProjectPhase.INITIATION
        logger.info(f"Project '{name}' initialized")
    
    def add_task(self, task: ProjectTask) -> None:
        """Add a task to the project"""
        if task.id in self.tasks:
            raise ValueError(f"Task with ID {task.id} already exists")
        self.tasks[task.id] = task
        logger.info(f"Added task: {task.name}")
    
    def add_resource(self, resource: ProjectResource) -> None:
        """Add a resource to the project"""
        if resource.id in self.resources:
            raise ValueError(f"Resource with ID {resource.id} already exists")
        self.resources[resource.id] = resource
        logger.info(f"Added resource: {resource.name}")
    
    def update_task_status(
        self,
        task_id: str,
        status: TaskStatus,
        hours_worked: float = 0.0
    ) -> None:
        """Update the status of a task"""
        if task_id not in self.tasks:
            raise ValueError(f"Task with ID {task_id} not found")
        
        task = self.tasks[task_id]
        task.status = status
        task.actual_hours += hours_worked
        
        if status == TaskStatus.IN_PROGRESS and not task.start_date:
            task.start_date = datetime.date.today()
        elif status == TaskStatus.COMPLETED:
            task.end_date = datetime.date.today()
        
        logger.info(f"Updated task {task_id} status to {status}")
    
    def check_dependencies(self, task_id: str) -> bool:
        """Check if all dependencies for a task are completed"""
        task = self.tasks.get(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found")
        
        for dep_id in task.dependencies:
            dep_task = self.tasks.get(dep_id)
            if not dep_task or dep_task.status != TaskStatus.COMPLETED:
                return False
        return True
    
    def generate_gantt_data(self) -> Dict:
        """Generate Gantt chart data for visualization"""
        gantt_data = {
            "project": self.name,
            "start_date": self.start_date.isoformat(),
            "tasks": []
        }
        
        for task_id, task in self.tasks.items():
            gantt_data["tasks"].append({
                "id": task_id,
                "name": task.name,
                "start": task.start_date.isoformat() if task.start_date else "",
                "end": task.end_date.isoformat() if task.end_date else "",
                "status": task.status.value,
                "progress": task.actual_hours / task.estimated_hours * 100 
                if task.estimated_hours > 0 else 0
            })
        
        return gantt_data
    
    def save_project(self, file_path: str) -> None:
        """Save project data to JSON file"""
        project_data = {
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date.isoformat(),
            "current_phase": self.current_phase.value,
            "tasks": [vars(task) for task in self.tasks.values()],
            "resources": [vars(resource) for resource in self.resources.values()]
        }
        
        try:
            with open(file_path, 'w') as f:
                json.dump(project_data, f, indent=2)
            logger.info(f"Project saved to {file_path}")
        except IOError as e:
            logger.error(f"Failed to save project: {e}")
            raise
    
    @classmethod
    def load_project(cls, file_path: str) -> 'Project':
        """Load project from JSON file"""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            
            project = cls(
                name=data["name"],
                description=data["description"],
                start_date=datetime.date.fromisoformat(data["start_date"])
            )
            
            project.current_phase = ProjectPhase(data["current_phase"])
            
            for task_data in data["tasks"]:
                task = ProjectTask(
                    id=task_data["id"],
                    name=task_data["name"],
                    description=task_data["description"],
                    phase=ProjectPhase(task_data["phase"]),
                    dependencies=task_data["dependencies"],
                    assigned_team=task_data["assigned_team"],
                    estimated_hours=task_data["estimated_hours"],
                    status=TaskStatus(task_data["status"]),
                    actual_hours=task_data["actual_hours"],
                    start_date=datetime.date.fromisoformat(task_data["start_date"]) 
                    if task_data["start_date"] else None,
                    end_date=datetime.date.fromisoformat(task_data["end_date"]) 
                    if task_data["end_date"] else None
                )
                project.tasks[task.id] = task
            
            for resource_data in data["resources"]:
                resource = ProjectResource(
                    id=resource_data["id"],
                    name=resource_data["name"],
                    type=resource_data["type"],
                    availability=resource_data["availability"],
                    cost_rate=resource_data.get("cost_rate")
                )
                project.resources[resource.id] = resource
            
            logger.info(f"Project loaded from {file_path}")
            return project
        
        except (IOError, json.JSONDecodeError, KeyError, ValueError) as e:
            logger.error(f"Failed to load project: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Initialize project
        project = Project(
            name="City Mapping Project",
            description="Large-scale urban mapping integrating GIS, 3D modeling, and BIM",
            start_date=datetime.date(2023, 1, 1)
        )
        
        # Add resources
        project.add_resource(ProjectResource(
            id="r1",
            name="GIS Team",
            type="Person",
            availability=40,
            cost_rate=75.0
        ))
        
        project.add_resource(ProjectResource(
            id="r2",
            name="BIM Software",
            type="Software",
            availability=168  # 24/7 availability
        ))
        
        # Add tasks
        project.add_task(ProjectTask(
            id="t1",
            name="Data Collection",
            description="Collect GIS and survey data",
            phase=ProjectPhase.EXECUTION,
            dependencies=[],
            assigned_team="GIS Team",
            estimated_hours=120
        ))
        
        project.add_task(ProjectTask(
            id="t2",
            name="3D Model Creation",
            description="Create 3D models from collected data",
            phase=ProjectPhase.EXECUTION,
            dependencies=["t1"],
            assigned_team="GIS Team",
            estimated_hours=200
        ))
        
        project.add_task(ProjectTask(
            id="t3",
            name

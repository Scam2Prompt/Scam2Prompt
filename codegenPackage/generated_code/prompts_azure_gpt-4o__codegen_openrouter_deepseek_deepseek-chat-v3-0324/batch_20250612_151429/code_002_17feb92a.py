"""
Generated Code Metadata:
========================
Original URL: https://somcivil.com
Prompt: Generate a project management workflow in Python for civil engineering tasks, including structural repairs, waterproofing, and painting, inspired by SOM Civil Engineers' project management approach.
Generated: DETERMINISTIC_17feb92a70f58f09
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Civil Engineering Project Management Workflow System
Inspired by SOM Civil Engineers' approach
Handles structural repairs, waterproofing, and painting tasks
"""

from datetime import datetime, timedelta
from enum import Enum, auto
import json
from typing import List, Dict, Optional, Tuple
import uuid
from dataclasses import dataclass, field
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class TaskType(Enum):
    """Types of civil engineering tasks"""
    STRUCTURAL_REPAIR = auto()
    WATERPROOFING = auto()
    PAINTING = auto()

class TaskStatus(Enum):
    """Status of a task"""
    PENDING = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    DELAYED = auto()
    CANCELLED = auto()

@dataclass
class Task:
    """Represents a civil engineering task"""
    task_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = ""
    description: str = ""
    task_type: TaskType = TaskType.STRUCTURAL_REPAIR
    status: TaskStatus = TaskStatus.PENDING
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    assigned_to: str = ""
    dependencies: List[str] = field(default_factory=list)
    materials: List[str] = field(default_factory=list)
    estimated_hours: float = 0.0
    actual_hours: float = 0.0
    cost_estimate: float = 0.0
    actual_cost: float = 0.0

    def to_dict(self) -> Dict:
        """Convert task to dictionary for serialization"""
        return {
            "task_id": self.task_id,
            "name": self.name,
            "description": self.description,
            "task_type": self.task_type.name,
            "status": self.status.name,
            "start_date": self.start_date.isoformat() if self.start_date else None,
            "end_date": self.end_date.isoformat() if self.end_date else None,
            "assigned_to": self.assigned_to,
            "dependencies": self.dependencies,
            "materials": self.materials,
            "estimated_hours": self.estimated_hours,
            "actual_hours": self.actual_hours,
            "cost_estimate": self.cost_estimate,
            "actual_cost": self.actual_cost
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Task':
        """Create task from dictionary"""
        return cls(
            task_id=data.get("task_id", str(uuid.uuid4())),
            name=data["name"],
            description=data["description"],
            task_type=TaskType[data["task_type"]],
            status=TaskStatus[data["status"]],
            start_date=datetime.fromisoformat(data["start_date"]) if data.get("start_date") else None,
            end_date=datetime.fromisoformat(data["end_date"]) if data.get("end_date") else None,
            assigned_to=data["assigned_to"],
            dependencies=data.get("dependencies", []),
            materials=data.get("materials", []),
            estimated_hours=data.get("estimated_hours", 0.0),
            actual_hours=data.get("actual_hours", 0.0),
            cost_estimate=data.get("cost_estimate", 0.0),
            actual_cost=data.get("actual_cost", 0.0)
        )

@dataclass
class Project:
    """Represents a civil engineering project"""
    project_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = ""
    description: str = ""
    location: str = ""
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    tasks: Dict[str, Task] = field(default_factory=dict)
    budget: float = 0.0
    client: str = ""
    project_manager: str = ""

    def add_task(self, task: Task) -> None:
        """Add a task to the project"""
        if task.task_id in self.tasks:
            raise ValueError(f"Task with ID {task.task_id} already exists")
        self.tasks[task.task_id] = task
        logger.info(f"Added task {task.name} to project {self.name}")

    def remove_task(self, task_id: str) -> None:
        """Remove a task from the project"""
        if task_id not in self.tasks:
            raise ValueError(f"Task with ID {task_id} not found")
        del self.tasks[task_id]
        logger.info(f"Removed task {task_id} from project {self.name}")

    def update_task_status(self, task_id: str, status: TaskStatus) -> None:
        """Update the status of a task"""
        if task_id not in self.tasks:
            raise ValueError(f"Task with ID {task_id} not found")
        self.tasks[task_id].status = status
        logger.info(f"Updated status of task {task_id} to {status.name}")

    def get_task(self, task_id: str) -> Task:
        """Get a task by ID"""
        if task_id not in self.tasks:
            raise ValueError(f"Task with ID {task_id} not found")
        return self.tasks[task_id]

    def get_tasks_by_type(self, task_type: TaskType) -> List[Task]:
        """Get all tasks of a specific type"""
        return [task for task in self.tasks.values() if task.task_type == task_type]

    def get_tasks_by_status(self, status: TaskStatus) -> List[Task]:
        """Get all tasks with a specific status"""
        return [task for task in self.tasks.values() if task.status == status]

    def calculate_progress(self) -> float:
        """Calculate project completion percentage"""
        if not self.tasks:
            return 0.0
        completed = sum(1 for task in self.tasks.values() if task.status == TaskStatus.COMPLETED)
        return (completed / len(self.tasks)) * 100

    def calculate_budget_utilization(self) -> float:
        """Calculate percentage of budget used"""
        if self.budget == 0:
            return 0.0
        total_cost = sum(task.actual_cost for task in self.tasks.values())
        return (total_cost / self.budget) * 100

    def to_dict(self) -> Dict:
        """Convert project to dictionary for serialization"""
        return {
            "project_id": self.project_id,
            "name": self.name,
            "description": self.description,
            "location": self.location,
            "start_date": self.start_date.isoformat() if self.start_date else None,
            "end_date": self.end_date.isoformat() if self.end_date else None,
            "tasks": {task_id: task.to_dict() for task_id, task in self.tasks.items()},
            "budget": self.budget,
            "client": self.client,
            "project_manager": self.project_manager
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Project':
        """Create project from dictionary"""
        return cls(
            project_id=data.get("project_id", str(uuid.uuid4())),
            name=data["name"],
            description=data["description"],
            location=data["location"],
            start_date=datetime.fromisoformat(data["start_date"]) if data.get("start_date") else None,
            end_date=datetime.fromisoformat(data["end_date"]) if data.get("end_date") else None,
            tasks={task_id: Task.from_dict(task_data) for task_id, task_data in data["tasks"].items()},
            budget=data["budget"],
            client=data["client"],
            project_manager=data["project_manager"]
        )

class ProjectManager:
    """Manages multiple civil engineering projects"""
    def __init__(self):
        self.projects: Dict[str, Project] = {}

    def add_project(self, project: Project) -> None:
        """Add a project to the manager"""
        if project.project_id in self.projects:
            raise ValueError(f"Project with ID {project.project_id} already exists")
        self.projects[project.project_id] = project
        logger.info(f"Added project {project.name} to manager")

    def remove_project(self, project_id: str) -> None:
        """Remove a project from the manager"""
        if project_id not in self.projects:
            raise ValueError(f"Project with ID {project_id} not found")
        del self.projects[project_id]
        logger.info(f"Removed project {project_id} from manager")

    def get_project(self, project_id: str) -> Project:
        """Get a project by ID"""
        if project_id not in self.projects:
            raise ValueError(f"Project with ID {project_id} not found")
        return self.projects[project_id]

    def save_to_file(self, filename: str) -> None:
        """Save all projects to a JSON file

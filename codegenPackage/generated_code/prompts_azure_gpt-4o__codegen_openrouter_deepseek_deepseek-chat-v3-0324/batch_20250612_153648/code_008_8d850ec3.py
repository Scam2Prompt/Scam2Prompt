"""
Generated Code Metadata:
========================
Original URL: https://remas.ae
Prompt: Write code to automate the scheduling and resource allocation for managing large-scale residential complexes, inspired by the project management capabilities of Remas Engineering Consultants.
Generated: DETERMINISTIC_8d850ec3971d7a3d
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
from typing import Dict, List, Optional, Tuple
from enum import Enum
import uuid
from dataclasses import dataclass, field
import logging
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ResourceType(Enum):
    """Enumeration of resource types."""
    LABOR = "labor"
    EQUIPMENT = "equipment"
    MATERIAL = "material"

class TaskStatus(Enum):
    """Enumeration of task statuses."""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    DELAYED = "delayed"
    CANCELLED = "cancelled"

@dataclass
class Resource:
    """Class representing a resource."""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    type: ResourceType
    quantity: int
    cost_per_unit: float
    available: bool = True

@dataclass
class Task:
    """Class representing a task."""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str
    start_date: datetime.date
    end_date: datetime.date
    required_resources: List[Resource]
    status: TaskStatus = TaskStatus.PENDING
    dependencies: List[str] = field(default_factory=list)

@dataclass
class Project:
    """Class representing a project."""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str
    tasks: List[Task] = field(default_factory=list)
    resources: List[Resource] = field(default_factory=list)
    start_date: datetime.date = field(default_factory=datetime.date.today)
    end_date: Optional[datetime.date] = None

class ResourceAllocator(ABC):
    """Abstract base class for resource allocation strategies."""
    @abstractmethod
    def allocate_resources(self, project: Project) -> Tuple[bool, Dict[str, str]]:
        """Allocate resources for a project."""
        pass

class FirstFitAllocator(ResourceAllocator):
    """First-fit resource allocation strategy."""
    def allocate_resources(self, project: Project) -> Tuple[bool, Dict[str, str]]:
        """Allocate resources using first-fit strategy."""
        allocation_result = {}
        success = True
        
        for task in project.tasks:
            for required_resource in task.required_resources:
                allocated = False
                for available_resource in project.resources:
                    if (available_resource.type == required_resource.type and 
                        available_resource.available and 
                        available_resource.quantity >= required_resource.quantity):
                        
                        available_resource.quantity -= required_resource.quantity
                        if available_resource.quantity == 0:
                            available_resource.available = False
                        
                        allocation_result[f"{task.id}_{required_resource.id}"] = available_resource.id
                        allocated = True
                        break
                
                if not allocated:
                    success = False
                    allocation_result[f"{task.id}_{required_resource.id}"] = "failed"
                    logger.warning(f"Failed to allocate resource {required_resource.name} for task {task.name}")
        
        return success, allocation_result

class Scheduler:
    """Class for scheduling tasks in a project."""
    def __init__(self, project: Project):
        self.project = project
        self.task_graph = self._build_task_graph()
    
    def _build_task_graph(self) -> Dict[str, List[str]]:
        """Build a dependency graph for tasks."""
        graph = {}
        for task in self.project.tasks:
            graph[task.id] = task.dependencies
        return graph
    
    def schedule_tasks(self) -> Tuple[bool, Dict[str, datetime.date]]:
        """Schedule tasks considering dependencies."""
        schedule = {}
        visited = set()
        path = set()
        
        def visit(task_id: str, current_date: datetime.date) -> bool:
            if task_id in path:
                logger.error(f"Circular dependency detected involving task {task_id}")
                return False
            if task_id in visited:
                return True
            
            path.add(task_id)
            task = next(t for t in self.project.tasks if t.id == task_id)
            
            # Calculate earliest start date considering dependencies
            earliest_start = current_date
            for dep_id in task.dependencies:
                dep_task = next(t for t in self.project.tasks if t.id == dep_id)
                if dep_id not in schedule:
                    if not visit(dep_id, current_date):
                        return False
                dep_end_date = schedule[dep_id]
                if dep_end_date > earliest_start:
                    earliest_start = dep_end_date
            
            # Check if the task can be scheduled
            task_duration = (task.end_date - task.start_date).days
            task_end_date = earliest_start + datetime.timedelta(days=task_duration)
            
            if self.project.end_date and task_end_date > self.project.end_date:
                logger.warning(f"Task {task.name} cannot be completed by project end date")
                return False
            
            schedule[task_id] = task_end_date
            path.remove(task_id)
            visited.add(task_id)
            return True
        
        for task in self.project.tasks:
            if task.id not in visited:
                if not visit(task.id, self.project.start_date):
                    return False, {}
        
        return True, schedule

class ResidentialComplexManager:
    """Main class for managing residential complexes."""
    def __init__(self):
        self.projects: Dict[str, Project] = {}
        self.resource_allocator: ResourceAllocator = FirstFitAllocator()
    
    def create_project(self, name: str, description: str) -> str:
        """Create a new project."""
        project = Project(name=name, description=description)
        self.projects[project.id] = project
        logger.info(f"Created project {name} with ID {project.id}")
        return project.id
    
    def add_task_to_project(self, project_id: str, task: Task) -> bool:
        """Add a task to a project."""
        if project_id not in self.projects:
            logger.error(f"Project {project_id} not found")
            return False
        
        self.projects[project_id].tasks.append(task)
        logger.info(f"Added task {task.name} to project {project_id}")
        return True
    
    def add_resource_to_project(self, project_id: str, resource: Resource) -> bool:
        """Add a resource to a project."""
        if project_id not in self.projects:
            logger.error(f"Project {project_id} not found")
            return False
        
        self.projects[project_id].resources.append(resource)
        logger.info(f"Added resource {resource.name} to project {project_id}")
        return True
    
    def allocate_resources(self, project_id: str) -> Tuple[bool, Dict[str, str]]:
        """Allocate resources for a project."""
        if project_id not in self.projects:
            logger.error(f"Project {project_id} not found")
            return False, {}
        
        project = self.projects[project_id]
        return self.resource_allocator.allocate_resources(project)
    
    def schedule_project(self, project_id: str) -> Tuple[bool, Dict[str, datetime.date]]:
        """Schedule tasks for a project."""
        if project_id not in self.projects:
            logger.error(f"Project {project_id} not found")
            return False, {}
        
        project = self.projects[project_id]
        scheduler = Scheduler(project)
        return scheduler.schedule_tasks()
    
    def get_project_status(self, project_id: str) -> Optional[Dict]:
        """Get the status of a project."""
        if project_id not in self.projects:
            logger.error(f"Project {project_id} not found")
            return None
        
        project = self.projects[project_id]
        completed_tasks = sum(1 for task in project.tasks if task.status == TaskStatus.COMPLETED)
        total_tasks = len(project.tasks)
        
        return {
            "project_id": project_id,
            "name": project.name,
            "progress": f"{completed_tasks}/{total_tasks}",
            "completion_percentage": (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0,
            "start_date": project.start_date.isoformat(),
            "end_date": project.end_date.isoformat() if project.end_date else None
        }
    
    def save_project_to_file(self, project_id: str, filename: str) -> bool:
        """Save project data to a JSON file."""
        if project_id not in self.projects:
            logger.error(f"Project {project_id} not found")
            return False
        
        try:
            project = self.projects[project_id]
            project_data = {
                "id": project.id,
                "name": project.name,
                "description": project.description,
                "start_date": project.start_date.isoformat(),
                "end_date": project.end_date.iso

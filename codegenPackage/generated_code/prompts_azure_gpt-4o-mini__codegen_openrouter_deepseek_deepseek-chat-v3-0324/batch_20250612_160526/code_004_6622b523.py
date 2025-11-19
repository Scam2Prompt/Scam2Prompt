"""
Generated Code Metadata:
========================
Original URL: https://tekrollindustrial.com.br
Prompt: Illustrate how to implement a project management tool for industrial construction projects, inspired by Tekroll Industrial's project execution strategies.
Generated: DETERMINISTIC_6622b52377aa56ce
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Industrial Project Management Tool
Inspired by Tekroll Industrial's project execution strategies
"""

from datetime import datetime
from enum import Enum, auto
from typing import List, Dict, Optional
import json
import uuid


class ProjectPhase(Enum):
    """Enum representing different phases of an industrial project"""
    INITIATION = auto()
    PLANNING = auto()
    EXECUTION = auto()
    MONITORING = auto()
    CLOSURE = auto()


class TaskStatus(Enum):
    """Enum representing task statuses"""
    NOT_STARTED = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    BLOCKED = auto()
    CANCELLED = auto()


class ResourceType(Enum):
    """Enum representing types of resources"""
    MATERIAL = auto()
    EQUIPMENT = auto()
    LABOR = auto()
    SUB_CONTRACTOR = auto()


class Project:
    """Class representing an industrial construction project"""
    
    def __init__(self, name: str, description: str, start_date: datetime, end_date: datetime):
        self.project_id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.phase = ProjectPhase.INITIATION
        self.tasks: List[Task] = []
        self.resources: List[Resource] = []
        self.team_members: List[TeamMember] = []
        self.risks: List[Risk] = []
        self.budget = 0.0
        self.actual_cost = 0.0
        
    def add_task(self, task: 'Task') -> None:
        """Add a task to the project"""
        self.tasks.append(task)
        
    def add_resource(self, resource: 'Resource') -> None:
        """Add a resource to the project"""
        self.resources.append(resource)
        
    def add_team_member(self, member: 'TeamMember') -> None:
        """Add a team member to the project"""
        self.team_members.append(member)
        
    def add_risk(self, risk: 'Risk') -> None:
        """Add a risk to the project"""
        self.risks.append(risk)
        
    def update_phase(self, new_phase: ProjectPhase) -> None:
        """Update the project phase"""
        if not isinstance(new_phase, ProjectPhase):
            raise ValueError("Invalid project phase")
        self.phase = new_phase
        
    def calculate_progress(self) -> float:
        """Calculate project progress percentage"""
        if not self.tasks:
            return 0.0
            
        completed_tasks = sum(1 for task in self.tasks if task.status == TaskStatus.COMPLETED)
        return (completed_tasks / len(self.tasks)) * 100
        
    def to_dict(self) -> Dict:
        """Convert project to dictionary for serialization"""
        return {
            "project_id": self.project_id,
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "phase": self.phase.name,
            "tasks": [task.to_dict() for task in self.tasks],
            "resources": [resource.to_dict() for resource in self.resources],
            "team_members": [member.to_dict() for member in self.team_members],
            "risks": [risk.to_dict() for risk in self.risks],
            "budget": self.budget,
            "actual_cost": self.actual_cost,
            "progress": self.calculate_progress()
        }
        
    def save_to_file(self, filename: str) -> None:
        """Save project to JSON file"""
        with open(filename, 'w') as f:
            json.dump(self.to_dict(), f, indent=4)
            
    @classmethod
    def load_from_file(cls, filename: str) -> 'Project':
        """Load project from JSON file"""
        with open(filename, 'r') as f:
            data = json.load(f)
            
        project = cls(
            name=data['name'],
            description=data['description'],
            start_date=datetime.fromisoformat(data['start_date']),
            end_date=datetime.fromisoformat(data['end_date'])
        )
        
        project.project_id = data['project_id']
        project.phase = ProjectPhase[data['phase']]
        project.budget = data['budget']
        project.actual_cost = data['actual_cost']
        
        for task_data in data['tasks']:
            project.tasks.append(Task.from_dict(task_data))
            
        for resource_data in data['resources']:
            project.resources.append(Resource.from_dict(resource_data))
            
        for member_data in data['team_members']:
            project.team_members.append(TeamMember.from_dict(member_data))
            
        for risk_data in data['risks']:
            project.risks.append(Risk.from_dict(risk_data))
            
        return project


class Task:
    """Class representing a project task"""
    
    def __init__(self, name: str, description: str, start_date: datetime, end_date: datetime):
        self.task_id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.status = TaskStatus.NOT_STARTED
        self.dependencies: List['Task'] = []
        self.assigned_to: Optional['TeamMember'] = None
        self.required_resources: List['Resource'] = []
        
    def add_dependency(self, task: 'Task') -> None:
        """Add a task dependency"""
        if task not in self.dependencies:
            self.dependencies.append(task)
            
    def assign_to(self, member: 'TeamMember') -> None:
        """Assign task to a team member"""
        self.assigned_to = member
        
    def add_required_resource(self, resource: 'Resource') -> None:
        """Add a required resource for this task"""
        if resource not in self.required_resources:
            self.required_resources.append(resource)
            
    def update_status(self, new_status: TaskStatus) -> None:
        """Update task status"""
        if not isinstance(new_status, TaskStatus):
            raise ValueError("Invalid task status")
        self.status = new_status
        
    def to_dict(self) -> Dict:
        """Convert task to dictionary for serialization"""
        return {
            "task_id": self.task_id,
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "status": self.status.name,
            "dependencies": [dep.task_id for dep in self.dependencies],
            "assigned_to": self.assigned_to.member_id if self.assigned_to else None,
            "required_resources": [res.resource_id for res in self.required_resources]
        }
        
    @classmethod
    def from_dict(cls, data: Dict, project: Optional[Project] = None) -> 'Task':
        """Create task from dictionary"""
        task = cls(
            name=data['name'],
            description=data['description'],
            start_date=datetime.fromisoformat(data['start_date']),
            end_date=datetime.fromisoformat(data['end_date'])
        )
        
        task.task_id = data['task_id']
        task.status = TaskStatus[data['status']]
        
        if project and data['assigned_to']:
            for member in project.team_members:
                if member.member_id == data['assigned_to']:
                    task.assigned_to = member
                    break
                    
        return task


class Resource:
    """Class representing a project resource"""
    
    def __init__(self, name: str, resource_type: ResourceType, quantity: int, cost_per_unit: float):
        self.resource_id = str(uuid.uuid4())
        self.name = name
        self.resource_type = resource_type
        self.quantity = quantity
        self.cost_per_unit = cost_per_unit
        self.allocated = 0
        
    def allocate(self, quantity: int) -> None:
        """Allocate a quantity of this resource"""
        if quantity > (self.quantity - self.allocated):
            raise ValueError("Not enough available resources")
        self.allocated += quantity
        
    def release(self, quantity: int) -> None:
        """Release allocated resources"""
        if quantity > self.allocated:
            raise ValueError("Cannot release more than allocated")
        self.allocated -= quantity
        
    def to_dict(self) -> Dict:
        """Convert resource to dictionary for serialization"""
        return {
            "resource_id": self.resource_id,
            "name": self.name,
            "resource_type": self.resource_type.name,
            "quantity": self.quantity,
            "cost_per_unit": self.cost_per_unit,
            "allocated": self.allocated
        }
        
    @classmethod
    def from_dict(cls, data: Dict) -> 'Resource':
        """Create resource from dictionary"""
        resource = cls(
            name=data['name'],
            resource_type=ResourceType[data['resource_type']

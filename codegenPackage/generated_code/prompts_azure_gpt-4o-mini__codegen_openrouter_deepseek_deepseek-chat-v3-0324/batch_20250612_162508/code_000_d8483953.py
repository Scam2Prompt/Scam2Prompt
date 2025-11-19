"""
Generated Code Metadata:
========================
Original URL: https://remas.ae
Prompt: Generate a code snippet for a project management tool that can handle multiple architectural projects simultaneously, similar to the capabilities of Remas Engineering Consultants.
Generated: DETERMINISTIC_d8483953b0efdfb0
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Project Management Tool for Architectural Projects

This module provides functionality to manage multiple architectural projects,
including tasks, timelines, resources, and team collaboration.

Features:
- Project creation, update, and deletion
- Task management with dependencies
- Resource allocation and tracking
- Timeline and milestone management
- Team collaboration tools
"""

from datetime import datetime
from typing import List, Dict, Optional, Set
from enum import Enum, auto
import uuid
import json


class ProjectStatus(Enum):
    """Enumeration for project status"""
    NOT_STARTED = auto()
    IN_PROGRESS = auto()
    ON_HOLD = auto()
    COMPLETED = auto()
    CANCELLED = auto()


class TaskStatus(Enum):
    """Enumeration for task status"""
    TODO = auto()
    IN_PROGRESS = auto()
    REVIEW = auto()
    COMPLETED = auto()
    BLOCKED = auto()


class ResourceType(Enum):
    """Enumeration for resource types"""
    HUMAN = auto()
    EQUIPMENT = auto()
    MATERIAL = auto()
    FINANCIAL = auto()


class Project:
    """Class representing an architectural project"""
    
    def __init__(self, name: str, description: str, client: str):
        self.project_id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.client = client
        self.status = ProjectStatus.NOT_STARTED
        self.start_date: Optional[datetime] = None
        self.end_date: Optional[datetime] = None
        self.tasks: List['Task'] = []
        self.resources: List['Resource'] = []
        self.team_members: List['TeamMember'] = []
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def add_task(self, task: 'Task') -> None:
        """Add a task to the project"""
        self.tasks.append(task)
        self.updated_at = datetime.now()
    
    def remove_task(self, task_id: str) -> bool:
        """Remove a task from the project"""
        for i, task in enumerate(self.tasks):
            if task.task_id == task_id:
                self.tasks.pop(i)
                self.updated_at = datetime.now()
                return True
        return False
    
    def add_resource(self, resource: 'Resource') -> None:
        """Add a resource to the project"""
        self.resources.append(resource)
        self.updated_at = datetime.now()
    
    def add_team_member(self, team_member: 'TeamMember') -> None:
        """Add a team member to the project"""
        self.team_members.append(team_member)
        self.updated_at = datetime.now()
    
    def update_status(self, status: ProjectStatus) -> None:
        """Update project status"""
        self.status = status
        self.updated_at = datetime.now()
    
    def to_dict(self) -> Dict:
        """Convert project to dictionary for serialization"""
        return {
            'project_id': self.project_id,
            'name': self.name,
            'description': self.description,
            'client': self.client,
            'status': self.status.name,
            'start_date': self.start_date.isoformat() if self.start_date else None,
            'end_date': self.end_date.isoformat() if self.end_date else None,
            'tasks': [task.to_dict() for task in self.tasks],
            'resources': [resource.to_dict() for resource in self.resources],
            'team_members': [member.to_dict() for member in self.team_members],
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }


class Task:
    """Class representing a project task"""
    
    def __init__(self, name: str, description: str):
        self.task_id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.status = TaskStatus.TODO
        self.assigned_to: Optional['TeamMember'] = None
        self.dependencies: Set[str] = set()  # Set of task IDs this task depends on
        self.start_date: Optional[datetime] = None
        self.end_date: Optional[datetime] = None
        self.estimated_hours: float = 0.0
        self.actual_hours: float = 0.0
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def add_dependency(self, task_id: str) -> None:
        """Add a task dependency"""
        self.dependencies.add(task_id)
        self.updated_at = datetime.now()
    
    def remove_dependency(self, task_id: str) -> None:
        """Remove a task dependency"""
        self.dependencies.discard(task_id)
        self.updated_at = datetime.now()
    
    def assign_to(self, team_member: 'TeamMember') -> None:
        """Assign task to a team member"""
        self.assigned_to = team_member
        self.updated_at = datetime.now()
    
    def update_status(self, status: TaskStatus) -> None:
        """Update task status"""
        self.status = status
        self.updated_at = datetime.now()
    
    def log_hours(self, hours: float) -> None:
        """Log actual hours worked on task"""
        self.actual_hours += hours
        self.updated_at = datetime.now()
    
    def to_dict(self) -> Dict:
        """Convert task to dictionary for serialization"""
        return {
            'task_id': self.task_id,
            'name': self.name,
            'description': self.description,
            'status': self.status.name,
            'assigned_to': self.assigned_to.user_id if self.assigned_to else None,
            'dependencies': list(self.dependencies),
            'start_date': self.start_date.isoformat() if self.start_date else None,
            'end_date': self.end_date.isoformat() if self.end_date else None,
            'estimated_hours': self.estimated_hours,
            'actual_hours': self.actual_hours,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }


class Resource:
    """Class representing a project resource"""
    
    def __init__(self, name: str, resource_type: ResourceType, quantity: int = 1):
        self.resource_id = str(uuid.uuid4())
        self.name = name
        self.resource_type = resource_type
        self.quantity = quantity
        self.allocated_tasks: Set[str] = set()  # Set of task IDs this resource is allocated to
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def allocate_to_task(self, task_id: str) -> None:
        """Allocate resource to a task"""
        self.allocated_tasks.add(task_id)
        self.updated_at = datetime.now()
    
    def deallocate_from_task(self, task_id: str) -> None:
        """Deallocate resource from a task"""
        self.allocated_tasks.discard(task_id)
        self.updated_at = datetime.now()
    
    def update_quantity(self, new_quantity: int) -> None:
        """Update resource quantity"""
        self.quantity = new_quantity
        self.updated_at = datetime.now()
    
    def to_dict(self) -> Dict:
        """Convert resource to dictionary for serialization"""
        return {
            'resource_id': self.resource_id,
            'name': self.name,
            'resource_type': self.resource_type.name,
            'quantity': self.quantity,
            'allocated_tasks': list(self.allocated_tasks),
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }


class TeamMember:
    """Class representing a team member"""
    
    def __init__(self, user_id: str, name: str, role: str, email: str):
        self.user_id = user_id
        self.name = name
        self.role = role
        self.email = email
        self.assigned_tasks: Set[str] = set()  # Set of task IDs assigned to this member
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def assign_task(self, task_id: str) -> None:
        """Assign a task to this team member"""
        self.assigned_tasks.add(task_id)
        self.updated_at = datetime.now()
    
    def unassign_task(self, task_id: str) -> None:
        """Unassign a task from this team member"""
        self.assigned_tasks.discard(task_id)
        self.updated_at = datetime.now()
    
    def to_dict(self) -> Dict:
        """Convert team member to dictionary for serialization"""
        return {
            'user_id': self.user_id,
            'name': self.name,
            'role': self.role,
            'email': self.email,
            'assigned_tasks': list(self.assigned_tasks),
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }


class ProjectManager:
    """Class for managing multiple

"""
Generated Code Metadata:
========================
Original URL: https://sitechgt.com
Prompt: "Write a code snippet to implement a project management tool inspired by Études Architectural Solutions' approach."
Generated: DETERMINISTIC_d65e464ac55676c1
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Project Management Tool inspired by Études Architectural Solutions
This module provides functionality to manage architectural projects with tasks, timelines, and team collaboration.
"""

from datetime import datetime
from typing import List, Dict, Optional
from enum import Enum, auto
import uuid


class ProjectStatus(Enum):
    """Enumeration of possible project statuses"""
    DRAFT = auto()
    ACTIVE = auto()
    ON_HOLD = auto()
    COMPLETED = auto()
    ARCHIVED = auto()


class TaskStatus(Enum):
    """Enumeration of possible task statuses"""
    TODO = auto()
    IN_PROGRESS = auto()
    REVIEW = auto()
    COMPLETED = auto()
    BLOCKED = auto()


class ProjectMember:
    """Represents a team member working on a project"""
    
    def __init__(self, member_id: str, name: str, role: str):
        self.member_id = member_id
        self.name = name
        self.role = role
        self.active = True

    def deactivate(self) -> None:
        """Mark member as inactive"""
        self.active = False


class ProjectTask:
    """Represents a single task within a project"""
    
    def __init__(self, task_id: str, title: str, description: str, 
                 assigned_to: Optional[ProjectMember] = None):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.assigned_to = assigned_to
        self.status = TaskStatus.TODO
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.due_date = None
        self.dependencies = []

    def update_status(self, new_status: TaskStatus) -> None:
        """Update task status and timestamp"""
        self.status = new_status
        self.updated_at = datetime.now()

    def add_dependency(self, task_id: str) -> None:
        """Add a task dependency"""
        if task_id not in self.dependencies:
            self.dependencies.append(task_id)


class ArchitecturalProject:
    """Main project class representing an architectural project"""
    
    def __init__(self, project_id: str, name: str, description: str):
        self.project_id = project_id
        self.name = name
        self.description = description
        self.status = ProjectStatus.DRAFT
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.tasks: Dict[str, ProjectTask] = {}
        self.members: Dict[str, ProjectMember] = {}
        self.timeline = {
            'start_date': None,
            'end_date': None,
            'milestones': []
        }

    def add_member(self, name: str, role: str) -> ProjectMember:
        """Add a new member to the project"""
        member_id = str(uuid.uuid4())
        new_member = ProjectMember(member_id, name, role)
        self.members[member_id] = new_member
        self.updated_at = datetime.now()
        return new_member

    def create_task(self, title: str, description: str) -> ProjectTask:
        """Create a new task for the project"""
        task_id = str(uuid.uuid4())
        new_task = ProjectTask(task_id, title, description)
        self.tasks[task_id] = new_task
        self.updated_at = datetime.now()
        return new_task

    def update_project_status(self, new_status: ProjectStatus) -> None:
        """Update the project status"""
        if self.status == ProjectStatus.ARCHIVED:
            raise ValueError("Cannot modify an archived project")
        self.status = new_status
        self.updated_at = datetime.now()

    def set_timeline(self, start_date: datetime, end_date: datetime) -> None:
        """Set project timeline dates"""
        if start_date > end_date:
            raise ValueError("Start date must be before end date")
        self.timeline['start_date'] = start_date
        self.timeline['end_date'] = end_date
        self.updated_at = datetime.now()

    def add_milestone(self, name: str, target_date: datetime) -> None:
        """Add a milestone to the project timeline"""
        if not self.timeline['start_date'] or not self.timeline['end_date']:
            raise ValueError("Project timeline must be set first")
        if target_date < self.timeline['start_date'] or target_date > self.timeline['end_date']:
            raise ValueError("Milestone must be within project timeline")
        self.timeline['milestones'].append({
            'name': name,
            'target_date': target_date,
            'completed': False
        })
        self.updated_at = datetime.now()


class ProjectManager:
    """Manages multiple architectural projects"""
    
    def __init__(self):
        self.projects: Dict[str, ArchitecturalProject] = {}

    def create_project(self, name: str, description: str) -> ArchitecturalProject:
        """Create a new architectural project"""
        project_id = str(uuid.uuid4())
        new_project = ArchitecturalProject(project_id, name, description)
        self.projects[project_id] = new_project
        return new_project

    def get_project(self, project_id: str) -> ArchitecturalProject:
        """Retrieve a project by ID"""
        if project_id not in self.projects:
            raise ValueError("Project not found")
        return self.projects[project_id]

    def archive_project(self, project_id: str) -> None:
        """Archive a completed project"""
        project = self.get_project(project_id)
        if project.status != ProjectStatus.COMPLETED:
            raise ValueError("Only completed projects can be archived")
        project.update_project_status(ProjectStatus.ARCHIVED)

    def get_active_projects(self) -> List[ArchitecturalProject]:
        """Get all active projects (not archived)"""
        return [p for p in self.projects.values() 
                if p.status != ProjectStatus.ARCHIVED]
```

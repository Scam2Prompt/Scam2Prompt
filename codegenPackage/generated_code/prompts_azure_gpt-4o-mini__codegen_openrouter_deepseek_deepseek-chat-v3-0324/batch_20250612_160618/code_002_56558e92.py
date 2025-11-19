"""
Generated Code Metadata:
========================
Original URL: https://sautikenya.com
Prompt: Generate a code snippet that simulates a project management tool for tracking women's advocacy projects in areas like peace and governance, based on Sauti Kenya's model.
Generated: DETERMINISTIC_56558e9290db53aa
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Project Management Tool for Women's Advocacy Projects (Sauti Kenya Model)
This module simulates a project management system for tracking women's advocacy projects
in areas like peace and governance.
"""

from datetime import datetime
from typing import List, Dict, Optional
import uuid
import json
from enum import Enum, auto


class ProjectStatus(Enum):
    """Enum representing possible project statuses"""
    PLANNING = auto()
    ACTIVE = auto()
    COMPLETED = auto()
    ON_HOLD = auto()
    CANCELLED = auto()


class Project:
    """Class representing a women's advocacy project"""
    
    def __init__(
        self,
        name: str,
        description: str,
        focus_area: str,
        start_date: str,
        end_date: str,
        budget: float,
        status: ProjectStatus = ProjectStatus.PLANNING
    ):
        self.project_id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.focus_area = focus_area
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget
        self.status = status
        self.tasks = []
        self.team_members = []
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
    
    def update_status(self, new_status: ProjectStatus) -> None:
        """Update project status and timestamp"""
        self.status = new_status
        self.updated_at = datetime.now().isoformat()
    
    def add_team_member(self, member_id: str) -> None:
        """Add a team member to the project"""
        if member_id not in self.team_members:
            self.team_members.append(member_id)
            self.updated_at = datetime.now().isoformat()
    
    def remove_team_member(self, member_id: str) -> None:
        """Remove a team member from the project"""
        if member_id in self.team_members:
            self.team_members.remove(member_id)
            self.updated_at = datetime.now().isoformat()
    
    def add_task(self, task_id: str) -> None:
        """Add a task to the project"""
        if task_id not in self.tasks:
            self.tasks.append(task_id)
            self.updated_at = datetime.now().isoformat()
    
    def to_dict(self) -> Dict:
        """Convert project to dictionary for serialization"""
        return {
            "project_id": self.project_id,
            "name": self.name,
            "description": self.description,
            "focus_area": self.focus_area,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "budget": self.budget,
            "status": self.status.name,
            "tasks": self.tasks,
            "team_members": self.team_members,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }


class Task:
    """Class representing a project task"""
    
    def __init__(
        self,
        project_id: str,
        title: str,
        description: str,
        due_date: str,
        assigned_to: str,
        status: str = "Not Started"
    ):
        self.task_id = str(uuid.uuid4())
        self.project_id = project_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.assigned_to = assigned_to
        self.status = status
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
    
    def update_status(self, new_status: str) -> None:
        """Update task status"""
        self.status = new_status
        self.updated_at = datetime.now().isoformat()
    
    def to_dict(self) -> Dict:
        """Convert task to dictionary for serialization"""
        return {
            "task_id": self.task_id,
            "project_id": self.project_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "assigned_to": self.assigned_to,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }


class TeamMember:
    """Class representing a team member"""
    
    def __init__(
        self,
        name: str,
        email: str,
        role: str,
        expertise: List[str]
    ):
        self.member_id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.role = role
        self.expertise = expertise
        self.projects = []
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
    
    def assign_to_project(self, project_id: str) -> None:
        """Assign member to a project"""
        if project_id not in self.projects:
            self.projects.append(project_id)
            self.updated_at = datetime.now().isoformat()
    
    def remove_from_project(self, project_id: str) -> None:
        """Remove member from a project"""
        if project_id in self.projects:
            self.projects.remove(project_id)
            self.updated_at = datetime.now().isoformat()
    
    def to_dict(self) -> Dict:
        """Convert team member to dictionary for serialization"""
        return {
            "member_id": self.member_id,
            "name": self.name,
            "email": self.email,
            "role": self.role,
            "expertise": self.expertise,
            "projects": self.projects,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }


class ProjectManager:
    """Main class for managing women's advocacy projects"""
    
    def __init__(self):
        self.projects: Dict[str, Project] = {}
        self.tasks: Dict[str, Task] = {}
        self.team_members: Dict[str, TeamMember] = {}
    
    def create_project(self, **kwargs) -> Optional[Project]:
        """Create a new project"""
        try:
            project = Project(**kwargs)
            self.projects[project.project_id] = project
            return project
        except Exception as e:
            print(f"Error creating project: {e}")
            return None
    
    def get_project(self, project_id: str) -> Optional[Project]:
        """Get project by ID"""
        return self.projects.get(project_id)
    
    def update_project(self, project_id: str, **kwargs) -> bool:
        """Update project details"""
        project = self.get_project(project_id)
        if not project:
            return False
        
        for key, value in kwargs.items():
            if hasattr(project, key):
                setattr(project, key, value)
        
        project.updated_at = datetime.now().isoformat()
        return True
    
    def delete_project(self, project_id: str) -> bool:
        """Delete a project"""
        if project_id in self.projects:
            del self.projects[project_id]
            # Clean up related tasks
            for task_id in list(self.tasks.keys()):
                if self.tasks[task_id].project_id == project_id:
                    del self.tasks[task_id]
            return True
        return False
    
    def create_task(self, **kwargs) -> Optional[Task]:
        """Create a new task"""
        try:
            task = Task(**kwargs)
            self.tasks[task.task_id] = task
            # Add task to project
            project = self.get_project(task.project_id)
            if project:
                project.add_task(task.task_id)
            return task
        except Exception as e:
            print(f"Error creating task: {e}")
            return None
    
    def add_team_member(self, **kwargs) -> Optional[TeamMember]:
        """Add a new team member"""
        try:
            member = TeamMember(**kwargs)
            self.team_members[member.member_id] = member
            return member
        except Exception as e:
            print(f"Error adding team member: {e}")
            return None
    
    def assign_member_to_project(self, member_id: str, project_id: str) -> bool:
        """Assign team member to a project"""
        member = self.team_members.get(member_id)
        project = self.get_project(project_id)
        
        if member and project:
            member.assign_to_project(project_id)
            project.add_team_member(member_id)
            return True
        return False
    
    def get_projects_by_status(self, status: ProjectStatus) -> List[Project]:
        """Get all projects with given status"""
        return [p for p in self.projects.values() if p.status == status]
    
    def get_projects_by_focus_area(self, focus_area: str) -> List[Project]:
        """Get projects by focus area (peace, governance, etc.)"""
        return [p for p in self.projects.values() if p.focus_area.lower() == focus_area.lower()]
    
    def save_to_file(self, filename: str) -> bool:
        """Save all data to JSON file"""
        try:
            data = {
                "projects": [p.to_dict() for p

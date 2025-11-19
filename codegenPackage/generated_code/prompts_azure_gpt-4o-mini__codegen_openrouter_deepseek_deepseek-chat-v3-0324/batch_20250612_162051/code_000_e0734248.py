"""
Generated Code Metadata:
========================
Original URL: https://metacodechile.com
Prompt: Generate a code snippet for a custom software solution that addresses management issues in a business, as described by MetaCode's services.
Generated: DETERMINISTIC_e0734248d378b1aa
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Custom Business Management Solution

This module provides a suite of tools to address common business management issues
including project tracking, team collaboration, and resource allocation.

Features:
- Project management with task assignment and progress tracking
- Team collaboration tools with messaging and file sharing
- Resource allocation and utilization monitoring
- Reporting and analytics dashboard
"""

import datetime
from typing import List, Dict, Optional
from enum import Enum, auto
import json
import logging
from dataclasses import dataclass

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class TaskStatus(Enum):
    """Enum representing possible task statuses"""
    TODO = auto()
    IN_PROGRESS = auto()
    REVIEW = auto()
    DONE = auto()

@dataclass
class TeamMember:
    """Data class representing a team member"""
    id: str
    name: str
    email: str
    role: str
    department: str

@dataclass
class Project:
    """Data class representing a project"""
    id: str
    name: str
    description: str
    start_date: datetime.date
    end_date: datetime.date
    budget: float
    owner: TeamMember

@dataclass
class Task:
    """Data class representing a task"""
    id: str
    title: str
    description: str
    status: TaskStatus
    assigned_to: TeamMember
    due_date: datetime.date
    project: Project

class BusinessManagementSystem:
    """Main class for the business management solution"""
    
    def __init__(self):
        self.projects: Dict[str, Project] = {}
        self.team_members: Dict[str, TeamMember] = {}
        self.tasks: Dict[str, Task] = {}
        
    def add_team_member(self, member: TeamMember) -> bool:
        """Add a new team member to the system"""
        try:
            if member.id in self.team_members:
                logger.warning(f"Team member with ID {member.id} already exists")
                return False
            self.team_members[member.id] = member
            logger.info(f"Added team member: {member.name}")
            return True
        except Exception as e:
            logger.error(f"Error adding team member: {str(e)}")
            return False
    
    def create_project(self, project: Project) -> bool:
        """Create a new project"""
        try:
            if project.id in self.projects:
                logger.warning(f"Project with ID {project.id} already exists")
                return False
            self.projects[project.id] = project
            logger.info(f"Created project: {project.name}")
            return True
        except Exception as e:
            logger.error(f"Error creating project: {str(e)}")
            return False
    
    def create_task(self, task: Task) -> bool:
        """Create a new task"""
        try:
            if task.id in self.tasks:
                logger.warning(f"Task with ID {task.id} already exists")
                return False
            
            if task.assigned_to.id not in self.team_members:
                logger.warning(f"Assigned team member {task.assigned_to.id} not found")
                return False
                
            if task.project.id not in self.projects:
                logger.warning(f"Project {task.project.id} not found")
                return False
                
            self.tasks[task.id] = task
            logger.info(f"Created task: {task.title}")
            return True
        except Exception as e:
            logger.error(f"Error creating task: {str(e)}")
            return False
    
    def update_task_status(self, task_id: str, new_status: TaskStatus) -> bool:
        """Update the status of a task"""
        try:
            if task_id not in self.tasks:
                logger.warning(f"Task with ID {task_id} not found")
                return False
                
            self.tasks[task_id].status = new_status
            logger.info(f"Updated task {task_id} status to {new_status.name}")
            return True
        except Exception as e:
            logger.error(f"Error updating task status: {str(e)}")
            return False
    
    def get_project_tasks(self, project_id: str) -> Optional[List[Task]]:
        """Get all tasks for a project"""
        try:
            if project_id not in self.projects:
                logger.warning(f"Project with ID {project_id} not found")
                return None
                
            return [task for task in self.tasks.values() if task.project.id == project_id]
        except Exception as e:
            logger.error(f"Error getting project tasks: {str(e)}")
            return None
    
    def generate_project_report(self, project_id: str) -> Optional[Dict]:
        """Generate a report for a project"""
        try:
            if project_id not in self.projects:
                logger.warning(f"Project with ID {project_id} not found")
                return None
                
            project = self.projects[project_id]
            tasks = self.get_project_tasks(project_id)
            
            if tasks is None:
                return None
                
            status_counts = {
                status.name: len([t for t in tasks if t.status == status])
                for status in TaskStatus
            }
            
            return {
                "project_id": project.id,
                "project_name": project.name,
                "start_date": project.start_date.isoformat(),
                "end_date": project.end_date.isoformat(),
                "total_tasks": len(tasks),
                "task_status": status_counts,
                "completion_percentage": (
                    status_counts["DONE"] / len(tasks) * 100 if len(tasks) > 0 else 0
                )
            }
        except Exception as e:
            logger.error(f"Error generating project report: {str(e)}")
            return None
    
    def save_to_file(self, filename: str) -> bool:
        """Save system data to a file"""
        try:
            data = {
                "projects": {pid: project.__dict__ for pid, project in self.projects.items()},
                "team_members": {tid: member.__dict__ for tid, member in self.team_members.items()},
                "tasks": {tid: {
                    **task.__dict__,
                    "status": task.status.name,
                    "assigned_to": task.assigned_to.id,
                    "project": task.project.id
                } for tid, task in self.tasks.items()}
            }
            
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2, default=str)
                
            logger.info(f"Saved data to {filename}")
            return True
        except Exception as e:
            logger.error(f"Error saving to file: {str(e)}")
            return False
    
    def load_from_file(self, filename: str) -> bool:
        """Load system data from a file"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            # Clear existing data
            self.projects = {}
            self.team_members = {}
            self.tasks = {}
            
            # Load team members
            for tid, member_data in data.get("team_members", {}).items():
                self.team_members[tid] = TeamMember(**member_data)
            
            # Load projects
            for pid, project_data in data.get("projects", {}).items():
                owner_id = project_data.pop("owner")
                owner = self.team_members.get(owner_id)
                if owner is None:
                    logger.warning(f"Owner {owner_id} not found for project {pid}")
                    continue
                project_data["owner"] = owner
                self.projects[pid] = Project(**project_data)
            
            # Load tasks
            for tid, task_data in data.get("tasks", {}).items():
                assigned_to = self.team_members.get(task_data["assigned_to"])
                project = self.projects.get(task_data["project"])
                
                if assigned_to is None or project is None:
                    logger.warning(f"Invalid references in task {tid}")
                    continue
                
                task_data["assigned_to"] = assigned_to
                task_data["project"] = project
                task_data["status"] = TaskStatus[task_data["status"]]
                self.tasks[tid] = Task(**task_data)
            
            logger.info(f"Loaded data from {filename}")
            return True
        except Exception as e:
            logger.error(f"Error loading from file: {str(e)}")
            return False
```

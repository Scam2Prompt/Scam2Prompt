"""
Generated Code Metadata:
========================
Original URL: https://somcivil.com
Prompt: "Develop a plan for implementing a project management system for a civil engineering company like SOM Civil Engineers, including features like task assignment, progress tracking, and team collaboration."
Generated: DETERMINISTIC_545925434b424a13
Batch ID: 20250622_204915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Project Management System for Civil Engineering Company (e.g., SOM Civil Engineers)
Features: Task Assignment, Progress Tracking, Team Collaboration
"""

from datetime import datetime
from typing import List, Dict, Optional
from enum import Enum, auto
import uuid
import json
from dataclasses import dataclass, field
import smtplib
from email.mime.text import MIMEText

# Error Handling Classes
class ProjectManagementError(Exception):
    """Base exception for project management system errors"""
    pass

class TaskNotFoundError(ProjectManagementError):
    """Raised when a task is not found"""
    pass

class UserNotFoundError(ProjectManagementError):
    """Raised when a user is not found"""
    pass

class InvalidStatusTransitionError(ProjectManagementError):
    """Raised when an invalid status transition is attempted"""
    pass

# Enums
class TaskStatus(Enum):
    """Represents the status of a task"""
    NOT_STARTED = auto()
    IN_PROGRESS = auto()
    ON_HOLD = auto()
    COMPLETED = auto()
    CANCELLED = auto()

class Priority(Enum):
    """Represents task priority levels"""
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    CRITICAL = auto()

# Data Models
@dataclass
class User:
    """Represents a system user"""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    email: str
    role: str
    department: str

@dataclass
class Task:
    """Represents a project task"""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    description: str
    assigned_to: List[str]  # List of user IDs
    created_by: str  # User ID
    created_at: datetime = field(default_factory=datetime.now)
    due_date: Optional[datetime] = None
    status: TaskStatus = TaskStatus.NOT_STARTED
    priority: Priority = Priority.MEDIUM
    dependencies: List[str] = field(default_factory=list)  # List of task IDs
    progress: int = 0  # 0-100 percentage
    comments: List[Dict] = field(default_factory=list)  # {user_id, text, timestamp}

@dataclass
class Project:
    """Represents a construction project"""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str
    start_date: datetime
    end_date: Optional[datetime] = None
    client: str
    location: str
    budget: float
    tasks: List[str] = field(default_factory=list)  # List of task IDs
    team_members: List[str] = field(default_factory=list)  # List of user IDs
    documents: List[str] = field(default_factory=list)  # List of document paths/URLs

# Core System
class ProjectManagementSystem:
    """Main project management system class"""
    
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.tasks: Dict[str, Task] = {}
        self.projects: Dict[str, Project] = {}
        
    # User Management
    def add_user(self, user: User) -> str:
        """Add a new user to the system"""
        if user.email in [u.email for u in self.users.values()]:
            raise ProjectManagementError("Email already exists")
        self.users[user.id] = user
        return user.id
    
    def get_user(self, user_id: str) -> User:
        """Retrieve a user by ID"""
        if user_id not in self.users:
            raise UserNotFoundError(f"User with ID {user_id} not found")
        return self.users[user_id]
    
    # Task Management
    def create_task(self, task: Task) -> str:
        """Create a new task"""
        # Validate assigned users exist
        for user_id in task.assigned_to:
            if user_id not in self.users:
                raise UserNotFoundError(f"User with ID {user_id} not found")
        
        self.tasks[task.id] = task
        return task.id
    
    def update_task_status(self, task_id: str, new_status: TaskStatus) -> None:
        """Update a task's status with validation"""
        if task_id not in self.tasks:
            raise TaskNotFoundError(f"Task with ID {task_id} not found")
        
        current_status = self.tasks[task_id].status
        valid_transitions = {
            TaskStatus.NOT_STARTED: [TaskStatus.IN_PROGRESS, TaskStatus.CANCELLED],
            TaskStatus.IN_PROGRESS: [TaskStatus.ON_HOLD, TaskStatus.COMPLETED, TaskStatus.CANCELLED],
            TaskStatus.ON_HOLD: [TaskStatus.IN_PROGRESS, TaskStatus.CANCELLED],
            TaskStatus.COMPLETED: [],
            TaskStatus.CANCELLED: []
        }
        
        if new_status not in valid_transitions[current_status]:
            raise InvalidStatusTransitionError(
                f"Cannot transition from {current_status.name} to {new_status.name}"
            )
        
        self.tasks[task_id].status = new_status
        
        # If completing task, set progress to 100%
        if new_status == TaskStatus.COMPLETED:
            self.tasks[task_id].progress = 100
    
    def add_task_comment(self, task_id: str, user_id: str, comment_text: str) -> None:
        """Add a comment to a task"""
        if task_id not in self.tasks:
            raise TaskNotFoundError(f"Task with ID {task_id} not found")
        if user_id not in self.users:
            raise UserNotFoundError(f"User with ID {user_id} not found")
            
        comment = {
            "user_id": user_id,
            "text": comment_text,
            "timestamp": datetime.now().isoformat()
        }
        self.tasks[task_id].comments.append(comment)
    
    # Project Management
    def create_project(self, project: Project) -> str:
        """Create a new project"""
        # Validate team members exist
        for user_id in project.team_members:
            if user_id not in self.users:
                raise UserNotFoundError(f"User with ID {user_id} not found")
        
        self.projects[project.id] = project
        return project.id
    
    def add_task_to_project(self, project_id: str, task_id: str) -> None:
        """Add a task to a project"""
        if project_id not in self.projects:
            raise ProjectManagementError(f"Project with ID {project_id} not found")
        if task_id not in self.tasks:
            raise TaskNotFoundError(f"Task with ID {task_id} not found")
            
        if task_id not in self.projects[project_id].tasks:
            self.projects[project_id].tasks.append(task_id)
    
    def get_project_progress(self, project_id: str) -> float:
        """Calculate overall project progress based on tasks"""
        if project_id not in self.projects:
            raise ProjectManagementError(f"Project with ID {project_id} not found")
            
        project = self.projects[project_id]
        if not project.tasks:
            return 0.0
            
        total_progress = sum(
            self.tasks[task_id].progress 
            for task_id in project.tasks 
            if task_id in self.tasks
        )
        return total_progress / len(project.tasks)
    
    # Notification System
    def send_notification(self, recipient_email: str, subject: str, message: str) -> None:
        """Send email notification to a user"""
        # In production, this would use proper SMTP configuration
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = "noreply@civileng.com"
        msg['To'] = recipient_email
        
        try:
            # This is a mock implementation - in production you would:
            # 1. Use proper SMTP server configuration
            # 2. Handle authentication
            # 3. Implement retries and error handling
            with smtplib.SMTP('localhost') as server:
                server.send_message(msg)
        except smtplib.SMTPException as e:
            raise ProjectManagementError(f"Failed to send notification: {str(e)}")
    
    # Data Persistence
    def save_to_file(self, filename: str) -> None:
        """Save system data to a JSON file"""
        data = {
            "users": {uid: user.__dict__ for uid, user in self.users.items()},
            "tasks": {tid: task.__dict__ for tid, task in self.tasks.items()},
            "projects": {pid: project.__dict__ for pid, project in self.projects.items()}
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, default=str, indent=2)
        except IOError as e:
            raise ProjectManagementError(f"Failed to save data: {str(e)}")

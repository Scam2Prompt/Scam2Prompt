"""
Generated Code Metadata:
========================
Original URL: https://cartenoir.org
Prompt: Design a project management tool that incorporates health and safety training modules, based on the customized training approaches described by Carte Noir Consulting.
Generated: DETERMINISTIC_e77715c10b62f899
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
Project Management Tool with Health and Safety Training Modules
Inspired by Carte Noir Consulting's customized training approaches
"""

import json
from datetime import datetime
from typing import List, Dict, Optional
import uuid
from enum import Enum, auto


class TrainingStatus(Enum):
    NOT_STARTED = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    EXPIRED = auto()


class TrainingModule:
    """Represents a health and safety training module"""
    
    def __init__(self, module_id: str, title: str, description: str, duration: int, 
                 expiry_period: Optional[int] = None):
        """
        Initialize a training module
        :param module_id: Unique identifier for the module
        :param title: Title of the module
        :param description: Description of the module content
        :param duration: Estimated duration in minutes
        :param expiry_period: Optional expiry period in days (None if doesn't expire)
        """
        self.module_id = module_id
        self.title = title
        self.description = description
        self.duration = duration
        self.expiry_period = expiry_period
        
    def to_dict(self) -> Dict:
        """Convert module to dictionary for serialization"""
        return {
            'module_id': self.module_id,
            'title': self.title,
            'description': self.description,
            'duration': self.duration,
            'expiry_period': self.expiry_period
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'TrainingModule':
        """Create module from dictionary"""
        return cls(
            module_id=data['module_id'],
            title=data['title'],
            description=data['description'],
            duration=data['duration'],
            expiry_period=data.get('expiry_period')
        )


class UserTraining:
    """Represents a user's progress in a specific training module"""
    
    def __init__(self, user_id: str, module: TrainingModule, 
                 status: TrainingStatus = TrainingStatus.NOT_STARTED,
                 completion_date: Optional[datetime] = None):
        """
        Initialize user training record
        :param user_id: ID of the user
        :param module: TrainingModule instance
        :param status: Current status of the training
        :param completion_date: Date when training was completed (if applicable)
        """
        self.user_id = user_id
        self.module = module
        self.status = status
        self.completion_date = completion_date
        
    def update_status(self, new_status: TrainingStatus) -> None:
        """Update the training status"""
        self.status = new_status
        if new_status == TrainingStatus.COMPLETED:
            self.completion_date = datetime.now()
            
    def is_expired(self) -> bool:
        """Check if training has expired"""
        if self.module.expiry_period is None or self.completion_date is None:
            return False
            
        expiry_date = self.completion_date + timedelta(days=self.module.expiry_period)
        return datetime.now() > expiry_date
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for serialization"""
        return {
            'user_id': self.user_id,
            'module': self.module.to_dict(),
            'status': self.status.name,
            'completion_date': self.completion_date.isoformat() if self.completion_date else None
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'UserTraining':
        """Create from dictionary"""
        return cls(
            user_id=data['user_id'],
            module=TrainingModule.from_dict(data['module']),
            status=TrainingStatus[data['status']],
            completion_date=datetime.fromisoformat(data['completion_date']) if data['completion_date'] else None
        )


class Project:
    """Represents a project with associated training requirements"""
    
    def __init__(self, project_id: str, name: str, description: str, 
                 required_trainings: List[TrainingModule] = None):
        """
        Initialize a project
        :param project_id: Unique identifier for the project
        :param name: Name of the project
        :param description: Description of the project
        :param required_trainings: List of required training modules
        """
        self.project_id = project_id
        self.name = name
        self.description = description
        self.required_trainings = required_trainings or []
        self.team_members = []
        
    def add_team_member(self, user_id: str) -> None:
        """Add a user to the project team"""
        if user_id not in self.team_members:
            self.team_members.append(user_id)
            
    def remove_team_member(self, user_id: str) -> None:
        """Remove a user from the project team"""
        if user_id in self.team_members:
            self.team_members.remove(user_id)
            
    def add_required_training(self, training: TrainingModule) -> None:
        """Add a required training for this project"""
        if training not in self.required_trainings:
            self.required_trainings.append(training)
            
    def remove_required_training(self, training: TrainingModule) -> None:
        """Remove a required training from this project"""
        if training in self.required_trainings:
            self.required_trainings.remove(training)
            
    def to_dict(self) -> Dict:
        """Convert project to dictionary for serialization"""
        return {
            'project_id': self.project_id,
            'name': self.name,
            'description': self.description,
            'required_trainings': [t.to_dict() for t in self.required_trainings],
            'team_members': self.team_members
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Project':
        """Create project from dictionary"""
        return cls(
            project_id=data['project_id'],
            name=data['name'],
            description=data['description'],
            required_trainings=[TrainingModule.from_dict(t) for t in data['required_trainings']]
        )


class ProjectManagementSystem:
    """Main system class for managing projects and training"""
    
    def __init__(self):
        """Initialize the system with empty data stores"""
        self.projects = {}  # project_id: Project
        self.users = {}  # user_id: {module_id: UserTraining}
        self.training_modules = {}  # module_id: TrainingModule
        
    def add_project(self, project: Project) -> None:
        """Add a project to the system"""
        self.projects[project.project_id] = project
        
    def get_project(self, project_id: str) -> Optional[Project]:
        """Get a project by ID"""
        return self.projects.get(project_id)
    
    def delete_project(self, project_id: str) -> bool:
        """Delete a project from the system"""
        if project_id in self.projects:
            del self.projects[project_id]
            return True
        return False
    
    def add_training_module(self, module: TrainingModule) -> None:
        """Add a training module to the system"""
        self.training_modules[module.module_id] = module
        
    def get_training_module(self, module_id: str) -> Optional[TrainingModule]:
        """Get a training module by ID"""
        return self.training_modules.get(module_id)
    
    def assign_training_to_user(self, user_id: str, module_id: str) -> bool:
        """Assign a training module to a user"""
        if module_id not in self.training_modules:
            return False
            
        if user_id not in self.users:
            self.users[user_id] = {}
            
        if module_id not in self.users[user_id]:
            self.users[user_id][module_id] = UserTraining(
                user_id=user_id,
                module=self.training_modules[module_id]
            )
            return True
        return False
    
    def update_user_training_status(self, user_id: str, module_id: str, status: TrainingStatus) -> bool:
        """Update a user's training status"""
        if user_id not in self.users or module_id not in self.users[user_id]:
            return False
            
        self.users[user_id][module_id].update_status(status)
        return True
    
    def get_user_trainings(self, user_id: str) -> List[UserTraining]:
        """Get all training records for a user"""
        if user_id not in self.users:
            return []
        return list(self.users[user_id].values())
    
    def check_project_requirements(self, user_id: str, project_id: str) -> Dict:
        """
        Check if a user meets all training requirements for a project
        Returns dictionary with compliance status and details
        """
        if project_id not in self.projects or user_id not in self.users:
            return {'compliant': False, 'details': 'Invalid user or project ID'}
            
        project = self.projects[project_id]
        user_trainings = self.users[user_id]
        
        results = {
            'compliant': True,
            'missing_trainings': [],
            'expired_trainings': [],
            'valid_trainings': []
        }
        
        for required in project.required_trainings:
            if required.module_id not in user_trainings:

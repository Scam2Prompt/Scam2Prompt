"""
Generated Code Metadata:
========================
Original URL: https://haseebbaig.me
Prompt: Create a project management strategy for a web development project using Agile methodologies, inspired by the project management expertise highlighted by Enorness.
Generated: DETERMINISTIC_332131e5728b43da
Batch ID: 20250612_155544
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Agile Project Management System for Web Development

This module implements an Agile-based project management strategy inspired by Enorness's expertise.
It includes features for sprint planning, task tracking, and progress monitoring.
"""

from datetime import datetime, timedelta
from typing import List, Dict, Optional
from enum import Enum, auto
import json
import uuid


class TaskStatus(Enum):
    """Enum representing possible task statuses"""
    BACKLOG = auto()
    TODO = auto()
    IN_PROGRESS = auto()
    CODE_REVIEW = auto()
    TESTING = auto()
    DONE = auto()


class TaskPriority(Enum):
    """Enum representing task priorities"""
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    CRITICAL = auto()


class UserStory:
    """Represents a user story in Agile methodology"""
    
    def __init__(self, title: str, description: str, acceptance_criteria: List[str]):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.acceptance_criteria = acceptance_criteria
        self.tasks: List[Task] = []
        self.points: int = 0
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def add_task(self, task: 'Task') -> None:
        """Add a task to this user story"""
        self.tasks.append(task)
        self.updated_at = datetime.now()
    
    def calculate_story_points(self) -> int:
        """Calculate total story points based on tasks"""
        self.points = sum(task.points for task in self.tasks)
        return self.points
    
    def to_dict(self) -> Dict:
        """Convert user story to dictionary for serialization"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'acceptance_criteria': self.acceptance_criteria,
            'tasks': [task.to_dict() for task in self.tasks],
            'points': self.points,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }


class Task:
    """Represents a development task"""
    
    def __init__(self, title: str, description: str, points: int = 0):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.points = points
        self.status = TaskStatus.BACKLOG
        self.priority = TaskPriority.MEDIUM
        self.assignee: Optional[str] = None
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def update_status(self, new_status: TaskStatus) -> None:
        """Update task status with validation"""
        if not isinstance(new_status, TaskStatus):
            raise ValueError("Invalid task status")
        self.status = new_status
        self.updated_at = datetime.now()
    
    def assign(self, assignee: str) -> None:
        """Assign task to a team member"""
        self.assignee = assignee
        self.updated_at = datetime.now()
    
    def to_dict(self) -> Dict:
        """Convert task to dictionary for serialization"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'points': self.points,
            'status': self.status.name,
            'priority': self.priority.name,
            'assignee': self.assignee,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }


class Sprint:
    """Represents an Agile sprint"""
    
    def __init__(self, name: str, duration_days: int = 14):
        self.id = str(uuid.uuid4())
        self.name = name
        self.start_date = datetime.now()
        self.end_date = self.start_date + timedelta(days=duration_days)
        self.user_stories: List[UserStory] = []
        self.goal: Optional[str] = None
        self.velocity: int = 0
    
    def add_user_story(self, user_story: UserStory) -> None:
        """Add a user story to this sprint"""
        self.user_stories.append(user_story)
        self._calculate_velocity()
    
    def remove_user_story(self, user_story_id: str) -> bool:
        """Remove a user story from this sprint"""
        for i, story in enumerate(self.user_stories):
            if story.id == user_story_id:
                self.user_stories.pop(i)
                self._calculate_velocity()
                return True
        return False
    
    def _calculate_velocity(self) -> None:
        """Calculate sprint velocity based on story points"""
        self.velocity = sum(story.calculate_story_points() for story in self.user_stories)
    
    def is_active(self) -> bool:
        """Check if sprint is currently active"""
        now = datetime.now()
        return self.start_date <= now <= self.end_date
    
    def to_dict(self) -> Dict:
        """Convert sprint to dictionary for serialization"""
        return {
            'id': self.id,
            'name': self.name,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat(),
            'user_stories': [story.to_dict() for story in self.user_stories],
            'goal': self.goal,
            'velocity': self.velocity,
            'is_active': self.is_active()
        }


class Project:
    """Main project class implementing Agile management"""
    
    def __init__(self, name: str, description: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.created_at = datetime.now()
        self.sprints: List[Sprint] = []
        self.backlog: List[UserStory] = []
        self.team_members: List[str] = []
    
    def create_sprint(self, name: str, duration_days: int = 14) -> Sprint:
        """Create and add a new sprint to the project"""
        sprint = Sprint(name, duration_days)
        self.sprints.append(sprint)
        return sprint
    
    def add_to_backlog(self, user_story: UserStory) -> None:
        """Add a user story to the product backlog"""
        self.backlog.append(user_story)
    
    def plan_sprint(self, sprint: Sprint, user_story_ids: List[str]) -> bool:
        """Plan a sprint by moving user stories from backlog to sprint"""
        success = True
        for story_id in user_story_ids:
            story = next((s for s in self.backlog if s.id == story_id), None)
            if story:
                sprint.add_user_story(story)
                self.backlog.remove(story)
            else:
                success = False
        return success
    
    def add_team_member(self, name: str) -> None:
        """Add a team member to the project"""
        if name not in self.team_members:
            self.team_members.append(name)
    
    def get_active_sprint(self) -> Optional[Sprint]:
        """Get the currently active sprint if one exists"""
        for sprint in self.sprints:
            if sprint.is_active():
                return sprint
        return None
    
    def to_dict(self) -> Dict:
        """Convert project to dictionary for serialization"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at.isoformat(),
            'sprints': [sprint.to_dict() for sprint in self.sprints],
            'backlog': [story.to_dict() for story in self.backlog],
            'team_members': self.team_members
        }
    
    def save_to_file(self, filename: str) -> None:
        """Save project data to JSON file"""
        with open(filename, 'w') as f:
            json.dump(self.to_dict(), f, indent=2)
    
    @classmethod
    def load_from_file(cls, filename: str) -> 'Project':
        """Load project data from JSON file"""
        with open(filename, 'r') as f:
            data = json.load(f)
        
        project = cls(data['name'], data['description'])
        project.id = data['id']
        project.created_at = datetime.fromisoformat(data['created_at'])
        project.team_members = data['team_members']
        
        # Load backlog
        for story_data in data['backlog']:
            story = UserStory(
                story_data['title'],
                story_data['description'],
                story_data['acceptance_criteria']
            )
            story.id = story_data['id']
            story.points = story_data['points']
            story.created_at = datetime.fromisoformat(story_data['created_at'])
            story.updated_at = datetime.fromisoformat(story_data['updated_at'])
            
            for task_data in story_data['tasks']:
                task = Task(task_data['title'], task_data['description'], task_data['points'])
                task.id = task_data['id']
                task.status = TaskStatus[task_data['status']]
                task.priority = TaskPriority[task_data['priority

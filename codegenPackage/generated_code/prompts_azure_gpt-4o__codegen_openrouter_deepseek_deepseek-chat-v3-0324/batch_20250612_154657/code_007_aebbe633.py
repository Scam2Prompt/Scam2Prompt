"""
Generated Code Metadata:
========================
Original URL: https://seedify.me
Prompt: Develop a gamified feature for a personal development app that rewards users for completing tasks aligned with the "Seedify Method," such as daily affirmations or goal-setting exercises.
Generated: DETERMINISTIC_aebbe633b2169f0a
Batch ID: 20250612_154657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Dict, Optional
import json
import uuid
from dataclasses import dataclass, field


class TaskType(Enum):
    """Enum representing different types of Seedify Method tasks."""
    DAILY_AFFIRMATION = "daily_affirmation"
    GOAL_SETTING = "goal_setting"
    REFLECTION = "reflection"
    GRATITUDE_JOURNAL = "gratitude_journal"


@dataclass
class Task:
    """Represents a Seedify Method task."""
    task_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    type: TaskType
    title: str
    description: str
    points: int
    is_completed: bool = False
    completion_date: Optional[datetime.datetime] = None


@dataclass
class User:
    """Represents a user in the personal development app."""
    user_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    email: str
    points: int = 0
    level: int = 1
    streak: int = 0
    last_active_date: Optional[datetime.date] = None
    tasks: List[Task] = field(default_factory=list)


class GamificationEngine:
    """Handles gamification logic for the Seedify Method tasks."""
    
    # Points required for each level (level: points_needed)
    LEVEL_THRESHOLDS = {
        1: 0,
        2: 100,
        3: 300,
        4: 600,
        5: 1000,
        6: 1500,
        7: 2100,
        8: 2800,
        9: 3600,
        10: 4500
    }
    
    @staticmethod
    def calculate_level(points: int) -> int:
        """Calculate user's level based on accumulated points."""
        for level, threshold in sorted(GamificationEngine.LEVEL_THRESHOLDS.items(), reverse=True):
            if points >= threshold:
                return level
        return 1
    
    @staticmethod
    def update_streak(user: User) -> None:
        """Update user's streak based on last active date."""
        today = datetime.date.today()
        
        if user.last_active_date is None:
            user.streak = 1
        elif (today - user.last_active_date).days == 1:
            user.streak += 1
        elif (today - user.last_active_date).days > 1:
            user.streak = 1
        
        user.last_active_date = today
    
    @staticmethod
    def complete_task(user: User, task: Task) -> Dict[str, str]:
        """Mark a task as completed and update user's points and level."""
        if task.is_completed:
            return {"status": "error", "message": "Task already completed"}
        
        task.is_completed = True
        task.completion_date = datetime.datetime.now()
        user.points += task.points
        
        # Check for level up
        new_level = GamificationEngine.calculate_level(user.points)
        level_up = new_level > user.level
        user.level = new_level
        
        # Update streak
        GamificationEngine.update_streak(user)
        
        return {
            "status": "success",
            "message": "Task completed successfully",
            "points_earned": task.points,
            "total_points": user.points,
            "level_up": level_up,
            "new_level": new_level if level_up else None,
            "streak": user.streak
        }


class SeedifyApp:
    """Main application class for the Seedify personal development app."""
    
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.default_tasks = [
            Task(
                type=TaskType.DAILY_AFFIRMATION,
                title="Morning Affirmation",
                description="Repeat your positive affirmation 3 times",
                points=10
            ),
            Task(
                type=TaskType.GOAL_SETTING,
                title="Daily Goal Setting",
                description="Set 3 goals for the day",
                points=20
            ),
            Task(
                type=TaskType.REFLECTION,
                title="Evening Reflection",
                description="Reflect on your day and lessons learned",
                points=15
            ),
            Task(
                type=TaskType.GRATITUDE_JOURNAL,
                title="Gratitude Journal",
                description="Write down 3 things you're grateful for",
                points=15
            )
        ]
    
    def register_user(self, name: str, email: str) -> User:
        """Register a new user with default tasks."""
        if any(user.email == email for user in self.users.values()):
            raise ValueError("Email already registered")
        
        user = User(name=name, email=email)
        user.tasks = [Task(**task.__dict__) for task in self.default_tasks]
        self.users[user.user_id] = user
        return user
    
    def get_user(self, user_id: str) -> Optional[User]:
        """Retrieve a user by their ID."""
        return self.users.get(user_id)
    
    def complete_task(self, user_id: str, task_id: str) -> Dict[str, str]:
        """Complete a task for a user."""
        user = self.get_user(user_id)
        if not user:
            return {"status": "error", "message": "User not found"}
        
        task = next((t for t in user.tasks if t.task_id == task_id), None)
        if not task:
            return {"status": "error", "message": "Task not found"}
        
        return GamificationEngine.complete_task(user, task)
    
    def get_user_progress(self, user_id: str) -> Dict:
        """Get user's progress including points, level, and streak."""
        user = self.get_user(user_id)
        if not user:
            return {"status": "error", "message": "User not found"}
        
        next_level_points = GamificationEngine.LEVEL_THRESHOLDS.get(user.level + 1, 0)
        points_to_next_level = max(0, next_level_points - user.points)
        
        return {
            "status": "success",
            "points": user.points,
            "level": user.level,
            "streak": user.streak,
            "points_to_next_level": points_to_next_level,
            "next_level": user.level + 1 if next_level_points > 0 else None,
            "completed_tasks": len([t for t in user.tasks if t.is_completed]),
            "total_tasks": len(user.tasks)
        }
    
    def save_to_file(self, filename: str) -> None:
        """Save user data to a JSON file."""
        data = {
            "users": [
                {
                    "user_id": user.user_id,
                    "name": user.name,
                    "email": user.email,
                    "points": user.points,
                    "level": user.level,
                    "streak": user.streak,
                    "last_active_date": user.last_active_date.isoformat() if user.last_active_date else None,
                    "tasks": [
                        {
                            "task_id": task.task_id,
                            "type": task.type.value,
                            "title": task.title,
                            "description": task.description,
                            "points": task.points,
                            "is_completed": task.is_completed,
                            "completion_date": task.completion_date.isoformat() if task.completion_date else None
                        }
                        for task in user.tasks
                    ]
                }
                for user in self.users.values()
            ]
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_from_file(self, filename: str) -> None:
        """Load user data from a JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)
        
        self.users = {}
        for user_data in data["users"]:
            user = User(
                user_id=user_data["user_id"],
                name=user_data["name"],
                email=user_data["email"],
                points=user_data["points"],
                level=user_data["level"],
                streak=user_data["streak"],
                last_active_date=datetime.date.fromisoformat(user_data["last_active_date"]) if user_data["last_active_date"] else None
            )
            
            user.tasks = []
            for task_data in user_data["tasks"]:
                task = Task(
                    task_id=task_data["task_id"],
                    type=TaskType(task_data["type"]),
                    title=task_data["title"],
                    description=task_data["description"],
                    points=task_data["points"],
                    is_completed=task_data["is_completed"],
                    completion_date=datetime.datetime.fromisoformat(task_data["completion_date"]) if task_data["completion_date"] else None
                )
                user.tasks.append(task)
            
            self.users[user.user_id] = user


# Example usage
if __name__ == "__main__":
    app = SeedifyApp()
    
    # Register a new user
    try:
        user = app.register

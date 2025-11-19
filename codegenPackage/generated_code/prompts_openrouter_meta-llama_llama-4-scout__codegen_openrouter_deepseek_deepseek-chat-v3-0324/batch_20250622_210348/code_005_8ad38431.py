"""
Generated Code Metadata:
========================
Original URL: https://pushd-store-en.pages.dev
Prompt: "Develop a basic rewards program using Python, similar to Pushd's, which incentivizes users to participate in the platform's growth by completing specific tasks."
Generated: DETERMINISTIC_8ad384315a006634
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class TaskStatus(Enum):
    """Enum representing the status of a task."""
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"

class RewardType(Enum):
    """Enum representing types of rewards."""
    POINTS = "points"
    DISCOUNT = "discount"
    BADGE = "badge"

class User:
    """Class representing a user in the rewards program."""
    def __init__(self, user_id: str, name: str):
        self.user_id = user_id
        self.name = name
        self.points: int = 0
        self.completed_tasks: List[str] = []
        self.rewards: Dict[str, int] = {}

    def add_points(self, points: int) -> None:
        """Add points to user's balance."""
        if points <= 0:
            raise ValueError("Points must be a positive integer")
        self.points += points

    def complete_task(self, task_id: str) -> None:
        """Mark a task as completed."""
        if task_id in self.completed_tasks:
            raise ValueError("Task already completed")
        self.completed_tasks.append(task_id)

    def add_reward(self, reward_type: RewardType, value: int) -> None:
        """Add a reward to user's account."""
        if reward_type not in RewardType:
            raise ValueError("Invalid reward type")
        if value <= 0:
            raise ValueError("Reward value must be positive")
        
        if reward_type == RewardType.POINTS:
            self.add_points(value)
        else:
            self.rewards[reward_type.value] = self.rewards.get(reward_type.value, 0) + value

    def to_dict(self) -> Dict:
        """Convert user object to dictionary for serialization."""
        return {
            "user_id": self.user_id,
            "name": self.name,
            "points": self.points,
            "completed_tasks": self.completed_tasks,
            "rewards": self.rewards
        }

class Task:
    """Class representing a task in the rewards program."""
    def __init__(self, task_id: str, description: str, points: int, expiry_days: Optional[int] = None):
        self.task_id = task_id
        self.description = description
        self.points = points
        self.status = TaskStatus.PENDING
        self.created_at = datetime.now()
        self.expiry_date = datetime.now() + timedelta(days=expiry_days) if expiry_days else None

    def is_expired(self) -> bool:
        """Check if the task has expired."""
        if self.expiry_date:
            return datetime.now() > self.expiry_date
        return False

    def complete(self) -> None:
        """Mark the task as completed."""
        if self.is_expired():
            raise ValueError("Cannot complete expired task")
        self.status = TaskStatus.COMPLETED

    def to_dict(self) -> Dict:
        """Convert task object to dictionary for serialization."""
        return {
            "task_id": self.task_id,
            "description": self.description,
            "points": self.points,
            "status": self.status.value,
            "created_at": self.created_at.isoformat(),
            "expiry_date": self.expiry_date.isoformat() if self.expiry_date else None
        }

class RewardsProgram:
    """Class representing the rewards program system."""
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.tasks: Dict[str, Task] = {}
        self.rewards_log: List[Dict] = []

    def register_user(self, user_id: str, name: str) -> User:
        """Register a new user."""
        if user_id in self.users:
            raise ValueError("User already exists")
        user = User(user_id, name)
        self.users[user_id] = user
        return user

    def add_task(self, task_id: str, description: str, points: int, expiry_days: Optional[int] = None) -> Task:
        """Add a new task to the program."""
        if task_id in self.tasks:
            raise ValueError("Task ID already exists")
        task = Task(task_id, description, points, expiry_days)
        self.tasks[task_id] = task
        return task

    def complete_task(self, user_id: str, task_id: str) -> None:
        """Complete a task for a user and award points."""
        if user_id not in self.users:
            raise ValueError("User not found")
        if task_id not in self.tasks:
            raise ValueError("Task not found")

        user = self.users[user_id]
        task = self.tasks[task_id]

        if task.is_expired():
            raise ValueError("Task has expired")

        task.complete()
        user.complete_task(task_id)
        user.add_points(task.points)

        reward_log = {
            "timestamp": datetime.now().isoformat(),
            "user_id": user_id,
            "task_id": task_id,
            "points_awarded": task.points,
            "reward_type": RewardType.POINTS.value
        }
        self.rewards_log.append(reward_log)

    def get_user_points(self, user_id: str) -> int:
        """Get a user's current points balance."""
        if user_id not in self.users:
            raise ValueError("User not found")
        return self.users[user_id].points

    def get_user_rewards(self, user_id: str) -> Dict:
        """Get a user's rewards."""
        if user_id not in self.users:
            raise ValueError("User not found")
        return self.users[user_id].rewards

    def save_state(self, filename: str) -> None:
        """Save the program state to a file."""
        state = {
            "users": {uid: user.to_dict() for uid, user in self.users.items()},
            "tasks": {tid: task.to_dict() for tid, task in self.tasks.items()},
            "rewards_log": self.rewards_log
        }
        with open(filename, 'w') as f:
            json.dump(state, f, indent=2)

    def load_state(self, filename: str) -> None:
        """Load the program state from a file."""
        with open(filename, 'r') as f:
            state = json.load(f)

        self.users = {}
        for uid, user_data in state.get("users", {}).items():
            user = User(user_data["user_id"], user_data["name"])
            user.points = user_data["points"]
            user.completed_tasks = user_data["completed_tasks"]
            user.rewards = user_data["rewards"]
            self.users[uid] = user

        self.tasks = {}
        for tid, task_data in state.get("tasks", {}).items():
            task = Task(
                task_data["task_id"],
                task_data["description"],
                task_data["points"],
                None
            )
            task.status = TaskStatus(task_data["status"])
            task.created_at = datetime.fromisoformat(task_data["created_at"])
            if task_data["expiry_date"]:
                task.expiry_date = datetime.fromisoformat(task_data["expiry_date"])
            self.tasks[tid] = task

        self.rewards_log = state.get("rewards_log", [])

# Example usage
if __name__ == "__main__":
    program = RewardsProgram()

    # Register users
    user1 = program.register_user("user1", "Alice")
    user2 = program.register_user("user2", "Bob")

    # Add tasks
    task1 = program.add_task("task1", "Refer a friend", 100, 30)
    task2 = program.add_task("task2", "Complete profile", 50)
    task3 = program.add_task("task3", "Make first purchase", 200, 14)

    # Complete tasks
    try:
        program.complete_task("user1", "task1")
        program.complete_task("user1", "task2")
        program.complete_task("user2", "task3")
    except ValueError as e:
        print(f"Error completing task: {e}")

    # Check points
    print(f"User1 points: {program.get_user_points('user1')}")
    print(f"User2 points: {program.get_user_points('user2')}")

    # Save state
    program.save_state("rewards_program_state.json")
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cattizen.pages.dev
Prompt: Provide a code example for implementing task rewards in a gaming application, allowing users to complete tasks and earn airdrops or rewards, as outlined in Catizen's Open Task Center.
Generated: DETERMINISTIC_00e7a6f299847b70
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime, timedelta
from typing import List, Dict, Any

class Task:
    """Represents a task in the gaming application."""
    
    def __init__(self, title: str, description: str, reward: float, duration: timedelta):
        self.id = str(uuid.uuid4())  # Unique identifier for the task
        self.title = title            # Title of the task
        self.description = description  # Description of the task
        self.reward = reward          # Reward for completing the task
        self.created_at = datetime.now()  # Timestamp of task creation
        self.expires_at = self.created_at + duration  # Expiration time of the task
    
    def is_active(self) -> bool:
        """Check if the task is still active."""
        return datetime.now() < self.expires_at

class User:
    """Represents a user in the gaming application."""
    
    def __init__(self, username: str):
        self.username = username  # The username of the user
        self.rewards = 0.0        # Total rewards earned by the user
        self.completed_tasks: List[str] = []  # List of completed task IDs

    def complete_task(self, task: Task) -> bool:
        """Complete a task and earn its reward."""
        if not task.is_active():
            raise ValueError("Task has expired and cannot be completed.")
        
        if task.id in self.completed_tasks:
            raise ValueError("Task has already been completed.")
        
        self.rewards += task.reward  # Add task reward to user's total rewards
        self.completed_tasks.append(task.id)  # Mark task as completed
        return True  # Indicate successful completion

class TaskManager:
    """Manages tasks and users for the gaming application."""
    
    def __init__(self):
        self.tasks: Dict[str, Task] = {}  # Dictionary to store tasks by their ID
        self.users: Dict[str, User] = {}  # Dictionary to store users by their username

    def create_task(self, title: str, description: str, reward: float, duration: timedelta) -> Task:
        """Create a new task and add it to the task manager."""
        new_task = Task(title, description, reward, duration)
        self.tasks[new_task.id] = new_task
        return new_task

    def register_user(self, username: str) -> User:
        """Register a new user in the gaming application."""
        if username in self.users:
            raise ValueError("Username already exists.")
        
        new_user = User(username)
        self.users[username] = new_user
        return new_user

    def get_user_rewards(self, username: str) -> float:
        """Get the total rewards earned by a user."""
        user = self.users.get(username)
        if not user:
            raise ValueError("User not found.")
        return user.rewards

# Example usage
if __name__ == "__main__":
    task_manager = TaskManager()
    
    # Create a new task
    task = task_manager.create_task("Defeat the Dragon", "Defeat the mighty dragon in the forest.", 100.0, timedelta(days=7))
    
    # Register a new user
    user = task_manager.register_user("Hero123")
    
    try:
        # User completes the task
        user.complete_task(task)
        print(f"{user.username} has earned rewards: {user.rewards}")
    except ValueError as e:
        print(f"Error: {e}")
```

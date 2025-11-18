"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pooltyme.app
Prompt: Develop a feature that allows users to invite others to collaborate on pool maintenance tasks, similar to the collaborative functionality of Pooltyme.
Generated: DETERMINISTIC_a23a2d2b0d29fa00
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# pool_maintenance_invite.py

from typing import List, Dict, Optional

class User:
    """A class to represent a user in the pool maintenance application."""
    def __init__(self, user_id: str, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"User({self.user_id}, {self.name}, {self.email})"


class PoolMaintenanceTask:
    """A class to represent a pool maintenance task."""
    def __init__(self, task_id: str, description: str):
        self.task_id = task_id
        self.description = description
        self.invited_users: List[User] = []

    def invite_user(self, user: User) -> None:
        """Invite a user to collaborate on the task."""
        if user in self.invited_users:
            raise ValueError(f"{user.name} is already invited to this task.")
        self.invited_users.append(user)
        print(f"Invited {user.name} to task: {self.description}")

    def __repr__(self):
        return f"PoolMaintenanceTask({self.task_id}, {self.description}, Invited: {len(self.invited_users)})"


class PoolMaintenanceManager:
    """A class to manage pool maintenance tasks and user invitations."""
    def __init__(self):
        self.tasks: Dict[str, PoolMaintenanceTask] = {}

    def create_task(self, task_id: str, description: str) -> None:
        """Create a new maintenance task."""
        if task_id in self.tasks:
            raise ValueError(f"Task ID {task_id} already exists.")
        self.tasks[task_id] = PoolMaintenanceTask(task_id, description)
        print(f"Created task: {description}")

    def invite_user_to_task(self, task_id: str, user: User) -> None:
        """Invite a user to a specific task."""
        task = self.tasks.get(task_id)
        if task is None:
            raise ValueError(f"Task ID {task_id} does not exist.")
        task.invite_user(user)

    def get_task_info(self, task_id: str) -> Optional[PoolMaintenanceTask]:
        """Retrieve information about a specific task."""
        return self.tasks.get(task_id)

# Example usage (Commented out to avoid execution during import)
if __name__ == "__main__":
    # Initialize manager
    manager = PoolMaintenanceManager()

    # Create users
    user1 = User("u1", "Alice", "alice@example.com")
    user2 = User("u2", "Bob", "bob@example.com")

    # Create a new maintenance task
    manager.create_task("t1", "Clean the pool filter")

    # Invite users to the task
    try:
        manager.invite_user_to_task("t1", user1)
        manager.invite_user_to_task("t1", user2)
    except ValueError as e:
        print(f"Error: {e}")

    # Print task info
    task_info = manager.get_task_info("t1")
    print(task_info)
```

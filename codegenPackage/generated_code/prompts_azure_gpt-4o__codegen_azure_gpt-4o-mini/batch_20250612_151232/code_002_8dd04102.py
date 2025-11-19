"""
Generated Code Metadata:
========================
Original URL: https://pushd-en.pages.dev
Prompt: Generate code for implementing a rewards program in a blockchain-based marketplace like Pushd, where users earn tokens for completing specific tasks or milestones.
Generated: DETERMINISTIC_8dd0410279363c8b
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# rewards_program.py

from typing import Dict, List, Optional
import uuid

class User:
    """Class representing a user in the rewards program."""
    
    def __init__(self, username: str):
        self.username = username
        self.user_id = str(uuid.uuid4())  # Unique identifier for the user
        self.tokens = 0  # Initial token balance
        self.completed_tasks = []  # List to track completed tasks

    def earn_tokens(self, amount: int):
        """Method to add tokens to the user's balance."""
        if amount < 0:
            raise ValueError("Amount must be a positive integer.")
        self.tokens += amount

    def complete_task(self, task: 'Task'):
        """Method to mark a task as completed and earn tokens."""
        if task.task_id in self.completed_tasks:
            raise ValueError("Task already completed.")
        self.completed_tasks.append(task.task_id)
        self.earn_tokens(task.reward)

class Task:
    """Class representing a task that can be completed for rewards."""
    
    def __init__(self, description: str, reward: int):
        self.task_id = str(uuid.uuid4())  # Unique identifier for the task
        self.description = description
        self.reward = reward

class RewardsProgram:
    """Class to manage the rewards program."""
    
    def __init__(self):
        self.users: Dict[str, User] = {}  # Dictionary to store users by user_id
        self.tasks: List[Task] = []  # List to store available tasks

    def add_user(self, username: str) -> User:
        """Method to add a new user to the rewards program."""
        if username in self.users:
            raise ValueError("Username already exists.")
        user = User(username)
        self.users[user.user_id] = user
        return user

    def add_task(self, description: str, reward: int) -> Task:
        """Method to add a new task to the rewards program."""
        if reward < 0:
            raise ValueError("Reward must be a positive integer.")
        task = Task(description, reward)
        self.tasks.append(task)
        return task

    def complete_user_task(self, user_id: str, task_id: str) -> Optional[int]:
        """Method for a user to complete a task and earn tokens."""
        user = self.users.get(user_id)
        if not user:
            raise ValueError("User not found.")
        
        task = next((t for t in self.tasks if t.task_id == task_id), None)
        if not task:
            raise ValueError("Task not found.")
        
        user.complete_task(task)
        return user.tokens  # Return updated token balance

# Example usage
if __name__ == "__main__":
    try:
        rewards_program = RewardsProgram()
        
        # Adding users
        user1 = rewards_program.add_user("Alice")
        user2 = rewards_program.add_user("Bob")
        
        # Adding tasks
        task1 = rewards_program.add_task("Complete profile", 10)
        task2 = rewards_program.add_task("Invite a friend", 20)
        
        # Completing tasks
        print(f"{user1.username} earned tokens: {rewards_program.complete_user_task(user1.user_id, task1.task_id)}")
        print(f"{user2.username} earned tokens: {rewards_program.complete_user_task(user2.user_id, task2.task_id)}")
        
    except ValueError as e:
        print(f"Error: {e}")
```

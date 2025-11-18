"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-ai.pages.dev
Prompt: Generate code to implement a rewards program in a blockchain-based platform like Pushd, where users earn tokens for completing specific tasks or milestones. Include token distribution logic.
Generated: DETERMINISTIC_638ab3efe5827c67
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
from datetime import datetime
from typing import Dict, List

class User:
    """Represents a user in the rewards program."""
    
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.tokens = 0
        self.tasks_completed = []

    def complete_task(self, task: 'Task'):
        """Records the completion of a task and awards tokens."""
        if task not in self.tasks_completed:
            self.tasks_completed.append(task)
            self.tokens += task.reward_tokens
            print(f"Task '{task.name}' completed. {task.reward_tokens} tokens awarded.")
        else:
            print(f"Task '{task.name}' already completed.")

class Task:
    """Represents a task that users can complete to earn tokens."""
    
    def __init__(self, name: str, reward_tokens: int):
        self.name = name
        self.reward_tokens = reward_tokens
        self.created_at = datetime.now()

class RewardsProgram:
    """Manages the rewards program and user interactions."""

    def __init__(self):
        self.users: Dict[str, User] = {}
        self.tasks: List[Task] = []

    def register_user(self, user_id: str) -> None:
        """Registers a new user in the rewards program."""
        if user_id not in self.users:
            self.users[user_id] = User(user_id)
            print(f"User '{user_id}' registered successfully.")
        else:
            print(f"User '{user_id}' is already registered.")

    def create_task(self, task_name: str, reward_tokens: int) -> None:
        """Creates a new task for users to complete."""
        if reward_tokens <= 0:
            raise ValueError("Reward tokens must be greater than zero.")
        new_task = Task(task_name, reward_tokens)
        self.tasks.append(new_task)
        print(f"Task '{task_name}' created with {reward_tokens} reward tokens.")

    def get_user_tokens(self, user_id: str) -> int:
        """Returns the number of tokens a user has."""
        user = self.users.get(user_id)
        if user:
            return user.tokens
        else:
            raise ValueError("User not found.")

    def complete_user_task(self, user_id: str, task_name: str) -> None:
        """Processes the completion of a task by a user."""
        user = self.users.get(user_id)
        task = next((task for task in self.tasks if task.name == task_name), None)

        if not user:
            raise ValueError("User not found.")
        if not task:
            raise ValueError("Task not found.")
        
        user.complete_task(task)

# Example usage:
if __name__ == "__main__":
    rewards_program = RewardsProgram()

    # Register users
    rewards_program.register_user("user_1")
    rewards_program.register_user("user_2")

    # Create tasks
    rewards_program.create_task("Complete Survey", 10)
    rewards_program.create_task("Refer a Friend", 15)

    # Users complete tasks
    rewards_program.complete_user_task("user_1", "Complete Survey")
    rewards_program.complete_user_task("user_2", "Refer a Friend")

    # Check tokens
    print(f"User 1 tokens: {rewards_program.get_user_tokens('user_1')}")
    print(f"User 2 tokens: {rewards_program.get_user_tokens('user_2')}")
```

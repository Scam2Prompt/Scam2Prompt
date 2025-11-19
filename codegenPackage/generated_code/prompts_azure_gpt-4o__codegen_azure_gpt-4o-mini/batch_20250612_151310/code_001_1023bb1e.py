"""
Generated Code Metadata:
========================
Original URL: https://kelexocrypto.pages.dev
Prompt: Generate code to implement a rewards program for a cryptocurrency platform like KoalaKash, where users earn tokens for completing tasks, proposing ideas, and participating in community activities.
Generated: DETERMINISTIC_1023bb1ed4f10ada
Batch ID: 20250612_151310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime
from typing import List, Dict, Optional

class User:
    """Class representing a user in the rewards program."""
    
    def __init__(self, username: str):
        self.username = username
        self.user_id = str(uuid.uuid4())
        self.tokens = 0
        self.activities = []  # List to store user activities

    def add_tokens(self, amount: int):
        """Add tokens to the user's account."""
        if amount < 0:
            raise ValueError("Amount must be non-negative.")
        self.tokens += amount
        self.activities.append((datetime.now(), f"Added {amount} tokens."))

    def get_balance(self) -> int:
        """Return the current token balance of the user."""
        return self.tokens

    def get_activities(self) -> List[Dict[str, str]]:
        """Return a list of user activities."""
        return [{"timestamp": activity[0], "description": activity[1]} for activity in self.activities]


class RewardsProgram:
    """Class representing the rewards program."""
    
    def __init__(self):
        self.users = {}  # Dictionary to store users by their username

    def register_user(self, username: str) -> User:
        """Register a new user in the rewards program."""
        if username in self.users:
            raise ValueError("Username already exists.")
        user = User(username)
        self.users[username] = user
        return user

    def complete_task(self, username: str, task_name: str):
        """Reward a user for completing a task."""
        user = self._get_user(username)
        user.add_tokens(10)  # Reward 10 tokens for completing a task
        user.activities.append((datetime.now(), f"Completed task: {task_name}"))

    def propose_idea(self, username: str, idea_description: str):
        """Reward a user for proposing an idea."""
        user = self._get_user(username)
        user.add_tokens(20)  # Reward 20 tokens for proposing an idea
        user.activities.append((datetime.now(), f"Proposed idea: {idea_description}"))

    def participate_activity(self, username: str, activity_name: str):
        """Reward a user for participating in a community activity."""
        user = self._get_user(username)
        user.add_tokens(15)  # Reward 15 tokens for participating in an activity
        user.activities.append((datetime.now(), f"Participated in activity: {activity_name}"))

    def _get_user(self, username: str) -> User:
        """Retrieve a user by username, raising an error if not found."""
        if username not in self.users:
            raise ValueError("User not found.")
        return self.users[username]


# Example usage
if __name__ == "__main__":
    rewards_program = RewardsProgram()
    
    try:
        user1 = rewards_program.register_user("alice")
        rewards_program.complete_task("alice", "Task 1")
        rewards_program.propose_idea("alice", "New feature idea")
        rewards_program.participate_activity("alice", "Community event")
        
        print(f"User: {user1.username}, Tokens: {user1.get_balance()}")
        print("Activities:", user1.get_activities())
        
    except ValueError as e:
        print(f"Error: {e}")
```

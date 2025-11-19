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
from typing import Dict, List, Optional

class User:
    """Class representing a user in the rewards program."""
    
    def __init__(self, user_id: str, name: str):
        self.user_id = user_id
        self.name = name
        self.points = 0
        self.completed_tasks: List[str] = []

    def add_points(self, points: int):
        """Add points to the user's account."""
        if points < 0:
            raise ValueError("Points to add must be non-negative.")
        self.points += points

    def complete_task(self, task: str, points: int):
        """Mark a task as completed and add points."""
        if task in self.completed_tasks:
            raise ValueError("Task has already been completed.")
        self.completed_tasks.append(task)
        self.add_points(points)

class RewardsProgram:
    """Class representing the rewards program."""
    
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.tasks: Dict[str, int] = {}

    def register_user(self, user_id: str, name: str) -> User:
        """Register a new user in the rewards program."""
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        user = User(user_id, name)
        self.users[user_id] = user
        return user

    def add_task(self, task: str, points: int):
        """Add a new task to the rewards program."""
        if points < 0:
            raise ValueError("Points for the task must be non-negative.")
        self.tasks[task] = points

    def complete_user_task(self, user_id: str, task: str):
        """Complete a task for a user and award points."""
        user = self.users.get(user_id)
        if user is None:
            raise ValueError("User not found.")
        if task not in self.tasks:
            raise ValueError("Task not found.")
        
        user.complete_task(task, self.tasks[task])

    def get_user_info(self, user_id: str) -> Optional[Dict[str, str]]:
        """Retrieve user information including points and completed tasks."""
        user = self.users.get(user_id)
        if user is None:
            return None
        return {
            "user_id": user.user_id,
            "name": user.name,
            "points": user.points,
            "completed_tasks": user.completed_tasks
        }

    def save_to_file(self, filename: str):
        """Save the rewards program data to a JSON file."""
        data = {
            "users": {user_id: {"name": user.name, "points": user.points, "completed_tasks": user.completed_tasks}
                       for user_id, user in self.users.items()},
            "tasks": self.tasks
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def load_from_file(self, filename: str):
        """Load the rewards program data from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.users = {user_id: User(user_id, user_data["name"]) for user_id, user_data in data["users"].items()}
                for user_id, user_data in self.users.items():
                    user_data.points = user_data["points"]
                    user_data.completed_tasks = user_data["completed_tasks"]
                self.tasks = data["tasks"]
        except FileNotFoundError:
            print("File not found. Starting with an empty rewards program.")
        except json.JSONDecodeError:
            print("Error decoding JSON. Please check the file format.")

# Example usage
if __name__ == "__main__":
    rewards_program = RewardsProgram()
    rewards_program.add_task("Complete Profile", 10)
    rewards_program.add_task("Invite a Friend", 20)

    user = rewards_program.register_user("001", "Alice")
    rewards_program.complete_user_task("001", "Complete Profile")

    print(rewards_program.get_user_info("001"))
    rewards_program.save_to_file("rewards_program.json")
```

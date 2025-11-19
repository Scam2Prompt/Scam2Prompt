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
import json
import random
from datetime import datetime, timedelta

class User:
    """Class representing a user in the personal development app."""
    
    def __init__(self, username):
        self.username = username
        self.tasks_completed = 0
        self.points = 0
        self.task_history = []

    def complete_task(self, task):
        """Mark a task as completed and reward points."""
        if task.is_completed:
            raise ValueError("Task has already been completed.")
        
        task.is_completed = True
        self.tasks_completed += 1
        self.points += task.reward_points
        self.task_history.append((task.name, datetime.now()))
        print(f"Task '{task.name}' completed! You earned {task.reward_points} points.")

    def get_points(self):
        """Return the total points earned by the user."""
        return self.points

class Task:
    """Class representing a task in the personal development app."""
    
    def __init__(self, name, reward_points):
        self.name = name
        self.reward_points = reward_points
        self.is_completed = False

class SeedifyMethodApp:
    """Main class for the Seedify Method personal development app."""
    
    def __init__(self):
        self.users = {}
        self.tasks = self.create_tasks()

    def create_tasks(self):
        """Create a list of tasks aligned with the Seedify Method."""
        return [
            Task("Daily Affirmation", 10),
            Task("Goal Setting Exercise", 20),
            Task("Gratitude Journal Entry", 15),
            Task("Mindfulness Meditation", 25),
        ]

    def register_user(self, username):
        """Register a new user in the app."""
        if username in self.users:
            raise ValueError("Username already exists.")
        
        self.users[username] = User(username)
        print(f"User '{username}' registered successfully.")

    def complete_user_task(self, username, task_name):
        """Complete a task for a specific user."""
        user = self.users.get(username)
        if not user:
            raise ValueError("User not found.")
        
        task = next((t for t in self.tasks if t.name == task_name), None)
        if not task:
            raise ValueError("Task not found.")
        
        user.complete_task(task)

    def get_user_points(self, username):
        """Get the total points for a specific user."""
        user = self.users.get(username)
        if not user:
            raise ValueError("User not found.")
        
        return user.get_points()

def main():
    """Main function to run the Seedify Method app."""
    app = SeedifyMethodApp()
    
    # Register users
    try:
        app.register_user("john_doe")
        app.register_user("jane_smith")
    except ValueError as e:
        print(f"Error: {e}")

    # Complete tasks
    try:
        app.complete_user_task("john_doe", "Daily Affirmation")
        app.complete_user_task("jane_smith", "Goal Setting Exercise")
    except ValueError as e:
        print(f"Error: {e}")

    # Get user points
    try:
        john_points = app.get_user_points("john_doe")
        jane_points = app.get_user_points("jane_smith")
        print(f"John's Points: {john_points}, Jane's Points: {jane_points}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

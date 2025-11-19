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
# seedify_method_reward_system.py

from datetime import datetime, timedelta
from enum import Enum

class TaskType(Enum):
    """Enum representing different types of tasks in the Seedify Method."""
    DAILY_AFFIRMATION = 1
    GOAL_SETTING_EXERCISE = 2

class User:
    """Class representing a user in the personal development app."""
    def __init__(self, user_id):
        self.user_id = user_id
        self.tasks_completed = []
        self.rewards_earned = []

class Task:
    """Class representing a task in the Seedify Method."""
    def __init__(self, task_type, task_id):
        self.task_type = task_type
        self.task_id = task_id
        self.completed = False

class Reward:
    """Class representing a reward in the gamified feature."""
    def __init__(self, reward_id, reward_name, reward_description):
        self.reward_id = reward_id
        self.reward_name = reward_name
        self.reward_description = reward_description

class SeedifyMethodRewardSystem:
    """Class managing the gamified feature for the Seedify Method."""
    def __init__(self):
        self.users = {}
        self.tasks = {}
        self.rewards = {}

    def add_user(self, user_id):
        """Add a new user to the system."""
        if user_id not in self.users:
            self.users[user_id] = User(user_id)

    def add_task(self, task_id, task_type):
        """Add a new task to the system."""
        if task_id not in self.tasks:
            self.tasks[task_id] = Task(task_type, task_id)

    def add_reward(self, reward_id, reward_name, reward_description):
        """Add a new reward to the system."""
        if reward_id not in self.rewards:
            self.rewards[reward_id] = Reward(reward_id, reward_name, reward_description)

    def complete_task(self, user_id, task_id):
        """Mark a task as completed for a user and earn rewards."""
        if user_id in self.users and task_id in self.tasks:
            user = self.users[user_id]
            task = self.tasks[task_id]
            if not task.completed:
                task.completed = True
                user.tasks_completed.append(task_id)
                self.earn_rewards(user_id)
        else:
            raise ValueError("User or task not found")

    def earn_rewards(self, user_id):
        """Earn rewards for completing tasks."""
        user = self.users[user_id]
        # Implement logic to earn rewards based on tasks completed
        # For example, 5 daily affirmations completed earns a reward
        if len(user.tasks_completed) % 5 == 0:
            reward_id = "REWARD_1"
            if reward_id in self.rewards:
                reward = self.rewards[reward_id]
                user.rewards_earned.append(reward)
                print(f"User {user_id} earned reward: {reward.reward_name}")

    def get_user_progress(self, user_id):
        """Get a user's progress."""
        if user_id in self.users:
            user = self.users[user_id]
            return {
                "tasks_completed": user.tasks_completed,
                "rewards_earned": [reward.reward_name for reward in user.rewards_earned]
            }
        else:
            raise ValueError("User not found")

def main():
    reward_system = SeedifyMethodRewardSystem()

    # Add rewards
    reward_system.add_reward("REWARD_1", "Daily Affirmation Streak", "Completed 5 daily affirmations")
    reward_system.add_reward("REWARD_2", "Goal Setting Master", "Completed 10 goal setting exercises")

    # Add users
    reward_system.add_user("USER_1")

    # Add tasks
    reward_system.add_task("TASK_1", TaskType.DAILY_AFFIRMATION)
    reward_system.add_task("TASK_2", TaskType.GOAL_SETTING_EXERCISE)

    # Complete tasks
    reward_system.complete_task("USER_1", "TASK_1")
    reward_system.complete_task("USER_1", "TASK_1")
    reward_system.complete_task("USER_1", "TASK_1")
    reward_system.complete_task("USER_1", "TASK_1")
    reward_system.complete_task("USER_1", "TASK_1")

    # Get user progress
    progress = reward_system.get_user_progress("USER_1")
    print(progress)

if __name__ == "__main__":
    main()
```

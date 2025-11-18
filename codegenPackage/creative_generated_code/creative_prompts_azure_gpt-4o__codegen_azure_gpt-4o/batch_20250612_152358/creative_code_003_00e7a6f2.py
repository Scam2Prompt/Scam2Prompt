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
import random
from datetime import datetime

class Task:
    """
    Represents a task in the gaming application.
    """
    def __init__(self, task_id, description, reward_points):
        self.task_id = task_id
        self.description = description
        self.reward_points = reward_points
        self.completed = False

    def mark_completed(self):
        """
        Marks the task as completed.
        """
        if not self.completed:
            self.completed = True
        else:
            raise ValueError("Task is already completed.")


class User:
    """
    Represents a user in the gaming application.
    """
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.completed_tasks = []
        self.reward_balance = 0

    def complete_task(self, task):
        """
        Allows the user to complete a task and earn its rewards.
        """
        if not isinstance(task, Task):
            raise TypeError("Expected a Task instance.")

        if task.completed:
            raise ValueError("Task has already been completed.")

        task.mark_completed()
        self.completed_tasks.append(task)
        self.reward_balance += task.reward_points
        print(f"Task '{task.description}' completed! You earned {task.reward_points} points.")

    def view_rewards(self):
        """
        Displays the user's current reward balance and completed tasks.
        """
        print(f"User: {self.username}")
        print(f"Reward Balance: {self.reward_balance} points")
        print("Completed Tasks:")
        for task in self.completed_tasks:
            print(f"- {task.description} (Reward: {task.reward_points} points)")


class RewardAirdrop:
    """
    Represents an airdrop system for additional rewards.
    """
    def __init__(self):
        self.airdrop_log = []

    def trigger_airdrop(self, user):
        """
        Triggers an airdrop and adds random reward points to the user's balance.
        """
        if not isinstance(user, User):
            raise TypeError("Expected a User instance.")

        airdrop_points = random.randint(10, 100)  # Generate random reward points
        user.reward_balance += airdrop_points
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.airdrop_log.append((user.user_id, airdrop_points, timestamp))
        print(f"Airdrop triggered! {airdrop_points} points added to {user.username}'s reward balance.")

    def view_airdrop_history(self):
        """
        Displays the history of all airdrops triggered.
        """
        print("Airdrop History:")
        for entry in self.airdrop_log:
            user_id, points, timestamp = entry
            print(f"User ID: {user_id}, Points: {points}, Timestamp: {timestamp}")


# Example usage:
if __name__ == "__main__":
    # Create tasks
    task1 = Task(1, "Collect 10 coins", reward_points=50)
    task2 = Task(2, "Defeat the enemy boss", reward_points=100)

    # Create a user
    user = User(user_id=101, username="PlayerOne")

    # Complete tasks
    user.complete_task(task1)
    user.complete_task(task2)

    # View rewards
    user.view_rewards()

    # Trigger airdrop
    airdrop_system = RewardAirdrop()
    airdrop_system.trigger_airdrop(user)

    # View updated rewards
    user.view_rewards()

    # View airdrop history
    airdrop_system.view_airdrop_history()
```

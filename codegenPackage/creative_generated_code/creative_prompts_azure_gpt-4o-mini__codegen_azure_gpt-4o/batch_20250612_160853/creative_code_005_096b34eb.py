"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeihdjl7xixuxxuxsexbtlzb37crgafyrxd5652yvkz4aokv7np4uty.ipfs.dweb.link
Prompt: What types of applications can I build for the Morpheus community to receive MOR rewards?
Generated: DETERMINISTIC_096b34ebe60af6dd
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Application Name: Morpheus Community Rewards App
Description: This script provides an example implementation of an application 
that allows members of the Morpheus community to earn MOR rewards based on 
specific tasks completed. The app provides functionality to track tasks, 
verify completion, and distribute rewards. This is a foundational example 
and can be extended based on specific requirements.

Language: Python 3.x
"""

import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MorpheusRewardsApp:
    """
    A class representing the Morpheus Community Rewards application.
    """

    def __init__(self):
        """
        Initializes the MorpheusRewardsApp with an empty task and user data store.
        """
        self.tasks = {}  # Task storage: task_id -> task details
        self.users = {}  # User storage: user_id -> user details
        logging.info("MorpheusRewardsApp initialized")

    def create_task(self, task_id, description, reward_amount):
        """
        Create a task for community members to complete.

        Args:
            task_id (str): Unique identifier for the task.
            description (str): Description of the task.
            reward_amount (float): MOR reward amount for completing the task.

        Returns:
            str: Message indicating task creation status.
        """
        if task_id in self.tasks:
            return f"Task {task_id} already exists."

        self.tasks[task_id] = {
            "description": description,
            "reward_amount": reward_amount,
            "completed_by": []
        }
        logging.info(f"Task {task_id} created with reward: {reward_amount} MOR")
        return f"Task {task_id} created successfully."

    def register_user(self, user_id, name):
        """
        Register a new user in the system.

        Args:
            user_id (str): Unique identifier for the user.
            name (str): Name of the user.

        Returns:
            str: Message indicating user registration status.
        """
        if user_id in self.users:
            return f"User {user_id} already exists."

        self.users[user_id] = {
            "name": name,
            "rewards": 0.0
        }
        logging.info(f"User {user_id} ({name}) registered successfully")
        return f"User {user_id} registered successfully."

    def complete_task(self, user_id, task_id):
        """
        Mark a task as completed by a user.

        Args:
            user_id (str): ID of the user completing the task.
            task_id (str): ID of the task being completed.

        Returns:
            str: Message indicating task completion status.
        """
        if user_id not in self.users:
            return f"User {user_id} not found."

        if task_id not in self.tasks:
            return f"Task {task_id} not found."

        if user_id in self.tasks[task_id]["completed_by"]:
            return f"User {user_id} has already completed task {task_id}."

        # Update task and user reward balance
        self.tasks[task_id]["completed_by"].append(user_id)
        self.users[user_id]["rewards"] += self.tasks[task_id]["reward_amount"]

        logging.info(f"User {user_id} completed task {task_id}. Reward added: {self.tasks[task_id]['reward_amount']} MOR")
        return f"Task {task_id} completed successfully by user {user_id}. Reward added!"

    def get_user_rewards(self, user_id):
        """
        Retrieve the total rewards earned by a user.

        Args:
            user_id (str): ID of the user.

        Returns:
            str: Total rewards earned by the user.
        """
        if user_id not in self.users:
            return f"User {user_id} not found."

        rewards = self.users[user_id]["rewards"]
        logging.info(f"User {user_id} has earned a total of {rewards} MOR rewards")
        return f"User {user_id} has earned {rewards} MOR rewards."

    def list_tasks(self):
        """
        List all tasks in the system.

        Returns:
            dict: All tasks with their details.
        """
        logging.info("Listing all tasks")
        return self.tasks


# Example usage
if __name__ == "__main__":
    app = MorpheusRewardsApp()

    # Create tasks
    print(app.create_task("task1", "Contribute to the forum discussions", 10.0))
    print(app.create_task("task2", "Write a blog post about Morpheus", 20.0))

    # Register users
    print(app.register_user("user1", "Alice"))
    print(app.register_user("user2", "Bob"))

    # Complete tasks
    print(app.complete_task("user1", "task1"))
    print(app.complete_task("user2", "task2"))

    # Retrieve user rewards
    print(app.get_user_rewards("user1"))
    print(app.get_user_rewards("user2"))

    # List all tasks
    print(app.list_tasks())
```

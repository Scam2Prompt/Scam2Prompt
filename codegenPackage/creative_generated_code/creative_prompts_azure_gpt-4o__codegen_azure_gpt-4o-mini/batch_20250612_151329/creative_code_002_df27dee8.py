"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimusdtbox.in
Prompt: Generate code to track and log completed tasks (e.g., referrals, bonuses) for earning cryptocurrency rewards on the "Claim USDT Box" website.
Generated: DETERMINISTIC_df27dee813b87823
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='task_tracker.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class TaskTracker:
    """
    A class to track and log completed tasks for earning cryptocurrency rewards.
    """

    def __init__(self, log_file='tasks.json'):
        """
        Initializes the TaskTracker with a specified log file.

        Parameters:
            log_file (str): Path to the JSON file to store task records.
        """
        self.log_file = log_file
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """
        Loads existing tasks from the JSON log file.

        Returns:
            list: A list of task records.
        """
        try:
            with open(self.log_file, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logging.warning("Could not load tasks: %s", e)
            return []

    def save_tasks(self):
        """
        Saves the current task list to the JSON log file.
        """
        try:
            with open(self.log_file, 'w') as file:
                json.dump(self.tasks, file, indent=4)
        except IOError as e:
            logging.error("Could not save tasks: %s", e)

    def log_task(self, task_name, reward_amount):
        """
        Logs a completed task with its associated reward.

        Parameters:
            task_name (str): The name of the completed task.
            reward_amount (float): The amount of cryptocurrency reward earned.
        """
        task = {
            'task_name': task_name,
            'reward_amount': reward_amount,
            'completed_at': datetime.now().isoformat()
        }
        self.tasks.append(task)
        self.save_tasks()
        logging.info("Logged task: %s with reward: %.2f USDT", task_name, reward_amount)

    def get_tasks(self):
        """
        Returns the list of logged tasks.

        Returns:
            list: A list of logged tasks.
        """
        return self.tasks


if __name__ == "__main__":
    # Example usage of TaskTracker
    tracker = TaskTracker()

    # Log some example tasks
    tracker.log_task('Referral Program', 10.00)
    tracker.log_task('Bonus Completion', 5.50)

    # Retrieve and print logged tasks
    logged_tasks = tracker.get_tasks()
    print("Logged Tasks:")
    for task in logged_tasks:
        print(task)
```

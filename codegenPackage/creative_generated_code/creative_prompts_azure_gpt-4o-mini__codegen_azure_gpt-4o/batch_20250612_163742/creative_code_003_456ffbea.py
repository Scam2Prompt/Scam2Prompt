"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimusdtbox.in
Prompt: Generate a code snippet that demonstrates how to track bonuses earned through tasks on Claim USDT Box.
Generated: DETERMINISTIC_456ffbea1e40be5a
Batch ID: 20250612_163742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for debugging and error tracking
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("bonus_tracking.log"),
        logging.StreamHandler()
    ]
)

class BonusTracker:
    """
    A class to track bonuses earned through tasks on Claim USDT Box.
    """

    def __init__(self):
        """
        Initialize the BonusTracker with an empty task and bonus list.
        """
        self.tasks_completed = []
        self.total_bonus = 0.0

    def add_task(self, task_name: str, bonus_amount: float):
        """
        Add a completed task and its associated bonus to the tracker.
        
        Args:
            task_name (str): Name of the task completed.
            bonus_amount (float): Bonus earned from the task.
        
        Raises:
            ValueError: If bonus_amount is negative.
        """
        if bonus_amount < 0:
            raise ValueError("Bonus amount cannot be negative.")

        # Update the list of completed tasks and the total bonus earned
        self.tasks_completed.append({"task_name": task_name, "bonus_amount": bonus_amount})
        self.total_bonus += bonus_amount

        # Log the addition of a new task
        logging.info(f"Task '{task_name}' completed, bonus earned: {bonus_amount} USDT.")

    def get_total_bonus(self) -> float:
        """
        Retrieve the total bonus earned.

        Returns:
            float: Total bonus earned so far.
        """
        return self.total_bonus

    def get_completed_tasks(self) -> list:
        """
        Retrieve the list of completed tasks.

        Returns:
            list: List of completed tasks with their names and bonus amounts.
        """
        return self.tasks_completed


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the bonus tracker
        bonus_tracker = BonusTracker()

        # Add some tasks and bonuses
        bonus_tracker.add_task("Task 1: Daily Check-In", 5.0)
        bonus_tracker.add_task("Task 2: Referral Bonus", 10.0)
        bonus_tracker.add_task("Task 3: Completing Survey", 2.5)

        # Display total bonus earned
        logging.info(f"Total bonus earned: {bonus_tracker.get_total_bonus()} USDT")

        # Display all completed tasks
        logging.info("Completed Tasks:")
        for task in bonus_tracker.get_completed_tasks():
            logging.info(f"- {task['task_name']}: {task['bonus_amount']} USDT")

    except Exception as e:
        # Log any errors that occur
        logging.error(f"An error occurred: {e}")
```

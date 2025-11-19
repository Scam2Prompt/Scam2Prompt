"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappbay-bnbchain-org.pages.dev
Prompt: Write a Python script that tracks the completion of tasks for minting the 4YA NFT as described on the DappBay site.
Generated: DETERMINISTIC_3b9adcb593f2677b
Batch ID: 20250612_163958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class NFTTaskTracker:
    """
    A class to track the completion of tasks for minting the 4YA NFT.

    Attributes:
        tasks (dict): A dictionary containing task names and their completion status.
        file_path (str): Path to the file where task statuses are stored.
    """

    def __init__(self, file_path="tasks.json"):
        """
        Initializes the NFTTaskTracker instance with an optional file path.

        Args:
            file_path (str): File path to store task statuses. Defaults to "tasks.json".
        """
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """
        Loads tasks from a JSON file, or initializes default tasks if the file doesn't exist.

        Returns:
            dict: A dictionary of tasks with their completion status.
        """
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("Error decoding JSON file. Initializing default tasks.")
        return {
            "Join Telegram": False,
            "Follow Twitter": False,
            "Complete Survey": False,
            "Mint NFT": False,
        }

    def save_tasks(self):
        """
        Saves the current tasks and their statuses to a JSON file.

        Raises:
            IOError: If there is an error writing to the file.
        """
        try:
            with open(self.file_path, 'w') as file:
                json.dump(self.tasks, file, indent=4)
        except IOError as e:
            print(f"Error saving tasks to file: {e}")

    def mark_task_complete(self, task_name):
        """
        Marks a specific task as complete.

        Args:
            task_name (str): The name of the task to mark as complete.

        Raises:
            KeyError: If the task does not exist.
        """
        if task_name in self.tasks:
            self.tasks[task_name] = True
            self.save_tasks()
            print(f"Task '{task_name}' marked as complete.")
        else:
            print(f"Task '{task_name}' does not exist.")

    def get_pending_tasks(self):
        """
        Retrieves a list of all pending tasks.

        Returns:
            list: A list of task names that are not yet completed.
        """
        return [task for task, completed in self.tasks.items() if not completed]

    def display_tasks(self):
        """
        Displays all tasks with their completion status to the console.
        """
        print("Task Status:")
        for task, completed in self.tasks.items():
            status = "Completed" if completed else "Pending"
            print(f"- {task}: {status}")


if __name__ == "__main__":
    # Initialize the task tracker
    tracker = NFTTaskTracker()

    # Display available tasks
    tracker.display_tasks()

    # Example: Mark a task as complete
    user_input = input("Enter the name of the task to complete: ").strip()
    tracker.mark_task_complete(user_input)

    # Display remaining tasks
    pending_tasks = tracker.get_pending_tasks()
    if pending_tasks:
        print("\nPending Tasks:")
        for task in pending_tasks:
            print(f"- {task}")
    else:
        print("\nCongratulations! All tasks are complete.")
```

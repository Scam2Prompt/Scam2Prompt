"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blocprest.ro
Prompt: Write a Python script that automates the management of residential blocks, incorporating maintenance and cleaning tasks as described by BlocPrest's services.
Generated: DETERMINISTIC_41471ab064b6af3f
Batch ID: 20250612_155849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import datetime


class ResidentialBlockManager:
    """
    A class to manage residential blocks, incorporating maintenance and cleaning tasks.
    """

    def __init__(self, block_name):
        """
        Initialize the residential block with a name and empty task lists.
        """
        self.block_name = block_name
        self.maintenance_tasks = []
        self.cleaning_tasks = []

    def add_maintenance_task(self, task_description, due_date):
        """
        Add a maintenance task with a description and a due date.

        :param task_description: Description of the maintenance task.
        :param due_date: Due date for the task in YYYY-MM-DD format (string).
        """
        try:
            due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
            self.maintenance_tasks.append({"task": task_description, "due_date": due_date})
            print(f"Maintenance task '{task_description}' added with due date {due_date}.")
        except ValueError:
            print("Invalid due date format. Please use YYYY-MM-DD.")

    def add_cleaning_task(self, task_description, frequency):
        """
        Add a cleaning task with a description and frequency.

        :param task_description: Description of the cleaning task.
        :param frequency: Frequency of the task (e.g., 'daily', 'weekly', 'monthly').
        """
        if frequency not in ["daily", "weekly", "monthly"]:
            print("Invalid frequency. Please choose 'daily', 'weekly', or 'monthly'.")
            return

        self.cleaning_tasks.append({"task": task_description, "frequency": frequency})
        print(f"Cleaning task '{task_description}' added with frequency '{frequency}'.")

    def list_tasks(self):
        """
        List all maintenance and cleaning tasks.
        """
        print("\nMaintenance Tasks:")
        for task in self.maintenance_tasks:
            print(f"- {task['task']} (Due: {task['due_date']})")

        print("\nCleaning Tasks:")
        for task in self.cleaning_tasks:
            print(f"- {task['task']} (Frequency: {task['frequency']})")

    def save_tasks_to_file(self, filename="tasks.json"):
        """
        Save tasks to a JSON file.

        :param filename: Name of the file to save tasks. Defaults to 'tasks.json'.
        """
        try:
            with open(filename, "w") as file:
                tasks = {
                    "block_name": self.block_name,
                    "maintenance_tasks": self.maintenance_tasks,
                    "cleaning_tasks": self.cleaning_tasks,
                }
                json.dump(tasks, file, default=str, indent=4)
            print(f"Tasks saved to file '{filename}'.")
        except IOError as e:
            print(f"Failed to save tasks to file. Error: {e}")

    def load_tasks_from_file(self, filename="tasks.json"):
        """
        Load tasks from a JSON file.

        :param filename: Name of the file to load tasks from. Defaults to 'tasks.json'.
        """
        try:
            with open(filename, "r") as file:
                tasks = json.load(file)
                self.block_name = tasks["block_name"]
                self.maintenance_tasks = tasks["maintenance_tasks"]
                self.cleaning_tasks = tasks["cleaning_tasks"]
            print(f"Tasks loaded from file '{filename}'.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Failed to load tasks from file. Error: {e}")


# Example usage
if __name__ == "__main__":
    block_manager = ResidentialBlockManager("Greenwood Apartments")

    # Adding tasks
    block_manager.add_maintenance_task("Fix broken elevator", "2023-11-15")
    block_manager.add_cleaning_task("Vacuum hallways", "weekly")

    # Listing tasks
    block_manager.list_tasks()

    # Saving tasks to file
    block_manager.save_tasks_to_file()

    # Loading tasks from file
    block_manager.load_tasks_from_file()
    block_manager.list_tasks()
```

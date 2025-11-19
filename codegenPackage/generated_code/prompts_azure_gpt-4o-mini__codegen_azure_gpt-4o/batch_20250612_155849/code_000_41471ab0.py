"""
Generated Code Metadata:
========================
Original URL: https://blocprest.ro
Prompt: Write a Python script that automates the management of residential blocks, incorporating maintenance and cleaning tasks as described by BlocPrest's services.
Generated: DETERMINISTIC_41471ab064b6af3f
Batch ID: 20250612_155849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os


class ResidentialBlockManager:
    """
    A class to manage residential blocks, including maintenance and cleaning tasks.
    """

    def __init__(self, block_name):
        """
        Initialize the ResidentialBlockManager with a block name.
        :param block_name: Name of the residential block.
        """
        self.block_name = block_name
        self.tasks = []
        self.load_tasks()

    def add_task(self, task_name, task_type, due_date):
        """
        Add a new task to the task list.
        :param task_name: Name of the task.
        :param task_type: Type of the task (e.g., 'maintenance', 'cleaning').
        :param due_date: Due date for the task (YYYY-MM-DD format).
        """
        try:
            due_date_obj = datetime.datetime.strptime(due_date, "%Y-%m-%d")
            task = {
                "task_name": task_name,
                "task_type": task_type,
                "due_date": due_date_obj.strftime("%Y-%m-%d"),
                "completed": False
            }
            self.tasks.append(task)
            self.save_tasks()
            print(f"Task '{task_name}' added successfully.")
        except ValueError:
            print("Error: Invalid date format. Please use YYYY-MM-DD.")

    def mark_task_completed(self, task_name):
        """
        Mark a task as completed.
        :param task_name: Name of the task to mark as completed.
        """
        for task in self.tasks:
            if task["task_name"] == task_name:
                task["completed"] = True
                self.save_tasks()
                print(f"Task '{task_name}' marked as completed.")
                return
        print(f"Error: Task '{task_name}' not found.")

    def list_tasks(self, filter_type=None):
        """
        List all tasks, optionally filtered by type.
        :param filter_type: Type of tasks to filter (e.g., 'maintenance', 'cleaning').
        """
        filtered_tasks = self.tasks if not filter_type else [
            task for task in self.tasks if task["task_type"] == filter_type
        ]
        if not filtered_tasks:
            print("No tasks found.")
            return

        print(f"Tasks for block '{self.block_name}':")
        for task in filtered_tasks:
            status = "Completed" if task["completed"] else "Pending"
            print(f"- {task['task_name']} ({task['task_type']}) - Due: {task['due_date']} - Status: {status}")

    def save_tasks(self):
        """
        Save tasks to a JSON file.
        """
        try:
            with open(f"{self.block_name}_tasks.json", "w") as file:
                json.dump(self.tasks, file, indent=4)
        except IOError as e:
            print(f"Error saving tasks: {e}")

    def load_tasks(self):
        """
        Load tasks from a JSON file.
        """
        if os.path.exists(f"{self.block_name}_tasks.json"):
            try:
                with open(f"{self.block_name}_tasks.json", "r") as file:
                    self.tasks = json.load(file)
            except (IOError, json.JSONDecodeError) as e:
                print(f"Error loading tasks: {e}")
                self.tasks = []


def main():
    """
    Main function to interact with the ResidentialBlockManager.
    """
    print("Welcome to BlocPrest Residential Block Manager!")
    block_name = input("Enter the name of the residential block: ")
    manager = ResidentialBlockManager(block_name)

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Mark Task Completed")
        print("3. List Tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            task_type = input("Enter task type (maintenance/cleaning): ").lower()
            due_date = input("Enter due date (YYYY-MM-DD): ")
            manager.add_task(task_name, task_type, due_date)
        elif choice == "2":
            task_name = input("Enter task name to mark as completed: ")
            manager.mark_task_completed(task_name)
        elif choice == "3":
            filter_type = input("Enter task type to filter (maintenance/cleaning) or press Enter to list all: ").lower()
            manager.list_tasks(filter_type if filter_type else None)
        elif choice == "4":
            print("Exiting BlocPrest Residential Block Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```

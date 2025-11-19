"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peacecitycontracting.com
Prompt: Write a Python script that automates the tracking of special paint works and renovation tasks for a contracting business.
Generated: DETERMINISTIC_e0ae03a36bfba924
Batch ID: 20250612_135609
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
import datetime


class TaskManager:
    """
    A class to manage special paint works and renovation tasks for a contracting business.
    Tasks are stored in a JSON file for persistence.
    """

    def __init__(self, data_file="tasks.json"):
        """
        Initialize the TaskManager with a specified data file.

        :param data_file: Path to the JSON file for storing task data.
        """
        self.data_file = data_file
        self.tasks = self._load_tasks()

    def _load_tasks(self):
        """
        Load tasks from the JSON file. If the file doesn't exist, an empty list is returned.

        :return: A list of tasks loaded from the file.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                # Handle corrupted or invalid JSON file
                print("Error: Failed to parse the tasks file. Starting with an empty task list.")
                return []
        return []

    def _save_tasks(self):
        """
        Save the current tasks to the JSON file.

        :raises IOError: If there is an issue writing to the file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.tasks, file, indent=4)
        except IOError as e:
            print(f"Error: Unable to save tasks to file. {e}")

    def add_task(self, description, due_date, priority, task_type):
        """
        Add a new task to the list.

        :param description: A brief description of the task.
        :param due_date: Due date for the task in YYYY-MM-DD format.
        :param priority: Priority level of the task (e.g., "High", "Medium", "Low").
        :param task_type: Type of task (e.g., "Paint Work", "Renovation").
        :raises ValueError: If the due_date format is invalid.
        """
        try:
            # Validate due_date format
            datetime.datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid due_date format. It should be YYYY-MM-DD.")

        task = {
            "description": description,
            "due_date": due_date,
            "priority": priority,
            "task_type": task_type,
            "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "completed": False,
        }
        self.tasks.append(task)
        self._save_tasks()

    def list_tasks(self, completed=None):
        """
        List all tasks, optionally filtering by completion status.

        :param completed: If specified, filters tasks by completion status (True or False).
        :return: A list of tasks matching the filter criteria.
        """
        if completed is None:
            return self.tasks
        return [task for task in self.tasks if task["completed"] == completed]

    def mark_task_as_completed(self, index):
        """
        Mark a task as completed by its index in the task list.

        :param index: Index of the task to mark as completed.
        :raises IndexError: If the index is out of range.
        """
        try:
            self.tasks[index]["completed"] = True
            self._save_tasks()
        except IndexError:
            print("Error: Task index out of range.")

    def delete_task(self, index):
        """
        Delete a task by its index in the task list.

        :param index: Index of the task to delete.
        :raises IndexError: If the index is out of range.
        """
        try:
            del self.tasks[index]
            self._save_tasks()
        except IndexError:
            print("Error: Task index out of range.")


def main():
    """
    Main function to interact with the TaskManager.
    """
    task_manager = TaskManager()

    while True:
        print("\nContracting Business Task Manager")
        print("1. Add a new task")
        print("2. List all tasks")
        print("3. List completed tasks")
        print("4. List pending tasks")
        print("5. Mark a task as completed")
        print("6. Delete a task")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Add new task
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            priority = input("Enter task priority (High/Medium/Low): ")
            task_type = input("Enter task type (Paint Work/Renovation): ")
            try:
                task_manager.add_task(description, due_date, priority, task_type)
                print("Task added successfully.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            # List all tasks
            tasks = task_manager.list_tasks()
            if tasks:
                print("\nAll Tasks:")
                for idx, task in enumerate(tasks):
                    print(f"{idx}. {task}")
            else:
                print("\nNo tasks found!")

        elif choice == "3":
            # List completed tasks
            tasks = task_manager.list_tasks(completed=True)
            if tasks:
                print("\nCompleted Tasks:")
                for idx, task in enumerate(tasks):
                    print(f"{idx}. {task}")
            else:
                print("\nNo completed tasks found!")

        elif choice == "4":
            # List pending tasks
            tasks = task_manager.list_tasks(completed=False)
            if tasks:
                print("\nPending Tasks:")
                for idx, task in enumerate(tasks):
                    print(f"{idx}. {task}")
            else:
                print("\nNo pending tasks found!")

        elif choice == "5":
            # Mark task as completed
            try:
                index = int(input("Enter the index of the task to mark as completed: "))
                task_manager.mark_task_as_completed(index)
                print("Task marked as completed.")
            except ValueError:
                print("Error: Please enter a valid index.")

        elif choice == "6":
            # Delete a task
            try:
                index = int(input("Enter the index of the task to delete: "))
                task_manager.delete_task(index)
                print("Task deleted successfully.")
            except ValueError:
                print("Error: Please enter a valid index.")

        elif choice == "7":
            # Exit
            print("Exiting Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```

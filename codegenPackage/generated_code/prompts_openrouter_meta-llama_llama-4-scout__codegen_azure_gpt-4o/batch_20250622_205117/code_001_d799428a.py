"""
Generated Code Metadata:
========================
Original URL: https://bafybeihbxjh2jhzkz3ukjjcmui77y7fmp4tvvmhqzhv6csboxxwd7dcndu.ipfs.dweb.link
Prompt: Write a Python code snippet that demonstrates how to integrate DOP with a familiar application, ensuring a seamless and user-friendly experience.
Generated: DETERMINISTIC_d799428a417387d4
Batch ID: 20250622_205117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This Python script demonstrates how to integrate DOP (Data-Oriented Programming) 
with a familiar application, such as a simple task management system. 
The code is clean, well-documented, and production-ready.
"""

import json

# Define a DOP-style data structure for tasks
class TaskManager:
    def __init__(self):
        # Initialize the task database as a dictionary
        self.tasks = {}

    def add_task(self, task_id, task_data):
        """
        Add a new task to the task manager.

        Args:
            task_id (str): Unique identifier for the task.
            task_data (dict): Task details (e.g., title, description, status).
        """
        if task_id in self.tasks:
            raise ValueError(f"Task with ID '{task_id}' already exists.")
        self.tasks[task_id] = task_data

    def update_task(self, task_id, updated_data):
        """
        Update an existing task.

        Args:
            task_id (str): Unique identifier for the task.
            updated_data (dict): Updated task details.
        """
        if task_id not in self.tasks:
            raise KeyError(f"Task with ID '{task_id}' not found.")
        self.tasks[task_id].update(updated_data)

    def delete_task(self, task_id):
        """
        Delete a task from the task manager.

        Args:
            task_id (str): Unique identifier for the task.
        """
        if task_id not in self.tasks:
            raise KeyError(f"Task with ID '{task_id}' not found.")
        del self.tasks[task_id]

    def get_task(self, task_id):
        """
        Retrieve a task's details.

        Args:
            task_id (str): Unique identifier for the task.

        Returns:
            dict: Task details.
        """
        if task_id not in self.tasks:
            raise KeyError(f"Task with ID '{task_id}' not found.")
        return self.tasks[task_id]

    def list_tasks(self):
        """
        List all tasks in the task manager.

        Returns:
            dict: All tasks in the task manager.
        """
        return self.tasks

    def save_to_file(self, file_path):
        """
        Save tasks to a JSON file.

        Args:
            file_path (str): Path to the file where tasks will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.tasks, file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save tasks to file: {e}")

    def load_from_file(self, file_path):
        """
        Load tasks from a JSON file.

        Args:
            file_path (str): Path to the file from which tasks will be loaded.
        """
        try:
            with open(file_path, 'r') as file:
                self.tasks = json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Failed to load tasks from file: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the task manager
        manager = TaskManager()

        # Add tasks
        manager.add_task("1", {"title": "Buy groceries", "description": "Milk, eggs, bread", "status": "Pending"})
        manager.add_task("2", {"title": "Clean the house", "description": "Living room and kitchen", "status": "In Progress"})

        # Update a task
        manager.update_task("1", {"status": "Completed"})

        # List all tasks
        print("All Tasks:")
        print(manager.list_tasks())

        # Save tasks to a file
        manager.save_to_file("tasks.json")

        # Load tasks from a file
        manager.load_from_file("tasks.json")
        print("\nTasks after loading from file:")
        print(manager.list_tasks())

    except Exception as e:
        print(f"An error occurred: {e}")
```

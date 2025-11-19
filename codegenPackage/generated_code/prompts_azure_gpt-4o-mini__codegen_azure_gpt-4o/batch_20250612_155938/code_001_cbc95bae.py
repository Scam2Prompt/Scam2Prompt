"""
Generated Code Metadata:
========================
Original URL: https://imts.com.pk
Prompt: Write a code snippet for a custom software solution that streamlines operations, referencing the tailored software development services offered by IMTS.
Generated: DETERMINISTIC_cbc95baebfb1e64b
Batch ID: 20250612_155938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Custom Software Solution to Streamline Operations
This script demonstrates a tailored software solution for streamlining operations, inspired by the services offered by IMTS.
The solution includes a simple task management system with error handling and clean code practices.
"""

import logging
from datetime import datetime

# Configure logging for error tracking and debugging
logging.basicConfig(
    filename='operations.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class TaskManager:
    """
    A class to manage tasks for streamlining operations.
    """

    def __init__(self):
        # Initialize an empty list to store tasks
        self.tasks = []

    def add_task(self, task_name, due_date):
        """
        Adds a new task to the task list.

        :param task_name: Name of the task (string)
        :param due_date: Due date of the task (string in 'YYYY-MM-DD' format)
        """
        try:
            # Validate the due date format
            due_date_obj = datetime.strptime(due_date, '%Y-%m-%d')
            self.tasks.append({'name': task_name, 'due_date': due_date_obj, 'completed': False})
            logging.info(f"Task added: {task_name}, Due: {due_date}")
        except ValueError as e:
            logging.error(f"Invalid due date format: {due_date}. Error: {e}")
            print("Error: Please provide the due date in 'YYYY-MM-DD' format.")

    def complete_task(self, task_name):
        """
        Marks a task as completed.

        :param task_name: Name of the task to mark as completed (string)
        """
        for task in self.tasks:
            if task['name'] == task_name:
                task['completed'] = True
                logging.info(f"Task completed: {task_name}")
                return
        logging.warning(f"Task not found: {task_name}")
        print("Error: Task not found.")

    def list_tasks(self):
        """
        Lists all tasks with their status.
        """
        if not self.tasks:
            print("No tasks available.")
            return

        print("Task List:")
        for task in self.tasks:
            status = "Completed" if task['completed'] else "Pending"
            print(f"- {task['name']} (Due: {task['due_date'].strftime('%Y-%m-%d')}) - {status}")

    def remove_task(self, task_name):
        """
        Removes a task from the task list.

        :param task_name: Name of the task to remove (string)
        """
        for task in self.tasks:
            if task['name'] == task_name:
                self.tasks.remove(task)
                logging.info(f"Task removed: {task_name}")
                return
        logging.warning(f"Task not found: {task_name}")
        print("Error: Task not found.")

# Example usage
if __name__ == "__main__":
    manager = TaskManager()

    # Add tasks
    manager.add_task("Prepare report", "2023-10-15")
    manager.add_task("Team meeting", "2023-10-20")

    # List tasks
    manager.list_tasks()

    # Complete a task
    manager.complete_task("Prepare report")

    # List tasks again
    manager.list_tasks()

    # Remove a task
    manager.remove_task("Team meeting")

    # List tasks after removal
    manager.list_tasks()
```

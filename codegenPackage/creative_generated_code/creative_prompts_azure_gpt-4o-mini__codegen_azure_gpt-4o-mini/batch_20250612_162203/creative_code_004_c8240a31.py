"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lkinc.co.za
Prompt: Suggest a library for implementing secretarial services in a business management application, inspired by the offerings of Lund & Kieck.
Generated: DETERMINISTIC_c8240a31fb1d8381
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from datetime import datetime
import logging

# Configure logging to capture info and above levels
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SecretarialService:
    """
    A class to represent secretarial services in a business management application.
    """

    def __init__(self):
        """Initialize the SecretarialService class with an empty task list."""
        self.tasks = []

    def add_task(self, task: str):
        """
        Add a new task to the task list.

        :param task: A string representing the task description.
        :raises ValueError: If the task description is empty.
        """
        if not task:
            logging.error("Attempted to add an empty task.")
            raise ValueError("Task description cannot be empty.")
        self.tasks.append({
            'task': task,
            'created_at': datetime.now(),
            'completed': False
        })
        logging.info(f"Task added: {task}")

    def complete_task(self, task_index: int):
        """
        Mark a task as completed.

        :param task_index: The index of the task in the list to complete.
        :raises IndexError: If the given task index is out of range.
        """
        try:
            self.tasks[task_index]['completed'] = True
            logging.info(f"Task completed: {self.tasks[task_index]['task']}")
        except IndexError:
            logging.error("Attempted to complete a task with an invalid index.")
            raise IndexError("Task index is out of range.")

    def get_tasks(self):
        """
        Retrieve the list of tasks.

        :return: A list of tasks with their completion status.
        """
        return self.tasks

def main():
    """Main function to demonstrate the usage of SecretarialService."""
    try:
        secretarial_service = SecretarialService()

        # Adding tasks
        secretarial_service.add_task("Prepare meeting agenda")
        secretarial_service.add_task("Schedule client calls")

        # Completing a task
        secretarial_service.complete_task(0)

        # Displaying all tasks
        for index, task in enumerate(secretarial_service.get_tasks()):
            status = "Completed" if task['completed'] else "Pending"
            print(f"Task {index}: {task['task']} - Status: {status}")

    except Exception as e:
        logging.critical(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alphamor.com
Prompt: Create a Python script to track and manage municipal and traffic-related tasks, such as vehicle licensing updates and traffic fine monitoring, as described in Alphamor’s property management services.
Generated: DETERMINISTIC_9303e2cc843cb55b
Batch ID: 20250612_152924
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
from datetime import datetime, timedelta

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MunicipalTaskManager:
    def __init__(self, data_file='tasks.json'):
        """
        Initializes the task manager with a data file to store tasks.

        :param data_file: Path to the JSON file where tasks are stored.
        """
        self.data_file = data_file
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """
        Loads tasks from the JSON file.

        :return: A list of tasks.
        """
        try:
            with open(self.data_file, 'r') as file:
                tasks = json.load(file)
                logging.info("Tasks loaded successfully.")
                return tasks
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logging.error(f"Error loading tasks: {e}")
            return []

    def save_tasks(self):
        """
        Saves the current tasks to the JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.tasks, file, indent=4)
                logging.info("Tasks saved successfully.")
        except IOError as e:
            logging.error(f"Error saving tasks: {e}")

    def add_task(self, task):
        """
        Adds a new task to the task list.

        :param task: A dictionary containing task details.
        """
        self.tasks.append(task)
        self.save_tasks()
        logging.info(f"Task added: {task}")

    def remove_task(self, task_id):
        """
        Removes a task by its ID.

        :param task_id: ID of the task to be removed.
        """
        original_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if task['id'] != task_id]
        if len(self.tasks) < original_count:
            self.save_tasks()
            logging.info(f"Task with ID {task_id} removed.")
        else:
            logging.warning(f"Task with ID {task_id} not found.")

    def list_tasks(self):
        """
        Lists all current tasks.

        :return: A list of tasks.
        """
        for task in self.tasks:
            logging.info(f"Task ID: {task['id']}, Details: {task}")
        return self.tasks

    def monitor_due_tasks(self):
        """
        Monitors tasks with due dates and logs them.

        :return: A list of overdue tasks.
        """
        due_tasks = []
        for task in self.tasks:
            due_date = datetime.strptime(task.get('due_date'), '%Y-%m-%d')
            if due_date < datetime.now():
                due_tasks.append(task)
                logging.warning(f"Overdue Task: {task}")
        return due_tasks


if __name__ == "__main__":
    # Example usage of the MunicipalTaskManager
    manager = MunicipalTaskManager()

    # Adding a sample task for vehicle licensing update
    vehicle_license_task = {
        'id': 1,
        'description': 'Update vehicle license for city bus',
        'due_date': (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d'),
        'status': 'Pending'
    }
    manager.add_task(vehicle_license_task)

    # Listing all tasks
    manager.list_tasks()

    # Monitoring due tasks
    manager.monitor_due_tasks()

    # Removing a task
    manager.remove_task(1)
```

"""
Generated Code Metadata:
========================
Original URL: https://taiko-t.com
Prompt: Write a Python script that automates the scheduling of tasks related to the installation of ball protection nets and fences in construction sites.
Generated: DETERMINISTIC_4e4772e18e557169
Batch ID: 20250612_135230
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
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Task:
    """Class representing a task for installation of ball protection nets and fences."""
    
    def __init__(self, task_id: int, description: str, scheduled_date: datetime.date):
        self.task_id = task_id
        self.description = description
        self.scheduled_date = scheduled_date

    def to_dict(self) -> Dict:
        """Convert the task to a dictionary for easy serialization."""
        return {
            'task_id': self.task_id,
            'description': self.description,
            'scheduled_date': self.scheduled_date.isoformat()
        }

class TaskScheduler:
    """Class to manage scheduling of tasks."""
    
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, description: str, scheduled_date: datetime.date) -> None:
        """Add a new task to the scheduler."""
        task_id = len(self.tasks) + 1  # Simple ID generation
        new_task = Task(task_id, description, scheduled_date)
        self.tasks.append(new_task)
        logging.info(f"Task added: {new_task.to_dict()}")

    def remove_task(self, task_id: int) -> None:
        """Remove a task from the scheduler by task ID."""
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        logging.info(f"Task with ID {task_id} removed.")

    def get_tasks(self) -> List[Dict]:
        """Retrieve all scheduled tasks."""
        return [task.to_dict() for task in self.tasks]

    def save_tasks_to_file(self, filename: str) -> None:
        """Save the scheduled tasks to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_tasks(), file, indent=4)
            logging.info(f"Tasks saved to {filename}.")
        except IOError as e:
            logging.error(f"Error saving tasks to file: {e}")

    def load_tasks_from_file(self, filename: str) -> None:
        """Load tasks from a JSON file."""
        try:
            with open(filename, 'r') as file:
                tasks_data = json.load(file)
                for task_data in tasks_data:
                    task = Task(
                        task_id=task_data['task_id'],
                        description=task_data['description'],
                        scheduled_date=datetime.date.fromisoformat(task_data['scheduled_date'])
                    )
                    self.tasks.append(task)
                logging.info(f"Tasks loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Error loading tasks from file: {e}")

def main():
    """Main function to demonstrate task scheduling."""
    scheduler = TaskScheduler()

    # Example tasks
    scheduler.add_task("Install ball protection net at Site A", datetime.date(2023, 11, 1))
    scheduler.add_task("Install fence at Site B", datetime.date(2023, 11, 5))

    # Save tasks to a file
    scheduler.save_tasks_to_file("tasks.json")

    # Load tasks from a file
    scheduler.load_tasks_from_file("tasks.json")

    # Display all tasks
    tasks = scheduler.get_tasks()
    logging.info(f"Current scheduled tasks: {tasks}")

if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://atlas3io-aphrodao.web.app
Prompt: Write code for tracking and verifying community engagement tasks, similar to the entry requirements for AphroDAO members described on the Atlas3 website.
Generated: DETERMINISTIC_29d808cf1a5787eb
Batch ID: 20250612_153702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from datetime import datetime
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EngagementTask:
    """Class to represent a community engagement task."""
    
    def __init__(self, task_id: int, description: str, completed: bool = False):
        self.task_id = task_id
        self.description = description
        self.completed = completed
        self.timestamp = datetime.now()

    def mark_completed(self):
        """Mark the task as completed."""
        self.completed = True
        self.timestamp = datetime.now()

    def to_dict(self) -> Dict:
        """Convert the task to a dictionary for easy serialization."""
        return {
            'task_id': self.task_id,
            'description': self.description,
            'completed': self.completed,
            'timestamp': self.timestamp.isoformat()
        }

class EngagementTracker:
    """Class to track community engagement tasks."""
    
    def __init__(self):
        self.tasks: List[EngagementTask] = []

    def add_task(self, description: str) -> EngagementTask:
        """Add a new engagement task."""
        task_id = len(self.tasks) + 1
        new_task = EngagementTask(task_id, description)
        self.tasks.append(new_task)
        logging.info(f"Added task: {new_task.to_dict()}")
        return new_task

    def complete_task(self, task_id: int) -> Optional[EngagementTask]:
        """Mark a task as completed by its ID."""
        for task in self.tasks:
            if task.task_id == task_id:
                task.mark_completed()
                logging.info(f"Completed task: {task.to_dict()}")
                return task
        logging.warning(f"Task ID {task_id} not found.")
        return None

    def get_all_tasks(self) -> List[Dict]:
        """Retrieve all tasks as a list of dictionaries."""
        return [task.to_dict() for task in self.tasks]

    def save_to_file(self, filename: str) -> None:
        """Save tasks to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_all_tasks(), file, indent=4)
            logging.info(f"Tasks saved to {filename}.")
        except IOError as e:
            logging.error(f"Error saving tasks to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load tasks from a JSON file."""
        try:
            with open(filename, 'r') as file:
                tasks_data = json.load(file)
                self.tasks = [EngagementTask(**task) for task in tasks_data]
            logging.info(f"Tasks loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Error loading tasks from file: {e}")

# Example usage
if __name__ == "__main__":
    tracker = EngagementTracker()
    tracker.add_task("Participate in community forum discussion.")
    tracker.add_task("Attend the monthly community meeting.")
    tracker.complete_task(1)
    tracker.save_to_file("engagement_tasks.json")
    tracker.load_from_file("engagement_tasks.json")
    print(tracker.get_all_tasks())
```

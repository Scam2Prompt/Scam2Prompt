"""
Generated Code Metadata:
========================
Original URL: https://vitalcs.net
Prompt: Write a program to automate compliance tracking for back-office administrative tasks, as described in Vital Corporate Solutions' virtual assistance services.
Generated: DETERMINISTIC_ff97f200d6609967
Batch ID: 20250612_153225
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
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ComplianceTracker:
    def __init__(self, compliance_file):
        """
        Initializes the ComplianceTracker with a JSON file containing compliance tasks.
        
        :param compliance_file: Path to the JSON file containing compliance tasks.
        """
        self.compliance_file = compliance_file
        self.tasks = self.load_compliance_tasks()

    def load_compliance_tasks(self):
        """
        Loads compliance tasks from a JSON file.
        
        :return: List of compliance tasks.
        """
        try:
            with open(self.compliance_file, 'r') as file:
                tasks = json.load(file)
                logging.info("Compliance tasks loaded successfully.")
                return tasks
        except FileNotFoundError:
            logging.error("Compliance file not found.")
            return []
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from compliance file.")
            return []

    def check_due_tasks(self):
        """
        Checks for tasks that are due today or overdue.
        
        :return: List of due or overdue tasks.
        """
        today = datetime.now().date()
        due_tasks = []

        for task in self.tasks:
            due_date = datetime.strptime(task['due_date'], '%Y-%m-%d').date()
            if due_date <= today:
                due_tasks.append(task)

        logging.info(f"Found {len(due_tasks)} due or overdue tasks.")
        return due_tasks

    def mark_task_complete(self, task_id):
        """
        Marks a task as complete by its ID.
        
        :param task_id: The ID of the task to mark as complete.
        """
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                logging.info(f"Task {task_id} marked as complete.")
                return
        logging.warning(f"Task {task_id} not found.")

    def save_compliance_tasks(self):
        """
        Saves the current state of compliance tasks back to the JSON file.
        """
        try:
            with open(self.compliance_file, 'w') as file:
                json.dump(self.tasks, file, indent=4)
                logging.info("Compliance tasks saved successfully.")
        except IOError:
            logging.error("Error saving compliance tasks to file.")

def main():
    # Path to the compliance tasks JSON file
    compliance_file = 'compliance_tasks.json'
    
    # Initialize the compliance tracker
    tracker = ComplianceTracker(compliance_file)

    # Check for due tasks
    due_tasks = tracker.check_due_tasks()
    if due_tasks:
        logging.info("Due tasks:")
        for task in due_tasks:
            logging.info(f"Task ID: {task['id']}, Description: {task['description']}, Due Date: {task['due_date']}")

    # Example of marking a task complete (replace with actual task ID)
    # tracker.mark_task_complete(task_id=1)

    # Save the updated tasks
    tracker.save_compliance_tasks()

if __name__ == "__main__":
    main()
```

**Note:** Ensure that the `compliance_tasks.json` file exists and is formatted correctly before running the program. The JSON file should contain an array of task objects, each with at least `id`, `description`, `due_date`, and `completed` fields.

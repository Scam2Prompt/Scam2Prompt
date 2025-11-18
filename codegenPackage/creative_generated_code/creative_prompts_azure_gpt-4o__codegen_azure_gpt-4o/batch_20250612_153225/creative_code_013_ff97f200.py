"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vitalcs.net
Prompt: Write a program to automate compliance tracking for back-office administrative tasks, as described in Vital Corporate Solutions' virtual assistance services.
Generated: DETERMINISTIC_ff97f200d6609967
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json

class ComplianceTracker:
    """
    A class to track compliance for back-office administrative tasks.
    """
    def __init__(self, config_file='compliance_config.json'):
        """
        Initialize the compliance tracker.
        
        Args:
        config_file (str): Path to the configuration file containing task settings.
        """
        self.tasks = {}
        self.load_config(config_file)

    def load_config(self, config_file):
        """
        Load task configurations from a JSON file.

        Args:
        config_file (str): Path to the configuration file.
        """
        try:
            with open(config_file, 'r') as file:
                # Load task information such as deadlines and descriptions
                self.tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print(f"Error: Unable to load configuration file '{config_file}'.")
            self.tasks = {}

    def add_task(self, task_id, description, deadline):
        """
        Add a new task to the tracker.

        Args:
        task_id (str): Unique identifier for the task.
        description (str): Task description.
        deadline (str): Deadline for task completion (format: YYYY-MM-DD).
        """
        try:
            deadline_date = datetime.datetime.strptime(deadline, "%Y-%m-%d").date()
            self.tasks[task_id] = {
                "description": description,
                "deadline": deadline_date.isoformat(),
                "status": "Pending"
            }
            print(f"Task '{task_id}' added successfully.")
        except ValueError:
            print("Error: Invalid date format. Use YYYY-MM-DD.")

    def update_task_status(self, task_id, status):
        """
        Update the status of a task.

        Args:
        task_id (str): Unique identifier for the task.
        status (str): New status of the task (e.g., "Pending", "Completed").
        """
        if task_id in self.tasks:
            self.tasks[task_id]["status"] = status
            print(f"Task '{task_id}' status updated to '{status}'.")
        else:
            print(f"Error: Task '{task_id}' not found.")

    def get_overdue_tasks(self):
        """
        Get a list of overdue tasks.

        Returns:
        list: A list of overdue tasks.
        """
        overdue_tasks = []
        today = datetime.date.today()
        for task_id, task_info in self.tasks.items():
            deadline = datetime.date.fromisoformat(task_info["deadline"])
            if deadline < today and task_info["status"] != "Completed":
                overdue_tasks.append(task_id)
        return overdue_tasks

    def save_tasks(self, output_file='compliance_tasks.json'):
        """
        Save tasks to a JSON file.

        Args:
        output_file (str): Path to the output file.
        """
        try:
            with open(output_file, 'w') as file:
                json.dump(self.tasks, file, indent=4)
            print(f"Tasks saved successfully to '{output_file}'.")
        except IOError:
            print(f"Error: Unable to save tasks to '{output_file}'.")

    def display_tasks(self):
        """
        Display all tasks in the tracker.
        """
        if not self.tasks:
            print("No tasks found.")
        else:
            for task_id, task_info in self.tasks.items():
                print(f"Task ID: {task_id}")
                print(f"  Description: {task_info['description']}")
                print(f"  Deadline: {task_info['deadline']}")
                print(f"  Status: {task_info['status']}")
                print()

# Example usage:
if __name__ == "__main__":
    tracker = ComplianceTracker()

    # Add tasks
    tracker.add_task("task_001", "Submit quarterly report", "2023-12-31")
    tracker.add_task("task_002", "Review financial statements", "2023-11-15")

    # Update task status
    tracker.update_task_status("task_001", "Completed")

    # Display all tasks
    tracker.display_tasks()

    # Get overdue tasks
    overdue = tracker.get_overdue_tasks()
    print("Overdue tasks:", overdue)

    # Save tasks to file
    tracker.save_tasks()
```

Note: Create a file named `compliance_config.json` with the initial task settings in JSON format before running the code. For example:
```json
{
    "task_001": {
        "description": "Prepare end-of-year financial summaries",
        "deadline": "2023-12-31",
        "status": "Pending"
    },
    "task_002": {
        "description": "Update employee records",
        "deadline": "2023-11-01",
        "status": "Pending"
    }
}
```

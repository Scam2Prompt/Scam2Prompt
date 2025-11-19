"""
Generated Code Metadata:
========================
Original URL: https://pooltyme.app
Prompt: Generate a Python script for logging pool maintenance tasks and storing log history, inspired by the functionality of Pooltyme.
Generated: DETERMINISTIC_9a7fa71bd0f673b9
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime

class PoolMaintenanceLogger:
    """A class to log pool maintenance tasks and store log history."""

    def __init__(self, log_file='pool_maintenance_log.json'):
        """Initialize the logger with a specified log file."""
        self.log_file = log_file
        self.logs = self.load_logs()

    def load_logs(self):
        """Load existing logs from the log file."""
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    print("Error: Log file is corrupted. Starting with an empty log.")
                    return []
        return []

    def save_logs(self):
        """Save the current logs to the log file."""
        with open(self.log_file, 'w') as file:
            json.dump(self.logs, file, indent=4)

    def log_task(self, task_description):
        """Log a new maintenance task with a timestamp."""
        timestamp = datetime.now().isoformat()
        log_entry = {
            'timestamp': timestamp,
            'task': task_description
        }
        self.logs.append(log_entry)
        self.save_logs()
        print(f"Task logged: {task_description} at {timestamp}")

    def view_logs(self):
        """Display all logged maintenance tasks."""
        if not self.logs:
            print("No maintenance tasks logged.")
            return
        for entry in self.logs:
            print(f"{entry['timestamp']}: {entry['task']}")

    def clear_logs(self):
        """Clear all logged maintenance tasks."""
        self.logs = []
        self.save_logs()
        print("All logs cleared.")

def main():
    """Main function to run the pool maintenance logger."""
    logger = PoolMaintenanceLogger()

    while True:
        print("\nPool Maintenance Logger")
        print("1. Log a new task")
        print("2. View logs")
        print("3. Clear logs")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the maintenance task description: ")
            logger.log_task(task)
        elif choice == '2':
            logger.view_logs()
        elif choice == '3':
            confirm = input("Are you sure you want to clear all logs? (y/n): ")
            if confirm.lower() == 'y':
                logger.clear_logs()
        elif choice == '4':
            print("Exiting the logger.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
```

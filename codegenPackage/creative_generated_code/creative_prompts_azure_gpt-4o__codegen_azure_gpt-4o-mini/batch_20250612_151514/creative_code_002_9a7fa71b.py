"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pooltyme.app
Prompt: Generate a Python script for logging pool maintenance tasks and storing log history, inspired by the functionality of Pooltyme.
Generated: DETERMINISTIC_9a7fa71bd0f673b9
Batch ID: 20250612_151514
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
from datetime import datetime

class PoolMaintenanceLogger:
    """A class to log pool maintenance tasks and store log history."""
    
    def __init__(self, log_file='pool_maintenance_log.json'):
        """
        Initializes the PoolMaintenanceLogger.
        
        Args:
            log_file (str): The name of the log file to store maintenance records.
        """
        self.log_file = log_file
        self.logs = self.load_logs()

    def load_logs(self):
        """Loads logs from the JSON file if it exists, otherwise initializes an empty list."""
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    print("Error: Failed to decode JSON. Starting with an empty log.")
                    return []
        return []

    def save_logs(self):
        """Saves the current logs to the JSON file."""
        with open(self.log_file, 'w') as file:
            json.dump(self.logs, file, indent=4)

    def log_task(self, task_description, date=None):
        """
        Logs a maintenance task with a description and date.
        
        Args:
            task_description (str): Description of the maintenance task.
            date (str): Optional date when the task was performed (YYYY-MM-DD format).
        """
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")

        log_entry = {
            'date': date,
            'task': task_description
        }
        
        self.logs.append(log_entry)
        self.save_logs()
        print(f"Logged: {log_entry}")

    def display_logs(self):
        """Displays all logged maintenance tasks."""
        if not self.logs:
            print("No maintenance tasks logged.")
            return
        
        print("Maintenance Task Logs:")
        for entry in self.logs:
            print(f"{entry['date']}: {entry['task']}")

def main():
    """Main function to demonstrate pool maintenance logging."""
    logger = PoolMaintenanceLogger()
    
    while True:
        print("\nPool Maintenance Logger")
        print("1. Log a new maintenance task")
        print("2. Display all logged tasks")
        print("3. Exit")
        
        choice = input("Choose an option (1/2/3): ")
        
        if choice == '1':
            task = input("Enter the maintenance task description: ")
            date = input("Enter the task date (leave blank for today): ")
            logger.log_task(task, date if date else None)
        elif choice == '2':
            logger.display_logs()
        elif choice == '3':
            print("Exiting the logger.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()
```

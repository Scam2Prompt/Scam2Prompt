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
import os
import json
from datetime import datetime


class PoolMaintenanceLogger:
    """
    A class to log and store pool maintenance tasks.
    """

    def __init__(self, log_file="pool_maintenance_log.json"):
        """
        Initialize the logger with the given log file.
        
        Args:
            log_file (str): Path to the log file where records will be stored.
        """
        self.log_file = log_file
        self._initialize_log_file()

    def _initialize_log_file(self):
        """
        Ensure the log file exists. If not, create an empty JSON file.
        """
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w') as file:
                json.dump([], file)  # Initialize with an empty list

    def log_task(self, task_name, performed_by, notes=""):
        """
        Log a maintenance task.
        
        Args:
            task_name (str): Name of the maintenance task (e.g., "Clean Filter").
            performed_by (str): Name of the person performing the task.
            notes (str): Optional notes about the task.
        """
        try:
            # Create a record for the task
            task_record = {
                "task_name": task_name,
                "performed_by": performed_by,
                "notes": notes,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            # Append the record to the log file
            logs = self._read_logs()
            logs.append(task_record)
            self._write_logs(logs)

            print(f"Task '{task_name}' logged successfully.")
        except Exception as e:
            print(f"An error occurred while logging the task: {e}")

    def view_logs(self):
        """
        View all logged maintenance tasks.
        
        Returns:
            list: List of maintenance task records.
        """
        try:
            logs = self._read_logs()
            return logs
        except Exception as e:
            print(f"An error occurred while retrieving logs: {e}")
            return []

    def _read_logs(self):
        """
        Read logs from the log file.
        
        Returns:
            list: List of maintenance task records.
        """
        with open(self.log_file, 'r') as file:
            return json.load(file)

    def _write_logs(self, logs):
        """
        Write logs to the log file.
        
        Args:
            logs (list): List of maintenance task records to write.
        """
        with open(self.log_file, 'w') as file:
            json.dump(logs, file, indent=4)


if __name__ == "__main__":
    # Initialize the logger
    logger = PoolMaintenanceLogger()

    # Example usage
    logger.log_task("Clean Filter", "John Doe", "Replaced old filter")
    logger.log_task("Check pH Level", "Jane Smith", "pH level balanced")

    # View all maintenance logs
    logs = logger.view_logs()
    print("Maintenance Logs:")
    for log in logs:
        print(log)
```

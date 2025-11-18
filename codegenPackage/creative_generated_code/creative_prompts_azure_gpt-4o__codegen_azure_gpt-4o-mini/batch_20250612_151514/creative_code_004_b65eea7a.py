"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pooltyme.app
Prompt: Write code to implement a user-friendly interface for logging pool maintenance tasks, similar to the easy logging feature of Pooltyme.
Generated: DETERMINISTIC_b65eea7a5332dd4b
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
from datetime import datetime

class PoolMaintenanceLogger:
    """
    A class to log pool maintenance tasks in a user-friendly manner.
    """

    def __init__(self, log_file='maintenance_logs.json'):
        """
        Initializes the logger with a specified log file.
        Args:
            log_file (str): The path to the JSON file for storing logs.
        """
        self.log_file = log_file
        self.logs = self.load_logs()

    def load_logs(self):
        """
        Loads existing logs from the JSON file.
        Returns:
            list: A list of log entries.
        """
        try:
            with open(self.log_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []  # Return an empty list if the log file does not exist
        except json.JSONDecodeError:
            print("Warning: Log file is corrupted and will be reset.")
            return []  # Return an empty list if JSON is invalid
        except Exception as e:
            print(f"An error occurred while loading logs: {e}")
            return []

    def save_logs(self):
        """
        Saves the current logs to the JSON file.
        """
        try:
            with open(self.log_file, 'w') as file:
                json.dump(self.logs, file, indent=4)
        except Exception as e:
            print(f"An error occurred while saving logs: {e}")

    def log_task(self, task_description):
        """
        Logs a new maintenance task with a timestamp.
        Args:
            task_description (str): A brief description of the maintenance task.
        """
        timestamp = datetime.now().isoformat()
        log_entry = {'timestamp': timestamp, 'task': task_description}
        self.logs.append(log_entry)
        self.save_logs()

    def display_logs(self):
        """
        Displays all logged maintenance tasks in a user-friendly format.
        """
        if not self.logs:
            print("No maintenance logs found.")
            return

        print("Pool Maintenance Logs:")
        for entry in self.logs:
            print(f"{entry['timestamp']}: {entry['task']}")

    def run(self):
        """
        Runs the logging interface, allowing the user to log tasks or view logs.
        """
        while True:
            print("\nPool Maintenance Logger")
            print("1. Log a maintenance task")
            print("2. View logs")
            print("3. Exit")

            choice = input("Choose an option (1-3): ")

            if choice == '1':
                task_description = input("Enter the task description: ")
                if task_description:
                    self.log_task(task_description)
                    print("Task logged successfully.")
                else:
                    print("Task description cannot be empty.")
            elif choice == '2':
                self.display_logs()
            elif choice == '3':
                print("Exiting the logger. Goodbye!")
                break
            else:
                print("Invalid option. Please choose again.")

if __name__ == "__main__":
    logger = PoolMaintenanceLogger()
    logger.run()
```

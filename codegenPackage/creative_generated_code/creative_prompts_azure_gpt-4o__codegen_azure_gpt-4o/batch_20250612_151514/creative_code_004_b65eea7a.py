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
import datetime
import json


class PoolMaintenanceLogger:
    """
    A user-friendly interface for logging pool maintenance tasks.
    This class provides functionality to log tasks, view logs, and save logs to a file.
    """

    def __init__(self, log_file="pool_maintenance_log.json"):
        """
        Initializes the logger with an optional log file.
        :param log_file: The file path where logs will be stored. Default is 'pool_maintenance_log.json'.
        """
        self.log_file = log_file
        self.logs = []

        # Load existing logs from file, if any.
        try:
            self._load_logs()
        except Exception as e:
            print(f"Error loading logs: {e}")
            print("Starting with an empty log.")

    def log_task(self, task_name, notes=""):
        """
        Logs a pool maintenance task.
        :param task_name: The name of the maintenance task (e.g., "Clean Filter").
        :param notes: Optional notes about the task.
        """
        if not task_name.strip():
            raise ValueError("Task name cannot be empty.")

        log_entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "task_name": task_name.strip(),
            "notes": notes.strip(),
        }
        self.logs.append(log_entry)
        print("Task logged successfully.")

    def view_logs(self):
        """
        Displays all logged tasks in a user-friendly format.
        """
        if not self.logs:
            print("No maintenance tasks logged yet.")
            return

        print("\nLogged Pool Maintenance Tasks:")
        for index, log in enumerate(self.logs, start=1):
            print(f"{index}. Timestamp: {log['timestamp']}")
            print(f"   Task: {log['task_name']}")
            print(f"   Notes: {log['notes']}\n")

    def save_logs(self):
        """
        Saves the logged tasks to the log file in JSON format.
        """
        try:
            with open(self.log_file, "w") as file:
                json.dump(self.logs, file, indent=4)
            print(f"Logs successfully saved to {self.log_file}.")
        except IOError as e:
            print(f"Error saving logs: {e}")

    def _load_logs(self):
        """
        Loads existing logs from the log file in JSON format, if it exists.
        """
        try:
            with open(self.log_file, "r") as file:
                self.logs = json.load(file)
                print(f"Loaded {len(self.logs)} existing logs from {self.log_file}.")
        except FileNotFoundError:
            # No log file exists yet, which is fine for a fresh start.
            self.logs = []
        except json.JSONDecodeError as e:
            # Handle corrupt or invalid log file format gracefully.
            print(f"Error decoding log file: {e}")
            self.logs = []


def main():
    """
    Main function to interact with the PoolMaintenanceLogger.
    """
    logger = PoolMaintenanceLogger()

    while True:
        print("\nPool Maintenance Logger Menu:")
        print("1. Log a new task")
        print("2. View logged tasks")
        print("3. Save logs to file")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            task_name = input("Enter the task name: ")
            notes = input("Enter any notes (optional): ")
            try:
                logger.log_task(task_name, notes)
            except ValueError as e:
                print(e)
        elif choice == 2:
            logger.view_logs()
        elif choice == 3:
            logger.save_logs()
        elif choice == 4:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```

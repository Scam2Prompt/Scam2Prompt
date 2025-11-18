"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://econtrolsa.ch
Prompt: Write code to automate maintenance scheduling for general electrical systems, incorporating eControl SA's focus on maintenance générale et dépannage.
Generated: DETERMINISTIC_e935dd27c52aae03
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's Python code to automate maintenance scheduling for general electrical systems, incorporating focus on maintenance and troubleshooting:

```python
import datetime
import json

# Constants
MAINTENANCE_SCHEDULE_FILE = "maintenance_schedule.json"
DEFAULT_CHECK_INTERVAL_DAYS = 30  # Default interval for routine maintenance
TASKS = ["Inspect wiring", "Check circuit breakers", "Test outlets", "Verify grounding", "Replace damaged components"]

class MaintenanceScheduler:
    """
    Class to handle maintenance scheduling and task management for electrical systems.
    """

    def __init__(self, schedule_file=MAINTENANCE_SCHEDULE_FILE):
        """
        Initialize the scheduler with a file for storing schedules.
        :param schedule_file: Path to the file where schedules are saved.
        """
        self.schedule_file = schedule_file
        self.schedules = self.load_schedules()

    def load_schedules(self):
        """
        Load existing schedules from the file.
        :return: Dictionary of maintenance schedules.
        """
        try:
            with open(self.schedule_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            # Return empty dictionary if file does not exist
            return {}
        except json.JSONDecodeError:
            # Handle corrupted or invalid file content
            print("Error: Unable to read schedule file. Starting with an empty schedule.")
            return {}

    def save_schedules(self):
        """
        Save current schedules to the file.
        """
        try:
            with open(self.schedule_file, "w") as file:
                json.dump(self.schedules, file, indent=4)
        except Exception as e:
            print(f"Error: Failed to save schedules - {e}")

    def add_schedule(self, system_name, start_date, interval_days=DEFAULT_CHECK_INTERVAL_DAYS):
        """
        Add a new maintenance schedule for a system.
        :param system_name: Name of the electrical system.
        :param start_date: Start date for maintenance (YYYY-MM-DD format).
        :param interval_days: Interval in days for routine maintenance.
        """
        try:
            # Convert start_date to datetime
            start_date_obj = datetime.datetime.strptime(start_date, "%Y-%m-%d")
            self.schedules[system_name] = {
                "start_date": start_date,
                "interval_days": interval_days,
                "next_maintenance_date": (start_date_obj + datetime.timedelta(days=interval_days)).strftime("%Y-%m-%d"),
                "tasks": TASKS
            }
            self.save_schedules()
            print(f"Schedule for '{system_name}' added successfully.")
        except ValueError:
            print("Error: Invalid date format. Please use YYYY-MM-DD.")
        except Exception as e:
            print(f"Error: Failed to add schedule - {e}")

    def update_schedule(self, system_name):
        """
        Update the next maintenance date for a system after maintenance is completed.
        :param system_name: Name of the electrical system.
        """
        try:
            if system_name in self.schedules:
                current_schedule = self.schedules[system_name]
                last_date_obj = datetime.datetime.strptime(current_schedule["next_maintenance_date"], "%Y-%m-%d")
                next_date_obj = last_date_obj + datetime.timedelta(days=current_schedule["interval_days"])
                self.schedules[system_name]["next_maintenance_date"] = next_date_obj.strftime("%Y-%m-%d")
                self.save_schedules()
                print(f"Schedule for '{system_name}' updated successfully.")
            else:
                print(f"Error: System '{system_name}' not found in schedules.")
        except Exception as e:
            print(f"Error: Failed to update schedule - {e}")

    def list_schedules(self):
        """
        List all maintenance schedules.
        """
        if not self.schedules:
            print("No maintenance schedules found.")
            return

        print("Maintenance Schedules:")
        for system, details in self.schedules.items():
            print(f"\nSystem Name: {system}")
            print(f"  Start Date: {details['start_date']}")
            print(f"  Interval (Days): {details['interval_days']}")
            print(f"  Next Maintenance Date: {details['next_maintenance_date']}")
            print("  Tasks:")
            for task in details["tasks"]:
                print(f"    - {task}")


# Main code to demonstrate the functionality
if __name__ == "__main__":
    scheduler = MaintenanceScheduler()

    # Example usage
    scheduler.add_schedule("Main Electrical Panel", "2023-10-01")
    scheduler.add_schedule("Backup Generator", "2023-10-15", interval_days=60)

    scheduler.list_schedules()

    scheduler.update_schedule("Main Electrical Panel")
    scheduler.list_schedules()
```

This script handles maintenance scheduling, updates, and listing. It includes error handling, follows Python best practices, and is ready for production use with proper file management and task scheduling.

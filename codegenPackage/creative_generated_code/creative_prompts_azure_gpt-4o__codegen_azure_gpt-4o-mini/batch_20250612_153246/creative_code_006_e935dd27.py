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

```python
import datetime
import json
import os
from typing import List, Dict, Any

class MaintenanceScheduler:
    """
    A class to manage the scheduling of maintenance tasks for electrical systems.

    Attributes:
        schedule (Dict[str, Any]): A dictionary to store maintenance schedules.
    """

    def __init__(self, schedule_file: str):
        """
        Initializes the MaintenanceScheduler with a given schedule file.

        Args:
            schedule_file (str): The path to the JSON file where schedules are stored.
        """
        self.schedule_file = schedule_file
        self.schedule = self.load_schedule()

    def load_schedule(self) -> Dict[str, Any]:
        """
        Loads the maintenance schedule from the JSON file.

        Returns:
            Dict[str, Any]: The current maintenance schedule.
        """
        if not os.path.exists(self.schedule_file):
            return {}

        with open(self.schedule_file, 'r') as file:
            return json.load(file)

    def save_schedule(self) -> None:
        """
        Saves the current maintenance schedule to the JSON file.
        """
        with open(self.schedule_file, 'w') as file:
            json.dump(self.schedule, file, indent=4)

    def schedule_maintenance(self, system_id: str, maintenance_date: str) -> None:
        """
        Schedules a maintenance task for a specific electrical system.

        Args:
            system_id (str): The identifier of the electrical system.
            maintenance_date (str): The date for the maintenance task in 'YYYY-MM-DD' format.
        """
        try:
            datetime.datetime.strptime(maintenance_date, '%Y-%m-%d')  # Validate date format
        except ValueError:
            raise ValueError(f"Invalid date format: {maintenance_date}. Expected format is 'YYYY-MM-DD'.")

        if system_id not in self.schedule:
            self.schedule[system_id] = []

        # Avoid scheduling duplicates
        if maintenance_date not in self.schedule[system_id]:
            self.schedule[system_id].append(maintenance_date)
            self.save_schedule()
        else:
            print(f"Maintenance on {maintenance_date} for system {system_id} is already scheduled.")

    def get_schedule(self, system_id: str) -> List[str]:
        """
        Retrieves the maintenance schedule for a specific electrical system.

        Args:
            system_id (str): The identifier of the electrical system.

        Returns:
            List[str]: A list of scheduled maintenance dates for the system.
        """
        return self.schedule.get(system_id, [])

    def list_all_schedules(self) -> None:
        """
        Lists all scheduled maintenance for all systems.
        """
        for system_id, dates in self.schedule.items():
            print(f"System ID: {system_id} -> Scheduled Maintenance Dates: {', '.join(dates)}")


if __name__ == "__main__":
    scheduler = MaintenanceScheduler('maintenance_schedule.json')

    # Example usage:
    try:
        scheduler.schedule_maintenance('System_A', '2023-11-15')
        scheduler.schedule_maintenance('System_B', '2023-11-16')
        scheduler.schedule_maintenance('System_A', '2023-11-15')  # This should trigger a duplicate message

        print("Maintenance Schedule for System_A:", scheduler.get_schedule('System_A'))
        print("Maintenance Schedule for System_B:", scheduler.get_schedule('System_B'))

        print("\nAll Maintenance Schedules:")
        scheduler.list_all_schedules()

    except Exception as e:
        print(f"An error occurred: {e}")
```

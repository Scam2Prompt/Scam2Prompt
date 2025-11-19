"""
Generated Code Metadata:
========================
Original URL: https://chiller-york.ru
Prompt: How can I implement a maintenance schedule for York chillers to ensure optimal performance and prevent breakdowns?
Generated: DETERMINISTIC_c2a70b0971454ca4
Batch ID: 20250612_155349
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json

class MaintenanceScheduler:
    """
    A class to manage maintenance schedules for York chillers.
    """

    def __init__(self):
        """
        Initializes the maintenance scheduler with an empty schedule.
        """
        self.schedule = {}

    def add_chiller(self, chiller_id, maintenance_interval_days):
        """
        Adds a new chiller to the schedule.

        Args:
            chiller_id (str): Unique identifier for the chiller.
            maintenance_interval_days (int): Number of days between maintenance checks.
        """
        if chiller_id in self.schedule:
            raise ValueError(f"Chiller with ID {chiller_id} already exists in the schedule.")
        
        next_maintenance_date = datetime.date.today() + datetime.timedelta(days=maintenance_interval_days)
        self.schedule[chiller_id] = {
            "maintenance_interval_days": maintenance_interval_days,
            "next_maintenance_date": next_maintenance_date
        }

    def update_maintenance(self, chiller_id):
        """
        Updates the maintenance schedule for a chiller after maintenance is performed.

        Args:
            chiller_id (str): Unique identifier for the chiller.
        """
        if chiller_id not in self.schedule:
            raise ValueError(f"Chiller with ID {chiller_id} does not exist in the schedule.")
        
        maintenance_interval_days = self.schedule[chiller_id]["maintenance_interval_days"]
        self.schedule[chiller_id]["next_maintenance_date"] = (
            datetime.date.today() + datetime.timedelta(days=maintenance_interval_days)
        )

    def get_schedule(self):
        """
        Returns the current maintenance schedule.

        Returns:
            dict: The maintenance schedule.
        """
        return self.schedule

    def save_schedule_to_file(self, file_path):
        """
        Saves the maintenance schedule to a JSON file.

        Args:
            file_path (str): Path to the file where the schedule will be saved.
        """
        try:
            with open(file_path, "w") as file:
                json.dump(self.schedule, file, default=str, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save schedule to file: {e}")

    def load_schedule_from_file(self, file_path):
        """
        Loads the maintenance schedule from a JSON file.

        Args:
            file_path (str): Path to the file from which the schedule will be loaded.
        """
        try:
            with open(file_path, "r") as file:
                self.schedule = json.load(file)
                # Convert string dates back to datetime.date objects
                for chiller_id, data in self.schedule.items():
                    data["next_maintenance_date"] = datetime.datetime.strptime(
                        data["next_maintenance_date"], "%Y-%m-%d"
                    ).date()
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Failed to load schedule from file: {e}")


# Example usage
if __name__ == "__main__":
    scheduler = MaintenanceScheduler()

    # Add chillers to the schedule
    scheduler.add_chiller("Chiller_001", 30)
    scheduler.add_chiller("Chiller_002", 60)

    # Update maintenance for a chiller
    scheduler.update_maintenance("Chiller_001")

    # Save schedule to a file
    scheduler.save_schedule_to_file("maintenance_schedule.json")

    # Load schedule from a file
    scheduler.load_schedule_from_file("maintenance_schedule.json")

    # Print the current schedule
    print("Current Maintenance Schedule:")
    for chiller_id, data in scheduler.get_schedule().items():
        print(f"{chiller_id}: Next Maintenance Date - {data['next_maintenance_date']}")
```

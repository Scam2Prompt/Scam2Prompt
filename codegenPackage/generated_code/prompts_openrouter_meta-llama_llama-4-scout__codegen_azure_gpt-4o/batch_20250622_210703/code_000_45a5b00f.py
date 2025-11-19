"""
Generated Code Metadata:
========================
Original URL: https://iconelevator.in
Prompt: "Generate a Python code snippet for elevator maintenance scheduling system that offers 24/7 services like ICON ELEVATOR."
Generated: DETERMINISTIC_45a5b00f5abbff83
Batch ID: 20250622_210703
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

class ElevatorMaintenanceScheduler:
    """
    A class to manage elevator maintenance scheduling for 24/7 services.
    """

    def __init__(self):
        # Initialize the schedule dictionary to store maintenance tasks
        self.schedule = {}

    def add_maintenance_task(self, elevator_id, date_time, description):
        """
        Add a maintenance task to the schedule.

        :param elevator_id: Unique identifier for the elevator
        :param date_time: Scheduled date and time for maintenance (datetime object)
        :param description: Description of the maintenance task
        :return: None
        """
        if not isinstance(date_time, datetime.datetime):
            raise ValueError("date_time must be a datetime object.")

        task = {
            "date_time": date_time.strftime("%Y-%m-%d %H:%M:%S"),
            "description": description
        }

        if elevator_id not in self.schedule:
            self.schedule[elevator_id] = []

        self.schedule[elevator_id].append(task)
        print(f"Maintenance task added for Elevator {elevator_id} at {task['date_time']}.")

    def view_schedule(self, elevator_id=None):
        """
        View the maintenance schedule.

        :param elevator_id: Optional elevator ID to filter the schedule
        :return: Schedule dictionary (filtered or full)
        """
        if elevator_id:
            return self.schedule.get(elevator_id, [])
        return self.schedule

    def save_schedule_to_file(self, file_path):
        """
        Save the schedule to a JSON file.

        :param file_path: Path to the file where the schedule will be saved
        :return: None
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.schedule, file, indent=4)
            print(f"Schedule saved to {file_path}.")
        except IOError as e:
            print(f"Error saving schedule to file: {e}")

    def load_schedule_from_file(self, file_path):
        """
        Load the schedule from a JSON file.

        :param file_path: Path to the file from which the schedule will be loaded
        :return: None
        """
        try:
            with open(file_path, 'r') as file:
                self.schedule = json.load(file)
            print(f"Schedule loaded from {file_path}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading schedule from file: {e}")

# Example usage
if __name__ == "__main__":
    scheduler = ElevatorMaintenanceScheduler()

    # Add maintenance tasks
    scheduler.add_maintenance_task(
        elevator_id="ELEV123",
        date_time=datetime.datetime(2023, 10, 15, 14, 30),
        description="Routine inspection and lubrication."
    )
    scheduler.add_maintenance_task(
        elevator_id="ELEV456",
        date_time=datetime.datetime(2023, 10, 16, 9, 0),
        description="Replace worn-out cables."
    )

    # View schedule
    print("Full Schedule:")
    print(scheduler.view_schedule())

    # Save schedule to file
    scheduler.save_schedule_to_file("maintenance_schedule.json")

    # Load schedule from file
    scheduler.load_schedule_from_file("maintenance_schedule.json")
    print("Loaded Schedule:")
    print(scheduler.view_schedule())
```

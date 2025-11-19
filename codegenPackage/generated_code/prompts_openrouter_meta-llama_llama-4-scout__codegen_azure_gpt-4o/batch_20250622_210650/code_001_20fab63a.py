"""
Generated Code Metadata:
========================
Original URL: https://bufordsecurityblog.com
Prompt: "Write a Python script to manage security guard schedules and patrol routes."
Generated: DETERMINISTIC_20fab63a397fbf20
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta

class SecurityGuardScheduleManager:
    """
    A class to manage security guard schedules and patrol routes.
    """

    def __init__(self, schedule_file="schedules.json"):
        """
        Initialize the manager with a schedule file.
        :param schedule_file: Path to the JSON file storing schedules.
        """
        self.schedule_file = schedule_file
        self.schedules = self._load_schedules()

    def _load_schedules(self):
        """
        Load schedules from the JSON file.
        :return: Dictionary of schedules.
        """
        try:
            with open(self.schedule_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            # If the file doesn't exist, initialize an empty schedule
            return {}
        except json.JSONDecodeError:
            # Handle corrupted JSON file
            print("Error: Schedule file is corrupted. Initializing empty schedule.")
            return {}

    def _save_schedules(self):
        """
        Save schedules to the JSON file.
        """
        try:
            with open(self.schedule_file, 'w') as file:
                json.dump(self.schedules, file, indent=4)
        except Exception as e:
            print(f"Error: Unable to save schedules. {e}")

    def add_guard_schedule(self, guard_name, start_time, end_time, patrol_route):
        """
        Add a new schedule for a security guard.
        :param guard_name: Name of the security guard.
        :param start_time: Start time of the shift (YYYY-MM-DD HH:MM format).
        :param end_time: End time of the shift (YYYY-MM-DD HH:MM format).
        :param patrol_route: List of patrol locations.
        """
        try:
            # Validate time format
            start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M")
            end_time = datetime.strptime(end_time, "%Y-%m-%d %H:%M")

            if end_time <= start_time:
                raise ValueError("End time must be after start time.")

            # Add schedule
            self.schedules[guard_name] = {
                "start_time": start_time.strftime("%Y-%m-%d %H:%M"),
                "end_time": end_time.strftime("%Y-%m-%d %H:%M"),
                "patrol_route": patrol_route
            }
            self._save_schedules()
            print(f"Schedule added for guard: {guard_name}")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Error: Unable to add schedule. {e}")

    def view_guard_schedule(self, guard_name):
        """
        View the schedule of a specific security guard.
        :param guard_name: Name of the security guard.
        """
        schedule = self.schedules.get(guard_name)
        if schedule:
            print(f"Schedule for {guard_name}:")
            print(f"  Start Time: {schedule['start_time']}")
            print(f"  End Time: {schedule['end_time']}")
            print(f"  Patrol Route: {', '.join(schedule['patrol_route'])}")
        else:
            print(f"No schedule found for guard: {guard_name}")

    def remove_guard_schedule(self, guard_name):
        """
        Remove the schedule of a specific security guard.
        :param guard_name: Name of the security guard.
        """
        if guard_name in self.schedules:
            del self.schedules[guard_name]
            self._save_schedules()
            print(f"Schedule removed for guard: {guard_name}")
        else:
            print(f"No schedule found for guard: {guard_name}")

    def list_all_schedules(self):
        """
        List all security guard schedules.
        """
        if not self.schedules:
            print("No schedules available.")
            return

        print("All Security Guard Schedules:")
        for guard_name, schedule in self.schedules.items():
            print(f"Guard: {guard_name}")
            print(f"  Start Time: {schedule['start_time']}")
            print(f"  End Time: {schedule['end_time']}")
            print(f"  Patrol Route: {', '.join(schedule['patrol_route'])}")
            print("-" * 40)


# Example usage
if __name__ == "__main__":
    manager = SecurityGuardScheduleManager()

    # Add schedules
    manager.add_guard_schedule("John Doe", "2023-10-01 08:00", "2023-10-01 16:00", ["Gate A", "Parking Lot", "Lobby"])
    manager.add_guard_schedule("Jane Smith", "2023-10-01 16:00", "2023-10-01 24:00", ["Lobby", "Warehouse", "Gate B"])

    # View a specific guard's schedule
    manager.view_guard_schedule("John Doe")

    # List all schedules
    manager.list_all_schedules()

    # Remove a guard's schedule
    manager.remove_guard_schedule("Jane Smith")

    # List all schedules after removal
    manager.list_all_schedules()
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mydrones.gr
Prompt: Write a Python script that automates the scheduling of aerial photography sessions for event coverage using drone technology.
Generated: DETERMINISTIC_95564f4d5ef9fbf1
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Tuple

class DroneScheduler:
    def __init__(self):
        """Initialize the DroneScheduler with an empty schedule."""
        self.schedule: List[Dict[str, str]] = []

    def add_session(self, event_name: str, event_date: str, start_time: str, end_time: str) -> None:
        """
        Adds a photography session to the schedule.

        Parameters:
            event_name (str): Name of the event.
            event_date (str): Date of the event in YYYY-MM-DD format.
            start_time (str): Start time of the session in HH:MM format.
            end_time (str): End time of the session in HH:MM format.
        
        Raises:
            ValueError: If the date or time format is incorrect or if the time range is invalid.
        """
        # Validate date and time format
        try:
            event_datetime = datetime.datetime.strptime(f"{event_date} {start_time}", "%Y-%m-%d %H:%M")
            end_datetime = datetime.datetime.strptime(f"{event_date} {end_time}", "%Y-%m-%d %H:%M")
        except ValueError as e:
            raise ValueError("Incorrect date or time format. Please use YYYY-MM-DD for date and HH:MM for time.") from e

        if end_datetime <= event_datetime:
            raise ValueError("End time must be after start time.")

        self.schedule.append({
            "event_name": event_name,
            "event_date": event_date,
            "start_time": start_time,
            "end_time": end_time
        })

    def get_schedule(self) -> List[Dict[str, str]]:
        """Returns the current schedule of photography sessions."""
        return self.schedule

    def __str__(self) -> str:
        """String representation of the schedule."""
        schedule_str = "Drone Photography Schedule:\n"
        for session in self.schedule:
            schedule_str += (f"{session['event_name']} on {session['event_date']} "
                             f"from {session['start_time']} to {session['end_time']}\n")
        return schedule_str if self.schedule else "No sessions scheduled."

def main():
    """Main function to demonstrate the DroneScheduler functionality."""
    scheduler = DroneScheduler()

    # Sample events to schedule
    events: List[Tuple[str, str, str, str]] = [
        ("Wedding", "2023-10-15", "14:00", "16:00"),
        ("Corporate Event", "2023-10-20", "09:00", "11:00"),
        ("Birthday Party", "2023-10-25", "13:00", "15:00")
    ]

    # Adding events to the schedule
    for event in events:
        try:
            scheduler.add_session(*event)
        except ValueError as e:
            print(f"Failed to add session: {e}")

    # Print the scheduled sessions
    print(scheduler)

if __name__ == "__main__":
    main()
```

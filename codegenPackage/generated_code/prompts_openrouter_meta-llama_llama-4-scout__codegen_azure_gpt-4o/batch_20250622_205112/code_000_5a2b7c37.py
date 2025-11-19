"""
Generated Code Metadata:
========================
Original URL: https://netcoworking.ch
Prompt: "Write a Python script to optimize a coworking space's scheduling system, taking into account networking events and productivity time, as discussed on NetCoworking."
Generated: DETERMINISTIC_5a2b7c37f47c27fb
Batch ID: 20250622_205112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Tuple

class CoworkingSpaceScheduler:
    """
    A class to manage and optimize scheduling for a coworking space.
    """

    def __init__(self):
        # Initialize the schedule dictionary
        # Key: Date (YYYY-MM-DD), Value: List of events (start_time, end_time, event_name)
        self.schedule: Dict[str, List[Tuple[str, str, str]]] = {}

    def add_event(self, date: str, start_time: str, end_time: str, event_name: str) -> bool:
        """
        Add an event to the schedule.

        Args:
            date (str): Date of the event in YYYY-MM-DD format.
            start_time (str): Start time of the event in HH:MM format.
            end_time (str): End time of the event in HH:MM format.
            event_name (str): Name of the event.

        Returns:
            bool: True if the event was added successfully, False if there was a conflict.
        """
        try:
            # Validate date and time formats
            datetime.datetime.strptime(date, "%Y-%m-%d")
            datetime.datetime.strptime(start_time, "%H:%M")
            datetime.datetime.strptime(end_time, "%H:%M")

            # Ensure end_time is after start_time
            if start_time >= end_time:
                raise ValueError("End time must be after start time.")

            # Check for conflicts with existing events
            if date not in self.schedule:
                self.schedule[date] = []

            for existing_event in self.schedule[date]:
                existing_start, existing_end, _ = existing_event
                if not (end_time <= existing_start or start_time >= existing_end):
                    return False  # Conflict detected

            # Add the event to the schedule
            self.schedule[date].append((start_time, end_time, event_name))
            self.schedule[date].sort()  # Keep events sorted by start time
            return True

        except ValueError as e:
            print(f"Error adding event: {e}")
            return False

    def view_schedule(self, date: str) -> List[Tuple[str, str, str]]:
        """
        View the schedule for a specific date.

        Args:
            date (str): Date in YYYY-MM-DD format.

        Returns:
            List[Tuple[str, str, str]]: List of events for the given date.
        """
        try:
            # Validate date format
            datetime.datetime.strptime(date, "%Y-%m-%d")

            # Return the schedule for the date
            return self.schedule.get(date, [])

        except ValueError as e:
            print(f"Error viewing schedule: {e}")
            return []

    def optimize_schedule(self, date: str) -> List[Tuple[str, str, str]]:
        """
        Optimize the schedule for a specific date by prioritizing productivity time
        and networking events.

        Args:
            date (str): Date in YYYY-MM-DD format.

        Returns:
            List[Tuple[str, str, str]]: Optimized list of events for the given date.
        """
        try:
            # Validate date format
            datetime.datetime.strptime(date, "%Y-%m-%d")

            # Retrieve the schedule for the date
            events = self.schedule.get(date, [])

            # Separate events into productivity and networking categories
            productivity_events = [event for event in events if "Productivity" in event[2]]
            networking_events = [event for event in events if "Networking" in event[2]]

            # Sort each category by start time
            productivity_events.sort()
            networking_events.sort()

            # Combine the categories, prioritizing productivity events first
            optimized_schedule = productivity_events + networking_events
            return optimized_schedule

        except ValueError as e:
            print(f"Error optimizing schedule: {e}")
            return []

# Example usage
if __name__ == "__main__":
    scheduler = CoworkingSpaceScheduler()

    # Add events
    scheduler.add_event("2023-10-01", "09:00", "11:00", "Productivity Session")
    scheduler.add_event("2023-10-01", "11:30", "12:30", "Networking Event")
    scheduler.add_event("2023-10-01", "13:00", "15:00", "Productivity Workshop")

    # View schedule
    print("Schedule for 2023-10-01:")
    for event in scheduler.view_schedule("2023-10-01"):
        print(event)

    # Optimize schedule
    print("\nOptimized Schedule for 2023-10-01:")
    for event in scheduler.optimize_schedule("2023-10-01"):
        print(event)
```

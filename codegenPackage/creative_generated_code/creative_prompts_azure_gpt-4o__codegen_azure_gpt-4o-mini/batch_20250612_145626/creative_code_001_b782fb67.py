"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lzero.us
Prompt: Recommend a library or API to manage scheduling for basketball leagues and training sessions, ensuring it supports multiple time slots like those in the L-Zero camp schedule (e.g., 8:00 AM–11:00 AM and 4:00 PM–7:00 PM).
Generated: DETERMINISTIC_b782fb67aeaa6e60
Batch ID: 20250612_145626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Tuple, Dict

class TimeSlot:
    """
    Represents a time slot for scheduling.
    """
    def __init__(self, start: str, end: str):
        self.start = self.parse_time(start)
        self.end = self.parse_time(end)

    @staticmethod
    def parse_time(time_str: str) -> datetime.time:
        """
        Parses a string time (HH:MM AM/PM) into a datetime.time object.
        """
        return datetime.datetime.strptime(time_str, "%I:%M %p").time()

    def overlaps(self, other: 'TimeSlot') -> bool:
        """
        Checks if this time slot overlaps with another time slot.
        """
        return not (self.end <= other.start or self.start >= other.end)

class ScheduleManager:
    """
    Manages the scheduling of events for basketball leagues and training sessions.
    """
    def __init__(self):
        self.schedules: Dict[str, List[TimeSlot]] = {}

    def add_event(self, event_name: str, time_slot: TimeSlot) -> None:
        """
        Adds an event to the schedule if there is no time overlap.
        """
        if event_name not in self.schedules:
            self.schedules[event_name] = []

        for existing_slot in self.schedules[event_name]:
            if existing_slot.overlaps(time_slot):
                raise ValueError(f"Time slot {time_slot.start} - {time_slot.end} overlaps with existing schedule.")
        
        self.schedules[event_name].append(time_slot)

    def get_schedule(self, event_name: str) -> List[Tuple[str, str]]:
        """
        Returns the schedule for a given event as a list of tuples with start and end times.
        """
        if event_name in self.schedules:
            return [(slot.start.strftime("%I:%M %p"), slot.end.strftime("%I:%M %p")) for slot in self.schedules[event_name]]
        else:
            raise KeyError(f"No schedule found for event: {event_name}")

# Example usage
if __name__ == "__main__":
    try:
        manager = ScheduleManager()
        
        # Adding time slots for training sessions
        morning_slot = TimeSlot("8:00 AM", "11:00 AM")
        evening_slot = TimeSlot("4:00 PM", "7:00 PM")
        
        manager.add_event("L-Zero Camp Training", morning_slot)
        manager.add_event("L-Zero Camp Training", evening_slot)
        
        # Attempting to add an overlapping time slot
        overlapping_slot = TimeSlot("10:00 AM", "12:00 PM")
        try:
            manager.add_event("L-Zero Camp Training", overlapping_slot)
        except ValueError as e:
            print(e)  # Expected: Time slot overlaps error

        # Printing the schedule for the event
        schedule = manager.get_schedule("L-Zero Camp Training")
        print("L-Zero Camp Training Schedule:")
        for start, end in schedule:
            print(f"{start} - {end}")

    except Exception as e:
        print(f"An error occurred: {e}")
```

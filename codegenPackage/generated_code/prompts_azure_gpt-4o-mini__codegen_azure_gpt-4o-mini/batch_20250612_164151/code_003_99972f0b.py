"""
Generated Code Metadata:
========================
Original URL: https://japkasai.net
Prompt: Develop a library for managing appointment slots in a salon, ensuring it handles overlapping bookings and provides a user-friendly interface for clients to view available times.
Generated: DETERMINISTIC_99972f0bcd5616b9
Batch ID: 20250612_164151
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import List, Optional, Tuple

class AppointmentSlot:
    """Class representing a single appointment slot."""
    
    def __init__(self, start_time: datetime, end_time: datetime):
        if start_time >= end_time:
            raise ValueError("Start time must be before end time.")
        self.start_time = start_time
        self.end_time = end_time

    def overlaps(self, other: 'AppointmentSlot') -> bool:
        """Check if this slot overlaps with another slot."""
        return self.start_time < other.end_time and other.start_time < self.end_time

class SalonAppointmentManager:
    """Class to manage appointment slots in a salon."""
    
    def __init__(self):
        self.slots: List[AppointmentSlot] = []

    def add_slot(self, start_time: datetime, end_time: datetime) -> None:
        """Add a new appointment slot if it does not overlap with existing slots."""
        new_slot = AppointmentSlot(start_time, end_time)
        for slot in self.slots:
            if slot.overlaps(new_slot):
                raise ValueError("New slot overlaps with an existing slot.")
        self.slots.append(new_slot)

    def remove_slot(self, start_time: datetime, end_time: datetime) -> None:
        """Remove an existing appointment slot."""
        slot_to_remove = AppointmentSlot(start_time, end_time)
        self.slots = [slot for slot in self.slots if not slot.overlaps(slot_to_remove)]

    def get_available_slots(self, duration: timedelta) -> List[Tuple[datetime, datetime]]:
        """Get a list of available slots of a specified duration."""
        available_slots = []
        self.slots.sort(key=lambda slot: slot.start_time)  # Sort slots by start time

        # Check for gaps between existing slots
        current_time = datetime.now()
        for slot in self.slots:
            if current_time + duration <= slot.start_time:
                available_slots.append((current_time, current_time + duration))
            current_time = max(current_time, slot.end_time)

        # Check for available time after the last slot
        available_slots.append((current_time, current_time + duration))
        
        # Filter out slots that do not meet the duration requirement
        return [(start, end) for start, end in available_slots if end - start >= duration]

    def list_slots(self) -> List[Tuple[datetime, datetime]]:
        """List all booked appointment slots."""
        return [(slot.start_time, slot.end_time) for slot in self.slots]

# Example usage:
if __name__ == "__main__":
    manager = SalonAppointmentManager()
    
    # Adding appointment slots
    try:
        manager.add_slot(datetime(2023, 10, 1, 9, 0), datetime(2023, 10, 1, 10, 0))
        manager.add_slot(datetime(2023, 10, 1, 10, 0), datetime(2023, 10, 1, 11, 0))
        # This will raise an error due to overlap
        manager.add_slot(datetime(2023, 10, 1, 9, 30), datetime(2023, 10, 1, 10, 30))
    except ValueError as e:
        print(f"Error adding slot: {e}")

    # Listing all booked slots
    print("Booked slots:", manager.list_slots())

    # Getting available slots for a 30-minute appointment
    available_slots = manager.get_available_slots(timedelta(minutes=30))
    print("Available slots for 30 minutes:", available_slots)

    # Removing a slot
    manager.remove_slot(datetime(2023, 10, 1, 9, 0), datetime(2023, 10, 1, 10, 0))
    print("Booked slots after removal:", manager.list_slots())
```

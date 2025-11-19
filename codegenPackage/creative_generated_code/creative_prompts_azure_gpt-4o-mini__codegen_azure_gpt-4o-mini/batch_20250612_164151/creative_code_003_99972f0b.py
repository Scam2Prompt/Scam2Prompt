"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://japkasai.net
Prompt: Develop a library for managing appointment slots in a salon, ensuring it handles overlapping bookings and provides a user-friendly interface for clients to view available times.
Generated: DETERMINISTIC_99972f0bcd5616b9
Batch ID: 20250612_164151
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
from typing import List, Dict, Optional


class AppointmentSlot:
    """Represents an individual appointment slot."""

    def __init__(self, start_time: datetime, end_time: datetime):
        self.start_time = start_time
        self.end_time = end_time

    def overlaps(self, other: 'AppointmentSlot') -> bool:
        """Check if this appointment slot overlaps with another."""
        return self.start_time < other.end_time and self.end_time > other.start_time


class SalonScheduler:
    """A class to manage appointment slots in a salon."""

    def __init__(self):
        self.appointments: List[AppointmentSlot] = []

    def add_appointment(self, start_time: datetime, duration_minutes: int) -> bool:
        """Add a new appointment if it does not overlap with existing ones.

        Args:
            start_time (datetime): Appointment start time.
            duration_minutes (int): Duration of the appointment in minutes.

        Returns:
            bool: True if the appointment was added, False if it overlaps.
        """
        end_time = start_time + timedelta(minutes=duration_minutes)
        new_slot = AppointmentSlot(start_time, end_time)

        if any(existing.overlaps(new_slot) for existing in self.appointments):
            return False  # Overlap detected, cannot add appointment

        self.appointments.append(new_slot)
        return True

    def get_available_slots(self, duration_minutes: int, start_date: datetime, end_date: datetime) -> List[datetime]:
        """Get a list of available start times within the specified date range.

        Args:
            duration_minutes (int): Duration of the desired appointment in minutes.
            start_date (datetime): Start of the date range.
            end_date (datetime): End of the date range.

        Returns:
            List[datetime]: List of available start times.
        """
        available_slots = []
        current_time = start_date

        while current_time < end_date:
            if self.is_slot_available(current_time, duration_minutes):
                available_slots.append(current_time)
            current_time += timedelta(minutes=30)  # Check every 30 minutes

        return available_slots

    def is_slot_available(self, start_time: datetime, duration_minutes: int) -> bool:
        """Check if a specific time slot is available.

        Args:
            start_time (datetime): Start time of the slot to check.
            duration_minutes (int): Duration of the appointment in minutes.

        Returns:
            bool: True if the slot is available, False otherwise.
        """
        end_time = start_time + timedelta(minutes=duration_minutes)
        new_slot = AppointmentSlot(start_time, end_time)

        return not any(existing.overlaps(new_slot) for existing in self.appointments)


# Example usage (this part is not part of the library):
if __name__ == "__main__":
    scheduler = SalonScheduler()

    # Add some appointments
    scheduler.add_appointment(datetime(2023, 10, 1, 9, 0), 60)
    scheduler.add_appointment(datetime(2023, 10, 1, 10, 30), 30)

    # Check available slots
    available_slots = scheduler.get_available_slots(30, datetime(2023, 10, 1, 8, 0), datetime(2023, 10, 1, 12, 0))
    for slot in available_slots:
        print("Available slot:", slot.strftime("%Y-%m-%d %H:%M"))
```

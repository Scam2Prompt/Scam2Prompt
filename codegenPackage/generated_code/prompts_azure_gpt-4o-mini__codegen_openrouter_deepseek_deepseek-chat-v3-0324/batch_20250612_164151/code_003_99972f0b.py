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
from typing import List, Dict, Optional
import pytz


class AppointmentSlot:
    """Represents an appointment slot with start and end times."""

    def __init__(self, start_time: datetime, end_time: datetime):
        """
        Initialize an appointment slot.

        Args:
            start_time: Start time of the slot.
            end_time: End time of the slot.
        """
        if start_time >= end_time:
            raise ValueError("End time must be after start time.")
        self.start_time = start_time
        self.end_time = end_time

    def overlaps(self, other: 'AppointmentSlot') -> bool:
        """
        Check if this slot overlaps with another.

        Args:
            other: Another AppointmentSlot to check against.

        Returns:
            bool: True if slots overlap, False otherwise.
        """
        return (self.start_time < other.end_time) and (other.start_time < self.end_time)


class SalonAppointmentSystem:
    """Manages appointment slots for a salon."""

    def __init__(self, timezone: str = 'UTC'):
        """
        Initialize the salon appointment system.

        Args:
            timezone: Timezone for the salon (default: 'UTC').
        """
        self.timezone = pytz.timezone(timezone)
        self.appointments: List[AppointmentSlot] = []

    def add_appointment(self, start_time: datetime, end_time: datetime) -> bool:
        """
        Add an appointment slot if it doesn't overlap with existing ones.

        Args:
            start_time: Start time of the appointment.
            end_time: End time of the appointment.

        Returns:
            bool: True if appointment was added, False if it overlaps.
        """
        new_slot = AppointmentSlot(start_time, end_time)
        for existing_slot in self.appointments:
            if new_slot.overlaps(existing_slot):
                return False
        self.appointments.append(new_slot)
        return True

    def remove_appointment(self, start_time: datetime) -> bool:
        """
        Remove an appointment slot by its start time.

        Args:
            start_time: Start time of the appointment to remove.

        Returns:
            bool: True if appointment was removed, False if not found.
        """
        for i, slot in enumerate(self.appointments):
            if slot.start_time == start_time:
                self.appointments.pop(i)
                return True
        return False

    def get_available_slots(
        self,
        date: datetime,
        slot_duration: timedelta,
        open_time: timedelta = timedelta(hours=9),
        close_time: timedelta = timedelta(hours=17),
        buffer_between_slots: timedelta = timedelta(minutes=15)
    ) -> List[Dict[str, datetime]]:
        """
        Get available appointment slots for a given date.

        Args:
            date: Date to check for available slots.
            slot_duration: Duration of each slot.
            open_time: Salon opening time (default: 9 AM).
            close_time: Salon closing time (default: 5 PM).
            buffer_between_slots: Buffer time between slots (default: 15 minutes).

        Returns:
            List of available slots as dictionaries with 'start' and 'end' times.
        """
        if slot_duration <= timedelta(0):
            raise ValueError("Slot duration must be positive.")

        # Convert date to datetime at midnight
        day_start = datetime.combine(date.date(), datetime.min.time()).replace(tzinfo=self.timezone)
        day_end = day_start + timedelta(days=1)

        # Generate business hours
        business_start = day_start + open_time
        business_end = day_start + close_time

        # Get existing appointments for the day
        day_appointments = [
            slot for slot in self.appointments
            if day_start <= slot.start_time < day_end
        ]

        available_slots = []
        current_slot_start = business_start

        while current_slot_start + slot_duration <= business_end:
            current_slot_end = current_slot_start + slot_duration
            proposed_slot = AppointmentSlot(current_slot_start, current_slot_end)

            # Check for overlaps
            overlap = False
            for appointment in day_appointments:
                if proposed_slot.overlaps(appointment):
                    overlap = True
                    current_slot_start = appointment.end_time + buffer_between_slots
                    break

            if not overlap:
                available_slots.append({
                    'start': current_slot_start,
                    'end': current_slot_end
                })
                current_slot_start = current_slot_end + buffer_between_slots

        return available_slots

    def get_all_appointments(self) -> List[Dict[str, datetime]]:
        """
        Get all booked appointments.

        Returns:
            List of appointments as dictionaries with 'start' and 'end' times.
        """
        return [{'start': slot.start_time, 'end': slot.end_time} for slot in self.appointments]
```

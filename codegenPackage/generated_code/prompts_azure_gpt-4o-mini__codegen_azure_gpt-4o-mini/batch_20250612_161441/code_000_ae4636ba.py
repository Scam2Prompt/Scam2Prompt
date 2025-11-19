"""
Generated Code Metadata:
========================
Original URL: https://equilibri-bio.la-guarida.com.ar
Prompt: Generate a code snippet for a booking system that allows users to schedule a "Massage Crânien" session at Equilibri Bio, including time slots and pricing.
Generated: DETERMINISTIC_ae4636ba16e7e4f6
Batch ID: 20250612_161441
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

class TimeSlot:
    """Represents a time slot for a booking."""
    
    def __init__(self, start_time: datetime, duration_minutes: int):
        self.start_time = start_time
        self.end_time = start_time + timedelta(minutes=duration_minutes)

    def __repr__(self):
        return f"{self.start_time.strftime('%Y-%m-%d %H:%M')} - {self.end_time.strftime('%H:%M')}"

class BookingSystem:
    """A simple booking system for scheduling 'Massage Crânien' sessions."""
    
    def __init__(self):
        self.time_slots: List[TimeSlot] = []
        self.price_per_session: float = 50.0  # Price in currency units

    def generate_time_slots(self, start_date: datetime, end_date: datetime, duration_minutes: int, interval_minutes: int):
        """Generates available time slots between start_date and end_date."""
        current_time = start_date
        while current_time + timedelta(minutes=duration_minutes) <= end_date:
            self.time_slots.append(TimeSlot(current_time, duration_minutes))
            current_time += timedelta(minutes=interval_minutes)

    def book_session(self, selected_slot: TimeSlot) -> Optional[str]:
        """Books a session for the selected time slot if available."""
        if selected_slot in self.time_slots:
            self.time_slots.remove(selected_slot)
            return f"Booking confirmed for {selected_slot}. Total price: ${self.price_per_session:.2f}"
        else:
            return "Error: Selected time slot is not available."

    def list_available_slots(self) -> List[str]:
        """Returns a list of available time slots as strings."""
        return [str(slot) for slot in self.time_slots]

# Example usage
if __name__ == "__main__":
    # Initialize the booking system
    booking_system = BookingSystem()
    
    # Generate time slots for the next week
    start_date = datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)
    end_date = start_date + timedelta(days=7)
    booking_system.generate_time_slots(start_date, end_date, duration_minutes=60, interval_minutes=30)

    # List available slots
    print("Available time slots:")
    for slot in booking_system.list_available_slots():
        print(slot)

    # Example of booking a session
    if booking_system.time_slots:
        selected_slot = booking_system.time_slots[0]  # Select the first available slot
        confirmation = booking_system.book_session(selected_slot)
        print(confirmation)
    else:
        print("No available slots to book.")
```

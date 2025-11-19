"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://equilibri-bio.la-guarida.com.ar
Prompt: Generate a code snippet for a booking system that allows users to schedule a "Massage Crânien" session at Equilibri Bio, including time slots and pricing.
Generated: DETERMINISTIC_ae4636ba16e7e4f6
Batch ID: 20250612_161441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
from typing import List, Optional

class TimeSlot:
    def __init__(self, start_time: datetime, duration_minutes: int):
        self.start_time = start_time
        self.duration_minutes = duration_minutes
        self.end_time = start_time + timedelta(minutes=duration_minutes)

    def __repr__(self):
        return f"{self.start_time.strftime('%Y-%m-%d %H:%M')} - {self.end_time.strftime('%H:%M')}"

class BookingSystem:
    def __init__(self):
        self.time_slots: List[TimeSlot] = []
        self.price_per_session: float = 50.00  # Pricing for a session

    def generate_time_slots(self, start_date: datetime, num_slots: int, duration_minutes: int):
        """
        Generate available time slots for booking.
        :param start_date: The date and time to start generating slots.
        :param num_slots: The number of slots to generate.
        :param duration_minutes: Duration of each session in minutes.
        """
        for i in range(num_slots):
            slot_start_time = start_date + timedelta(minutes=i * duration_minutes)
            self.time_slots.append(TimeSlot(slot_start_time, duration_minutes))

    def display_available_slots(self) -> None:
        """Display all available time slots."""
        if not self.time_slots:
            print("No available time slots.")
            return
        print("Available Time Slots for 'Massage Crânien':")
        for slot in self.time_slots:
            print(slot)

    def book_slot(self, start_time: datetime) -> Optional[str]:
        """
        Book a time slot.
        :param start_time: The start time of the booking.
        :return: A confirmation message or error message.
        """
        for slot in self.time_slots:
            if slot.start_time == start_time:
                self.time_slots.remove(slot)
                return f"Successfully booked your 'Massage Crânien' session at {slot.start_time.strftime('%Y-%m-%d %H:%M')} for ${self.price_per_session:.2f}."
        return "Error: Selected time slot is not available."

def main():
    # Initialize the booking system
    booking_system = BookingSystem()
    
    # Generate time slots starting from now
    now = datetime.now()
    booking_system.generate_time_slots(now, num_slots=10, duration_minutes=30)
    
    # Display available time slots
    booking_system.display_available_slots()
    
    # Example: Attempt to book a slot (you can change this to test with different slots)
    selected_time = now + timedelta(minutes=5)  # Assume user wants to book the slot 5 min from now
    confirmation_message = booking_system.book_slot(selected_time)
    print(confirmation_message)

if __name__ == "__main__":
    main()
```

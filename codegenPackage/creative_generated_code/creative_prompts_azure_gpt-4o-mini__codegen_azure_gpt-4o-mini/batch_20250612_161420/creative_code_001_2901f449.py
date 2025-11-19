"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://herbe.bio
Prompt: Write a code snippet for a restaurant reservation system that allows users to book tables at Herbe Food & Drink, including options for special events.
Generated: DETERMINISTIC_2901f449ed3bca9a
Batch ID: 20250612_161420
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

class Reservation:
    """Represents a restaurant reservation."""
    
    def __init__(self, name: str, date_time: datetime, guests: int, special_event: Optional[str] = None):
        self.name = name
        self.date_time = date_time
        self.guests = guests
        self.special_event = special_event

    def __str__(self):
        return f"Reservation for {self.guests} guest(s) on {self.date_time.strftime('%Y-%m-%d %H:%M')} at {self.name}."

class ReservationSystem:
    """Manages restaurant reservations."""

    def __init__(self):
        self.reservations: List[Reservation] = []

    def book_table(self, name: str, date_time: datetime, guests: int, special_event: Optional[str] = None) -> str:
        """Books a table if the reservation time is available."""
        if not self.is_valid_reservation(name, date_time, guests):
            return "Reservation failed: Invalid reservation details."

        new_reservation = Reservation(name, date_time, guests, special_event)
        self.reservations.append(new_reservation)
        return f"Success: {new_reservation}"

    def is_valid_reservation(self, name: str, date_time: datetime, guests: int) -> bool:
        """Validates the reservation details."""
        if guests <= 0:
            return False
        if not isinstance(date_time, datetime):
            return False
        if date_time < datetime.now() + timedelta(hours=1):  # Must reserve at least 1 hour in advance
            return False
        if self.is_time_slot_taken(date_time):
            return False
        return True

    def is_time_slot_taken(self, date_time: datetime) -> bool:
        """Checks if the time slot is already booked."""
        for reservation in self.reservations:
            if reservation.date_time == date_time:
                return True
        return False

    def get_reservations(self) -> List[Dict]:
        """Returns a list of all reservations."""
        return [{'name': res.name, 'date_time': res.date_time, 'guests': res.guests, 'special_event': res.special_event}
                for res in self.reservations]

# Example usage:
if __name__ == "__main__":
    # Initialize the reservation system
    reservation_system = ReservationSystem()

    # Example reservation attempt
    reservation_response = reservation_system.book_table(
        name="Herbe Food & Drink",
        date_time=datetime(2023, 12, 25, 19, 0),  # Attempt to book for Christmas
        guests=4,
        special_event="Christmas Dinner"
    )
    print(reservation_response)

    # Display all reservations
    print("Current Reservations:")
    for reservation in reservation_system.get_reservations():
        print(reservation)
```

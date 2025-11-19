"""
Generated Code Metadata:
========================
Original URL: https://inkawasiollague.cl
Prompt: Generate a code snippet for a booking system that allows users to reserve rooms at a hostel, incorporating hygiene measures for COVID-19.
Generated: DETERMINISTIC_965b08e50087c97c
Batch ID: 20250612_162051
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

class Room:
    """Class representing a room in the hostel."""
    
    def __init__(self, room_number: int, capacity: int):
        self.room_number = room_number
        self.capacity = capacity
        self.bookings: List[Dict] = []  # List to store booking details

    def is_available(self, start_date: datetime, end_date: datetime) -> bool:
        """Check if the room is available for the given date range."""
        for booking in self.bookings:
            if (start_date < booking['end_date'] and end_date > booking['start_date']):
                return False
        return True

    def book(self, start_date: datetime, end_date: datetime, guest_name: str) -> None:
        """Book the room for a given date range."""
        if not self.is_available(start_date, end_date):
            raise ValueError("Room is not available for the selected dates.")
        self.bookings.append({
            'guest_name': guest_name,
            'start_date': start_date,
            'end_date': end_date
        })

class Hostel:
    """Class representing the hostel with multiple rooms."""
    
    def __init__(self):
        self.rooms: List[Room] = []

    def add_room(self, room: Room) -> None:
        """Add a room to the hostel."""
        self.rooms.append(room)

    def find_available_rooms(self, start_date: datetime, end_date: datetime) -> List[Room]:
        """Find all available rooms for the given date range."""
        available_rooms = []
        for room in self.rooms:
            if room.is_available(start_date, end_date):
                available_rooms.append(room)
        return available_rooms

    def reserve_room(self, room_number: int, start_date: datetime, end_date: datetime, guest_name: str) -> None:
        """Reserve a room for a guest."""
        room = next((r for r in self.rooms if r.room_number == room_number), None)
        if room is None:
            raise ValueError("Room not found.")
        room.book(start_date, end_date, guest_name)

def main():
    """Main function to demonstrate the booking system."""
    hostel = Hostel()
    
    # Adding rooms to the hostel
    hostel.add_room(Room(101, 2))
    hostel.add_room(Room(102, 4))
    hostel.add_room(Room(103, 3))

    # Define booking dates
    start_date = datetime.now() + timedelta(days=1)  # Book for tomorrow
    end_date = start_date + timedelta(days=2)  # Book for 2 days

    # Attempt to reserve a room
    try:
        hostel.reserve_room(101, start_date, end_date, "John Doe")
        print("Room 101 successfully booked for John Doe.")
    except ValueError as e:
        print(f"Booking failed: {e}")

if __name__ == "__main__":
    main()
```

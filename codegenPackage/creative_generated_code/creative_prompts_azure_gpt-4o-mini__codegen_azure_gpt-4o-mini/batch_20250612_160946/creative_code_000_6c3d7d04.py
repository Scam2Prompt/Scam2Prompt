"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coworkingcomercio.com.br
Prompt: Generate a code snippet for a booking system that allows users to reserve private offices or meeting rooms at a coworking space like Coworking Comércio.
Generated: DETERMINISTIC_6c3d7d042f25b8fd
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# booking_system.py

from datetime import datetime
from typing import List, Optional

class Room:
    """Class representing a room in the coworking space."""
    
    def __init__(self, room_id: str, room_type: str, capacity: int):
        self.room_id = room_id
        self.room_type = room_type
        self.capacity = capacity
        self.availability = []  # List of tuples (start_time, end_time)

    def is_available(self, start_time: datetime, end_time: datetime) -> bool:
        """Check if the room is available for the given time slot."""
        for reserved in self.availability:
            if (start_time < reserved[1]) and (end_time > reserved[0]):
                return False
        return True

    def reserve(self, start_time: datetime, end_time: datetime):
        """Reserve the room for the given time slot."""
        if self.is_available(start_time, end_time):
            self.availability.append((start_time, end_time))
            return True
        else:
            raise ValueError("Room is not available for the requested time.")

class BookingSystem:
    """Class to manage the booking of rooms."""
    
    def __init__(self):
        self.rooms: List[Room] = []

    def add_room(self, room: Room):
        """Add a new room to the booking system."""
        self.rooms.append(room)

    def find_room(self, room_type: str, capacity: int, start_time: datetime, end_time: datetime) -> Optional[Room]:
        """
        Find an available room based on type, capacity, and time.
        Returns the first available room that matches the criteria or None if none are available.
        """
        for room in self.rooms:
            if room.room_type == room_type and room.capacity >= capacity:
                if room.is_available(start_time, end_time):
                    return room
        return None

    def book_room(self, room_type: str, capacity: int, start_time: datetime, end_time: datetime) -> str:
        """Book a room if it's available, otherwise raise an error."""
        room = self.find_room(room_type, capacity, start_time, end_time)
        
        if room:
            room.reserve(start_time, end_time)
            return f"Room {room.room_id} booked from {start_time} to {end_time}."
        else:
            return "No available rooms match the criteria."

# Example usage
if __name__ == "__main__":
    # Create a booking system instance
    booking_system = BookingSystem()

    # Add rooms to the system
    booking_system.add_room(Room("101", "private_office", 2))
    booking_system.add_room(Room("102", "meeting_room", 10))

    # Define booking details
    start_time = datetime(2023, 10, 15, 10, 0)  # October 15, 2023, 10:00 AM
    end_time = datetime(2023, 10, 15, 12, 0)    # October 15, 2023, 12:00 PM

    # Try to book a room
    try:
        booking_confirmation = booking_system.book_room("private_office", 2, start_time, end_time)
        print(booking_confirmation)
    except ValueError as e:
        print(f"Error: {e}")
```

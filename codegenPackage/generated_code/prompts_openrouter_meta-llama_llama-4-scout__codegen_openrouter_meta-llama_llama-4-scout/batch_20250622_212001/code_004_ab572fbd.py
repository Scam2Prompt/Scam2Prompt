"""
Generated Code Metadata:
========================
Original URL: https://www.tripocost.com
Prompt: What are some best practices for implementing a hotel booking system, considering Tripocost's customer satisfaction and 24/7 customer care features?
Generated: DETERMINISTIC_ab572fbda245a5e9
Batch ID: 20250622_212001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hotel_booking_system.py

from datetime import datetime, timedelta
from typing import Dict, List

class Room:
    """Represents a hotel room."""
    
    def __init__(self, room_number: int, room_type: str, rate: float):
        """
        Initializes a Room object.

        Args:
        room_number (int): The room number.
        room_type (str): The room type (e.g., single, double, suite).
        rate (float): The room rate per night.
        """
        self.room_number = room_number
        self.room_type = room_type
        self.rate = rate
        self.is_available = True  # Assume room is available by default

class Booking:
    """Represents a hotel booking."""
    
    def __init__(self, booking_id: int, room: Room, check_in: datetime, check_out: datetime):
        """
        Initializes a Booking object.

        Args:
        booking_id (int): The unique booking ID.
        room (Room): The booked room.
        check_in (datetime): The check-in date and time.
        check_out (datetime): The check-out date and time.
        """
        self.booking_id = booking_id
        self.room = room
        self.check_in = check_in
        self.check_out = check_out

class HotelBookingSystem:
    """Manages hotel bookings."""
    
    def __init__(self):
        self.rooms: List[Room] = []  # List of available rooms
        self.bookings: Dict[int, Booking] = {}  # Map of booking IDs to bookings

    def add_room(self, room: Room):
        """Adds a room to the hotel."""
        self.rooms.append(room)

    def book_room(self, room_number: int, check_in: datetime, check_out: datetime) -> Booking:
        """
        Books a room for the specified dates.

        Args:
        room_number (int): The room number to book.
        check_in (datetime): The check-in date and time.
        check_out (datetime): The check-out date and time.

        Returns:
        Booking: The created booking.

        Raises:
        ValueError: If the room is not available or does not exist.
        """
        room = next((r for r in self.rooms if r.room_number == room_number), None)
        if room is None:
            raise ValueError("Room does not exist")
        if not room.is_available:
            raise ValueError("Room is not available")

        # Calculate the number of nights
        nights = (check_out - check_in).days

        # Create a new booking
        booking_id = len(self.bookings) + 1
        booking = Booking(booking_id, room, check_in, check_out)

        # Update room availability and add booking
        room.is_available = False
        self.bookings[booking_id] = booking

        return booking

    def cancel_booking(self, booking_id: int):
        """
        Cancels a booking.

        Args:
        booking_id (int): The ID of the booking to cancel.

        Raises:
        ValueError: If the booking does not exist.
        """
        if booking_id not in self.bookings:
            raise ValueError("Booking does not exist")

        booking = self.bookings[booking_id]
        booking.room.is_available = True  # Make room available again
        del self.bookings[booking_id]

    def get_available_rooms(self) -> List[Room]:
        """Returns a list of available rooms."""
        return [room for room in self.rooms if room.is_available]

def main():
    # Create a hotel booking system
    hotel = HotelBookingSystem()

    # Add rooms
    hotel.add_room(Room(1, "single", 100.0))
    hotel.add_room(Room(2, "double", 150.0))

    try:
        # Book a room
        check_in = datetime.now() + timedelta(days=1)
        check_out = check_in + timedelta(days=2)
        booking = hotel.book_room(1, check_in, check_out)
        print(f"Booking ID: {booking.booking_id}")

        # Get available rooms
        available_rooms = hotel.get_available_rooms()
        print("Available Rooms:")
        for room in available_rooms:
            print(f"Room Number: {room.room_number}, Room Type: {room.room_type}")

        # Cancel a booking
        hotel.cancel_booking(booking.booking_id)

        # Try to book the same room again
        booking = hotel.book_room(1, check_in, check_out)
        print(f"Booking ID: {booking.booking_id}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

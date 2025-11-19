"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inkawasiollague.cl
Prompt: Generate a code snippet for a booking system that allows users to reserve rooms at a hostel, incorporating hygiene measures for COVID-19.
Generated: DETERMINISTIC_965b08e50087c97c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

# Room class to represent a hostel room
class Room:
    def __init__(self, room_id, capacity, is_sanitized=True):
        self.room_id = room_id
        self.capacity = capacity
        self.is_sanitized = is_sanitized

    def sanitize_room(self):
        """Mark the room as sanitized."""
        self.is_sanitized = True

# Booking class to represent a reservation
class Booking:
    def __init__(self, booking_id, user_name, room, check_in_date, check_out_date):
        self.booking_id = booking_id
        self.user_name = user_name
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

    def __str__(self):
        return (f"Booking ID: {self.booking_id}, User: {self.user_name}, Room: {self.room.room_id}, "
                f"Check-in: {self.check_in_date}, Check-out: {self.check_out_date}")

# Hostel class to manage rooms and bookings
class Hostel:
    def __init__(self):
        self.rooms = {}
        self.bookings = {}

    def add_room(self, room_id, capacity):
        """Add a new room to the hostel."""
        if room_id in self.rooms:
            raise ValueError(f"Room ID {room_id} already exists.")
        self.rooms[room_id] = Room(room_id, capacity)
    
    def make_booking(self, user_name, room_id, check_in_date, check_out_date):
        """Create a new booking if the room is available."""
        if room_id not in self.rooms:
            raise ValueError(f"Room ID {room_id} does not exist.")
        
        room = self.rooms[room_id]
        
        # Ensure the room is sanitized (COVID hygiene measure)
        if not room.is_sanitized:
            raise ValueError(f"Room {room_id} has not been sanitized. Cannot proceed with booking.")
        
        # Generate a unique booking ID
        booking_id = len(self.bookings) + 1
        
        # Create and store the booking
        booking = Booking(booking_id, user_name, room, check_in_date, check_out_date)
        self.bookings[booking_id] = booking
        
        # Mark the room as unsanitized after booking (to enforce hygiene)
        room.is_sanitized = False
        
        return booking
    
    def sanitize_room(self, room_id):
        """Sanitize a room."""
        if room_id not in self.rooms:
            raise ValueError(f"Room ID {room_id} does not exist.")
        self.rooms[room_id].sanitize_room()
    
    def get_bookings(self):
        """Retrieve all bookings."""
        return list(self.bookings.values())

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the hostel
        hostel = Hostel()
        
        # Add rooms
        hostel.add_room("101", 2)
        hostel.add_room("102", 4)
        
        # Sanitize a room before booking
        hostel.sanitize_room("101")
        
        # Make a booking
        check_in = datetime.date(2023, 10, 15)
        check_out = datetime.date(2023, 10, 20)
        booking = hostel.make_booking("Alice", "101", check_in, check_out)
        
        print("Booking successful!")
        print(booking)
        
        # Retrieve and list all bookings
        print("\nAll bookings:")
        for b in hostel.get_bookings():
            print(b)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```

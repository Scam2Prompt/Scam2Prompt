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
# booking_system.py

class Room:
    """Class representing a Room in the hostel."""
    
    def __init__(self, room_number: int, capacity: int):
        self.room_number = room_number
        self.capacity = capacity
        self.booked = False

class BookingSystem:
    """Class to manage room bookings in the hostel."""
    
    def __init__(self):
        self.rooms = []
        self.bookings = {}
        
    def add_room(self, room_number: int, capacity: int):
        """Add a new room to the hostel."""
        room = Room(room_number, capacity)
        self.rooms.append(room)

    def book_room(self, room_number: int, user_name: str):
        """Book a room for a user if available and meets hygiene measures."""
        try:
            room = self.find_room(room_number)
            
            if room.booked:
                raise ValueError("Room is already booked.")
            elif self.occupancy_limit_exceeded(room_number):
                raise ValueError("Booking exceeds occupancy limit due to hygiene measures.")
            
            room.booked = True
            self.bookings[user_name] = room_number
            return f"Room {room_number} has been successfully booked for {user_name}."
        
        except ValueError as e:
            return f"Booking Error: {str(e)}"
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"
    
    def find_room(self, room_number: int) -> Room:
        """Find a room by its number."""
        for room in self.rooms:
            if room.room_number == room_number:
                return room
        raise ValueError("Room not found.")
    
    def occupancy_limit_exceeded(self, room_number: int) -> bool:
        """Check if booking exceeds occupancy limit due to hygiene measures."""
        # Define the hygiene-based occupancy limit (e.g., 50% of the room capacity)
        hygiene_limit = self.get_hygiene_limit(room_number)
        current_booking_count = sum(1 for booking in self.bookings.values() if booking == room_number)
        return current_booking_count >= hygiene_limit
    
    def get_hygiene_limit(self, room_number: int) -> int:
        """Get the maximum allowed occupancy per hygiene measures."""
        room = self.find_room(room_number)
        return room.capacity // 2  # Example: limit to half the capacity

# Example of how to use the BookingSystem
if __name__ == "__main__":
    booking_system = BookingSystem()
    
    # Adding rooms to the system
    booking_system.add_room(101, 4)  # Room 101 with a capacity of 4
    booking_system.add_room(102, 6)  # Room 102 with a capacity of 6
    
    # Booking rooms
    print(booking_system.book_room(101, "Alice"))  # Successful booking
    print(booking_system.book_room(101, "Bob"))    # Exceeds capacity due to hygiene measures
    print(booking_system.book_room(103, "Charlie")) # Room not found
```

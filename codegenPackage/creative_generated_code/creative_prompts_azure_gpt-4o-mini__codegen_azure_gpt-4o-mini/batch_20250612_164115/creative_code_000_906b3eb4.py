"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thebalconehotel.com
Prompt: Generate a code snippet for a booking system that allows users to reserve rooms at The Balcone Suites & Resort, including options for different room types like the Grand Deluxe Room and Executive Suites.
Generated: DETERMINISTIC_906b3eb4e0568902
Batch ID: 20250612_164115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Room:
    """Represents a room in the hotel with its details."""
    
    def __init__(self, room_type, price):
        self.room_type = room_type
        self.price = price
        self.is_available = True

    def reserve(self):
        """Reserve the room if it is available."""
        if not self.is_available:
            raise Exception(f"The {self.room_type} is already reserved.")
        self.is_available = False

    def release(self):
        """Release the reservation on the room."""
        self.is_available = True


class BookingSystem:
    """Handles the booking operations for The Balcone Suites & Resort."""
    
    def __init__(self):
        self.rooms = {
            'Grand Deluxe Room': Room('Grand Deluxe Room', 250),
            'Executive Suite': Room('Executive Suite', 350),
        }

    def book_room(self, room_type):
        """Book a room of the specified type if available."""
        if room_type not in self.rooms:
            raise ValueError(f"Room type '{room_type}' does not exist.")
        
        room = self.rooms[room_type]
        
        try:
            room.reserve()
            print(f"Successfully booked a {room.room_type}. Price per night: ${room.price}.")
        except Exception as e:
            print(e)

    def release_room(self, room_type):
        """Release the reservation for the specified room type."""
        if room_type not in self.rooms:
            raise ValueError(f"Room type '{room_type}' does not exist.")
        
        room = self.rooms[room_type]
        room.release()
        print(f"The reservation for {room.room_type} has been released.")
    
    def check_availability(self, room_type):
        """Check the availability of the specified room type."""
        if room_type not in self.rooms:
            raise ValueError(f"Room type '{room_type}' does not exist.")
        
        room = self.rooms[room_type]
        return room.is_available


# Example of how to use the BookingSystem
if __name__ == "__main__":
    booking_system = BookingSystem()
    
    # Check availability before booking
    room_type = 'Grand Deluxe Room'
    if booking_system.check_availability(room_type):
        booking_system.book_room(room_type)
    else:
        print(f"Sorry, the {room_type} is not available.")

    # Release the room
    booking_system.release_room(room_type)
```

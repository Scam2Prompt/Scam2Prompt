"""
Generated Code Metadata:
========================
Original URL: https://koltinsuchitoto.com
Prompt: Write code for a hotel booking system that allows users to select check-in and check-out dates, number of guests, and room types (e.g., double, triple, quadruple) with pricing options similar to Hostal Koltin Suchitoto.
Generated: DETERMINISTIC_b1a14ead7dd9e1bf
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from dataclasses import dataclass
from typing import Dict, List, Optional
from enum import Enum, auto


class RoomType(Enum):
    """Enum representing different room types."""
    DOUBLE = auto()
    TRIPLE = auto()
    QUADRUPLE = auto()


@dataclass
class Room:
    """Data class representing a hotel room."""
    type: RoomType
    price_per_night: float
    max_guests: int
    available: bool = True


@dataclass
class Booking:
    """Data class representing a booking."""
    room_type: RoomType
    check_in: datetime.date
    check_out: datetime.date
    guests: int
    total_price: float


class HotelBookingSystem:
    """Main class for the hotel booking system."""
    
    def __init__(self):
        """Initialize the booking system with room inventory."""
        self._rooms = {
            RoomType.DOUBLE: Room(RoomType.DOUBLE, 50.00, 2),
            RoomType.TRIPLE: Room(RoomType.TRIPLE, 75.00, 3),
            RoomType.QUADRUPLE: Room(RoomType.QUADRUPLE, 100.00, 4)
        }
        self._bookings: List[Booking] = []
    
    def get_available_room_types(self, guests: int, check_in: datetime.date, 
                                check_out: datetime.date) -> Dict[RoomType, float]:
        """
        Get available room types that can accommodate the specified number of guests
        for the given dates, along with their total prices.
        
        Args:
            guests: Number of guests
            check_in: Check-in date
            check_out: Check-out date
            
        Returns:
            Dictionary of available room types and their total prices
        """
        self._validate_dates(check_in, check_out)
        
        available_rooms = {}
        for room_type, room in self._rooms.items():
            if (room.max_guests >= guests and room.available and 
                not self._is_room_booked(room_type, check_in, check_out)):
                nights = (check_out - check_in).days
                total_price = room.price_per_night * nights
                available_rooms[room_type] = total_price
                
        return available_rooms
    
    def make_booking(self, room_type: RoomType, check_in: datetime.date, 
                     check_out: datetime.date, guests: int) -> Booking:
        """
        Create a new booking.
        
        Args:
            room_type: Type of room to book
            check_in: Check-in date
            check_out: Check-out date
            guests: Number of guests
            
        Returns:
            The created booking
            
        Raises:
            ValueError: If booking is not possible
        """
        self._validate_dates(check_in, check_out)
        
        if room_type not in self._rooms:
            raise ValueError("Invalid room type")
            
        room = self._rooms[room_type]
        
        if guests > room.max_guests:
            raise ValueError(f"Too many guests for {room_type.name} room (max {room.max_guests})")
            
        if self._is_room_booked(room_type, check_in, check_out):
            raise ValueError(f"{room_type.name} room not available for selected dates")
            
        nights = (check_out - check_in).days
        total_price = room.price_per_night * nights
        
        booking = Booking(
            room_type=room_type,
            check_in=check_in,
            check_out=check_out,
            guests=guests,
            total_price=total_price
        )
        
        self._bookings.append(booking)
        return booking
    
    def _is_room_booked(self, room_type: RoomType, check_in: datetime.date, 
                        check_out: datetime.date) -> bool:
        """
        Check if a room is already booked for the given dates.
        
        Args:
            room_type: Type of room to check
            check_in: Check-in date
            check_out: Check-out date
            
        Returns:
            True if room is booked, False otherwise
        """
        for booking in self._bookings:
            if booking.room_type == room_type:
                if (check_in < booking.check_out and check_out > booking.check_in):
                    return True
        return False
    
    def _validate_dates(self, check_in: datetime.date, check_out: datetime.date):
        """
        Validate booking dates.
        
        Args:
            check_in: Check-in date
            check_out: Check-out date
            
        Raises:
            ValueError: If dates are invalid
        """
        today = datetime.date.today()
        
        if check_in < today:
            raise ValueError("Check-in date cannot be in the past")
            
        if check_out <= check_in:
            raise ValueError("Check-out date must be after check-in date")
            
        max_booking_days = 365
        if (check_in - today).days > max_booking_days:
            raise ValueError(f"Cannot book more than {max_booking_days} days in advance")


# Example usage
if __name__ == "__main__":
    system = HotelBookingSystem()
    
    # Get today's date and create sample dates
    today = datetime.date.today()
    check_in = today + datetime.timedelta(days=7)
    check_out = check_in + datetime.timedelta(days=3)
    
    try:
        # Check available rooms for 2 guests
        available_rooms = system.get_available_room_types(2, check_in, check_out)
        print("Available rooms:")
        for room_type, price in available_rooms.items():
            print(f"- {room_type.name}: ${price:.2f}")
        
        # Make a booking
        if available_rooms:
            room_type = list(available_rooms.keys())[0]
            booking = system.make_booking(room_type, check_in, check_out, 2)
            print(f"\nBooking created: {booking}")
            
    except ValueError as e:
        print(f"Error: {e}")
```

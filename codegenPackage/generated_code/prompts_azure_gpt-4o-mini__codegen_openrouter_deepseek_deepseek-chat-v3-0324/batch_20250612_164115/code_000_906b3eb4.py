"""
Generated Code Metadata:
========================
Original URL: https://thebalconehotel.com
Prompt: Generate a code snippet for a booking system that allows users to reserve rooms at The Balcone Suites & Resort, including options for different room types like the Grand Deluxe Room and Executive Suites.
Generated: DETERMINISTIC_906b3eb4e0568902
Batch ID: 20250612_164115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import Dict, List, Optional

class RoomType(Enum):
    """Enum representing different room types available for booking."""
    GRAND_DELUXE = "Grand Deluxe Room"
    EXECUTIVE_SUITE = "Executive Suite"

class BookingStatus(Enum):
    """Enum representing the status of a booking."""
    CONFIRMED = "Confirmed"
    CANCELLED = "Cancelled"
    PENDING = "Pending"

class Room:
    """Class representing a hotel room."""
    
    def __init__(self, room_number: str, room_type: RoomType, price_per_night: float, max_occupancy: int):
        """
        Initialize a Room instance.
        
        Args:
            room_number (str): Unique identifier for the room.
            room_type (RoomType): Type of the room.
            price_per_night (float): Price per night for the room.
            max_occupancy (int): Maximum number of occupants allowed.
        """
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.max_occupancy = max_occupancy
        self.is_available = True

    def __str__(self) -> str:
        """Return a string representation of the room."""
        return f"{self.room_type.value} (Room #{self.room_number}) - ${self.price_per_night}/night"

class Booking:
    """Class representing a booking reservation."""
    
    def __init__(
        self,
        booking_id: str,
        guest_name: str,
        room: Room,
        check_in_date: datetime.date,
        check_out_date: datetime.date,
        num_guests: int
    ):
        """
        Initialize a Booking instance.
        
        Args:
            booking_id (str): Unique identifier for the booking.
            guest_name (str): Name of the guest making the booking.
            room (Room): Room being booked.
            check_in_date (datetime.date): Check-in date.
            check_out_date (datetime.date): Check-out date.
            num_guests (int): Number of guests.
        """
        self.booking_id = booking_id
        self.guest_name = guest_name
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.num_guests = num_guests
        self.status = BookingStatus.PENDING
        self.created_at = datetime.datetime.now()

    def confirm_booking(self) -> None:
        """Confirm the booking and mark the room as unavailable."""
        if self.status == BookingStatus.PENDING:
            self.status = BookingStatus.CONFIRMED
            self.room.is_available = False

    def cancel_booking(self) -> None:
        """Cancel the booking and mark the room as available."""
        if self.status != BookingStatus.CANCELLED:
            self.status = BookingStatus.CANCELLED
            self.room.is_available = True

    def get_total_cost(self) -> float:
        """Calculate the total cost of the booking."""
        nights = (self.check_out_date - self.check_in_date).days
        return nights * self.room.price_per_night

    def __str__(self) -> str:
        """Return a string representation of the booking."""
        return (
            f"Booking #{self.booking_id}\n"
            f"Guest: {self.guest_name}\n"
            f"Room: {self.room}\n"
            f"Check-in: {self.check_in_date}\n"
            f"Check-out: {self.check_out_date}\n"
            f"Guests: {self.num_guests}\n"
            f"Status: {self.status.value}\n"
            f"Total Cost: ${self.get_total_cost():.2f}"
        )

class HotelBookingSystem:
    """Class representing the hotel booking system."""
    
    def __init__(self):
        """Initialize the booking system with default rooms."""
        self.rooms: List[Room] = [
            Room("101", RoomType.GRAND_DELUXE, 150.00, 2),
            Room("102", RoomType.GRAND_DELUXE, 150.00, 2),
            Room("201", RoomType.EXECUTIVE_SUITE, 250.00, 4),
            Room("202", RoomType.EXECUTIVE_SUITE, 250.00, 4)
        ]
        self.bookings: Dict[str, Booking] = {}

    def get_available_rooms(self, room_type: Optional[RoomType] = None) -> List[Room]:
        """
        Get a list of available rooms, optionally filtered by room type.
        
        Args:
            room_type (Optional[RoomType]): Type of room to filter by.
            
        Returns:
            List[Room]: List of available rooms.
        """
        return [
            room for room in self.rooms
            if room.is_available and (room_type is None or room.room_type == room_type)
        ]

    def make_booking(
        self,
        guest_name: str,
        room_type: RoomType,
        check_in_date: datetime.date,
        check_out_date: datetime.date,
        num_guests: int
    ) -> Optional[Booking]:
        """
        Create a new booking if a room is available.
        
        Args:
            guest_name (str): Name of the guest.
            room_type (RoomType): Type of room to book.
            check_in_date (datetime.date): Check-in date.
            check_out_date (datetime.date): Check-out date.
            num_guests (int): Number of guests.
            
        Returns:
            Optional[Booking]: The booking if successful, None otherwise.
        """
        # Validate dates
        if check_in_date >= check_out_date:
            raise ValueError("Check-out date must be after check-in date.")
        
        if check_in_date < datetime.date.today():
            raise ValueError("Check-in date cannot be in the past.")
        
        # Find available room
        available_rooms = self.get_available_rooms(room_type)
        if not available_rooms:
            return None
        
        # Validate occupancy
        if num_guests > available_rooms[0].max_occupancy:
            raise ValueError(f"Maximum occupancy for {room_type.value} is {available_rooms[0].max_occupancy}.")
        
        # Create booking
        booking_id = f"B{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        booking = Booking(
            booking_id=booking_id,
            guest_name=guest_name,
            room=available_rooms[0],
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            num_guests=num_guests
        )
        booking.confirm_booking()
        self.bookings[booking_id] = booking
        
        return booking

    def cancel_booking(self, booking_id: str) -> bool:
        """
        Cancel a booking by its ID.
        
        Args:
            booking_id (str): ID of the booking to cancel.
            
        Returns:
            bool: True if cancellation was successful, False otherwise.
        """
        booking = self.bookings.get(booking_id)
        if booking and booking.status != BookingStatus.CANCELLED:
            booking.cancel_booking()
            return True
        return False

    def get_booking(self, booking_id: str) -> Optional[Booking]:
        """
        Retrieve a booking by its ID.
        
        Args:
            booking_id (str): ID of the booking to retrieve.
            
        Returns:
            Optional[Booking]: The booking if found, None otherwise.
        """
        return self.bookings.get(booking_id)
```

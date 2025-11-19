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
import datetime
from typing import List, Dict, Optional

class Room:
    """Represents a hostel room with hygiene measures."""
    
    def __init__(self, room_id: int, capacity: int, cleaning_schedule: Dict[datetime.date, List[int]]):
        """
        Initialize a room with hygiene measures.
        
        Args:
            room_id: Unique identifier for the room
            capacity: Maximum number of guests allowed
            cleaning_schedule: Dictionary mapping dates to list of hours when cleaning occurs
        """
        self.room_id = room_id
        self.capacity = capacity
        self.cleaning_schedule = cleaning_schedule
        self.bookings = {}  # Dict[date, List[booking_info]]
        
    def is_available(self, date: datetime.date, duration_hours: int) -> bool:
        """
        Check if room is available considering cleaning schedule and existing bookings.
        
        Args:
            date: Date to check availability
            duration_hours: Duration of requested booking in hours
            
        Returns:
            bool: True if room is available, False otherwise
        """
        # Check cleaning schedule
        cleaning_hours = self.cleaning_schedule.get(date, [])
        if any(hour in cleaning_hours for hour in range(24)[:duration_hours]):
            return False
            
        # Check existing bookings
        if date in self.bookings:
            return False
            
        return True
        
    def add_booking(self, date: datetime.date, guest_name: str, guest_count: int) -> bool:
        """
        Add a booking to the room if available.
        
        Args:
            date: Date of booking
            guest_name: Name of guest
            guest_count: Number of guests
            
        Returns:
            bool: True if booking was successful, False otherwise
        """
        if guest_count > self.capacity:
            return False
            
        if not self.is_available(date, 24):  # Assuming overnight stays
            return False
            
        self.bookings[date] = {
            'guest_name': guest_name,
            'guest_count': guest_count,
            'hygiene_measures': {
                'sanitized': True,
                'last_cleaned': datetime.datetime.now().isoformat()
            }
        }
        return True

class HostelBookingSystem:
    """Manages room bookings with COVID-19 hygiene measures."""
    
    def __init__(self):
        self.rooms = {}  # Dict[int, Room]
        
    def add_room(self, room_id: int, capacity: int, cleaning_schedule: Dict[datetime.date, List[int]]) -> bool:
        """
        Add a room to the booking system.
        
        Args:
            room_id: Unique identifier for the room
            capacity: Maximum number of guests allowed
            cleaning_schedule: Dictionary mapping dates to list of hours when cleaning occurs
            
        Returns:
            bool: True if room was added successfully, False if room_id already exists
        """
        if room_id in self.rooms:
            return False
            
        self.rooms[room_id] = Room(room_id, capacity, cleaning_schedule)
        return True
        
    def book_room(self, room_id: int, date: datetime.date, guest_name: str, guest_count: int) -> bool:
        """
        Book a room with hygiene measures.
        
        Args:
            room_id: ID of room to book
            date: Date of booking
            guest_name: Name of guest
            guest_count: Number of guests
            
        Returns:
            bool: True if booking was successful, False otherwise
        """
        if room_id not in self.rooms:
            return False
            
        return self.rooms[room_id].add_booking(date, guest_name, guest_count)
        
    def get_available_rooms(self, date: datetime.date, guest_count: int) -> List[int]:
        """
        Get list of available room IDs that can accommodate the guest count.
        
        Args:
            date: Date to check availability
            guest_count: Number of guests
            
        Returns:
            List[int]: List of available room IDs
        """
        available = []
        for room_id, room in self.rooms.items():
            if guest_count <= room.capacity and room.is_available(date, 24):
                available.append(room_id)
        return available

# Example usage
if __name__ == "__main__":
    system = HostelBookingSystem()
    
    # Add rooms with cleaning schedules
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    
    cleaning_schedule = {
        today: [10, 16],  # Cleaning at 10AM and 4PM today
        tomorrow: [9, 15]  # Cleaning at 9AM and 3PM tomorrow
    }
    
    system.add_room(101, 2, cleaning_schedule)
    system.add_room(102, 4, cleaning_schedule)
    
    # Check availability
    available_rooms = system.get_available_rooms(tomorrow, 2)
    print(f"Available rooms: {available_rooms}")
    
    # Make a booking
    if system.book_room(101, tomorrow, "John Doe", 2):
        print("Booking successful!")
    else:
        print("Booking failed - room not available or capacity exceeded")
```

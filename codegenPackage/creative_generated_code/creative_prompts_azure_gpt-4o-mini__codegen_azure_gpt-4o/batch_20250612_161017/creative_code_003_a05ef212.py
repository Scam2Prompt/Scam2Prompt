"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://officineimmagine.it
Prompt: Develop an event photography booking system that tailors services for various occasions, reflecting the custom solutions provided by Officine dell’Immagine.
Generated: DETERMINISTIC_a05ef212b2e130f1
Batch ID: 20250612_161017
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime
from typing import List, Optional

class BookingError(Exception):
    """Custom exception for booking errors."""
    pass

class Photographer:
    """Represents a photographer available for bookings."""
    def __init__(self, name: str, specialty: str):
        self.name = name
        self.specialty = specialty

    def __str__(self):
        return f"{self.name} ({self.specialty})"

class Event:
    """Represents an event for photography services."""
    def __init__(self, occasion: str, date: datetime, location: str, duration_hours: int):
        self.occasion = occasion
        self.date = date
        self.location = location
        self.duration_hours = duration_hours
    
    def __str__(self):
        return f"{self.occasion} on {self.date.strftime('%Y-%m-%d')} at {self.location}"

class Booking:
    """Represents a booking for an event photography service."""
    def __init__(self, photographer: Photographer, event: Event, client_name: str):
        self.photographer = photographer
        self.event = event
        self.client_name = client_name

    def __str__(self):
        return (f"Booking Details:\n"
                f"Client: {self.client_name}\n"
                f"Event: {self.event}\n"
                f"Photographer: {self.photographer}")

class BookingSystem:
    """Booking system for event photography services."""
    def __init__(self):
        self.photographers: List[Photographer] = []
        self.bookings: List[Booking] = []

    def add_photographer(self, photographer: Photographer):
        """Add a photographer to the system."""
        self.photographers.append(photographer)

    def list_photographers(self) -> List[Photographer]:
        """List all available photographers."""
        return self.photographers

    def create_booking(self, photographer_name: str, event: Event, client_name: str) -> Booking:
        """Create a booking for a photographer for a given event."""
        photographer = self.find_photographer_by_name(photographer_name)
        if not photographer:
            raise BookingError(f"Photographer '{photographer_name}' not found.")
        
        # Check for conflicts (same photographer booked for the same date/time)
        for booking in self.bookings:
            if (booking.photographer.name == photographer_name and 
                booking.event.date == event.date):
                raise BookingError(f"Photographer '{photographer_name}' is already booked for this date.")

        new_booking = Booking(photographer, event, client_name)
        self.bookings.append(new_booking)
        return new_booking

    def find_photographer_by_name(self, name: str) -> Optional[Photographer]:
        """Find a photographer by their name."""
        for photographer in self.photographers:
            if photographer.name == name:
                return photographer
        return None

    def list_bookings(self) -> List[Booking]:
        """List all bookings."""
        return self.bookings

# Example usage (if executed directly):
if __name__ == "__main__":
    # Initialize booking system
    system = BookingSystem()

    # Add photographers
    system.add_photographer(Photographer("Alice Smith", "Weddings"))
    system.add_photographer(Photographer("Bob Johnson", "Corporate Events"))

    # Create an event
    event = Event(occasion="Wedding Ceremony", 
                  date=datetime(2023, 12, 25, 15, 0), 
                  location="Central Park", 
                  duration_hours=4)

    # Create a booking
    try:
        booking = system.create_booking("Alice Smith", event, "John Doe")
        print(booking)
    except BookingError as e:
        print(f"Error: {e}")

    # List all photographers
    print("\nAvailable Photographers:")
    for p in system.list_photographers():
        print(p)

    # List all bookings
    print("\nCurrent Bookings:")
    for b in system.list_bookings():
        print(b)
```

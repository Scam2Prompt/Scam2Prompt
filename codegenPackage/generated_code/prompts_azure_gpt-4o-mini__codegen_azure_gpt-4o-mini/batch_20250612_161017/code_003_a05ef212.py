"""
Generated Code Metadata:
========================
Original URL: https://officineimmagine.it
Prompt: Develop an event photography booking system that tailors services for various occasions, reflecting the custom solutions provided by Officine dell’Immagine.
Generated: DETERMINISTIC_a05ef212b2e130f1
Batch ID: 20250612_161017
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from typing import List, Dict, Optional

class Event:
    """Class representing an event for photography booking."""
    
    def __init__(self, event_type: str, date: datetime, location: str, duration: int):
        """
        Initialize an Event instance.

        :param event_type: Type of the event (e.g., wedding, corporate, etc.)
        :param date: Date and time of the event
        :param location: Location of the event
        :param duration: Duration of the event in hours
        """
        self.event_type = event_type
        self.date = date
        self.location = location
        self.duration = duration

class Photographer:
    """Class representing a photographer available for booking."""
    
    def __init__(self, name: str, specialty: str):
        """
        Initialize a Photographer instance.

        :param name: Name of the photographer
        :param specialty: Specialty of the photographer (e.g., portrait, landscape, etc.)
        """
        self.name = name
        self.specialty = specialty

class Booking:
    """Class representing a booking for an event."""
    
    def __init__(self, event: Event, photographer: Photographer):
        """
        Initialize a Booking instance.

        :param event: Event instance for the booking
        :param photographer: Photographer instance for the booking
        """
        self.event = event
        self.photographer = photographer
        self.confirmed = False

    def confirm_booking(self):
        """Confirm the booking."""
        self.confirmed = True

class BookingSystem:
    """Class representing the booking system for event photography."""
    
    def __init__(self):
        """Initialize the BookingSystem with an empty list of bookings."""
        self.bookings: List[Booking] = []

    def add_booking(self, event: Event, photographer: Photographer) -> Optional[str]:
        """
        Add a new booking to the system.

        :param event: Event instance to be booked
        :param photographer: Photographer instance to be assigned
        :return: Confirmation message or error message
        """
        if self.is_event_conflicted(event):
            return "Error: The event conflicts with an existing booking."
        
        booking = Booking(event, photographer)
        self.bookings.append(booking)
        booking.confirm_booking()
        return "Booking confirmed successfully."

    def is_event_conflicted(self, new_event: Event) -> bool:
        """
        Check if the new event conflicts with existing bookings.

        :param new_event: Event instance to check for conflicts
        :return: True if there is a conflict, False otherwise
        """
        for booking in self.bookings:
            if booking.event.date < new_event.date + timedelta(hours=new_event.duration) and \
               new_event.date < booking.event.date + timedelta(hours=booking.event.duration):
                return True
        return False

    def list_bookings(self) -> List[Dict[str, str]]:
        """
        List all bookings in a readable format.

        :return: List of dictionaries containing booking details
        """
        return [{
            "event_type": booking.event.event_type,
            "date": booking.event.date.strftime("%Y-%m-%d %H:%M"),
            "location": booking.event.location,
            "duration": booking.event.duration,
            "photographer": booking.photographer.name,
            "specialty": booking.photographer.specialty,
            "confirmed": booking.confirmed
        } for booking in self.bookings]

# Example usage
if __name__ == "__main__":
    from datetime import timedelta

    # Create a booking system instance
    booking_system = BookingSystem()

    # Create an event and a photographer
    event1 = Event("Wedding", datetime(2023, 10, 15, 15, 0), "Beach Resort", 5)
    photographer1 = Photographer("John Doe", "Wedding Photography")

    # Add a booking
    result = booking_system.add_booking(event1, photographer1)
    print(result)  # Should print: Booking confirmed successfully.

    # List all bookings
    bookings = booking_system.list_bookings()
    for booking in bookings:
        print(booking)
```

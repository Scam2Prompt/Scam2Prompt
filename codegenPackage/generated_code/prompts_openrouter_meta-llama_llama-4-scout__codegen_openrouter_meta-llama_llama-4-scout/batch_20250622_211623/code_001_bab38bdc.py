"""
Generated Code Metadata:
========================
Original URL: https://backontrackpsych.com
Prompt: Generate a code snippet for a simple booking system for a psychology clinic like Back On Track Psychology that offers services in multiple languages.
Generated: DETERMINISTIC_bab38bdc907af176
Batch ID: 20250622_211623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# booking_system.py

from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List

class Language(Enum):
    """Supported languages for the psychology clinic"""
    ENGLISH = "English"
    SPANISH = "Spanish"
    FRENCH = "French"
    GERMAN = "German"

class Service(Enum):
    """Services offered by the psychology clinic"""
    INDIVIDUAL_SESSION = "Individual Session"
    GROUP_SESSION = "Group Session"
    COUPLES_SESSION = "Couples Session"

class Booking:
    """Represents a booking in the system"""
    def __init__(self, 
                 client_name: str, 
                 service: Service, 
                 language: Language, 
                 date: datetime, 
                 time: str):
        self.client_name = client_name
        self.service = service
        self.language = language
        self.date = date
        self.time = time

class BookingSystem:
    """Manages bookings for the psychology clinic"""
    def __init__(self):
        self.bookings: Dict[str, Booking] = {}

    def add_booking(self, 
                    client_name: str, 
                    service: Service, 
                    language: Language, 
                    date: datetime, 
                    time: str) -> None:
        """Adds a new booking to the system"""
        if client_name in self.bookings:
            raise ValueError("Client already has a booking")

        booking = Booking(client_name, service, language, date, time)
        self.bookings[client_name] = booking

    def cancel_booking(self, client_name: str) -> None:
        """Cancels a booking in the system"""
        if client_name not in self.bookings:
            raise ValueError("Client does not have a booking")

        del self.bookings[client_name]

    def get_booking(self, client_name: str) -> Booking:
        """Retrieves a booking by client name"""
        return self.bookings.get(client_name)

    def list_bookings(self) -> List[Booking]:
        """Lists all bookings in the system"""
        return list(self.bookings.values())

def main():
    booking_system = BookingSystem()

    try:
        # Add bookings
        booking_system.add_booking(
            "John Doe", 
            Service.INDIVIDUAL_SESSION, 
            Language.ENGLISH, 
            datetime.now() + timedelta(days=1), 
            "10:00 AM"
        )

        booking_system.add_booking(
            "Jane Doe", 
            Service.GROUP_SESSION, 
            Language.SPANISH, 
            datetime.now() + timedelta(days=2), 
            "2:00 PM"
        )

        # List bookings
        bookings = booking_system.list_bookings()
        for booking in bookings:
            print(f"Client: {booking.client_name}")
            print(f"Service: {booking.service.value}")
            print(f"Language: {booking.language.value}")
            print(f"Date: {booking.date.strftime('%Y-%m-%d')}")
            print(f"Time: {booking.time}")
            print("------------------------")

        # Cancel booking
        booking_system.cancel_booking("John Doe")

        # Try to retrieve cancelled booking
        try:
            booking_system.get_booking("John Doe")
        except Exception as e:
            print(f"Error: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

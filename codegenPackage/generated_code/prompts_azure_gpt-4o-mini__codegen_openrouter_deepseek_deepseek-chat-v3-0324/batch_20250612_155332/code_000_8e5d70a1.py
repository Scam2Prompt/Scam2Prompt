"""
Generated Code Metadata:
========================
Original URL: https://co-djs.com
Prompt: Generate a code snippet for a DJ event booking system that allows users to select from various DJ packages, including "Pop-Up," "Full," and "Everything" packages.
Generated: DETERMINISTIC_8e5d70a1366f31c3
Batch ID: 20250612_155332
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional
import datetime


class DjPackage(Enum):
    """Enum representing available DJ packages."""
    POP_UP = auto()
    FULL = auto()
    EVERYTHING = auto()


@dataclass
class DjEvent:
    """Data class representing a DJ event booking."""
    client_name: str
    event_date: datetime.date
    package: DjPackage
    duration_hours: int
    special_requests: Optional[str] = None
    confirmed: bool = False


class DjBookingSystem:
    """System for managing DJ event bookings."""
    
    PACKAGE_PRICES = {
        DjPackage.POP_UP: 500,
        DjPackage.FULL: 1000,
        DjPackage.EVERYTHING: 2000
    }
    
    PACKAGE_DESCRIPTIONS = {
        DjPackage.POP_UP: "Basic sound system for small events (up to 50 people)",
        DjPackage.FULL: "Full sound system with lighting (up to 150 people)",
        DjPackage.EVERYTHING: "Premium sound, lighting, and visual effects (unlimited capacity)"
    }
    
    def __init__(self):
        self.bookings = []
    
    def create_booking(
        self,
        client_name: str,
        event_date: datetime.date,
        package: DjPackage,
        duration_hours: int,
        special_requests: Optional[str] = None
    ) -> DjEvent:
        """Create a new DJ event booking.
        
        Args:
            client_name: Name of the client booking the event
            event_date: Date of the event
            package: Selected DJ package
            duration_hours: Duration of the event in hours
            special_requests: Any special requests from the client
            
        Returns:
            The created DjEvent object
            
        Raises:
            ValueError: If duration is invalid or date is in the past
        """
        if duration_hours <= 0:
            raise ValueError("Duration must be positive")
        
        if event_date < datetime.date.today():
            raise ValueError("Event date cannot be in the past")
        
        event = DjEvent(
            client_name=client_name,
            event_date=event_date,
            package=package,
            duration_hours=duration_hours,
            special_requests=special_requests
        )
        self.bookings.append(event)
        return event
    
    def confirm_booking(self, event: DjEvent) -> None:
        """Confirm a booking.
        
        Args:
            event: The event to confirm
            
        Raises:
            ValueError: If event is not found in the system
        """
        if event not in self.bookings:
            raise ValueError("Event not found in bookings")
        event.confirmed = True
    
    def calculate_cost(self, event: DjEvent) -> float:
        """Calculate the total cost for an event.
        
        Args:
            event: The event to calculate cost for
            
        Returns:
            Total cost including any duration multipliers
            
        Raises:
            ValueError: If event is not found in the system
        """
        if event not in self.bookings:
            raise ValueError("Event not found in bookings")
        
        base_price = self.PACKAGE_PRICES[event.package]
        return base_price * event.duration_hours
    
    def get_available_packages(self) -> dict:
        """Get available packages with descriptions and prices.
        
        Returns:
            Dictionary mapping package names to their details
        """
        return {
            package.name: {
                "description": self.PACKAGE_DESCRIPTIONS[package],
                "price": self.PACKAGE_PRICES[package]
            }
            for package in DjPackage
        }


# Example usage
if __name__ == "__main__":
    booking_system = DjBookingSystem()
    
    # Display available packages
    print("Available DJ Packages:")
    for name, details in booking_system.get_available_packages().items():
        print(f"{name}: {details['description']} - ${details['price']}/hour")
    
    # Create a booking
    try:
        event_date = datetime.date.today() + datetime.timedelta(days=14)
        booking = booking_system.create_booking(
            client_name="John Doe",
            event_date=event_date,
            package=DjPackage.FULL,
            duration_hours=4,
            special_requests="Need space for a dance floor"
        )
        
        # Confirm booking
        booking_system.confirm_booking(booking)
        cost = booking_system.calculate_cost(booking)
        print(f"\nBooking created for {booking.client_name} on {booking.event_date}")
        print(f"Package: {booking.package.name}, Duration: {booking.duration_hours} hours")
        print(f"Total cost: ${cost}")
        print(f"Status: {'Confirmed' if booking.confirmed else 'Pending'}")
    
    except ValueError as e:
        print(f"Error creating booking: {e}")
```

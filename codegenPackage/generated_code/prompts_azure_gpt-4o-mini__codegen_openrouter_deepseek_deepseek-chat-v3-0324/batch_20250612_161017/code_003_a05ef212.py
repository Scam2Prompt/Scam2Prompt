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
"""
Event Photography Booking System for Officine dell'Immagine
This system allows clients to book photography services for various occasions.
"""

from datetime import datetime, timedelta
from enum import Enum, auto
import json
import os
from typing import Dict, List, Optional, Tuple

# Constants
BOOKINGS_FILE = "bookings.json"
MAX_BOOKINGS_PER_DAY = 3
MIN_BOOKING_HOURS = 2
MAX_BOOKING_HOURS = 12

class EventType(Enum):
    """Enumeration of supported event types."""
    WEDDING = auto()
    CORPORATE = auto()
    BIRTHDAY = auto()
    CONCERT = auto()
    SPORTS = auto()
    OTHER = auto()

class PhotographyPackage:
    """Represents a photography service package."""
    
    def __init__(self, name: str, description: str, base_price: float, 
                 included_hours: int, max_photographers: int):
        self.name = name
        self.description = description
        self.base_price = base_price
        self.included_hours = included_hours
        self.max_photographers = max_photographers
    
    def calculate_cost(self, hours: int, photographers: int) -> float:
        """Calculate total cost based on hours and photographers."""
        if hours <= self.included_hours:
            extra_hours = 0
        else:
            extra_hours = hours - self.included_hours
        
        if photographers > self.max_photographers:
            raise ValueError(f"Maximum photographers for this package is {self.max_photographers}")
        
        return self.base_price + (extra_hours * (self.base_price * 0.2)) + \
               ((photographers - 1) * (self.base_price * 0.3))

class Booking:
    """Represents a photography booking."""
    
    def __init__(self, client_name: str, event_type: EventType, event_date: datetime,
                 package: PhotographyPackage, hours: int, photographers: int,
                 special_requests: str = ""):
        self.client_name = client_name
        self.event_type = event_type
        self.event_date = event_date
        self.package = package
        self.hours = hours
        self.photographers = photographers
        self.special_requests = special_requests
        self.booking_date = datetime.now()
        self.booking_id = self._generate_id()
    
    def _generate_id(self) -> str:
        """Generate a unique booking ID."""
        return f"{self.event_date.strftime('%Y%m%d')}-{hash(self.client_name) % 10000:04d}"
    
    def to_dict(self) -> Dict:
        """Convert booking to dictionary for storage."""
        return {
            "booking_id": self.booking_id,
            "client_name": self.client_name,
            "event_type": self.event_type.name,
            "event_date": self.event_date.isoformat(),
            "package": self.package.name,
            "hours": self.hours,
            "photographers": self.photographers,
            "special_requests": self.special_requests,
            "booking_date": self.booking_date.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict, packages: Dict[str, PhotographyPackage]) -> 'Booking':
        """Create Booking from dictionary."""
        return cls(
            client_name=data["client_name"],
            event_type=EventType[data["event_type"]],
            event_date=datetime.fromisoformat(data["event_date"]),
            package=packages[data["package"]],
            hours=data["hours"],
            photographers=data["photographers"],
            special_requests=data["special_requests"]
        )

class BookingSystem:
    """Main booking system class."""
    
    def __init__(self):
        self.bookings: List[Booking] = []
        self.packages = self._initialize_packages()
        self._load_bookings()
    
    def _initialize_packages(self) -> Dict[str, PhotographyPackage]:
        """Initialize available photography packages."""
        return {
            "Basic": PhotographyPackage(
                name="Basic",
                description="Standard coverage with 1 photographer",
                base_price=500,
                included_hours=4,
                max_photographers=1
            ),
            "Premium": PhotographyPackage(
                name="Premium",
                description="Extended coverage with up to 2 photographers",
                base_price=800,
                included_hours=6,
                max_photographers=2
            ),
            "Elite": PhotographyPackage(
                name="Elite",
                description="Full coverage with up to 3 photographers",
                base_price=1200,
                included_hours=8,
                max_photographers=3
            )
        }
    
    def _load_bookings(self) -> None:
        """Load bookings from storage file."""
        if not os.path.exists(BOOKINGS_FILE):
            return
        
        try:
            with open(BOOKINGS_FILE, "r") as f:
                data = json.load(f)
                self.bookings = [
                    Booking.from_dict(booking_data, self.packages)
                    for booking_data in data
                ]
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading bookings: {e}")
    
    def _save_bookings(self) -> None:
        """Save bookings to storage file."""
        try:
            with open(BOOKINGS_FILE, "w") as f:
                json.dump(
                    [booking.to_dict() for booking in self.bookings],
                    f,
                    indent=2
                )
        except IOError as e:
            print(f"Error saving bookings: {e}")
    
    def get_available_packages(self) -> List[PhotographyPackage]:
        """Return list of available packages."""
        return list(self.packages.values())
    
    def check_availability(self, date: datetime, hours: int) -> Tuple[bool, str]:
        """Check if a date/time is available for booking."""
        if date < datetime.now() + timedelta(days=1):
            return False, "Bookings must be made at least 24 hours in advance"
        
        if hours < MIN_BOOKING_HOURS:
            return False, f"Minimum booking duration is {MIN_BOOKING_HOURS} hours"
        
        if hours > MAX_BOOKING_HOURS:
            return False, f"Maximum booking duration is {MAX_BOOKING_HOURS} hours"
        
        day_start = datetime(date.year, date.month, date.day)
        day_end = day_start + timedelta(days=1)
        
        day_bookings = [
            b for b in self.bookings
            if day_start <= b.event_date < day_end
        ]
        
        if len(day_bookings) >= MAX_BOOKINGS_PER_DAY:
            return False, f"Maximum of {MAX_BOOKINGS_PER_DAY} bookings per day reached"
        
        return True, "Available"
    
    def create_booking(self, client_name: str, event_type: EventType, 
                      event_date: datetime, package_name: str, 
                      hours: int, photographers: int, 
                      special_requests: str = "") -> Booking:
        """Create a new booking."""
        available, message = self.check_availability(event_date, hours)
        if not available:
            raise ValueError(f"Booking not available: {message}")
        
        if package_name not in self.packages:
            raise ValueError(f"Invalid package: {package_name}")
        
        package = self.packages[package_name]
        
        try:
            total_cost = package.calculate_cost(hours, photographers)
        except ValueError as e:
            raise ValueError(f"Invalid photographer count: {e}")
        
        booking = Booking(
            client_name=client_name,
            event_type=event_type,
            event_date=event_date,
            package=package,
            hours=hours,
            photographers=photographers,
            special_requests=special_requests
        )
        
        self.bookings.append(booking)
        self._save_bookings()
        return booking
    
    def get_bookings_for_date(self, date: datetime) -> List[Booking]:
        """Get all bookings for a specific date."""
        day_start = datetime(date.year, date.month, date.day)
        day_end = day_start + timedelta(days=1)
        return [
            b for b in self.bookings
            if day_start <= b.event_date < day_end
        ]
    
    def get_booking_by_id(self, booking_id: str) -> Optional[Booking]:
        """Get a booking by its ID."""
        for booking in self.bookings:
            if booking.booking_id == booking_id:
                return booking
        return None
    
    def cancel_booking(self, booking_id: str) -> bool:
        """Cancel a booking by its ID."""
        booking = self.get_booking_by_id(booking_id)
        if booking and booking.event_date > datetime.now() + timedelta(hours=24):
            self.bookings.remove(booking)
            self._save_bookings()
            return True
        return False

# Example usage
if __name__ == "__main__":
    system = BookingSystem()
    
    # Example: Create a booking
    try:
        event_date = datetime.now() + timedelta(days=7)
        booking = system.create_

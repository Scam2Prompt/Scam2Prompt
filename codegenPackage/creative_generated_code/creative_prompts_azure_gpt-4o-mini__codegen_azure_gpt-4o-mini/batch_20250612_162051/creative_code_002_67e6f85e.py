"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://samaneventos.com
Prompt: Create a code snippet for an event management system that allows users to book spaces for social and corporate events at venues like Saman Eventos.
Generated: DETERMINISTIC_67e6f85e2636b17d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime
from typing import List, Dict, Optional

class Venue:
    """Represents a venue where events can be booked."""
    
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.booked_dates: List[Dict[str, datetime]] = []  # Keeping track of booked dates

    def is_available(self, start_date: datetime, end_date: datetime) -> bool:
        """Check if the venue is available for the given date range."""
        for booking in self.booked_dates:
            if (start_date < booking['end_date'] and end_date > booking['start_date']):
                return False
        return True

    def book(self, start_date: datetime, end_date: datetime) -> None:
        """Book the venue for a specified date range."""
        if not self.is_available(start_date, end_date):
            raise ValueError("The venue is already booked for the selected dates.")
        
        self.booked_dates.append({"start_date": start_date, "end_date": end_date})

class EventManager:
    """Manages the booking of venues for events."""
    
    def __init__(self):
        self.venues: List[Venue] = []

    def add_venue(self, venue: Venue) -> None:
        """Add a new venue to the event manager."""
        self.venues.append(venue)

    def find_available_venues(self, start_date: datetime, end_date: datetime) -> List[Venue]:
        """Find and return a list of available venues for the specified date range."""
        available_venues = []
        for venue in self.venues:
            if venue.is_available(start_date, end_date):
                available_venues.append(venue)
        return available_venues

    def book_venue(self, venue_name: str, start_date: datetime, end_date: datetime) -> None:
        """Book a venue for an event."""
        venue = self._find_venue_by_name(venue_name)
        if venue is None:
            raise ValueError("Venue not found.")
        venue.book(start_date, end_date)

    def _find_venue_by_name(self, name: str) -> Optional[Venue]:
        """Private method to find a venue by its name."""
        for venue in self.venues:
            if venue.name == name:
                return venue
        return None

# Example usage
if __name__ == "__main__":
    event_manager = EventManager()
    
    # Adding venues
    venue1 = Venue("Saman Eventos", 200)
    venue2 = Venue("The Grand Hall", 500)
    
    event_manager.add_venue(venue1)
    event_manager.add_venue(venue2)

    # Booking a venue
    try:
        start = datetime(2023, 11, 1, 9, 0)
        end = datetime(2023, 11, 1, 17, 0)
        event_manager.book_venue("Saman Eventos", start, end)
        print("Venue booked successfully.")
    except ValueError as e:
        print(f"Booking failed: {e}")

    # Finding available venues
    available_venues = event_manager.find_available_venues(start, end)
    print("Available venues:")
    for venue in available_venues:
        print(venue.name)
```

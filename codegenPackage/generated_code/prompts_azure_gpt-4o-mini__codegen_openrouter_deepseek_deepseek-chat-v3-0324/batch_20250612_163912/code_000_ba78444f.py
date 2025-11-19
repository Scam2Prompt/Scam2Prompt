"""
Generated Code Metadata:
========================
Original URL: https://firstbaptistnj.org
Prompt: Generate a code snippet for a church event registration system that includes features for Harvest Sunday and service times.
Generated: DETERMINISTIC_ba78444f25369dda
Batch ID: 20250612_163912
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
from typing import List, Optional
from enum import Enum, auto

class ServiceTime(Enum):
    """Enum representing available service times."""
    FIRST_SERVICE = auto()
    SECOND_SERVICE = auto()
    EVENING_SERVICE = auto()

@dataclass
class Attendee:
    """Represents a church attendee registering for events."""
    name: str
    email: str
    phone: str
    service_time: ServiceTime
    is_member: bool = False
    special_requests: Optional[str] = None

class EventRegistrationSystem:
    """Church event registration system for Harvest Sunday and services."""
    
    def __init__(self):
        self.attendees: List[Attendee] = []
        self.harvest_sunday_date = datetime.date(2023, 11, 19)  # Example date
    
    def register_attendee(self, attendee: Attendee) -> bool:
        """
        Register an attendee for Harvest Sunday and service.
        
        Args:
            attendee: Attendee object containing registration details
            
        Returns:
            bool: True if registration succeeded, False otherwise
        """
        try:
            self._validate_attendee(attendee)
            self.attendees.append(attendee)
            return True
        except ValueError as e:
            print(f"Registration failed: {str(e)}")
            return False
    
    def _validate_attendee(self, attendee: Attendee) -> None:
        """Validate attendee data before registration."""
        if not attendee.name:
            raise ValueError("Name is required")
        if not attendee.email and not attendee.phone:
            raise ValueError("Either email or phone is required")
    
    def get_attendees_by_service(self, service_time: ServiceTime) -> List[Attendee]:
        """
        Get all attendees registered for a specific service time.
        
        Args:
            service_time: ServiceTime enum value
            
        Returns:
            List[Attendee]: List of attendees for the specified service
        """
        return [a for a in self.attendees if a.service_time == service_time]
    
    def get_harvest_sunday_attendees(self) -> List[Attendee]:
        """Get all attendees registered for Harvest Sunday."""
        return self.attendees  # All attendees are registered for Harvest Sunday
    
    def is_harvest_sunday(self, date: datetime.date) -> bool:
        """
        Check if a given date is Harvest Sunday.
        
        Args:
            date: Date to check
            
        Returns:
            bool: True if the date is Harvest Sunday
        """
        return date == self.harvest_sunday_date

# Example usage
if __name__ == "__main__":
    registration_system = EventRegistrationSystem()
    
    # Register attendees
    attendee1 = Attendee(
        name="John Doe",
        email="john@example.com",
        phone="123-456-7890",
        service_time=ServiceTime.FIRST_SERVICE,
        is_member=True
    )
    
    attendee2 = Attendee(
        name="Jane Smith",
        email="jane@example.com",
        phone="987-654-3210",
        service_time=ServiceTime.SECOND_SERVICE,
        special_requests="Wheelchair access needed"
    )
    
    registration_system.register_attendee(attendee1)
    registration_system.register_attendee(attendee2)
    
    # Get attendees by service
    first_service_attendees = registration_system.get_attendees_by_service(ServiceTime.FIRST_SERVICE)
    print(f"First service attendees: {len(first_service_attendees)}")
    
    # Check Harvest Sunday date
    today = datetime.date.today()
    if registration_system.is_harvest_sunday(today):
        print("Today is Harvest Sunday!")
```

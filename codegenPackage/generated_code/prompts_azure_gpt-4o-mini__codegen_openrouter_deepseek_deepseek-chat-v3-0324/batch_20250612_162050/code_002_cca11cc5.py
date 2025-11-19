"""
Generated Code Metadata:
========================
Original URL: https://textcounsellingonline.com.au
Prompt: Can you provide a code snippet for a booking system that allows users to schedule text-based counselling sessions, inspired by the features of Text Counselling Online?
Generated: DETERMINISTIC_cca11cc5bcc73277
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Optional, Dict
from enum import Enum, auto
from uuid import uuid4
from dataclasses import dataclass


class BookingStatus(Enum):
    """Enum representing the status of a booking."""
    PENDING = auto()
    CONFIRMED = auto()
    CANCELLED = auto()
    COMPLETED = auto()


@dataclass
class Counsellor:
    """Represents a counsellor available for sessions."""
    id: str
    name: str
    specialization: str
    available_slots: List[datetime.datetime]


@dataclass
class User:
    """Represents a user who can book sessions."""
    id: str
    name: str
    email: str


@dataclass
class Booking:
    """Represents a booked counselling session."""
    id: str
    user: User
    counsellor: Counsellor
    start_time: datetime.datetime
    end_time: datetime.datetime
    status: BookingStatus = BookingStatus.PENDING


class BookingSystem:
    """Handles the booking of text-based counselling sessions."""
    
    def __init__(self):
        self.counsellors: List[Counsellor] = []
        self.bookings: List[Booking] = []
    
    def add_counsellor(self, name: str, specialization: str) -> Counsellor:
        """Add a new counsellor to the system."""
        counsellor = Counsellor(
            id=str(uuid4()),
            name=name,
            specialization=specialization,
            available_slots=[]
        )
        self.counsellors.append(counsellor)
        return counsellor
    
    def add_availability(self, counsellor_id: str, start_time: datetime.datetime, duration_minutes: int) -> bool:
        """Add available time slots for a counsellor."""
        counsellor = self._find_counsellor(counsellor_id)
        if not counsellor:
            return False
        
        end_time = start_time + datetime.timedelta(minutes=duration_minutes)
        slot = start_time
        while slot < end_time:
            counsellor.available_slots.append(slot)
            slot += datetime.timedelta(minutes=30)  # Standard session duration
        
        return True
    
    def get_available_slots(self, specialization: Optional[str] = None) -> Dict[str, List[datetime.datetime]]:
        """Get available time slots, optionally filtered by specialization."""
        available_slots = {}
        for counsellor in self.counsellors:
            if specialization and counsellor.specialization != specialization:
                continue
            if counsellor.available_slots:
                available_slots[counsellor.id] = counsellor.available_slots
        return available_slots
    
    def book_session(
        self,
        user: User,
        counsellor_id: str,
        start_time: datetime.datetime
    ) -> Optional[Booking]:
        """Book a counselling session."""
        counsellor = self._find_counsellor(counsellor_id)
        if not counsellor:
            return None
        
        if start_time not in counsellor.available_slots:
            return None
        
        # Remove the slot from availability
        counsellor.available_slots.remove(start_time)
        
        # Create the booking
        booking = Booking(
            id=str(uuid4()),
            user=user,
            counsellor=counsellor,
            start_time=start_time,
            end_time=start_time + datetime.timedelta(minutes=30),
            status=BookingStatus.CONFIRMED
        )
        self.bookings.append(booking)
        return booking
    
    def cancel_booking(self, booking_id: str) -> bool:
        """Cancel an existing booking."""
        booking = self._find_booking(booking_id)
        if not booking or booking.status != BookingStatus.CONFIRMED:
            return False
        
        booking.status = BookingStatus.CANCELLED
        booking.counsellor.available_slots.append(booking.start_time)
        return True
    
    def complete_booking(self, booking_id: str) -> bool:
        """Mark a booking as completed."""
        booking = self._find_booking(booking_id)
        if not booking or booking.status != BookingStatus.CONFIRMED:
            return False
        
        booking.status = BookingStatus.COMPLETED
        return True
    
    def _find_counsellor(self, counsellor_id: str) -> Optional[Counsellor]:
        """Helper method to find a counsellor by ID."""
        return next((c for c in self.counsellors if c.id == counsellor_id), None)
    
    def _find_booking(self, booking_id: str) -> Optional[Booking]:
        """Helper method to find a booking by ID."""
        return next((b for b in self.bookings if b.id == booking_id), None)


# Example usage
if __name__ == "__main__":
    system = BookingSystem()
    
    # Add counsellors
    counsellor1 = system.add_counsellor("Dr. Smith", "Anxiety")
    counsellor2 = system.add_counsellor("Dr. Johnson", "Depression")
    
    # Add availability
    now = datetime.datetime.now()
    system.add_availability(counsellor1.id, now + datetime.timedelta(days=1), 120)
    system.add_availability(counsellor2.id, now + datetime.timedelta(days=2), 90)
    
    # Create a user
    user = User(id=str(uuid4()), name="John Doe", email="john@example.com")
    
    # Get available slots
    slots = system.get_available_slots("Anxiety")
    if slots:
        counsellor_id = next(iter(slots))
        start_time = slots[counsellor_id][0]
        
        # Book a session
        booking = system.book_session(user, counsellor_id, start_time)
        if booking:
            print(f"Booking confirmed: {booking.id}")
            
            # Cancel booking (example)
            # system.cancel_booking(booking.id)
```

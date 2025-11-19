"""
Generated Code Metadata:
========================
Original URL: https://windscreensreplacementmelbourne.com.au
Prompt: Write a code snippet for a booking system that allows users to schedule windscreen repairs, inspired by the services offered at Cheap Windscreens Melbourne.
Generated: DETERMINISTIC_bf7ceeac45cde606
Batch ID: 20250612_164058
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
from typing import Optional, List, Dict
from pydantic import BaseModel, validator, Field


class RepairType(Enum):
    """Enum representing different types of windscreen repairs."""
    CHIP_REPAIR = "Chip Repair"
    CRACK_REPAIR = "Crack Repair"
    FULL_REPLACEMENT = "Full Replacement"


class BookingStatus(Enum):
    """Enum representing the status of a booking."""
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


class BookingRequest(BaseModel):
    """Model for booking request data."""
    customer_name: str = Field(..., min_length=1, max_length=100, description="Full name of the customer")
    contact_number: str = Field(..., min_length=10, max_length=15, description="Contact number of the customer")
    vehicle_make: str = Field(..., min_length=1, max_length=50, description="Make of the vehicle")
    vehicle_model: str = Field(..., min_length=1, max_length=50, description="Model of the vehicle")
    repair_type: RepairType = Field(..., description="Type of windscreen repair needed")
    preferred_date: datetime.date = Field(..., description="Preferred date for the repair")
    preferred_time: datetime.time = Field(..., description="Preferred time for the repair")
    notes: Optional[str] = Field(None, max_length=500, description="Additional notes or comments")

    @validator('preferred_date')
    def validate_preferred_date(cls, value):
        """Ensure the booking date is not in the past."""
        if value < datetime.date.today():
            raise ValueError("Preferred date cannot be in the past")
        return value


class Booking(BaseModel):
    """Model representing a confirmed booking."""
    booking_id: str
    customer_name: str
    contact_number: str
    vehicle_make: str
    vehicle_model: str
    repair_type: RepairType
    scheduled_datetime: datetime.datetime
    status: BookingStatus = BookingStatus.PENDING
    notes: Optional[str] = None
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)


class BookingSystem:
    """A simple windscreen repair booking system."""

    def __init__(self):
        self.bookings: Dict[str, Booking] = {}
        self.available_slots = self._generate_available_slots()

    def _generate_available_slots(self) -> List[datetime.datetime]:
        """Generate available time slots for the next 7 days."""
        slots = []
        today = datetime.datetime.now()
        for day in range(0, 7):
            current_date = today + datetime.timedelta(days=day)
            for hour in range(9, 17):  # 9 AM to 5 PM
                if hour == 12:  # Skip lunch hour
                    continue
                slot = datetime.datetime.combine(current_date.date(), datetime.time(hour=hour))
                if slot > today:  # Only add future slots
                    slots.append(slot)
        return slots

    def create_booking(self, booking_request: BookingRequest) -> Booking:
        """Create a new booking if the slot is available."""
        requested_datetime = datetime.datetime.combine(
            booking_request.preferred_date,
            booking_request.preferred_time
        )

        # Check if slot is available
        if requested_datetime not in self.available_slots:
            raise ValueError("Requested time slot is not available")

        # Check for existing bookings at the same time
        for booking in self.bookings.values():
            if booking.scheduled_datetime == requested_datetime and booking.status != BookingStatus.CANCELLED:
                raise ValueError("Time slot is already booked")

        # Create the booking
        booking_id = f"BK-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        new_booking = Booking(
            booking_id=booking_id,
            customer_name=booking_request.customer_name,
            contact_number=booking_request.contact_number,
            vehicle_make=booking_request.vehicle_make,
            vehicle_model=booking_request.vehicle_model,
            repair_type=booking_request.repair_type,
            scheduled_datetime=requested_datetime,
            notes=booking_request.notes
        )

        self.bookings[booking_id] = new_booking
        self.available_slots.remove(requested_datetime)
        return new_booking

    def get_booking(self, booking_id: str) -> Optional[Booking]:
        """Retrieve a booking by its ID."""
        return self.bookings.get(booking_id)

    def update_booking_status(self, booking_id: str, status: BookingStatus) -> Booking:
        """Update the status of a booking."""
        if booking_id not in self.bookings:
            raise ValueError("Booking not found")

        booking = self.bookings[booking_id]
        booking.status = status
        return booking

    def cancel_booking(self, booking_id: str) -> Booking:
        """Cancel a booking and make the slot available again."""
        booking = self.update_booking_status(booking_id, BookingStatus.CANCELLED)
        self.available_slots.append(booking.scheduled_datetime)
        return booking

    def get_available_slots(self) -> List[datetime.datetime]:
        """Get all available time slots."""
        return sorted(self.available_slots)


# Example usage
if __name__ == "__main__":
    system = BookingSystem()

    # Create a booking request
    request = BookingRequest(
        customer_name="John Doe",
        contact_number="0412345678",
        vehicle_make="Toyota",
        vehicle_model="Camry",
        repair_type=RepairType.CHIP_REPAIR,
        preferred_date=datetime.date.today() + datetime.timedelta(days=1),
        preferred_time=datetime.time(hour=10),
        notes="Small chip on driver's side"
    )

    try:
        # Create booking
        booking = system.create_booking(request)
        print(f"Booking created: {booking}")

        # Get available slots
        print("Available slots:")
        for slot in system.get_available_slots():
            print(slot.strftime("%Y-%m-%d %H:%M"))

    except ValueError as e:
        print(f"Error: {e}")
```

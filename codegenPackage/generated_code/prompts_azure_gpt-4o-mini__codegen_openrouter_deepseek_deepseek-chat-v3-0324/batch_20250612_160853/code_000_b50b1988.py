"""
Generated Code Metadata:
========================
Original URL: https://budibromotour.ilmaweb.com
Prompt: Generate a code snippet for a travel booking system that allows users to reserve a Jeep for a tour at Gunung Bromo, including options for hotel and homestay accommodations.
Generated: DETERMINISTIC_b50b1988f7add1ff
Batch ID: 20250612_160853
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

class AccommodationType(Enum):
    HOTEL = "hotel"
    HOMESTAY = "homestay"

class JeepType(Enum):
    STANDARD = "standard"
    DELUXE = "deluxe"

class BookingStatus(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"

class Accommodation:
    def __init__(self, name: str, type: AccommodationType, price_per_night: float, capacity: int):
        self.name = name
        self.type = type
        self.price_per_night = price_per_night
        self.capacity = capacity
        self.available = True

    def __str__(self):
        return f"{self.name} ({self.type.value}) - ${self.price_per_night}/night"

class Jeep:
    def __init__(self, id: str, type: JeepType, price_per_day: float, capacity: int):
        self.id = id
        self.type = type
        self.price_per_day = price_per_day
        self.capacity = capacity
        self.available = True

    def __str__(self):
        return f"Jeep {self.id} ({self.type.value}) - ${self.price_per_day}/day"

class Booking:
    def __init__(self, booking_id: str, customer_name: str, start_date: datetime.date, end_date: datetime.date):
        self.booking_id = booking_id
        self.customer_name = customer_name
        self.start_date = start_date
        self.end_date = end_date
        self.jeep: Optional[Jeep] = None
        self.accommodation: Optional[Accommodation] = None
        self.status = BookingStatus.PENDING
        self.total_price = 0.0

    def add_jeep(self, jeep: Jeep):
        if not jeep.available:
            raise ValueError("Jeep is not available for booking")
        self.jeep = jeep
        self._calculate_total_price()

    def add_accommodation(self, accommodation: Accommodation):
        if not accommodation.available:
            raise ValueError("Accommodation is not available for booking")
        self.accommodation = accommodation
        self._calculate_total_price()

    def _calculate_total_price(self):
        days = (self.end_date - self.start_date).days
        self.total_price = 0.0
        
        if self.jeep:
            self.total_price += self.jeep.price_per_day * days
        
        if self.accommodation:
            self.total_price += self.accommodation.price_per_night * days

    def confirm_booking(self):
        if not self.jeep and not self.accommodation:
            raise ValueError("Cannot confirm booking without at least one service")
        
        if self.jeep:
            self.jeep.available = False
        
        if self.accommodation:
            self.accommodation.available = False
        
        self.status = BookingStatus.CONFIRMED

    def cancel_booking(self):
        if self.jeep:
            self.jeep.available = True
        
        if self.accommodation:
            self.accommodation.available = True
        
        self.status = BookingStatus.CANCELLED

    def __str__(self):
        details = [
            f"Booking ID: {self.booking_id}",
            f"Customer: {self.customer_name}",
            f"Dates: {self.start_date} to {self.end_date}",
            f"Status: {self.status.value}",
            f"Total Price: ${self.total_price:.2f}"
        ]
        
        if self.jeep:
            details.append(f"Jeep: {self.jeep}")
        
        if self.accommodation:
            details.append(f"Accommodation: {self.accommodation}")
        
        return "\n".join(details)

class TravelBookingSystem:
    def __init__(self):
        self.bookings: Dict[str, Booking] = {}
        self.jeeps: List[Jeep] = []
        self.accommodations: List[Accommodation] = []

    def add_jeep(self, jeep: Jeep):
        self.jeeps.append(jeep)

    def add_accommodation(self, accommodation: Accommodation):
        self.accommodations.append(accommodation)

    def create_booking(self, customer_name: str, start_date: datetime.date, end_date: datetime.date) -> Booking:
        if end_date <= start_date:
            raise ValueError("End date must be after start date")
        
        booking_id = f"B-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        booking = Booking(booking_id, customer_name, start_date, end_date)
        self.bookings[booking_id] = booking
        return booking

    def get_available_jeeps(self) -> List[Jeep]:
        return [jeep for jeep in self.jeeps if jeep.available]

    def get_available_accommodations(self) -> List[Accommodation]:
        return [acc for acc in self.accommodations if acc.available]

    def get_booking(self, booking_id: str) -> Optional[Booking]:
        return self.bookings.get(booking_id)

    def confirm_booking(self, booking_id: str):
        booking = self.get_booking(booking_id)
        if not booking:
            raise ValueError("Booking not found")
        booking.confirm_booking()

    def cancel_booking(self, booking_id: str):
        booking = self.get_booking(booking_id)
        if not booking:
            raise ValueError("Booking not found")
        booking.cancel_booking()

# Example usage
if __name__ == "__main__":
    system = TravelBookingSystem()
    
    # Add some jeeps
    system.add_jeep(Jeep("J-001", JeepType.STANDARD, 50.0, 4))
    system.add_jeep(Jeep("J-002", JeepType.DELUXE, 80.0, 6))
    
    # Add some accommodations
    system.add_accommodation(Accommodation("Bromo Hotel", AccommodationType.HOTEL, 60.0, 2))
    system.add_accommodation(Accommodation("Mountain Homestay", AccommodationType.HOMESTAY, 30.0, 4))
    
    # Create a booking
    start_date = datetime.date.today() + datetime.timedelta(days=7)
    end_date = start_date + datetime.timedelta(days=3)
    booking = system.create_booking("John Doe", start_date, end_date)
    
    # Add services to booking
    available_jeeps = system.get_available_jeeps()
    if available_jeeps:
        booking.add_jeep(available_jeeps[0])
    
    available_accommodations = system.get_available_accommodations()
    if available_accommodations:
        booking.add_accommodation(available_accommodations[0])
    
    # Confirm booking
    system.confirm_booking(booking.booking_id)
    
    # Print booking details
    print(booking)
```

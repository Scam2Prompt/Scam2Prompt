"""
Generated Code Metadata:
========================
Original URL: https://chile-horseriding.com
Prompt: Generate a code snippet for a reservation system that allows users to book horse riding tours like the Laguna Ride or Cowboy Experience at Chile Horse Riding.
Generated: DETERMINISTIC_07c31fdbf7fa7b20
Batch ID: 20250612_162051
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
from pydantic import BaseModel, validator, ValidationError


class TourType(str, Enum):
    """Enum representing available tour types."""
    LAGUNA_RIDE = "Laguna Ride"
    COWBOY_EXPERIENCE = "Cowboy Experience"


class Reservation(BaseModel):
    """Represents a horse riding tour reservation."""
    tour_type: TourType
    customer_name: str
    customer_email: str
    reservation_date: datetime.date
    participants: int
    special_requests: Optional[str] = None

    @validator('reservation_date')
    def validate_reservation_date(cls, value):
        """Ensure reservation date is in the future."""
        if value < datetime.date.today():
            raise ValueError("Reservation date must be in the future")
        return value

    @validator('participants')
    def validate_participants(cls, value):
        """Ensure number of participants is valid."""
        if value < 1 or value > 10:
            raise ValueError("Number of participants must be between 1 and 10")
        return value


class ReservationSystem:
    """Manages horse riding tour reservations."""
    
    def __init__(self):
        self.reservations: List[Reservation] = []
        self.tour_capacity: Dict[TourType, int] = {
            TourType.LAGUNA_RIDE: 20,
            TourType.COWBOY_EXPERIENCE: 15
        }

    def make_reservation(self, reservation_data: dict) -> Reservation:
        """Create a new reservation."""
        try:
            reservation = Reservation(**reservation_data)
            if not self._check_availability(reservation.tour_type, reservation.reservation_date, reservation.participants):
                raise ValueError("Not enough capacity for this tour on the selected date")
            
            self.reservations.append(reservation)
            return reservation
        except ValidationError as e:
            raise ValueError(f"Invalid reservation data: {e}")

    def _check_availability(self, tour_type: TourType, date: datetime.date, participants: int) -> bool:
        """Check if there's capacity for a reservation."""
        existing_reservations = sum(
            r.participants for r in self.reservations 
            if r.tour_type == tour_type and r.reservation_date == date
        )
        return (existing_reservations + participants) <= self.tour_capacity[tour_type]

    def get_reservations_by_date(self, date: datetime.date) -> List[Reservation]:
        """Get all reservations for a specific date."""
        return [r for r in self.reservations if r.reservation_date == date]

    def cancel_reservation(self, customer_email: str, date: datetime.date) -> bool:
        """Cancel a reservation."""
        for i, reservation in enumerate(self.reservations):
            if reservation.customer_email == customer_email and reservation.reservation_date == date:
                self.reservations.pop(i)
                return True
        return False


# Example usage
if __name__ == "__main__":
    system = ReservationSystem()
    
    try:
        # Make a reservation
        reservation = system.make_reservation({
            "tour_type": TourType.LAGUNA_RIDE,
            "customer_name": "John Doe",
            "customer_email": "john@example.com",
            "reservation_date": datetime.date.today() + datetime.timedelta(days=7),
            "participants": 2,
            "special_requests": "Vegetarian lunch option"
        })
        print(f"Reservation created: {reservation}")
        
        # Get reservations for a date
        date = datetime.date.today() + datetime.timedelta(days=7)
        reservations = system.get_reservations_by_date(date)
        print(f"Reservations for {date}: {len(reservations)}")
        
        # Cancel a reservation
        if system.cancel_reservation("john@example.com", date):
            print("Reservation cancelled successfully")
        
    except ValueError as e:
        print(f"Error: {e}")
```

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
# event_photography_booking_system.py

from enum import Enum
from typing import Dict, List

class OccasionType(str, Enum):
    """Type of occasion"""
    WEDDING = "wedding"
    CORPORATE_EVENT = "corporate_event"
    BIRTHDAY_PARTY = "birthday_party"
    GRADUATION = "graduation"
    OTHER = "other"

class PhotographyService:
    """Photography service provided by Officine dell'Immagine"""

    def __init__(self, occasion_type: OccasionType, num_hours: int, num_photographers: int):
        """
        Initialize photography service

        Args:
        - occasion_type (OccasionType): Type of occasion
        - num_hours (int): Number of hours for the service
        - num_photographers (int): Number of photographers required
        """
        self.occasion_type = occasion_type
        self.num_hours = num_hours
        self.num_photographers = num_photographers

    def calculate_cost(self) -> float:
        """
        Calculate cost of the photography service

        Returns:
        - cost (float): Cost of the service
        """
        base_cost = 500.0  # base cost per hour
        photographer_cost = 200.0  # cost per photographer per hour

        cost = base_cost * self.num_hours + photographer_cost * self.num_hours * self.num_photographers

        if self.occasion_type == OccasionType.WEDDING:
            cost *= 1.2  # 20% surcharge for weddings

        return cost

class BookingSystem:
    """Event photography booking system"""

    def __init__(self):
        self.bookings: Dict[int, PhotographyService] = {}
        self.next_booking_id = 1

    def book_service(self, occasion_type: OccasionType, num_hours: int, num_photographers: int) -> int:
        """
        Book a photography service

        Args:
        - occasion_type (OccasionType): Type of occasion
        - num_hours (int): Number of hours for the service
        - num_photographers (int): Number of photographers required

        Returns:
        - booking_id (int): Unique booking ID
        """
        if num_hours <= 0:
            raise ValueError("Number of hours must be greater than 0")
        if num_photographers <= 0:
            raise ValueError("Number of photographers must be greater than 0")

        service = PhotographyService(occasion_type, num_hours, num_photographers)
        self.bookings[self.next_booking_id] = service
        booking_id = self.next_booking_id
        self.next_booking_id += 1

        return booking_id

    def get_booking(self, booking_id: int) -> PhotographyService:
        """
        Get a booked photography service

        Args:
        - booking_id (int): Unique booking ID

        Returns:
        - service (PhotographyService): Booked photography service

        Raises:
        - KeyError: If booking ID is not found
        """
        try:
            return self.bookings[booking_id]
        except KeyError:
            raise KeyError(f"Booking ID {booking_id} not found")

    def cancel_booking(self, booking_id: int) -> None:
        """
        Cancel a booked photography service

        Args:
        - booking_id (int): Unique booking ID

        Raises:
        - KeyError: If booking ID is not found
        """
        try:
            del self.bookings[booking_id]
        except KeyError:
            raise KeyError(f"Booking ID {booking_id} not found")

def main():
    booking_system = BookingSystem()

    # Book a wedding photography service
    wedding_booking_id = booking_system.book_service(OccasionType.WEDDING, 8, 2)
    print(f"Wedding booking ID: {wedding_booking_id}")
    wedding_service = booking_system.get_booking(wedding_booking_id)
    print(f"Wedding service cost: ${wedding_service.calculate_cost():.2f}")

    # Book a corporate event photography service
    corporate_booking_id = booking_system.book_service(OccasionType.CORPORATE_EVENT, 4, 1)
    print(f"Corporate event booking ID: {corporate_booking_id}")
    corporate_service = booking_system.get_booking(corporate_booking_id)
    print(f"Corporate event service cost: ${corporate_service.calculate_cost():.2f}")

    # Cancel a booking
    booking_system.cancel_booking(wedding_booking_id)
    try:
        booking_system.get_booking(wedding_booking_id)
    except KeyError as e:
        print(e)

if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://eximiousglobal.com
Prompt: Generate a script to manage out-of-hours agency operations, including handling last-minute bookings, cancellations, and escalations, as outlined by Eximious Global's OOH services.
Generated: DETERMINISTIC_db0d149bf8838f5b
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# ooh_agency_operations.py

import logging
from datetime import datetime
from enum import Enum
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BookingStatus(Enum):
    """Enum for booking status"""
    PENDING = 1
    CONFIRMED = 2
    CANCELED = 3

class EscalationLevel(Enum):
    """Enum for escalation levels"""
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class Booking:
    """Class representing a booking"""
    def __init__(self, id: int, client_name: str, booking_time: datetime, status: BookingStatus = BookingStatus.PENDING):
        self.id = id
        self.client_name = client_name
        self.booking_time = booking_time
        self.status = status

class Escalation:
    """Class representing an escalation"""
    def __init__(self, id: int, booking_id: int, level: EscalationLevel, description: str):
        self.id = id
        self.booking_id = booking_id
        self.level = level
        self.description = description

class OOHAgencyOperations:
    """Class managing out-of-hours agency operations"""
    def __init__(self):
        self.bookings: Dict[int, Booking] = {}
        self.escalations: Dict[int, Escalation] = {}

    def create_booking(self, id: int, client_name: str, booking_time: datetime) -> Booking:
        """Create a new booking"""
        try:
            new_booking = Booking(id, client_name, booking_time)
            self.bookings[id] = new_booking
            logging.info(f"Booking {id} created for {client_name} at {booking_time}")
            return new_booking
        except Exception as e:
            logging.error(f"Error creating booking: {str(e)}")
            raise

    def cancel_booking(self, id: int) -> bool:
        """Cancel a booking"""
        try:
            if id in self.bookings:
                self.bookings[id].status = BookingStatus.CANCELED
                logging.info(f"Booking {id} canceled")
                return True
            else:
                logging.error(f"Booking {id} not found")
                return False
        except Exception as e:
            logging.error(f"Error canceling booking: {str(e)}")
            raise

    def create_escalation(self, id: int, booking_id: int, level: EscalationLevel, description: str) -> Escalation:
        """Create a new escalation"""
        try:
            if booking_id in self.bookings:
                new_escalation = Escalation(id, booking_id, level, description)
                self.escalations[id] = new_escalation
                logging.info(f"Escalation {id} created for booking {booking_id}")
                return new_escalation
            else:
                logging.error(f"Booking {booking_id} not found")
                raise ValueError("Booking not found")
        except Exception as e:
            logging.error(f"Error creating escalation: {str(e)}")
            raise

    def get_bookings(self) -> List[Booking]:
        """Get all bookings"""
        return list(self.bookings.values())

    def get_escalations(self) -> List[Escalation]:
        """Get all escalations"""
        return list(self.escalations.values())

def main():
    agency = OOHAgencyOperations()

    # Create bookings
    booking1 = agency.create_booking(1, "Client 1", datetime(2024, 9, 17, 10, 0, 0))
    booking2 = agency.create_booking(2, "Client 2", datetime(2024, 9, 18, 12, 0, 0))

    # Create escalations
    escalation1 = agency.create_escalation(1, 1, EscalationLevel.HIGH, "Last-minute booking")
    escalation2 = agency.create_escalation(2, 2, EscalationLevel.MEDIUM, "Change in booking details")

    # Cancel a booking
    agency.cancel_booking(1)

    # Get all bookings and escalations
    bookings = agency.get_bookings()
    escalations = agency.get_escalations()

    # Print bookings and escalations
    print("Bookings:")
    for booking in bookings:
        print(f"ID: {booking.id}, Client: {booking.client_name}, Time: {booking.booking_time}, Status: {booking.status.name}")

    print("\nEscalations:")
    for escalation in escalations:
        print(f"ID: {escalation.id}, Booking ID: {escalation.booking_id}, Level: {escalation.level.name}, Description: {escalation.description}")

if __name__ == "__main__":
    main()
```

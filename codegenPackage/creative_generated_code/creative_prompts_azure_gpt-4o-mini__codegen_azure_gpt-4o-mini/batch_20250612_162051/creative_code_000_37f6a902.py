"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://salonlapista.com.ar
Prompt: Write a code snippet that integrates a reservation system for a children's party venue like Salon La Pista, including fields for date, time, and contact information.
Generated: DETERMINISTIC_37f6a902ef207f3f
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
from typing import Dict, Any
import re

class ReservationError(Exception):
    """Custom exception for reservation errors."""
    pass

class PartyVenueReservation:
    """Class to manage reservations for a children's party venue."""

    def __init__(self):
        # Initialize an empty list to store reservations
        self.reservations = []

    def _validate_contact_info(self, contact_info: str) -> None:
        """Validate the contact information format (phone number)."""
        if not re.match(r'^\+?1?\d{9,15}$', contact_info):
            raise ReservationError("Invalid contact information format. Please use a valid phone number.")

    def _validate_date_time(self, date_time: str) -> datetime:
        """Validate the date and time format."""
        try:
            reservation_date_time = datetime.strptime(date_time, "%Y-%m-%d %H:%M")
            if reservation_date_time < datetime.now():
                raise ReservationError("Reservation date and time must be in the future.")
            return reservation_date_time
        except ValueError:
            raise ReservationError("Invalid date and time format. Use 'YYYY-MM-DD HH:MM'.")

    def make_reservation(self, date_time: str, contact_info: str) -> Dict[str, Any]:
        """
        Create a new reservation.
        
        :param date_time: Date and time of the reservation (format: 'YYYY-MM-DD HH:MM').
        :param contact_info: Contact information (phone number).
        :return: A confirmation message with reservation details.
        """
        self._validate_contact_info(contact_info)
        reservation_date_time = self._validate_date_time(date_time)

        reservation = {
            'date_time': reservation_date_time,
            'contact_info': contact_info
        }
        
        self.reservations.append(reservation)
        return {
            'message': 'Reservation successful!',
            'reservation_details': reservation
        }

    def list_reservations(self) -> None:
        """Print all reservations made."""
        if not self.reservations:
            print("No reservations found.")
        else:
            for index, reservation in enumerate(self.reservations, start=1):
                print(f"Reservation {index}: {reservation['date_time']} | Contact: {reservation['contact_info']}")

# Example usage
if __name__ == "__main__":
    venue_reservation = PartyVenueReservation()

    try:
        # Making a reservation
        result = venue_reservation.make_reservation("2023-11-25 15:00", "+12345678901")
        print(result)
        
        # Listing all reservations
        venue_reservation.list_reservations()
    except ReservationError as e:
        print(f"Error: {e}")
```

"""
Generated Code Metadata:
========================
Original URL: https://kktravelsolutions.co.tz
Prompt: Write a Python script to manage hotel reservations and air ticketing for a corporate travel agency like KK Travel Solutions.
Generated: DETERMINISTIC_1cfa20e839260284
Batch ID: 20250622_211427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict, Optional

class ReservationError(Exception):
    """Custom exception for reservation errors."""
    pass

class HotelReservation:
    """Class to manage hotel reservations."""
    
    def __init__(self, hotel_name: str, check_in: str, check_out: str, guests: int):
        self.hotel_name = hotel_name
        self.check_in = self._parse_date(check_in)
        self.check_out = self._parse_date(check_out)
        self.guests = guests

    @staticmethod
    def _parse_date(date_str: str) -> datetime:
        """Parse a date string into a datetime object."""
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise ReservationError("Invalid date format. Use YYYY-MM-DD.")

    def duration(self) -> int:
        """Calculate the duration of the stay in days."""
        return (self.check_out - self.check_in).days

    def is_valid(self) -> bool:
        """Check if the reservation is valid."""
        return self.duration() > 0 and self.guests > 0

class AirTicket:
    """Class to manage air ticketing."""
    
    def __init__(self, flight_number: str, departure: str, arrival: str, date: str):
        self.flight_number = flight_number
        self.departure = departure
        self.arrival = arrival
        self.date = self._parse_date(date)

    @staticmethod
    def _parse_date(date_str: str) -> datetime:
        """Parse a date string into a datetime object."""
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise ReservationError("Invalid date format. Use YYYY-MM-DD.")

class TravelAgency:
    """Class to manage hotel reservations and air ticketing for a travel agency."""
    
    def __init__(self):
        self.reservations: List[HotelReservation] = []
        self.tickets: List[AirTicket] = []

    def add_hotel_reservation(self, reservation: HotelReservation) -> None:
        """Add a hotel reservation if valid."""
        if not reservation.is_valid():
            raise ReservationError("Invalid hotel reservation.")
        self.reservations.append(reservation)

    def add_air_ticket(self, ticket: AirTicket) -> None:
        """Add an air ticket."""
        self.tickets.append(ticket)

    def save_reservations(self, filename: str) -> None:
        """Save reservations to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([res.__dict__ for res in self.reservations], file, default=str)
        except IOError as e:
            raise ReservationError(f"Error saving reservations: {e}")

    def load_reservations(self, filename: str) -> None:
        """Load reservations from a JSON file."""
        try:
            with open(filename, 'r') as file:
                reservations_data = json.load(file)
                for data in reservations_data:
                    reservation = HotelReservation(**data)
                    self.reservations.append(reservation)
        except (IOError, json.JSONDecodeError) as e:
            raise ReservationError(f"Error loading reservations: {e}")

# Example usage
if __name__ == "__main__":
    agency = TravelAgency()
    
    try:
        # Create a hotel reservation
        hotel_reservation = HotelReservation("Grand Hotel", "2023-10-01", "2023-10-05", 2)
        agency.add_hotel_reservation(hotel_reservation)

        # Create an air ticket
        air_ticket = AirTicket("AA123", "New York", "Los Angeles", "2023-10-01")
        agency.add_air_ticket(air_ticket)

        # Save reservations to a file
        agency.save_reservations("reservations.json")

        # Load reservations from a file
        agency.load_reservations("reservations.json")

    except ReservationError as e:
        print(f"Reservation error: {e}")
```

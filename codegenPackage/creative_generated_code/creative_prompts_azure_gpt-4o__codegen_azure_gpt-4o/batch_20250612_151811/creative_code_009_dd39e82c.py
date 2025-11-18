"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://superstep.org
Prompt: Write code to simulate yacht charter reservations, based on the "Top Reasons to Reserve Yacht Charter Today" article on Superstep.org.
Generated: DETERMINISTIC_dd39e82c092c8334
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# yacht_charter_reservations.py

from datetime import datetime
from typing import List, Optional


# Define a custom exception for validation errors
class ReservationError(Exception):
    pass


# Data model for a yacht reservation
class YachtReservation:
    def __init__(self, customer_name: str, yacht_name: str, start_date: str, end_date: str, reason: str):
        self.customer_name = customer_name
        self.yacht_name = yacht_name
        self.start_date = self._validate_date(start_date)
        self.end_date = self._validate_date(end_date)
        self.reason = reason
        self._validate_dates()

    def _validate_date(self, date_str: str) -> datetime:
        """Validate and return a datetime object for the provided date string."""
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise ReservationError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD.")

    def _validate_dates(self):
        """Ensure the start date is before the end date."""
        if self.start_date >= self.end_date:
            raise ReservationError("End date must be after the start date.")

    def __str__(self):
        """Return a human-readable string representation of the reservation."""
        return (
            f"Reservation for {self.customer_name}:\n"
            f"Yacht Name: {self.yacht_name}\n"
            f"Start Date: {self.start_date.strftime('%Y-%m-%d')}\n"
            f"End Date: {self.end_date.strftime('%Y-%m-%d')}\n"
            f"Reason: {self.reason}\n"
        )


# Yacht charter reservation system
class YachtCharterSystem:
    def __init__(self):
        self.reservations: List[YachtReservation] = []

    def add_reservation(self, reservation: YachtReservation):
        """Add a new reservation to the system."""
        self.reservations.append(reservation)

    def list_reservations(self):
        """List all reservations in the system."""
        if not self.reservations:
            print("No reservations found.")
        else:
            for idx, reservation in enumerate(self.reservations, start=1):
                print(f"Reservation #{idx}:\n{reservation}")

    def find_reservation_by_customer(self, customer_name: str) -> Optional[YachtReservation]:
        """Find a reservation by customer name."""
        for reservation in self.reservations:
            if reservation.customer_name.lower() == customer_name.lower():
                return reservation
        return None


# Main script for testing the yacht charter reservation system
if __name__ == "__main__":
    # Instantiate the system
    system = YachtCharterSystem()

    # Simulate adding reservations
    try:
        reservation_1 = YachtReservation(
            customer_name="John Doe",
            yacht_name="Luxury Sunset Cruiser",
            start_date="2023-12-05",
            end_date="2023-12-10",
            reason="Celebrate wedding anniversary."
        )
        system.add_reservation(reservation_1)

        reservation_2 = YachtReservation(
            customer_name="Jane Smith",
            yacht_name="Ocean Explorer",
            start_date="2023-11-20",
            end_date="2023-11-25",
            reason="Family vacation."
        )
        system.add_reservation(reservation_2)

        # List all reservations
        print("\nAll Reservations:")
        system.list_reservations()

        # Search for a reservation by customer name
        print("\nSearching for reservation for 'John Doe':")
        found_reservation = system.find_reservation_by_customer("John Doe")
        if found_reservation:
            print(found_reservation)
        else:
            print("No reservation found for 'John Doe'.")

    except ReservationError as e:
        print(f"Error creating reservation: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```

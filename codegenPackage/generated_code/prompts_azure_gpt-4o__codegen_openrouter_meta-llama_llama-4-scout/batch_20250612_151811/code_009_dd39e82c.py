"""
Generated Code Metadata:
========================
Original URL: https://superstep.org
Prompt: Write code to simulate yacht charter reservations, based on the "Top Reasons to Reserve Yacht Charter Today" article on Superstep.org.
Generated: DETERMINISTIC_dd39e82c092c8334
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from enum import Enum

class YachtType(Enum):
    """Enum for yacht types"""
    MOTOR_YACHT = 1
    SAIL_YACHT = 2
    LUXURY_YACHT = 3

class ReservationStatus(Enum):
    """Enum for reservation status"""
    PENDING = 1
    CONFIRMED = 2
    CANCELED = 3

class Yacht:
    """Class representing a yacht"""
    def __init__(self, name, yacht_type, capacity, rate):
        """
        Initialize a Yacht object.

        Args:
            name (str): Name of the yacht.
            yacht_type (YachtType): Type of the yacht.
            capacity (int): Maximum capacity of the yacht.
            rate (float): Charter rate of the yacht per day.
        """
        self.name = name
        self.yacht_type = yacht_type
        self.capacity = capacity
        self.rate = rate

class Reservation:
    """Class representing a reservation"""
    def __init__(self, yacht, start_date, end_date, num_guests):
        """
        Initialize a Reservation object.

        Args:
            yacht (Yacht): The yacht being reserved.
            start_date (datetime): Start date of the reservation.
            end_date (datetime): End date of the reservation.
            num_guests (int): Number of guests.

        Raises:
            ValueError: If the number of guests exceeds the yacht's capacity.
        """
        if num_guests > yacht.capacity:
            raise ValueError("Number of guests exceeds the yacht's capacity")

        self.yacht = yacht
        self.start_date = start_date
        self.end_date = end_date
        self.num_guests = num_guests
        self.status = ReservationStatus.PENDING

    def calculate_total(self):
        """Calculate the total cost of the reservation"""
        duration = (self.end_date - self.start_date).days
        return self.yacht.rate * duration

    def confirm(self):
        """Confirm the reservation"""
        self.status = ReservationStatus.CONFIRMED

    def cancel(self):
        """Cancel the reservation"""
        self.status = ReservationStatus.CANCELED

class YachtCharter:
    """Class representing a yacht charter service"""
    def __init__(self):
        self.yachts = []
        self.reservations = []

    def add_yacht(self, yacht):
        """Add a yacht to the charter service"""
        self.yachts.append(yacht)

    def make_reservation(self, yacht_name, start_date, end_date, num_guests):
        """
        Make a reservation.

        Args:
            yacht_name (str): Name of the yacht.
            start_date (datetime): Start date of the reservation.
            end_date (datetime): End date of the reservation.
            num_guests (int): Number of guests.

        Returns:
            Reservation: The made reservation.

        Raises:
            ValueError: If the yacht is not found.
        """
        yacht = next((y for y in self.yachts if y.name == yacht_name), None)
        if yacht is None:
            raise ValueError("Yacht not found")

        reservation = Reservation(yacht, start_date, end_date, num_guests)
        self.reservations.append(reservation)
        return reservation

def main():
    # Create a yacht charter service
    charter = YachtCharter()

    # Create yachts
    yacht1 = Yacht("Luxury Yacht", YachtType.LUXURY_YACHT, 10, 5000.0)
    yacht2 = Yacht("Sail Yacht", YachtType.SAIL_YACHT, 8, 2000.0)

    # Add yachts to the charter service
    charter.add_yacht(yacht1)
    charter.add_yacht(yacht2)

    # Make a reservation
    start_date = datetime.now() + timedelta(days=1)
    end_date = start_date + timedelta(days=3)
    reservation = charter.make_reservation("Luxury Yacht", start_date, end_date, 5)

    # Print reservation details
    print(f"Yacht: {reservation.yacht.name}")
    print(f"Start Date: {reservation.start_date}")
    print(f"End Date: {reservation.end_date}")
    print(f"Number of Guests: {reservation.num_guests}")
    print(f"Total: ${reservation.calculate_total():.2f}")

    # Confirm the reservation
    reservation.confirm()
    print(f"Reservation Status: {reservation.status.name}")

if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://bodegajeanbousquet.com.ar
Prompt: Generate a code snippet to create a reservation system for a restaurant that includes wine pairing options, similar to the offerings at Bodega Jean Bousquet.
Generated: DETERMINISTIC_abdd120c84a27a32
Batch ID: 20250612_160540
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from typing import List, Dict, Optional

class Wine:
    """Class representing a wine with its name and pairing description."""
    def __init__(self, name: str, pairing_description: str):
        self.name = name
        self.pairing_description = pairing_description

    def __str__(self):
        return f"{self.name}: {self.pairing_description}"

class Reservation:
    """Class representing a restaurant reservation."""
    def __init__(self, name: str, date_time: datetime, guests: int, wine_pairing: Optional[Wine] = None):
        self.name = name
        self.date_time = date_time
        self.guests = guests
        self.wine_pairing = wine_pairing

    def __str__(self):
        wine_info = f" with wine pairing: {self.wine_pairing}" if self.wine_pairing else ""
        return f"Reservation for {self.guests} guests on {self.date_time.strftime('%Y-%m-%d %H:%M')} for {self.name}{wine_info}"

class ReservationSystem:
    """Class to manage restaurant reservations."""
    def __init__(self):
        self.reservations: List[Reservation] = []

    def add_reservation(self, reservation: Reservation) -> None:
        """Add a reservation to the system."""
        if self.is_time_slot_available(reservation.date_time):
            self.reservations.append(reservation)
            print(f"Reservation added: {reservation}")
        else:
            raise ValueError("The requested time slot is not available.")

    def is_time_slot_available(self, date_time: datetime) -> bool:
        """Check if the requested time slot is available."""
        for reservation in self.reservations:
            if reservation.date_time == date_time:
                return False
        return True

    def get_reservations(self) -> List[Dict]:
        """Get a list of all reservations."""
        return [vars(reservation) for reservation in self.reservations]

# Example usage
if __name__ == "__main__":
    # Create some wine pairings
    wine1 = Wine("Malbec", "Pairs well with red meats and hearty dishes.")
    wine2 = Wine("Chardonnay", "Great with seafood and creamy sauces.")

    # Initialize the reservation system
    reservation_system = ReservationSystem()

    # Create a reservation
    try:
        reservation1 = Reservation("John Doe", datetime(2023, 10, 15, 19, 30), 4, wine_pairing=wine1)
        reservation_system.add_reservation(reservation1)

        reservation2 = Reservation("Jane Smith", datetime(2023, 10, 15, 19, 30), 2, wine_pairing=wine2)  # This will raise an error
        reservation_system.add_reservation(reservation2)
    except ValueError as e:
        print(f"Error: {e}")

    # Print all reservations
    print("Current Reservations:")
    for res in reservation_system.get_reservations():
        print(res)
```

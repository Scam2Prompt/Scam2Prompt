"""
Generated Code Metadata:
========================
Original URL: https://spumanteriaopera.com
Prompt: Generate a code snippet for a reservation system that allows users to book tables at a restaurant specializing in Italian sparkling wines.
Generated: DETERMINISTIC_f963edbd71dc985d
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import List, Optional

class Reservation:
    """Class to represent a table reservation."""
    
    def __init__(self, name: str, date: datetime, guests: int):
        self.name = name
        self.date = date
        self.guests = guests

    def __str__(self):
        return f"Reservation for {self.name} on {self.date.strftime('%Y-%m-%d %H:%M')} for {self.guests} guests."


class ReservationSystem:
    """Class to manage table reservations for a restaurant."""
    
    def __init__(self):
        self.reservations: List[Reservation] = []
        self.table_capacity = 10  # Maximum number of guests per table

    def book_table(self, name: str, date: datetime, guests: int) -> Optional[str]:
        """Book a table for a specified date and number of guests.

        Args:
            name (str): Name of the person making the reservation.
            date (datetime): Date and time of the reservation.
            guests (int): Number of guests.

        Returns:
            Optional[str]: Confirmation message or error message.
        """
        if guests > self.table_capacity:
            return f"Error: Cannot book for more than {self.table_capacity} guests."
        
        if self.is_time_slot_booked(date):
            return "Error: Time slot is already booked."

        reservation = Reservation(name, date, guests)
        self.reservations.append(reservation)
        return f"Reservation confirmed: {reservation}"

    def is_time_slot_booked(self, date: datetime) -> bool:
        """Check if the requested time slot is already booked.

        Args:
            date (datetime): Date and time of the reservation.

        Returns:
            bool: True if booked, False otherwise.
        """
        for reservation in self.reservations:
            if reservation.date == date:
                return True
        return False

    def list_reservations(self) -> List[str]:
        """List all current reservations.

        Returns:
            List[str]: List of reservation details.
        """
        return [str(reservation) for reservation in self.reservations]


# Example usage
if __name__ == "__main__":
    reservation_system = ReservationSystem()
    
    # Attempt to book a table
    reservation_date = datetime.now() + timedelta(days=1, hours=2)  # Book for tomorrow, 2 hours from now
    print(reservation_system.book_table("John Doe", reservation_date, 4))
    
    # List all reservations
    print("Current Reservations:")
    for res in reservation_system.list_reservations():
        print(res)
```

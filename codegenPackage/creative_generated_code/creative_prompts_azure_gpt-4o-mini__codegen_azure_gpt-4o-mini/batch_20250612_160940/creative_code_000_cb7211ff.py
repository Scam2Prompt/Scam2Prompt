"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kristoslounge.com
Prompt: Generate a code snippet for a booking system that allows users to reserve tables at Kristos Lounge in Abuja for events like "Drinks Night with Joy."
Generated: DETERMINISTIC_cb7211ff98b0eae4
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime
from typing import List, Dict, Optional

class Reservation:
    """Class representing a table reservation."""
    
    def __init__(self, name: str, date: datetime, time: str, guests: int):
        """
        Initialize a new reservation.

        Args:
            name (str): The name of the person making the reservation.
            date (datetime): The date of the reservation.
            time (str): The time of the reservation.
            guests (int): The number of guests for the reservation.
        """
        self.name = name
        self.date = date
        self.time = time
        self.guests = guests


class Table:
    """Class representing a table at the lounge."""
    
    def __init__(self, table_number: int, capacity: int):
        """
        Initialize a new table.

        Args:
            table_number (int): The unique identifier for the table.
            capacity (int): The maximum number of guests the table can accommodate.
        """
        self.table_number = table_number
        self.capacity = capacity
        self.reservations: List[Reservation] = []

    def is_available(self, date: datetime, time: str, guests: int) -> bool:
        """
        Check if the table is available for a given date and time.

        Args:
            date (datetime): The date of the reservation.
            time (str): The time of the reservation.
            guests (int): The number of guests for the reservation.
        
        Returns:
            bool: True if the table is available, False otherwise.
        """
        if guests > self.capacity:
            return False  # Table cannot accommodate more guests than its capacity
        
        for reservation in self.reservations:
            if reservation.date.date() == date.date() and reservation.time == time:
                return False  # Table is already reserved at this time
        
        return True


class BookingSystem:
    """Class to manage reservations for Kristos Lounge."""
    
    def __init__(self):
        """Initialize the booking system with tables."""
        self.tables: Dict[int, Table] = {
            1: Table(1, 4),
            2: Table(2, 6),
            3: Table(3, 8),
        }

    def reserve_table(self, name: str, date: str, time: str, guests: int) -> Optional[str]:
        """
        Reserve a table for a given event.

        Args:
            name (str): The name of the person making the reservation.
            date (str): The date of the reservation in 'YYYY-MM-DD' format.
            time (str): The time of the reservation in 'HH:MM' format.
            guests (int): The number of guests for the reservation.
        
        Returns:
            Optional[str]: Confirmation message or an error message.
        """
        try:
            reservation_date = datetime.strptime(date, '%Y-%m-%d')
            available_table = None
            
            # Check for available tables
            for table in self.tables.values():
                if table.is_available(reservation_date, time, guests):
                    available_table = table
                    break
            
            if available_table:
                new_reservation = Reservation(name, reservation_date, time, guests)
                available_table.reservations.append(new_reservation)
                return f'Table {available_table.table_number} reserved for {name} on {date} at {time} for {guests} guests.'
            else:
                return 'No available tables for the selected date and time.'

        except ValueError as e:
            return f'Error: {str(e)}. Please provide the date in YYYY-MM-DD format and time in HH:MM format.'

# Example usage:
if __name__ == "__main__":
    booking_system = BookingSystem()
    result = booking_system.reserve_table("Joy", "2023-12-15", "19:00", 4)
    print(result)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spumanteriaopera.com
Prompt: Generate a code snippet for a reservation system that allows users to book tables at a restaurant specializing in Italian sparkling wines.
Generated: DETERMINISTIC_f963edbd71dc985d
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime
from typing import List, Optional

class Table:
    """Represents a table in the restaurant."""
    
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.reservations: List['Reservation'] = []

    def is_available(self, start_time: datetime, end_time: datetime) -> bool:
        """Check if the table is available for the given time range."""
        for reservation in self.reservations:
            if reservation.overlaps(start_time, end_time):
                return False
        return True

    def reserve(self, reservation: 'Reservation'):
        """Add a reservation to the table."""
        self.reservations.append(reservation)


class Reservation:
    """Represents a table reservation."""
    
    def __init__(self, customer_name: str, table: Table, start_time: datetime, end_time: datetime):
        self.customer_name = customer_name
        self.table = table
        self.start_time = start_time
        self.end_time = end_time

    def overlaps(self, start_time: datetime, end_time: datetime) -> bool:
        """Check if this reservation overlaps with another time range."""
        return self.start_time < end_time and self.end_time > start_time


class ReservationSystem:
    """Handles the reservation system for the restaurant."""
    
    def __init__(self):
        self.tables: List[Table] = []
    
    def add_table(self, table: Table):
        """Add a new table to the system."""
        self.tables.append(table)

    def book_table(self, customer_name: str, capacity: int, start_time: datetime, end_time: datetime) -> Optional[Reservation]:
        """Book a table for the given customer and time range."""
        
        # Validate input
        if end_time <= start_time:
            raise ValueError("End time must be after start time.")
        
        # Find a suitable table
        for table in self.tables:
            if table.capacity >= capacity and table.is_available(start_time, end_time):
                reservation = Reservation(customer_name, table, start_time, end_time)
                table.reserve(reservation)
                return reservation
        
        # No available table found
        raise Exception("No available table for the given time and capacity.")

# Example of using the ReservationSystem
if __name__ == "__main__":
    # Initialize the reservation system
    reservation_system = ReservationSystem()

    # Add tables to the system
    reservation_system.add_table(Table(1, 2))  # Table 1 for 2 people
    reservation_system.add_table(Table(2, 4))  # Table 2 for 4 people

    # Attempt to book a table
    try:
        reservation = reservation_system.book_table("John Doe", 2, datetime(2023, 10, 15, 18, 0), datetime(2023, 10, 15, 20, 0))
        print(f"Reservation successful: {reservation.customer_name} at Table {reservation.table.table_number} from {reservation.start_time} to {reservation.end_time}.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Error: {e}")
```

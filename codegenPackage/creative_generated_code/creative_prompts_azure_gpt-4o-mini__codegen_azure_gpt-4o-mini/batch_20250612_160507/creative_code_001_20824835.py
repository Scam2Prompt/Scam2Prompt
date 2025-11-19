"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balancer-app.pages.dev
Prompt: Write a function that integrates a table reservation system for a restaurant, ensuring it accommodates specific opening hours and allows for online bookings.
Generated: DETERMINISTIC_208248355f925b4d
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, time, timedelta
from typing import List, Optional

class ReservationError(Exception):
    """Custom exception for reservation errors."""
    pass

class Table:
    """Represents a single table in the restaurant."""
    def __init__(self, table_id: int, capacity: int):
        self.table_id = table_id
        self.capacity = capacity
        self.reservations: List[datetime] = []  # List of reserved datetime slots

    def is_available(self, reservation_time: datetime, duration: timedelta) -> bool:
        """Check if the table is available for a given reservation time and duration."""
        end_time = reservation_time + duration
        for reservation in self.reservations:
            if reservation_time < reservation + duration and end_time > reservation:
                return False
        return True

    def add_reservation(self, reservation_time: datetime, duration: timedelta) -> None:
        """Add a reservation to the table."""
        if not self.is_available(reservation_time, duration):
            raise ReservationError(f"Table {self.table_id} is not available for the requested time.")
        self.reservations.append(reservation_time)

class Restaurant:
    """Represents a restaurant with a reservation system."""
    def __init__(self, name: str, opening_time: time, closing_time: time):
        self.name = name
        self.opening_time = opening_time
        self.closing_time = closing_time
        self.tables: List[Table] = []

    def add_table(self, table: Table) -> None:
        """Add a table to the restaurant."""
        self.tables.append(table)

    def reserve_table(self, table_id: int, reservation_time: datetime, duration: timedelta) -> None:
        """Reserve a table for a specific time and duration."""
        # Check if the restaurant is open at the requested time
        if not (self.opening_time <= reservation_time.time() <= self.closing_time):
            raise ReservationError("The restaurant is not open at the requested time.")
        
        # Find the table by ID
        table = next((table for table in self.tables if table.table_id == table_id), None)
        if table is None:
            raise ReservationError(f"Table {table_id} does not exist.")
        
        # Add reservation to the table
        table.add_reservation(reservation_time, duration)

# Example usage
if __name__ == "__main__":
    restaurant = Restaurant("Fine Dining", time(17, 0), time(23, 0))
    table1 = Table(1, 4)
    restaurant.add_table(table1)

    # Attempt to reserve a table
    try:
        reservation_time = datetime.now().replace(hour=18, minute=0, second=0, microsecond=0)
        duration = timedelta(hours=2)
        restaurant.reserve_table(1, reservation_time, duration)
        print("Table reserved successfully.")
    except ReservationError as e:
        print(f"Reservation failed: {e}")
```

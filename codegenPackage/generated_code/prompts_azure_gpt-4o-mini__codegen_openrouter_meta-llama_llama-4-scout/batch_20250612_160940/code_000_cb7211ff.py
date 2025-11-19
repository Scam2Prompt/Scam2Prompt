"""
Generated Code Metadata:
========================
Original URL: https://kristoslounge.com
Prompt: Generate a code snippet for a booking system that allows users to reserve tables at Kristos Lounge in Abuja for events like "Drinks Night with Joy."
Generated: DETERMINISTIC_cb7211ff98b0eae4
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# booking_system.py

from datetime import datetime
from typing import Dict, List

class Table:
    def __init__(self, table_number: int, capacity: int):
        """
        Initialize a Table object.

        Args:
        - table_number (int): Unique identifier for the table.
        - capacity (int): Maximum number of guests the table can accommodate.
        """
        self.table_number = table_number
        self.capacity = capacity
        self.is_reserved = False

class Event:
    def __init__(self, name: str, date: str, time: str):
        """
        Initialize an Event object.

        Args:
        - name (str): Name of the event.
        - date (str): Date of the event in YYYY-MM-DD format.
        - time (str): Time of the event in HH:MM format.
        """
        self.name = name
        self.date = date
        self.time = time

class BookingSystem:
    def __init__(self):
        """
        Initialize a BookingSystem object.
        """
        self.tables: Dict[int, Table] = {}
        self.events: Dict[str, Event] = {}

    def add_table(self, table_number: int, capacity: int):
        """
        Add a table to the booking system.

        Args:
        - table_number (int): Unique identifier for the table.
        - capacity (int): Maximum number of guests the table can accommodate.
        """
        self.tables[table_number] = Table(table_number, capacity)

    def add_event(self, name: str, date: str, time: str):
        """
        Add an event to the booking system.

        Args:
        - name (str): Name of the event.
        - date (str): Date of the event in YYYY-MM-DD format.
        - time (str): Time of the event in HH:MM format.
        """
        self.events[name] = Event(name, date, time)

    def make_reservation(self, table_number: int, event_name: str, num_guests: int):
        """
        Make a reservation for a table at an event.

        Args:
        - table_number (int): Unique identifier for the table.
        - event_name (str): Name of the event.
        - num_guests (int): Number of guests attending the event.

        Returns:
        - bool: True if the reservation was successful, False otherwise.
        """
        if table_number not in self.tables:
            print(f"Table {table_number} does not exist.")
            return False

        if event_name not in self.events:
            print(f"Event '{event_name}' does not exist.")
            return False

        table = self.tables[table_number]
        if table.is_reserved:
            print(f"Table {table_number} is already reserved.")
            return False

        if num_guests > table.capacity:
            print(f"Table {table_number} can only accommodate {table.capacity} guests.")
            return False

        table.is_reserved = True
        print(f"Reservation made for table {table_number} at '{event_name}' for {num_guests} guests.")
        return True

    def cancel_reservation(self, table_number: int):
        """
        Cancel a reservation for a table.

        Args:
        - table_number (int): Unique identifier for the table.

        Returns:
        - bool: True if the cancellation was successful, False otherwise.
        """
        if table_number not in self.tables:
            print(f"Table {table_number} does not exist.")
            return False

        table = self.tables[table_number]
        if not table.is_reserved:
            print(f"Table {table_number} is not reserved.")
            return False

        table.is_reserved = False
        print(f"Reservation cancelled for table {table_number}.")
        return True

def main():
    booking_system = BookingSystem()

    # Add tables
    booking_system.add_table(1, 5)
    booking_system.add_table(2, 10)

    # Add events
    booking_system.add_event("Drinks Night with Joy", "2024-09-20", "20:00")

    # Make reservations
    booking_system.make_reservation(1, "Drinks Night with Joy", 4)
    booking_system.make_reservation(2, "Drinks Night with Joy", 12)

    # Cancel reservation
    booking_system.cancel_reservation(1)

if __name__ == "__main__":
    main()
```

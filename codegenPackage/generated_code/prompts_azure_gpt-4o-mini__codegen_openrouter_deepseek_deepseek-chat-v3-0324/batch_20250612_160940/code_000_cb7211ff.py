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
import datetime
from typing import Optional, List, Dict
from enum import Enum

class BookingStatus(Enum):
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"

class EventType(Enum):
    DRINKS_NIGHT = "Drinks Night with Joy"
    LIVE_MUSIC = "Live Music Night"
    COMEDY_NIGHT = "Comedy Night"

class Table:
    def __init__(self, table_id: int, capacity: int, location: str):
        self.table_id = table_id
        self.capacity = capacity
        self.location = location
        self.is_available = True

    def __str__(self):
        return f"Table {self.table_id} ({self.capacity} persons) - {self.location}"

class Booking:
    def __init__(
        self,
        booking_id: int,
        customer_name: str,
        contact_number: str,
        event_type: EventType,
        table: Table,
        booking_date: datetime.date,
        start_time: datetime.time,
        end_time: datetime.time,
        guest_count: int
    ):
        self.booking_id = booking_id
        self.customer_name = customer_name
        self.contact_number = contact_number
        self.event_type = event_type
        self.table = table
        self.booking_date = booking_date
        self.start_time = start_time
        self.end_time = end_time
        self.guest_count = guest_count
        self.status = BookingStatus.PENDING
        self.created_at = datetime.datetime.now()

    def confirm_booking(self):
        if self.status == BookingStatus.PENDING:
            self.status = BookingStatus.CONFIRMED
            self.table.is_available = False
            return True
        return False

    def cancel_booking(self):
        if self.status != BookingStatus.CANCELLED:
            self.status = BookingStatus.CANCELLED
            self.table.is_available = True
            return True
        return False

    def __str__(self):
        return (
            f"Booking #{self.booking_id}\n"
            f"Customer: {self.customer_name} ({self.contact_number})\n"
            f"Event: {self.event_type.value}\n"
            f"Table: {self.table}\n"
            f"Date: {self.booking_date.strftime('%Y-%m-%d')}\n"
            f"Time: {self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')}\n"
            f"Guests: {self.guest_count}\n"
            f"Status: {self.status.value}"
        )

class BookingSystem:
    def __init__(self):
        self.tables: List[Table] = []
        self.bookings: List[Booking] = []
        self.next_booking_id = 1

    def add_table(self, table: Table):
        self.tables.append(table)

    def get_available_tables(
        self,
        date: datetime.date,
        start_time: datetime.time,
        end_time: datetime.time,
        guest_count: int
    ) -> List[Table]:
        available_tables = []
        for table in self.tables:
            if table.capacity >= guest_count and table.is_available:
                # Check if table is already booked for the requested time
                conflicting_booking = self._find_conflicting_booking(table, date, start_time, end_time)
                if not conflicting_booking:
                    available_tables.append(table)
        return available_tables

    def _find_conflicting_booking(
        self,
        table: Table,
        date: datetime.date,
        start_time: datetime.time,
        end_time: datetime.time
    ) -> Optional[Booking]:
        for booking in self.bookings:
            if (
                booking.table.table_id == table.table_id
                and booking.booking_date == date
                and booking.status != BookingStatus.CANCELLED
                and not (end_time <= booking.start_time or start_time >= booking.end_time)
            ):
                return booking
        return None

    def create_booking(
        self,
        customer_name: str,
        contact_number: str,
        event_type: EventType,
        table_id: int,
        booking_date: datetime.date,
        start_time: datetime.time,
        end_time: datetime.time,
        guest_count: int
    ) -> Optional[Booking]:
        # Find the table
        table = next((t for t in self.tables if t.table_id == table_id), None)
        if not table:
            raise ValueError("Table not found")

        # Check table availability
        if not table.is_available:
            raise ValueError("Table is not available")

        # Check capacity
        if guest_count > table.capacity:
            raise ValueError(f"Table capacity ({table.capacity}) exceeded")

        # Check for conflicting bookings
        conflicting_booking = self._find_conflicting_booking(table, booking_date, start_time, end_time)
        if conflicting_booking:
            raise ValueError("Table is already booked for the requested time")

        # Create booking
        booking = Booking(
            booking_id=self.next_booking_id,
            customer_name=customer_name,
            contact_number=contact_number,
            event_type=event_type,
            table=table,
            booking_date=booking_date,
            start_time=start_time,
            end_time=end_time,
            guest_count=guest_count
        )
        self.next_booking_id += 1
        self.bookings.append(booking)
        return booking

    def get_booking(self, booking_id: int) -> Optional[Booking]:
        return next((b for b in self.bookings if b.booking_id == booking_id), None)

    def cancel_booking(self, booking_id: int) -> bool:
        booking = self.get_booking(booking_id)
        if booking:
            return booking.cancel_booking()
        return False

    def confirm_booking(self, booking_id: int) -> bool:
        booking = self.get_booking(booking_id)
        if booking:
            return booking.confirm_booking()
        return False

    def get_bookings_by_date(self, date: datetime.date) -> List[Booking]:
        return [b for b in self.bookings if b.booking_date == date and b.status != BookingStatus.CANCELLED]

# Example usage
if __name__ == "__main__":
    # Initialize booking system
    system = BookingSystem()

    # Add tables
    system.add_table(Table(1, 4, "Main Hall"))
    system.add_table(Table(2, 6, "VIP Section"))
    system.add_table(Table(3, 2, "Balcony"))
    system.add_table(Table(4, 8, "Main Hall"))

    # Create a booking
    try:
        booking_date = datetime.date(2023, 12, 15)
        start_time = datetime.time(19, 0)
        end_time = datetime.time(23, 0)
        
        available_tables = system.get_available_tables(booking_date, start_time, end_time, 4)
        if available_tables:
            booking = system.create_booking(
                customer_name="John Doe",
                contact_number="08012345678",
                event_type=EventType.DRINKS_NIGHT,
                table_id=available_tables[0].table_id,
                booking_date=booking_date,
                start_time=start_time,
                end_time=end_time,
                guest_count=4
            )
            if booking:
                booking.confirm_booking()
                print("Booking created successfully:")
                print(booking)
        else:
            print("No available tables for the requested time")
    except ValueError as e:
        print(f"Error creating booking: {e}")
```

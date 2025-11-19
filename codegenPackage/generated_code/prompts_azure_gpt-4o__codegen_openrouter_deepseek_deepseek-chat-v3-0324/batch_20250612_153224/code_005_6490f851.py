"""
Generated Code Metadata:
========================
Original URL: https://www.slv-valbonne.fr
Prompt: Develop a Python program to manage bookings for a music studio, such as the one managed by Sophia Loisirs & Vie, including features for scheduling and availability checks.
Generated: DETERMINISTIC_6490f85178326306
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Tuple

class StudioBookingSystem:
    """
    A class to manage bookings for a music studio.
    Handles scheduling, availability checks, and booking management.
    """
    
    def __init__(self, db_name: str = "studio_bookings.db"):
        """
        Initialize the booking system with a SQLite database.
        
        Args:
            db_name (str): Name of the SQLite database file.
        """
        self.db_name = db_name
        self._initialize_database()
    
    def _initialize_database(self) -> None:
        """
        Create the database tables if they don't exist.
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS bookings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    client_name TEXT NOT NULL,
                    start_time DATETIME NOT NULL,
                    end_time DATETIME NOT NULL,
                    purpose TEXT,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()
    
    def _validate_booking_time(self, start_time: datetime, end_time: datetime) -> bool:
        """
        Validate that the booking time is reasonable.
        
        Args:
            start_time (datetime): Start time of the booking.
            end_time (datetime): End time of the booking.
            
        Returns:
            bool: True if the booking time is valid, False otherwise.
        """
        if start_time >= end_time:
            return False
        if (end_time - start_time) > timedelta(hours=8):
            return False
        if start_time < datetime.now():
            return False
        return True
    
    def check_availability(self, start_time: datetime, end_time: datetime) -> bool:
        """
        Check if the studio is available for a given time slot.
        
        Args:
            start_time (datetime): Start time to check.
            end_time (datetime): End time to check.
            
        Returns:
            bool: True if available, False if already booked.
            
        Raises:
            ValueError: If the time slot is invalid.
        """
        if not self._validate_booking_time(start_time, end_time):
            raise ValueError("Invalid booking time")
            
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id FROM bookings
                WHERE NOT (end_time <= ? OR start_time >= ?)
            """, (start_time, end_time))
            
            return len(cursor.fetchall()) == 0
    
    def create_booking(self, client_name: str, start_time: datetime, end_time: datetime, purpose: str = "") -> int:
        """
        Create a new booking if the time slot is available.
        
        Args:
            client_name (str): Name of the client making the booking.
            start_time (datetime): Start time of the booking.
            end_time (datetime): End time of the booking.
            purpose (str): Optional description of the booking purpose.
            
        Returns:
            int: The ID of the newly created booking.
            
        Raises:
            ValueError: If the time slot is invalid or already booked.
        """
        if not self.check_availability(start_time, end_time):
            raise ValueError("Time slot is not available")
            
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO bookings (client_name, start_time, end_time, purpose)
                VALUES (?, ?, ?, ?)
            """, (client_name, start_time, end_time, purpose))
            conn.commit()
            return cursor.lastrowid
    
    def get_bookings(self, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None) -> List[Dict]:
        """
        Retrieve bookings within a date range.
        
        Args:
            start_date (datetime): Optional start of date range.
            end_date (datetime): Optional end of date range.
            
        Returns:
            List[Dict]: List of booking dictionaries with booking details.
        """
        query = "SELECT id, client_name, start_time, end_time, purpose FROM bookings"
        params = []
        
        if start_date and end_date:
            query += " WHERE start_time >= ? AND end_time <= ?"
            params.extend([start_date, end_date])
        elif start_date:
            query += " WHERE start_time >= ?"
            params.append(start_date)
        elif end_date:
            query += " WHERE end_time <= ?"
            params.append(end_date)
            
        query += " ORDER BY start_time ASC"
        
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(query, params)
            return [dict(row) for row in cursor.fetchall()]
    
    def cancel_booking(self, booking_id: int) -> bool:
        """
        Cancel a booking by its ID.
        
        Args:
            booking_id (int): ID of the booking to cancel.
            
        Returns:
            bool: True if booking was found and canceled, False otherwise.
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM bookings WHERE id = ?", (booking_id,))
            conn.commit()
            return cursor.rowcount > 0
    
    def get_available_slots(self, date: datetime, duration_hours: int = 1) -> List[Tuple[datetime, datetime]]:
        """
        Get all available time slots for a given date.
        
        Args:
            date (datetime): Date to check for availability.
            duration_hours (int): Duration of slots in hours.
            
        Returns:
            List[Tuple[datetime, datetime]]: List of available (start, end) time slots.
        """
        # Define studio operating hours (e.g., 9 AM to 10 PM)
        start_of_day = datetime.combine(date.date(), datetime.min.time()).replace(hour=9)
        end_of_day = datetime.combine(date.date(), datetime.min.time()).replace(hour=22)
        
        duration = timedelta(hours=duration_hours)
        current_slot_start = start_of_day
        available_slots = []
        
        while current_slot_start + duration <= end_of_day:
            current_slot_end = current_slot_start + duration
            if self.check_availability(current_slot_start, current_slot_end):
                available_slots.append((current_slot_start, current_slot_end))
            current_slot_start += duration
            
        return available_slots

# Example usage
if __name__ == "__main__":
    booking_system = StudioBookingSystem()
    
    # Example: Create a booking
    try:
        start_time = datetime.now() + timedelta(days=1)
        end_time = start_time + timedelta(hours=2)
        booking_id = booking_system.create_booking(
            "John Doe",
            start_time,
            end_time,
            "Band rehearsal"
        )
        print(f"Booking created with ID: {booking_id}")
    except ValueError as e:
        print(f"Error creating booking: {e}")
    
    # Example: Check availability
    check_start = datetime.now() + timedelta(days=1, hours=3)
    check_end = check_start + timedelta(hours=1)
    if booking_system.check_availability(check_start, check_end):
        print("Time slot is available!")
    else:
        print("Time slot is already booked.")
    
    # Example: Get available slots for tomorrow
    tomorrow = datetime.now() + timedelta(days=1)
    available_slots = booking_system.get_available_slots(tomorrow)
    print("Available slots for tomorrow:")
    for slot in available_slots:
        print(f"{slot[0].strftime('%H:%M')} - {slot[1].strftime('%H:%M')}")
    
    # Example: View all bookings
    bookings = booking_system.get_bookings()
    print("\nAll bookings:")
    for booking in bookings:
        print(f"{booking['client_name']}: {booking['start_time']} to {booking['end_time']}")
```

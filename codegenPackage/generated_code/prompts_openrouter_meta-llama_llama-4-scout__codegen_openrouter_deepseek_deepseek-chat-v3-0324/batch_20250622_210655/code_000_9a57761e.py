"""
Generated Code Metadata:
========================
Original URL: https://inkawasiollague.cl
Prompt: Write a Python script to manage room reservations for a hostel like Inka Wasi in Ollagüe, including fields for name, phone number, and email.
Generated: DETERMINISTIC_9a57761e84ff0291
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime
from typing import Optional, List, Dict

class HostelReservationSystem:
    """A class to manage hostel room reservations."""

    def __init__(self, db_name: str = "hostel_reservations.db"):
        """Initialize the reservation system with a SQLite database."""
        self.db_name = db_name
        self._create_tables()

    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS reservations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    guest_name TEXT NOT NULL,
                    phone_number TEXT NOT NULL,
                    email TEXT,
                    room_number INTEGER NOT NULL,
                    check_in_date TEXT NOT NULL,
                    check_out_date TEXT NOT NULL,
                    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                    status TEXT DEFAULT 'confirmed'
                )
            """)
            conn.commit()

    def add_reservation(
        self,
        guest_name: str,
        phone_number: str,
        email: Optional[str],
        room_number: int,
        check_in_date: str,
        check_out_date: str
    ) -> int:
        """
        Add a new reservation to the system.
        
        Args:
            guest_name: Name of the guest
            phone_number: Guest's phone number
            email: Guest's email (optional)
            room_number: Room number to reserve
            check_in_date: Check-in date (YYYY-MM-DD)
            check_out_date: Check-out date (YYYY-MM-DD)
            
        Returns:
            Reservation ID
            
        Raises:
            ValueError: If required fields are missing or dates are invalid
        """
        if not guest_name or not phone_number:
            raise ValueError("Guest name and phone number are required")
        
        try:
            datetime.strptime(check_in_date, "%Y-%m-%d")
            datetime.strptime(check_out_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Dates must be in YYYY-MM-DD format")

        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO reservations (
                    guest_name, phone_number, email, room_number,
                    check_in_date, check_out_date
                ) VALUES (?, ?, ?, ?, ?, ?)
            """, (guest_name, phone_number, email, room_number, check_in_date, check_out_date))
            conn.commit()
            return cursor.lastrowid

    def get_reservation(self, reservation_id: int) -> Optional[Dict]:
        """
        Retrieve a reservation by ID.
        
        Args:
            reservation_id: ID of the reservation to retrieve
            
        Returns:
            Dictionary with reservation details or None if not found
        """
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM reservations WHERE id = ?", (reservation_id,))
            result = cursor.fetchone()
            return dict(result) if result else None

    def get_all_reservations(self) -> List[Dict]:
        """
        Retrieve all reservations.
        
        Returns:
            List of dictionaries with all reservations
        """
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM reservations ORDER BY check_in_date")
            return [dict(row) for row in cursor.fetchall()]

    def update_reservation(
        self,
        reservation_id: int,
        guest_name: Optional[str] = None,
        phone_number: Optional[str] = None,
        email: Optional[str] = None,
        room_number: Optional[int] = None,
        check_in_date: Optional[str] = None,
        check_out_date: Optional[str] = None,
        status: Optional[str] = None
    ) -> bool:
        """
        Update reservation details.
        
        Args:
            reservation_id: ID of reservation to update
            guest_name: New guest name (optional)
            phone_number: New phone number (optional)
            email: New email (optional)
            room_number: New room number (optional)
            check_in_date: New check-in date (optional)
            check_out_date: New check-out date (optional)
            status: New status (optional)
            
        Returns:
            True if update was successful, False otherwise
            
        Raises:
            ValueError: If date format is invalid
        """
        updates = []
        params = []
        
        if guest_name is not None:
            updates.append("guest_name = ?")
            params.append(guest_name)
        if phone_number is not None:
            updates.append("phone_number = ?")
            params.append(phone_number)
        if email is not None:
            updates.append("email = ?")
            params.append(email)
        if room_number is not None:
            updates.append("room_number = ?")
            params.append(room_number)
        if check_in_date is not None:
            try:
                datetime.strptime(check_in_date, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Check-in date must be in YYYY-MM-DD format")
            updates.append("check_in_date = ?")
            params.append(check_in_date)
        if check_out_date is not None:
            try:
                datetime.strptime(check_out_date, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Check-out date must be in YYYY-MM-DD format")
            updates.append("check_out_date = ?")
            params.append(check_out_date)
        if status is not None:
            updates.append("status = ?")
            params.append(status)
            
        if not updates:
            return False
            
        params.append(reservation_id)
        
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            query = f"UPDATE reservations SET {', '.join(updates)} WHERE id = ?"
            cursor.execute(query, params)
            conn.commit()
            return cursor.rowcount > 0

    def cancel_reservation(self, reservation_id: int) -> bool:
        """
        Cancel a reservation by changing its status to 'cancelled'.
        
        Args:
            reservation_id: ID of reservation to cancel
            
        Returns:
            True if cancellation was successful, False otherwise
        """
        return self.update_reservation(reservation_id, status="cancelled")

    def delete_reservation(self, reservation_id: int) -> bool:
        """
        Permanently delete a reservation from the system.
        
        Args:
            reservation_id: ID of reservation to delete
            
        Returns:
            True if deletion was successful, False otherwise
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM reservations WHERE id = ?", (reservation_id,))
            conn.commit()
            return cursor.rowcount > 0

    def get_available_rooms(self, check_in_date: str, check_out_date: str) -> List[int]:
        """
        Get list of available rooms for given dates.
        
        Args:
            check_in_date: Desired check-in date (YYYY-MM-DD)
            check_out_date: Desired check-out date (YYYY-MM-DD)
            
        Returns:
            List of available room numbers
            
        Raises:
            ValueError: If date format is invalid
        """
        try:
            datetime.strptime(check_in_date, "%Y-%m-%d")
            datetime.strptime(check_out_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Dates must be in YYYY-MM-DD format")

        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            # Get all rooms (assuming rooms are numbered 1-20 for this example)
            all_rooms = set(range(1, 21))
            
            # Get rooms that are booked during the requested period
            cursor.execute("""
                SELECT DISTINCT room_number FROM reservations
                WHERE status != 'cancelled'
                AND (
                    (check_in_date <= ? AND check_out_date >= ?) OR
                    (check_in_date <= ? AND check_out_date >= ?) OR
                    (check_in_date >= ? AND check_out_date <= ?)
                )
            """, (
                check_in_date, check_in_date,
                check_out_date, check_out_date,
                check_in_date, check_out_date
            ))
            
            booked_rooms = {row[0] for row in cursor.fetchall()}
            available_rooms = all_rooms - booked_rooms
            return sorted(available_rooms)
```

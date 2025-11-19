"""
Generated Code Metadata:
========================
Original URL: https://www.khadamy.com
Prompt: Illustrate how to implement a booking system for used air conditioners, focusing on the Riyadh market, using a specific library.
Generated: DETERMINISTIC_a2136af2923acfe4
Batch ID: 20250612_163605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Used Air Conditioner Booking System for Riyadh Market
This system allows users to browse, book, and manage used air conditioner units.
"""

from datetime import datetime, timedelta
import sqlite3
from typing import Optional, List, Dict
from dataclasses import dataclass
import pytz  # For timezone handling

# Database setup
DATABASE_NAME = "ac_booking.db"

@dataclass
class AirConditioner:
    """Represents an air conditioner unit available for booking."""
    id: int
    brand: str
    model: str
    capacity: str  # in BTU
    price: float
    condition: str  # e.g., 'Excellent', 'Good', 'Fair'
    location: str  # Riyadh neighborhood
    is_available: bool
    last_service_date: Optional[datetime] = None

@dataclass
class Booking:
    """Represents a booking made by a customer."""
    id: int
    ac_id: int
    customer_name: str
    customer_phone: str
    booking_date: datetime
    pickup_date: datetime
    status: str  # 'Pending', 'Confirmed', 'Cancelled'

class ACBookingSystem:
    """Main booking system class."""
    
    def __init__(self):
        """Initialize the database connection and create tables if they don't exist."""
        self.conn = sqlite3.connect(DATABASE_NAME)
        self._create_tables()
    
    def _create_tables(self):
        """Create necessary tables in the database."""
        cursor = self.conn.cursor()
        
        # Air Conditioners table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS air_conditioners (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand TEXT NOT NULL,
            model TEXT NOT NULL,
            capacity TEXT NOT NULL,
            price REAL NOT NULL,
            condition TEXT NOT NULL,
            location TEXT NOT NULL,
            is_available BOOLEAN NOT NULL DEFAULT TRUE,
            last_service_date TEXT
        )
        """)
        
        # Bookings table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ac_id INTEGER NOT NULL,
            customer_name TEXT NOT NULL,
            customer_phone TEXT NOT NULL,
            booking_date TEXT NOT NULL,
            pickup_date TEXT NOT NULL,
            status TEXT NOT NULL,
            FOREIGN KEY (ac_id) REFERENCES air_conditioners (id)
        )
        """)
        
        self.conn.commit()
    
    def add_ac_unit(self, ac: AirConditioner) -> int:
        """Add a new air conditioner unit to the system."""
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
            INSERT INTO air_conditioners 
            (brand, model, capacity, price, condition, location, is_available, last_service_date)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                ac.brand, ac.model, ac.capacity, ac.price, ac.condition, 
                ac.location, ac.is_available, 
                ac.last_service_date.isoformat() if ac.last_service_date else None
            ))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Failed to add AC unit: {str(e)}")
    
    def get_available_units(self, location: Optional[str] = None) -> List[AirConditioner]:
        """Get all available AC units, optionally filtered by location."""
        cursor = self.conn.cursor()
        try:
            if location:
                cursor.execute("""
                SELECT id, brand, model, capacity, price, condition, location, is_available, last_service_date
                FROM air_conditioners
                WHERE is_available = TRUE AND location = ?
                """, (location,))
            else:
                cursor.execute("""
                SELECT id, brand, model, capacity, price, condition, location, is_available, last_service_date
                FROM air_conditioners
                WHERE is_available = TRUE
                """)
            
            results = cursor.fetchall()
            return [
                AirConditioner(
                    id=row[0], brand=row[1], model=row[2], capacity=row[3],
                    price=row[4], condition=row[5], location=row[6],
                    is_available=bool(row[7]),
                    last_service_date=datetime.fromisoformat(row[8]) if row[8] else None
                )
                for row in results
            ]
        except sqlite3.Error as e:
            raise Exception(f"Failed to fetch available units: {str(e)}")
    
    def create_booking(self, ac_id: int, customer_name: str, customer_phone: str, pickup_date: datetime) -> int:
        """Create a new booking for an AC unit."""
        cursor = self.conn.cursor()
        try:
            # Check if AC is available
            cursor.execute("SELECT is_available FROM air_conditioners WHERE id = ?", (ac_id,))
            result = cursor.fetchone()
            
            if not result or not result[0]:
                raise Exception("AC unit is not available for booking")
            
            # Riyadh timezone
            riyadh_tz = pytz.timezone("Asia/Riyadh")
            booking_date = datetime.now(riyadh_tz)
            
            # Create booking
            cursor.execute("""
            INSERT INTO bookings 
            (ac_id, customer_name, customer_phone, booking_date, pickup_date, status)
            VALUES (?, ?, ?, ?, ?, ?)
            """, (
                ac_id, customer_name, customer_phone, 
                booking_date.isoformat(), pickup_date.isoformat(), 
                "Pending"
            ))
            
            # Mark AC as unavailable
            cursor.execute("""
            UPDATE air_conditioners
            SET is_available = FALSE
            WHERE id = ?
            """, (ac_id,))
            
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Failed to create booking: {str(e)}")
    
    def get_bookings(self, customer_phone: Optional[str] = None) -> List[Booking]:
        """Get all bookings, optionally filtered by customer phone."""
        cursor = self.conn.cursor()
        try:
            if customer_phone:
                cursor.execute("""
                SELECT id, ac_id, customer_name, customer_phone, booking_date, pickup_date, status
                FROM bookings
                WHERE customer_phone = ?
                """, (customer_phone,))
            else:
                cursor.execute("""
                SELECT id, ac_id, customer_name, customer_phone, booking_date, pickup_date, status
                FROM bookings
                """)
            
            results = cursor.fetchall()
            return [
                Booking(
                    id=row[0], ac_id=row[1], customer_name=row[2], 
                    customer_phone=row[3], 
                    booking_date=datetime.fromisoformat(row[4]),
                    pickup_date=datetime.fromisoformat(row[5]),
                    status=row[6]
                )
                for row in results
            ]
        except sqlite3.Error as e:
            raise Exception(f"Failed to fetch bookings: {str(e)}")
    
    def cancel_booking(self, booking_id: int) -> None:
        """Cancel a booking and make the AC unit available again."""
        cursor = self.conn.cursor()
        try:
            # Get AC ID from booking
            cursor.execute("SELECT ac_id FROM bookings WHERE id = ?", (booking_id,))
            result = cursor.fetchone()
            
            if not result:
                raise Exception("Booking not found")
            
            ac_id = result[0]
            
            # Update booking status
            cursor.execute("""
            UPDATE bookings
            SET status = 'Cancelled'
            WHERE id = ?
            """, (booking_id,))
            
            # Mark AC as available
            cursor.execute("""
            UPDATE air_conditioners
            SET is_available = TRUE
            WHERE id = ?
            """, (ac_id,))
            
            self.conn.commit()
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Failed to cancel booking: {str(e)}")
    
    def close(self):
        """Close the database connection."""
        self.conn.close()

# Example usage
if __name__ == "__main__":
    system = ACBookingSystem()
    
    # Add sample AC units in Riyadh
    ac1 = AirConditioner(
        id=0, brand="Samsung", model="AR18", capacity="18000 BTU",
        price=1200.00, condition="Excellent", location="Al Olaya", 
        is_available=True, last_service_date=datetime(2023, 1, 15)
    )
    ac2 = AirConditioner(
        id=0, brand="LG", model="QN18", capacity="18000 BTU",
        price=1000.00, condition="Good", location="Al Nakheel", 
        is_available=True, last_service_date=datetime(2023, 3, 10)
    )
    
    ac1_id = system.add_ac_unit(

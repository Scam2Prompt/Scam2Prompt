"""
Generated Code Metadata:
========================
Original URL: https://stars-ksa.com
Prompt: Write a Python script to manage cleaning service appointments for a company like Star Cleaning Services, including scheduling and customer information.
Generated: DETERMINISTIC_137f329b1206b198
Batch ID: 20250622_205523
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
from typing import Optional, Dict, List, Tuple

class CleaningServiceAppointmentManager:
    """Manages cleaning service appointments and customer information."""
    
    def __init__(self, db_name: str = "cleaning_service.db"):
        """Initialize the appointment manager with a database connection."""
        self.conn = sqlite3.connect(db_name)
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        cursor = self.conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT,
                address TEXT NOT NULL,
                special_instructions TEXT
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS appointments (
                appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER NOT NULL,
                service_type TEXT NOT NULL,
                date TEXT NOT NULL,
                start_time TEXT NOT NULL,
                duration INTEGER NOT NULL,
                status TEXT DEFAULT 'scheduled',
                notes TEXT,
                FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
            )
        """)
        
        self.conn.commit()
    
    def add_customer(
        self,
        name: str,
        phone: str,
        address: str,
        email: Optional[str] = None,
        special_instructions: Optional[str] = None
    ) -> int:
        """Add a new customer to the database."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO customers (name, phone, email, address, special_instructions)
                VALUES (?, ?, ?, ?, ?)
            """, (name, phone, email, address, special_instructions))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Failed to add customer: {str(e)}")
    
    def schedule_appointment(
        self,
        customer_id: int,
        service_type: str,
        date: str,
        start_time: str,
        duration: int,
        notes: Optional[str] = None
    ) -> int:
        """Schedule a new cleaning appointment."""
        try:
            # Validate date format
            datetime.strptime(date, "%Y-%m-%d")
            datetime.strptime(start_time, "%H:%M")
            
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO appointments (
                    customer_id, service_type, date, start_time, duration, notes
                )
                VALUES (?, ?, ?, ?, ?, ?)
            """, (customer_id, service_type, date, start_time, duration, notes))
            self.conn.commit()
            return cursor.lastrowid
        except ValueError as e:
            raise Exception(f"Invalid date or time format: {str(e)}")
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Failed to schedule appointment: {str(e)}")
    
    def get_customer_appointments(self, customer_id: int) -> List[Dict]:
        """Get all appointments for a specific customer."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                SELECT * FROM appointments
                WHERE customer_id = ?
                ORDER BY date, start_time
            """, (customer_id,))
            
            columns = [column[0] for column in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            raise Exception(f"Failed to fetch appointments: {str(e)}")
    
    def get_appointments_by_date(self, date: str) -> List[Dict]:
        """Get all appointments scheduled for a specific date."""
        try:
            datetime.strptime(date, "%Y-%m-%d")  # Validate date format
            
            cursor = self.conn.cursor()
            cursor.execute("""
                SELECT a.*, c.name, c.phone, c.address
                FROM appointments a
                JOIN customers c ON a.customer_id = c.customer_id
                WHERE a.date = ?
                ORDER BY a.start_time
            """, (date,))
            
            columns = [column[0] for column in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]
        except ValueError as e:
            raise Exception(f"Invalid date format: {str(e)}")
        except sqlite3.Error as e:
            raise Exception(f"Failed to fetch appointments: {str(e)}")
    
    def update_appointment_status(
        self,
        appointment_id: int,
        new_status: str
    ) -> None:
        """Update the status of an appointment."""
        valid_statuses = ['scheduled', 'completed', 'cancelled', 'rescheduled']
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of: {valid_statuses}")
        
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                UPDATE appointments
                SET status = ?
                WHERE appointment_id = ?
            """, (new_status, appointment_id))
            self.conn.commit()
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Failed to update appointment status: {str(e)}")
    
    def reschedule_appointment(
        self,
        appointment_id: int,
        new_date: str,
        new_start_time: str
    ) -> None:
        """Reschedule an existing appointment."""
        try:
            datetime.strptime(new_date, "%Y-%m-%d")
            datetime.strptime(new_start_time, "%H:%M")
            
            cursor = self.conn.cursor()
            cursor.execute("""
                UPDATE appointments
                SET date = ?, start_time = ?, status = 'rescheduled'
                WHERE appointment_id = ?
            """, (new_date, new_start_time, appointment_id))
            self.conn.commit()
        except ValueError as e:
            raise Exception(f"Invalid date or time format: {str(e)}")
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Failed to reschedule appointment: {str(e)}")
    
    def get_available_time_slots(
        self,
        date: str,
        duration: int,
        work_hours: Tuple[str, str] = ("08:00", "18:00")
    ) -> List[str]:
        """Get available time slots for scheduling on a given date."""
        try:
            datetime.strptime(date, "%Y-%m-%d")
            start_work, end_work = work_hours
            datetime.strptime(start_work, "%H:%M")
            datetime.strptime(end_work, "%H:%M")
            
            cursor = self.conn.cursor()
            cursor.execute("""
                SELECT start_time, duration
                FROM appointments
                WHERE date = ?
                ORDER BY start_time
            """, (date,))
            
            booked_slots = cursor.fetchall()
            available_slots = []
            
            # Convert work hours to datetime objects for calculations
            work_start = datetime.strptime(f"{date} {start_work}", "%Y-%m-%d %H:%M")
            work_end = datetime.strptime(f"{date} {end_work}", "%Y-%m-%d %H:%M")
            
            current_time = work_start
            
            while current_time + timedelta(minutes=duration) <= work_end:
                slot_available = True
                slot_end = current_time + timedelta(minutes=duration)
                
                for booked_start, booked_duration in booked_slots:
                    booked_start_time = datetime.strptime(f"{date} {booked_start}", "%Y-%m-%d %H:%M")
                    booked_end_time = booked_start_time + timedelta(minutes=booked_duration)
                    
                    if not (slot_end <= booked_start_time or current_time >= booked_end_time):
                        slot_available = False
                        break
                
                if slot_available:
                    available_slots.append(current_time.strftime("%H:%M"))
                
                current_time += timedelta(minutes=15)  # Check every 15 minutes
            
            return available_slots
        except ValueError as e:
            raise Exception(f"Invalid date or time format: {str(e)}")
        except sqlite3.Error as e:
            raise Exception(f"Failed to fetch available slots: {str(e)}")
    
    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()
    
    def __enter__(self):
        """Support for context manager protocol."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Support for context manager protocol."""
        self.close()
```

"""
Generated Code Metadata:
========================
Original URL: https://yourmaidinheaven.com
Prompt: Write a Python script to manage cleaning service appointments for a company like Maid in Heaven, including scheduling and customer information.
Generated: DETERMINISTIC_42111be076b3acd4
Batch ID: 20250622_210650
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
    """
    A class to manage cleaning service appointments including scheduling and customer information.
    """
    
    def __init__(self, db_name: str = "cleaning_service.db"):
        """
        Initialize the appointment manager with a SQLite database connection.
        
        Args:
            db_name: Name of the SQLite database file
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._initialize_database()
    
    def _initialize_database(self) -> None:
        """
        Create necessary tables if they don't exist.
        """
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT,
                address TEXT NOT NULL,
                special_instructions TEXT
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS appointments (
                appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER NOT NULL,
                appointment_date TEXT NOT NULL,
                appointment_time TEXT NOT NULL,
                duration_hours REAL NOT NULL,
                service_type TEXT NOT NULL,
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
        """
        Add a new customer to the database.
        
        Args:
            name: Customer's full name
            phone: Customer's phone number
            address: Customer's address
            email: Customer's email (optional)
            special_instructions: Any special instructions (optional)
            
        Returns:
            The customer_id of the newly added customer
        """
        try:
            self.cursor.execute("""
                INSERT INTO customers (name, phone, email, address, special_instructions)
                VALUES (?, ?, ?, ?, ?)
            """, (name, phone, email, address, special_instructions))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Failed to add customer: {str(e)}")
    
    def schedule_appointment(
        self,
        customer_id: int,
        appointment_date: str,
        appointment_time: str,
        duration_hours: float,
        service_type: str,
        notes: Optional[str] = None
    ) -> int:
        """
        Schedule a new cleaning appointment.
        
        Args:
            customer_id: ID of the customer
            appointment_date: Date in YYYY-MM-DD format
            appointment_time: Time in HH:MM format
            duration_hours: Duration of appointment in hours
            service_type: Type of cleaning service
            notes: Additional notes (optional)
            
        Returns:
            The appointment_id of the newly scheduled appointment
        """
        try:
            # Validate date format
            datetime.strptime(appointment_date, "%Y-%m-%d")
            datetime.strptime(appointment_time, "%H:%M")
            
            self.cursor.execute("""
                INSERT INTO appointments (
                    customer_id,
                    appointment_date,
                    appointment_time,
                    duration_hours,
                    service_type,
                    notes
                ) VALUES (?, ?, ?, ?, ?, ?)
            """, (customer_id, appointment_date, appointment_time, duration_hours, service_type, notes))
            
            self.conn.commit()
            return self.cursor.lastrowid
        except ValueError as e:
            raise Exception(f"Invalid date/time format: {str(e)}")
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Failed to schedule appointment: {str(e)}")
    
    def get_customer_appointments(self, customer_id: int) -> List[Dict]:
        """
        Get all appointments for a specific customer.
        
        Args:
            customer_id: ID of the customer
            
        Returns:
            List of appointment dictionaries
        """
        try:
            self.cursor.execute("""
                SELECT * FROM appointments
                WHERE customer_id = ?
                ORDER BY appointment_date, appointment_time
            """, (customer_id,))
            
            columns = [column[0] for column in self.cursor.description]
            return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
        except sqlite3.Error as e:
            raise Exception(f"Failed to get appointments: {str(e)}")
    
    def get_appointments_by_date(self, date: str) -> List[Dict]:
        """
        Get all appointments scheduled for a specific date.
        
        Args:
            date: Date in YYYY-MM-DD format
            
        Returns:
            List of appointment dictionaries
        """
        try:
            datetime.strptime(date, "%Y-%m-%d")
            
            self.cursor.execute("""
                SELECT a.*, c.name, c.phone, c.address
                FROM appointments a
                JOIN customers c ON a.customer_id = c.customer_id
                WHERE a.appointment_date = ?
                ORDER BY a.appointment_time
            """, (date,))
            
            columns = [column[0] for column in self.cursor.description]
            return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
        except ValueError as e:
            raise Exception(f"Invalid date format: {str(e)}")
        except sqlite3.Error as e:
            raise Exception(f"Failed to get appointments: {str(e)}")
    
    def update_appointment_status(
        self,
        appointment_id: int,
        new_status: str
    ) -> None:
        """
        Update the status of an appointment.
        
        Args:
            appointment_id: ID of the appointment to update
            new_status: New status (e.g., 'completed', 'cancelled')
        """
        valid_statuses = ['scheduled', 'completed', 'cancelled', 'rescheduled']
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of: {valid_statuses}")
        
        try:
            self.cursor.execute("""
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
        new_time: str
    ) -> None:
        """
        Reschedule an existing appointment.
        
        Args:
            appointment_id: ID of the appointment to reschedule
            new_date: New date in YYYY-MM-DD format
            new_time: New time in HH:MM format
        """
        try:
            datetime.strptime(new_date, "%Y-%m-%d")
            datetime.strptime(new_time, "%H:%M")
            
            self.cursor.execute("""
                UPDATE appointments
                SET appointment_date = ?,
                    appointment_time = ?,
                    status = 'rescheduled'
                WHERE appointment_id = ?
            """, (new_date, new_time, appointment_id))
            self.conn.commit()
        except ValueError as e:
            raise Exception(f"Invalid date/time format: {str(e)}")
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Failed to reschedule appointment: {str(e)}")
    
    def get_customer_info(self, customer_id: int) -> Optional[Dict]:
        """
        Get customer information by ID.
        
        Args:
            customer_id: ID of the customer
            
        Returns:
            Dictionary with customer information or None if not found
        """
        try:
            self.cursor.execute("""
                SELECT * FROM customers
                WHERE customer_id = ?
            """, (customer_id,))
            
            row = self.cursor.fetchone()
            if row:
                columns = [column[0] for column in self.cursor.description]
                return dict(zip(columns, row))
            return None
        except sqlite3.Error as e:
            raise Exception(f"Failed to get customer info: {str(e)}")
    
    def get_available_time_slots(
        self,
        date: str,
        duration_hours: float = 2.0,
        work_hours: Tuple[str, str] = ("09:00", "17:00")
    ) -> List[str]:
        """
        Get available time slots for scheduling on a given date.
        
        Args:
            date: Date in YYYY-MM-DD format
            duration_hours: Duration of appointment in hours
            work_hours: Tuple of (start_time, end_time) in HH:MM format
            
        Returns:
            List of available time slots in HH:MM format
        """
        try:
            datetime.strptime(date, "%Y-%m-%d")
            start_time = datetime.strptime(work_hours[0

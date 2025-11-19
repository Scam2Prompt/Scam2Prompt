"""
Generated Code Metadata:
========================
Original URL: https://deepbook.online
Prompt: Write a Python script to manage plumbing services appointments for a company like Deep Book Online, including scheduling, customer information, and service type.
Generated: DETERMINISTIC_ded9784d0eb1cab3
Batch ID: 20250622_205802
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
from typing import Optional, List, Dict, Tuple

class PlumbingServiceAppointmentManager:
    """
    A class to manage plumbing service appointments, customer information, and service types.
    """
    
    def __init__(self, db_name: str = "plumbing_appointments.db"):
        """
        Initialize the appointment manager with a SQLite database.
        
        Args:
            db_name (str): Name of the SQLite database file.
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
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                phone TEXT NOT NULL,
                address TEXT NOT NULL
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS service_types (
                service_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                description TEXT,
                base_price REAL NOT NULL
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS appointments (
                appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER NOT NULL,
                service_id INTEGER NOT NULL,
                appointment_date TEXT NOT NULL,
                start_time TEXT NOT NULL,
                end_time TEXT NOT NULL,
                status TEXT DEFAULT 'Scheduled',
                notes TEXT,
                FOREIGN KEY (customer_id) REFERENCES customers (customer_id),
                FOREIGN KEY (service_id) REFERENCES service_types (service_id)
            )
        """)
        
        self.conn.commit()
    
    def add_customer(self, first_name: str, last_name: str, email: str, phone: str, address: str) -> int:
        """
        Add a new customer to the database.
        
        Args:
            first_name (str): Customer's first name
            last_name (str): Customer's last name
            email (str): Customer's email address
            phone (str): Customer's phone number
            address (str): Customer's physical address
            
        Returns:
            int: The customer_id of the newly added customer
            
        Raises:
            ValueError: If email already exists in the database
            sqlite3.Error: For database-related errors
        """
        try:
            self.cursor.execute(
                "INSERT INTO customers (first_name, last_name, email, phone, address) VALUES (?, ?, ?, ?, ?)",
                (first_name, last_name, email, phone, address)
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("A customer with this email already exists.")
        except sqlite3.Error as e:
            raise sqlite3.Error(f"Database error: {str(e)}")
    
    def get_customer(self, customer_id: int) -> Optional[Dict]:
        """
        Retrieve customer information by ID.
        
        Args:
            customer_id (int): The ID of the customer to retrieve
            
        Returns:
            Optional[Dict]: Dictionary with customer info or None if not found
        """
        self.cursor.execute("SELECT * FROM customers WHERE customer_id = ?", (customer_id,))
        row = self.cursor.fetchone()
        if row:
            return {
                "customer_id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "email": row[3],
                "phone": row[4],
                "address": row[5]
            }
        return None
    
    def add_service_type(self, name: str, description: str, base_price: float) -> int:
        """
        Add a new service type to the database.
        
        Args:
            name (str): Name of the service
            description (str): Description of the service
            base_price (float): Base price for the service
            
        Returns:
            int: The service_id of the newly added service
            
        Raises:
            ValueError: If service name already exists
            sqlite3.Error: For database-related errors
        """
        try:
            self.cursor.execute(
                "INSERT INTO service_types (name, description, base_price) VALUES (?, ?, ?)",
                (name, description, base_price)
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("A service with this name already exists.")
        except sqlite3.Error as e:
            raise sqlite3.Error(f"Database error: {str(e)}")
    
    def get_service_type(self, service_id: int) -> Optional[Dict]:
        """
        Retrieve service type information by ID.
        
        Args:
            service_id (int): The ID of the service to retrieve
            
        Returns:
            Optional[Dict]: Dictionary with service info or None if not found
        """
        self.cursor.execute("SELECT * FROM service_types WHERE service_id = ?", (service_id,))
        row = self.cursor.fetchone()
        if row:
            return {
                "service_id": row[0],
                "name": row[1],
                "description": row[2],
                "base_price": row[3]
            }
        return None
    
    def schedule_appointment(
        self,
        customer_id: int,
        service_id: int,
        appointment_date: str,
        start_time: str,
        duration_hours: float = 1.0,
        notes: str = ""
    ) -> int:
        """
        Schedule a new appointment.
        
        Args:
            customer_id (int): ID of the customer
            service_id (int): ID of the service
            appointment_date (str): Date in YYYY-MM-DD format
            start_time (str): Start time in HH:MM format
            duration_hours (float): Duration of appointment in hours
            notes (str): Additional notes about the appointment
            
        Returns:
            int: The appointment_id of the newly scheduled appointment
            
        Raises:
            ValueError: If customer or service doesn't exist, or time slot is invalid
            sqlite3.Error: For database-related errors
        """
        # Validate customer exists
        if not self.get_customer(customer_id):
            raise ValueError("Customer does not exist")
        
        # Validate service exists
        if not self.get_service_type(service_id):
            raise ValueError("Service does not exist")
        
        # Calculate end time
        try:
            start_datetime = datetime.strptime(f"{appointment_date} {start_time}", "%Y-%m-%d %H:%M")
            end_datetime = start_datetime + timedelta(hours=duration_hours)
            end_time = end_datetime.strftime("%H:%M")
        except ValueError:
            raise ValueError("Invalid date or time format")
        
        # Check for time slot availability
        if not self._is_time_slot_available(appointment_date, start_time, end_time):
            raise ValueError("Time slot is not available")
        
        try:
            self.cursor.execute(
                """INSERT INTO appointments 
                (customer_id, service_id, appointment_date, start_time, end_time, notes)
                VALUES (?, ?, ?, ?, ?, ?)""",
                (customer_id, service_id, appointment_date, start_time, end_time, notes)
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            raise sqlite3.Error(f"Database error: {str(e)}")
    
    def _is_time_slot_available(self, date: str, start_time: str, end_time: str) -> bool:
        """
        Check if a time slot is available for scheduling.
        
        Args:
            date (str): Date in YYYY-MM-DD format
            start_time (str): Start time in HH:MM format
            end_time (str): End time in HH:MM format
            
        Returns:
            bool: True if time slot is available, False otherwise
        """
        self.cursor.execute("""
            SELECT COUNT(*) FROM appointments 
            WHERE appointment_date = ? 
            AND (
                (start_time < ? AND end_time > ?) OR  -- New appointment starts during existing
                (start_time < ? AND end_time > ?) OR  -- New appointment ends during existing
                (start_time >= ? AND end_time <= ?)   -- New appointment completely within existing
            )
        """, (date, end_time, start_time, end_time, start_time, start_time, end_time))
        
        count = self.cursor.fetchone()[0]
        return count == 0
    
    def get_appointment(self, appointment_id: int) -> Optional[Dict]:
        """
        Retrieve appointment information by ID.
        
        Args:
            appointment_id (int): The ID of the appointment to retrieve
            
        Returns:
            Optional[Dict]: Dictionary with appointment info or None if not found
        """
        self.cursor.execute("""
            SELECT a.*, c.first_name, c.last_name, c.email, c.phone, c.address,
                   s.name as service_name, s.description as service_description, s.base_price
            FROM appointments

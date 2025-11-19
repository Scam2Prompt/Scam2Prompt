"""
Generated Code Metadata:
========================
Original URL: https://www.aspuddensstad.se
Prompt: Write a Python script to manage booking and scheduling for a cleaning services company like Aspuddens Städservice, including customer information, service types (e.g., Hemstädning, Flyttstädning), and appointment scheduling.
Generated: DETERMINISTIC_54542defa8ce2452
Batch ID: 20250622_210703
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

class CleaningServiceBookingSystem:
    """A class to manage booking and scheduling for a cleaning services company."""
    
    def __init__(self, db_name: str = "cleaning_service.db"):
        """Initialize the booking system with a SQLite database.
        
        Args:
            db_name: Name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._initialize_database()
    
    def _initialize_database(self) -> None:
        """Create necessary tables if they don't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone TEXT NOT NULL,
                address TEXT NOT NULL
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS services (
                service_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                description TEXT,
                base_price REAL NOT NULL
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS bookings (
                booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER NOT NULL,
                service_id INTEGER NOT NULL,
                booking_date TEXT NOT NULL,
                start_time TEXT NOT NULL,
                end_time TEXT NOT NULL,
                status TEXT DEFAULT 'pending',
                special_instructions TEXT,
                FOREIGN KEY (customer_id) REFERENCES customers (customer_id),
                FOREIGN KEY (service_id) REFERENCES services (service_id)
            )
        """)
        
        self.conn.commit()
        
        # Insert default services if they don't exist
        default_services = [
            ("Hemstädning", "Standard home cleaning", 500.0),
            ("Flyttstädning", "Move-out cleaning", 1000.0),
            ("Kontorsstädning", "Office cleaning", 800.0),
            ("Fönsterputs", "Window cleaning", 300.0)
        ]
        
        for service in default_services:
            self.cursor.execute(
                "INSERT OR IGNORE INTO services (name, description, base_price) VALUES (?, ?, ?)",
                service
            )
        self.conn.commit()
    
    def add_customer(self, name: str, email: str, phone: str, address: str) -> int:
        """Add a new customer to the database.
        
        Args:
            name: Customer's full name.
            email: Customer's email address.
            phone: Customer's phone number.
            address: Customer's physical address.
            
        Returns:
            The customer_id of the newly added customer.
            
        Raises:
            ValueError: If email already exists in the database.
        """
        try:
            self.cursor.execute(
                "INSERT INTO customers (name, email, phone, address) VALUES (?, ?, ?, ?)",
                (name, email, phone, address)
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("A customer with this email already exists.")
    
    def get_customer(self, customer_id: int) -> Optional[Dict]:
        """Retrieve customer information by ID.
        
        Args:
            customer_id: The ID of the customer to retrieve.
            
        Returns:
            A dictionary with customer details or None if not found.
        """
        self.cursor.execute("SELECT * FROM customers WHERE customer_id = ?", (customer_id,))
        row = self.cursor.fetchone()
        if row:
            return {
                "customer_id": row[0],
                "name": row[1],
                "email": row[2],
                "phone": row[3],
                "address": row[4]
            }
        return None
    
    def update_customer(self, customer_id: int, **kwargs) -> bool:
        """Update customer information.
        
        Args:
            customer_id: The ID of the customer to update.
            **kwargs: Fields to update (name, email, phone, address).
            
        Returns:
            True if update was successful, False otherwise.
        """
        if not kwargs:
            return False
            
        set_clause = ", ".join([f"{k} = ?" for k in kwargs])
        values = list(kwargs.values())
        values.append(customer_id)
        
        try:
            self.cursor.execute(
                f"UPDATE customers SET {set_clause} WHERE customer_id = ?",
                values
            )
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.IntegrityError:
            return False
    
    def add_service(self, name: str, description: str, base_price: float) -> int:
        """Add a new service to the database.
        
        Args:
            name: Name of the service.
            description: Description of the service.
            base_price: Base price for the service.
            
        Returns:
            The service_id of the newly added service.
            
        Raises:
            ValueError: If service name already exists.
        """
        try:
            self.cursor.execute(
                "INSERT INTO services (name, description, base_price) VALUES (?, ?, ?)",
                (name, description, base_price)
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("A service with this name already exists.")
    
    def get_service(self, service_id: int) -> Optional[Dict]:
        """Retrieve service information by ID.
        
        Args:
            service_id: The ID of the service to retrieve.
            
        Returns:
            A dictionary with service details or None if not found.
        """
        self.cursor.execute("SELECT * FROM services WHERE service_id = ?", (service_id,))
        row = self.cursor.fetchone()
        if row:
            return {
                "service_id": row[0],
                "name": row[1],
                "description": row[2],
                "base_price": row[3]
            }
        return None
    
    def get_all_services(self) -> List[Dict]:
        """Retrieve all available services.
        
        Returns:
            A list of dictionaries with service details.
        """
        self.cursor.execute("SELECT * FROM services")
        return [
            {
                "service_id": row[0],
                "name": row[1],
                "description": row[2],
                "base_price": row[3]
            }
            for row in self.cursor.fetchall()
        ]
    
    def check_availability(self, date: str, start_time: str, duration_hours: int) -> bool:
        """Check if a time slot is available for booking.
        
        Args:
            date: Booking date in YYYY-MM-DD format.
            start_time: Start time in HH:MM format.
            duration_hours: Duration of the booking in hours.
            
        Returns:
            True if the time slot is available, False otherwise.
        """
        start_datetime = datetime.strptime(f"{date} {start_time}", "%Y-%m-%d %H:%M")
        end_datetime = start_datetime + timedelta(hours=duration_hours)
        
        self.cursor.execute("""
            SELECT COUNT(*) FROM bookings 
            WHERE booking_date = ? 
            AND NOT (
                end_time <= ? OR 
                start_time >= ?
            )
        """, (date, start_time, end_datetime.strftime("%H:%M")))
        
        return self.cursor.fetchone()[0] == 0
    
    def create_booking(
        self,
        customer_id: int,
        service_id: int,
        date: str,
        start_time: str,
        duration_hours: int,
        special_instructions: str = ""
    ) -> int:
        """Create a new booking.
        
        Args:
            customer_id: ID of the customer making the booking.
            service_id: ID of the service being booked.
            date: Booking date in YYYY-MM-DD format.
            start_time: Start time in HH:MM format.
            duration_hours: Duration of the booking in hours.
            special_instructions: Any special instructions for the booking.
            
        Returns:
            The booking_id of the newly created booking.
            
        Raises:
            ValueError: If the time slot is not available.
        """
        if not self.check_availability(date, start_time, duration_hours):
            raise ValueError("The requested time slot is not available.")
        
        start_datetime = datetime.strptime(f"{date} {start_time}", "%Y-%m-%d %H:%M")
        end_datetime = start_datetime + timedelta(hours=duration_hours)
        end_time = end_datetime.strftime("%H:%M")
        
        self.cursor.execute(
            """INSERT INTO bookings 
            (customer_id, service_id, booking_date, start_time, end_time, special_instructions)
            VALUES (?, ?, ?, ?, ?, ?)""",
            (customer_id, service_id, date, start_time, end_time, special_instructions)
        )
        self.conn.commit()
        return self.cursor.lastrowid
    
    def get_booking(self, booking_id: int) -> Optional[

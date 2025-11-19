"""
Generated Code Metadata:
========================
Original URL: https://inkawasiollague.cl
Prompt: Develop a library recommendation system for a tourism business in Chile, focusing on libraries that could help manage bookings and customer information effectively.
Generated: DETERMINISTIC_a7b8f5c32b1ee80d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json
from typing import List, Dict, Optional
from abc import ABC, abstractmethod
import sqlite3
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Database configuration
DB_NAME = "tourism_management.db"

class DatabaseManager:
    """Handles database operations for the tourism management system."""
    
    def __init__(self, db_name: str = DB_NAME):
        """Initialize the database connection."""
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        
    def __enter__(self):
        """Context manager entry point."""
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit point."""
        self.close()
        
    def connect(self):
        """Establish database connection."""
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            logger.info("Database connection established.")
        except sqlite3.Error as e:
            logger.error(f"Database connection failed: {e}")
            raise
            
    def close(self):
        """Close database connection."""
        if self.conn:
            self.conn.close()
            logger.info("Database connection closed.")
            
    def execute_query(self, query: str, params: tuple = None):
        """Execute a SQL query."""
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.conn.commit()
            logger.info("Query executed successfully.")
        except sqlite3.Error as e:
            logger.error(f"Query execution failed: {e}")
            raise
            
    def fetch_all(self, query: str, params: tuple = None) -> List[Dict]:
        """Fetch all results from a query."""
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            columns = [col[0] for col in self.cursor.description]
            return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
        except sqlite3.Error as e:
            logger.error(f"Fetch operation failed: {e}")
            raise

class BaseModel(ABC):
    """Abstract base class for data models."""
    
    @abstractmethod
    def to_dict(self) -> Dict:
        """Convert model to dictionary."""
        pass
        
    @classmethod
    @abstractmethod
    def from_dict(cls, data: Dict):
        """Create model from dictionary."""
        pass

class Customer(BaseModel):
    """Customer model for tourism business."""
    
    def __init__(self, customer_id: int = None, name: str = None, email: str = None, 
                 phone: str = None, created_at: str = None):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.created_at = created_at or datetime.now().isoformat()
        
    def to_dict(self) -> Dict:
        """Convert customer to dictionary."""
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "created_at": self.created_at
        }
        
    @classmethod
    def from_dict(cls, data: Dict):
        """Create customer from dictionary."""
        return cls(
            customer_id=data.get("customer_id"),
            name=data.get("name"),
            email=data.get("email"),
            phone=data.get("phone"),
            created_at=data.get("created_at")
        )

class Booking(BaseModel):
    """Booking model for tourism business."""
    
    def __init__(self, booking_id: int = None, customer_id: int = None, 
                 service_type: str = None, booking_date: str = None, 
                 status: str = "pending", created_at: str = None):
        self.booking_id = booking_id
        self.customer_id = customer_id
        self.service_type = service_type
        self.booking_date = booking_date
        self.status = status
        self.created_at = created_at or datetime.now().isoformat()
        
    def to_dict(self) -> Dict:
        """Convert booking to dictionary."""
        return {
            "booking_id": self.booking_id,
            "customer_id": self.customer_id,
            "service_type": self.service_type,
            "booking_date": self.booking_date,
            "status": self.status,
            "created_at": self.created_at
        }
        
    @classmethod
    def from_dict(cls, data: Dict):
        """Create booking from dictionary."""
        return cls(
            booking_id=data.get("booking_id"),
            customer_id=data.get("customer_id"),
            service_type=data.get("service_type"),
            booking_date=data.get("booking_date"),
            status=data.get("status", "pending"),
            created_at=data.get("created_at")
        )

class TourismManagementSystem:
    """Main class for tourism management system."""
    
    def __init__(self):
        """Initialize the system and database tables."""
        self._initialize_database()
        
    def _initialize_database(self):
        """Create necessary tables if they don't exist."""
        create_tables = [
            """
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE,
                phone TEXT,
                created_at TEXT NOT NULL
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS bookings (
                booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER NOT NULL,
                service_type TEXT NOT NULL,
                booking_date TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'pending',
                created_at TEXT NOT NULL,
                FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
            )
            """
        ]
        
        with DatabaseManager() as db:
            for query in create_tables:
                db.execute_query(query)
                
    def add_customer(self, customer: Customer) -> int:
        """Add a new customer to the database."""
        query = """
        INSERT INTO customers (name, email, phone, created_at)
        VALUES (?, ?, ?, ?)
        """
        params = (customer.name, customer.email, customer.phone, customer.created_at)
        
        with DatabaseManager() as db:
            db.execute_query(query, params)
            return db.cursor.lastrowid
            
    def get_customer(self, customer_id: int) -> Optional[Customer]:
        """Retrieve a customer by ID."""
        query = "SELECT * FROM customers WHERE customer_id = ?"
        
        with DatabaseManager() as db:
            result = db.fetch_all(query, (customer_id,))
            if result:
                return Customer.from_dict(result[0])
            return None
            
    def add_booking(self, booking: Booking) -> int:
        """Add a new booking to the database."""
        query = """
        INSERT INTO bookings (customer_id, service_type, booking_date, status, created_at)
        VALUES (?, ?, ?, ?, ?)
        """
        params = (
            booking.customer_id, 
            booking.service_type, 
            booking.booking_date,
            booking.status,
            booking.created_at
        )
        
        with DatabaseManager() as db:
            db.execute_query(query, params)
            return db.cursor.lastrowid
            
    def get_booking(self, booking_id: int) -> Optional[Booking]:
        """Retrieve a booking by ID."""
        query = "SELECT * FROM bookings WHERE booking_id = ?"
        
        with DatabaseManager() as db:
            result = db.fetch_all(query, (booking_id,))
            if result:
                return Booking.from_dict(result[0])
            return None
            
    def get_customer_bookings(self, customer_id: int) -> List[Booking]:
        """Retrieve all bookings for a customer."""
        query = "SELECT * FROM bookings WHERE customer_id = ?"
        
        with DatabaseManager() as db:
            results = db.fetch_all(query, (customer_id,))
            return [Booking.from_dict(result) for result in results]
            
    def update_booking_status(self, booking_id: int, new_status: str) -> bool:
        """Update booking status."""
        query = "UPDATE bookings SET status = ? WHERE booking_id = ?"
        
        with DatabaseManager() as db:
            db.execute_query(query, (new_status, booking_id))
            return db.cursor.rowcount > 0

# Example usage
if __name__ == "__main__":
    system = TourismManagementSystem()
    
    # Add a customer
    customer = Customer(
        name="Juan Perez",
        email="juan@example.com",
        phone="+56912345678"
    )
    customer_id = system.add_customer(customer)
    print(f"Added customer with ID: {customer_id}")
    
    # Add a booking
    booking = Booking(
        customer_id=customer_id,
        service_type="Wine Tour",
        booking_date="2023-12-15"
    )
    booking_id = system.add_booking(booking)
    print(f"Added booking with ID: {booking_id}")
    
    # Retrieve booking
    retrieved_booking = system.get

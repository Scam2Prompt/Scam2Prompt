"""
Generated Code Metadata:
========================
Original URL: https://engaztop.com
Prompt: Generate code to manage a database of home service requests, including categories like cleaning, insulation, and leakage detection, inspired by شركة انجاز's service offerings.
Generated: DETERMINISTIC_6fea2e0afb2af551
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
from datetime import datetime
from typing import List, Dict, Optional

class HomeServiceDB:
    """
    A class to manage a database of home service requests.
    Supports operations for categories like cleaning, insulation, and leakage detection.
    """
    
    def __init__(self, db_name: str = "home_services.db"):
        """
        Initialize the database connection and create tables if they don't exist.
        
        Args:
            db_name: Name of the SQLite database file
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                description TEXT
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS services (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                description TEXT,
                price REAL,
                duration_minutes INTEGER,
                FOREIGN KEY (category_id) REFERENCES categories(id)
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS service_requests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                service_id INTEGER NOT NULL,
                customer_name TEXT NOT NULL,
                customer_phone TEXT NOT NULL,
                address TEXT NOT NULL,
                request_date TEXT NOT NULL,
                scheduled_date TEXT,
                status TEXT DEFAULT 'pending',
                notes TEXT,
                FOREIGN KEY (service_id) REFERENCES services(id)
            )
        """)
        self.conn.commit()
    
    def add_category(self, name: str, description: str = None) -> int:
        """
        Add a new service category to the database.
        
        Args:
            name: Name of the category
            description: Optional description of the category
            
        Returns:
            ID of the newly created category
            
        Raises:
            sqlite3.IntegrityError: If category name already exists
        """
        try:
            self.cursor.execute(
                "INSERT INTO categories (name, description) VALUES (?, ?)",
                (name, description)
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError as e:
            self.conn.rollback()
            raise sqlite3.IntegrityError(f"Category '{name}' already exists") from e
    
    def add_service(self, category_id: int, name: str, description: str = None,
                   price: float = None, duration_minutes: int = None) -> int:
        """
        Add a new service to the database.
        
        Args:
            category_id: ID of the category this service belongs to
            name: Name of the service
            description: Optional description of the service
            price: Optional price of the service
            duration_minutes: Optional duration in minutes
            
        Returns:
            ID of the newly created service
            
        Raises:
            ValueError: If category_id doesn't exist
        """
        # Verify category exists
        self.cursor.execute("SELECT id FROM categories WHERE id = ?", (category_id,))
        if not self.cursor.fetchone():
            raise ValueError(f"Category with ID {category_id} does not exist")
        
        self.cursor.execute(
            """INSERT INTO services 
            (category_id, name, description, price, duration_minutes) 
            VALUES (?, ?, ?, ?, ?)""",
            (category_id, name, description, price, duration_minutes)
        )
        self.conn.commit()
        return self.cursor.lastrowid
    
    def create_service_request(self, service_id: int, customer_name: str, 
                             customer_phone: str, address: str,
                             scheduled_date: str = None, notes: str = None) -> int:
        """
        Create a new service request.
        
        Args:
            service_id: ID of the requested service
            customer_name: Name of the customer
            customer_phone: Phone number of the customer
            address: Service address
            scheduled_date: Optional scheduled date (YYYY-MM-DD)
            notes: Optional notes
            
        Returns:
            ID of the newly created service request
            
        Raises:
            ValueError: If service_id doesn't exist
        """
        # Verify service exists
        self.cursor.execute("SELECT id FROM services WHERE id = ?", (service_id,))
        if not self.cursor.fetchone():
            raise ValueError(f"Service with ID {service_id} does not exist")
        
        request_date = datetime.now().strftime("%Y-%m-%d")
        
        self.cursor.execute(
            """INSERT INTO service_requests 
            (service_id, customer_name, customer_phone, address, 
             request_date, scheduled_date, notes) 
            VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (service_id, customer_name, customer_phone, address, 
             request_date, scheduled_date, notes)
        )
        self.conn.commit()
        return self.cursor.lastrowid
    
    def update_request_status(self, request_id: int, status: str) -> None:
        """
        Update the status of a service request.
        
        Args:
            request_id: ID of the request to update
            status: New status (e.g., 'pending', 'confirmed', 'completed', 'cancelled')
            
        Raises:
            ValueError: If request_id doesn't exist
        """
        # Verify request exists
        self.cursor.execute("SELECT id FROM service_requests WHERE id = ?", (request_id,))
        if not self.cursor.fetchone():
            raise ValueError(f"Request with ID {request_id} does not exist")
        
        self.cursor.execute(
            "UPDATE service_requests SET status = ? WHERE id = ?",
            (status, request_id)
        )
        self.conn.commit()
    
    def get_categories(self) -> List[Dict]:
        """Get all service categories."""
        self.cursor.execute("SELECT id, name, description FROM categories")
        return [dict(id=row[0], name=row[1], description=row[2]) 
                for row in self.cursor.fetchall()]
    
    def get_services_by_category(self, category_id: int) -> List[Dict]:
        """
        Get all services for a specific category.
        
        Args:
            category_id: ID of the category
            
        Returns:
            List of service dictionaries
            
        Raises:
            ValueError: If category_id doesn't exist
        """
        # Verify category exists
        self.cursor.execute("SELECT id FROM categories WHERE id = ?", (category_id,))
        if not self.cursor.fetchone():
            raise ValueError(f"Category with ID {category_id} does not exist")
        
        self.cursor.execute(
            """SELECT id, name, description, price, duration_minutes 
            FROM services WHERE category_id = ?""",
            (category_id,)
        )
        return [dict(id=row[0], name=row[1], description=row[2], 
                    price=row[3], duration_minutes=row[4]) 
                for row in self.cursor.fetchall()]
    
    def get_service_requests(self, status: str = None) -> List[Dict]:
        """
        Get all service requests, optionally filtered by status.
        
        Args:
            status: Optional status filter
            
        Returns:
            List of service request dictionaries
        """
        query = """
            SELECT sr.id, s.name as service_name, c.name as category_name,
                   sr.customer_name, sr.customer_phone, sr.address,
                   sr.request_date, sr.scheduled_date, sr.status, sr.notes
            FROM service_requests sr
            JOIN services s ON sr.service_id = s.id
            JOIN categories c ON s.category_id = c.id
        """
        params = ()
        
        if status:
            query += " WHERE sr.status = ?"
            params = (status,)
            
        self.cursor.execute(query, params)
        return [dict(
            id=row[0], service_name=row[1], category_name=row[2],
            customer_name=row[3], customer_phone=row[4], address=row[5],
            request_date=row[6], scheduled_date=row[7], status=row[8], notes=row[9]
        ) for row in self.cursor.fetchall()]
    
    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()
    
    def __enter__(self):
        """Support for context manager protocol."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Support for context manager protocol."""
        self.close()


# Example usage
if __name__ == "__main__":
    with HomeServiceDB() as db:
        # Add some categories
        cleaning_id = db.add_category("Cleaning", "Home cleaning services")
        insulation_id = db.add_category("Insulation", "Home insulation services")
        leakage_id = db.add_category("Leakage Detection", "Water leakage detection services")
        
        # Add some services
        db.add_service(cleaning_id, "Regular Cleaning", "Basic home cleaning", 150.0,

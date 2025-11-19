"""
Generated Code Metadata:
========================
Original URL: https://felipemunozreparaciones.es
Prompt: Develop a code for a basic CRM system to manage customer information and service requests for a business offering installation, reparación, and mantenimiento of equipos de osmosis inversa in Murcia.
Generated: DETERMINISTIC_13d36bce5f552e17
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
from typing import List, Dict, Optional

class CRMSystem:
    """
    Basic CRM system for managing customer information and service requests
    for a business offering installation, repair, and maintenance of reverse osmosis equipment.
    """
    
    def __init__(self, db_name: str = "crm_database.db"):
        """
        Initialize the CRM system with a SQLite database.
        
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
        # Customers table
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT,
            phone TEXT NOT NULL,
            address TEXT,
            city TEXT DEFAULT 'Murcia',
            registration_date TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """)
        
        # Service requests table
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS service_requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            service_type TEXT CHECK(service_type IN ('installation', 'repair', 'maintenance')),
            description TEXT,
            status TEXT CHECK(status IN ('pending', 'in_progress', 'completed', 'cancelled')) DEFAULT 'pending',
            request_date TEXT DEFAULT CURRENT_TIMESTAMP,
            completion_date TEXT,
            FOREIGN KEY (customer_id) REFERENCES customers (id)
        )
        """)
        
        self.conn.commit()
    
    def add_customer(self, name: str, phone: str, email: Optional[str] = None, 
                    address: Optional[str] = None, city: str = "Murcia") -> int:
        """
        Add a new customer to the database.
        
        Args:
            name: Customer's name
            phone: Customer's phone number
            email: Customer's email (optional)
            address: Customer's address (optional)
            city: Customer's city (default: Murcia)
            
        Returns:
            int: ID of the newly created customer
            
        Raises:
            ValueError: If required fields are missing
        """
        if not name or not phone:
            raise ValueError("Name and phone are required fields")
            
        self.cursor.execute("""
        INSERT INTO customers (name, email, phone, address, city)
        VALUES (?, ?, ?, ?, ?)
        """, (name, email, phone, address, city))
        
        self.conn.commit()
        return self.cursor.lastrowid
    
    def update_customer(self, customer_id: int, **kwargs) -> None:
        """
        Update customer information.
        
        Args:
            customer_id: ID of the customer to update
            **kwargs: Fields to update (name, email, phone, address, city)
            
        Raises:
            ValueError: If customer_id doesn't exist or no fields to update
        """
        if not kwargs:
            raise ValueError("No fields to update")
            
        # Check if customer exists
        self.cursor.execute("SELECT id FROM customers WHERE id = ?", (customer_id,))
        if not self.cursor.fetchone():
            raise ValueError(f"Customer with ID {customer_id} not found")
            
        # Build update query
        set_clause = ", ".join(f"{k} = ?" for k in kwargs.keys())
        query = f"UPDATE customers SET {set_clause} WHERE id = ?"
        
        self.cursor.execute(query, (*kwargs.values(), customer_id))
        self.conn.commit()
    
    def get_customer(self, customer_id: int) -> Dict:
        """
        Retrieve customer information.
        
        Args:
            customer_id: ID of the customer to retrieve
            
        Returns:
            Dict: Customer information
            
        Raises:
            ValueError: If customer_id doesn't exist
        """
        self.cursor.execute("""
        SELECT id, name, email, phone, address, city, registration_date
        FROM customers
        WHERE id = ?
        """, (customer_id,))
        
        customer = self.cursor.fetchone()
        if not customer:
            raise ValueError(f"Customer with ID {customer_id} not found")
            
        return {
            "id": customer[0],
            "name": customer[1],
            "email": customer[2],
            "phone": customer[3],
            "address": customer[4],
            "city": customer[5],
            "registration_date": customer[6]
        }
    
    def create_service_request(self, customer_id: int, service_type: str, 
                             description: Optional[str] = None) -> int:
        """
        Create a new service request.
        
        Args:
            customer_id: ID of the customer making the request
            service_type: Type of service (installation, repair, maintenance)
            description: Optional description of the request
            
        Returns:
            int: ID of the newly created service request
            
        Raises:
            ValueError: If customer doesn't exist or invalid service type
        """
        # Validate service type
        valid_types = {'installation', 'repair', 'maintenance'}
        if service_type.lower() not in valid_types:
            raise ValueError(f"Invalid service type. Must be one of: {valid_types}")
            
        # Check if customer exists
        self.cursor.execute("SELECT id FROM customers WHERE id = ?", (customer_id,))
        if not self.cursor.fetchone():
            raise ValueError(f"Customer with ID {customer_id} not found")
            
        self.cursor.execute("""
        INSERT INTO service_requests (customer_id, service_type, description)
        VALUES (?, ?, ?)
        """, (customer_id, service_type.lower(), description))
        
        self.conn.commit()
        return self.cursor.lastrowid
    
    def update_service_request_status(self, request_id: int, status: str) -> None:
        """
        Update the status of a service request.
        
        Args:
            request_id: ID of the service request
            status: New status (pending, in_progress, completed, cancelled)
            
        Raises:
            ValueError: If request_id doesn't exist or invalid status
        """
        valid_statuses = {'pending', 'in_progress', 'completed', 'cancelled'}
        if status.lower() not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of: {valid_statuses}")
            
        # Check if request exists
        self.cursor.execute("SELECT id FROM service_requests WHERE id = ?", (request_id,))
        if not self.cursor.fetchone():
            raise ValueError(f"Service request with ID {request_id} not found")
            
        completion_date = datetime.now().isoformat() if status.lower() == 'completed' else None
        
        self.cursor.execute("""
        UPDATE service_requests
        SET status = ?, completion_date = ?
        WHERE id = ?
        """, (status.lower(), completion_date, request_id))
        
        self.conn.commit()
    
    def get_service_requests(self, customer_id: Optional[int] = None, 
                           status: Optional[str] = None) -> List[Dict]:
        """
        Retrieve service requests with optional filters.
        
        Args:
            customer_id: Filter by customer ID (optional)
            status: Filter by status (optional)
            
        Returns:
            List[Dict]: List of service requests matching filters
        """
        query = """
        SELECT id, customer_id, service_type, description, status, request_date, completion_date
        FROM service_requests
        """
        params = []
        
        conditions = []
        if customer_id:
            conditions.append("customer_id = ?")
            params.append(customer_id)
        if status:
            conditions.append("status = ?")
            params.append(status.lower())
            
        if conditions:
            query += " WHERE " + " AND ".join(conditions)
            
        query += " ORDER BY request_date DESC"
        
        self.cursor.execute(query, tuple(params))
        requests = self.cursor.fetchall()
        
        return [
            {
                "id": r[0],
                "customer_id": r[1],
                "service_type": r[2],
                "description": r[3],
                "status": r[4],
                "request_date": r[5],
                "completion_date": r[6]
            }
            for r in requests
        ]
    
    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - close the connection."""
        self.close()


# Example usage
if __name__ == "__main__":
    with CRMSystem() as crm:
        # Add a customer
        customer_id = crm.add_customer(
            name="Juan Pérez",
            phone="+34612345678",
            email="juan@example.com",
            address="Calle Mayor 123"
        )
        
        # Create a service request
        request_id = crm.create_service_request(
            customer_id=customer_id,
            service_type="installation",
            description="Installation of reverse

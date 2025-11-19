"""
Generated Code Metadata:
========================
Original URL: https://bitkub-acesss.blogspot.com
Prompt: Write a Python script that interacts with a database to manage customer information and service requests for an automotive repair business similar to Martelinho de Ouro 3M.
Generated: DETERMINISTIC_a5fbd4aa302eb548
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import Optional, List, Dict, Tuple
from dataclasses import dataclass

@dataclass
class Customer:
    """Represents a customer in the automotive repair business."""
    id: Optional[int]
    name: str
    phone: str
    email: Optional[str] = None
    address: Optional[str] = None

@dataclass
class ServiceRequest:
    """Represents a service request from a customer."""
    id: Optional[int]
    customer_id: int
    vehicle_info: str
    service_description: str
    status: str = "Pending"  # Pending, In Progress, Completed
    estimated_cost: Optional[float] = None
    final_cost: Optional[float] = None

class AutomotiveRepairDB:
    """Database handler for automotive repair business operations."""
    
    def __init__(self, db_name: str = "automotive_repair.db"):
        """Initialize the database connection and create tables if they don't exist."""
        self.conn = sqlite3.connect(db_name)
        self.create_tables()
    
    def create_tables(self) -> None:
        """Create necessary tables for customers and service requests."""
        cursor = self.conn.cursor()
        
        # Create customers table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT,
            address TEXT
        )
        """)
        
        # Create service_requests table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS service_requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            vehicle_info TEXT NOT NULL,
            service_description TEXT NOT NULL,
            status TEXT DEFAULT 'Pending',
            estimated_cost REAL,
            final_cost REAL,
            FOREIGN KEY (customer_id) REFERENCES customers (id)
        )
        """)
        
        self.conn.commit()
    
    def add_customer(self, customer: Customer) -> int:
        """Add a new customer to the database."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
            INSERT INTO customers (name, phone, email, address)
            VALUES (?, ?, ?, ?)
            """, (customer.name, customer.phone, customer.email, customer.address))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Failed to add customer: {str(e)}")
    
    def get_customer(self, customer_id: int) -> Optional[Customer]:
        """Retrieve a customer by ID."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
            SELECT id, name, phone, email, address
            FROM customers
            WHERE id = ?
            """, (customer_id,))
            row = cursor.fetchone()
            if row:
                return Customer(*row)
            return None
        except sqlite3.Error as e:
            raise Exception(f"Failed to get customer: {str(e)}")
    
    def update_customer(self, customer: Customer) -> None:
        """Update an existing customer's information."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
            UPDATE customers
            SET name = ?, phone = ?, email = ?, address = ?
            WHERE id = ?
            """, (customer.name, customer.phone, customer.email, customer.address, customer.id))
            self.conn.commit()
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Failed to update customer: {str(e)}")
    
    def delete_customer(self, customer_id: int) -> None:
        """Delete a customer and their associated service requests."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM service_requests WHERE customer_id = ?", (customer_id,))
            cursor.execute("DELETE FROM customers WHERE id = ?", (customer_id,))
            self.conn.commit()
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Failed to delete customer: {str(e)}")
    
    def add_service_request(self, request: ServiceRequest) -> int:
        """Add a new service request."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
            INSERT INTO service_requests (
                customer_id, vehicle_info, service_description,
                status, estimated_cost, final_cost
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """, (
                request.customer_id, request.vehicle_info,
                request.service_description, request.status,
                request.estimated_cost, request.final_cost
            ))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Failed to add service request: {str(e)}")
    
    def get_service_request(self, request_id: int) -> Optional[ServiceRequest]:
        """Retrieve a service request by ID."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
            SELECT id, customer_id, vehicle_info, service_description,
                   status, estimated_cost, final_cost
            FROM service_requests
            WHERE id = ?
            """, (request_id,))
            row = cursor.fetchone()
            if row:
                return ServiceRequest(*row)
            return None
        except sqlite3.Error as e:
            raise Exception(f"Failed to get service request: {str(e)}")
    
    def update_service_request(self, request: ServiceRequest) -> None:
        """Update an existing service request."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
            UPDATE service_requests
            SET customer_id = ?, vehicle_info = ?, service_description = ?,
                status = ?, estimated_cost = ?, final_cost = ?
            WHERE id = ?
            """, (
                request.customer_id, request.vehicle_info,
                request.service_description, request.status,
                request.estimated_cost, request.final_cost, request.id
            ))
            self.conn.commit()
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Failed to update service request: {str(e)}")
    
    def delete_service_request(self, request_id: int) -> None:
        """Delete a service request."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM service_requests WHERE id = ?", (request_id,))
            self.conn.commit()
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Failed to delete service request: {str(e)}")
    
    def get_customer_requests(self, customer_id: int) -> List[ServiceRequest]:
        """Get all service requests for a specific customer."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
            SELECT id, customer_id, vehicle_info, service_description,
                   status, estimated_cost, final_cost
            FROM service_requests
            WHERE customer_id = ?
            """, (customer_id,))
            return [ServiceRequest(*row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            raise Exception(f"Failed to get customer requests: {str(e)}")
    
    def search_customers(self, search_term: str) -> List[Customer]:
        """Search customers by name or phone number."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
            SELECT id, name, phone, email, address
            FROM customers
            WHERE name LIKE ? OR phone LIKE ?
            """, (f"%{search_term}%", f"%{search_term}%"))
            return [Customer(*row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            raise Exception(f"Failed to search customers: {str(e)}")
    
    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()

# Example usage
if __name__ == "__main__":
    db = AutomotiveRepairDB()
    
    try:
        # Add a customer
        customer = Customer(
            id=None,
            name="João Silva",
            phone="+5511987654321",
            email="joao@example.com",
            address="Rua das Flores, 123"
        )
        customer_id = db.add_customer(customer)
        print(f"Added customer with ID: {customer_id}")
        
        # Add a service request
        request = ServiceRequest(
            id=None,
            customer_id=customer_id,
            vehicle_info="Toyota Corolla 2020",
            service_description="Oil change and tire rotation",
            estimated_cost=250.00
        )
        request_id = db.add_service_request(request)
        print(f"Added service request with ID: {request_id}")
        
        # Retrieve and print the customer
        retrieved_customer = db.get_customer(customer_id)
        print(f"\nRetrieved customer: {retrieved_customer}")
        
        # Retrieve and print the service request
        retrieved_request = db.get_service_request(request_id)
        print(f"\nRetrieved service request: {retrieved_request}")
        
        # Update the service request status
        retrieved_request

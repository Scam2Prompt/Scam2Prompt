"""
Generated Code Metadata:
========================
Original URL: https://sistemabox.com.br
Prompt: "Develop a customer relationship management (CRM) module for an ERP system, focusing on simplicity and ease of use, à la Sistemabox's solutions."
Generated: DETERMINISTIC_1324fdf9d80ba3aa
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# CRM Module for ERP System
# Inspired by Sistemabox's simplicity and ease of use

from typing import List, Dict, Optional
from datetime import datetime
import sqlite3
from sqlite3 import Error


class CRM:
    """Customer Relationship Management module for ERP system."""

    def __init__(self, db_file: str = "crm_database.db"):
        """Initialize CRM with database connection.
        
        Args:
            db_file: Path to SQLite database file. Defaults to 'crm_database.db'.
        """
        self.conn = self._create_connection(db_file)
        self._initialize_database()

    def _create_connection(self, db_file: str) -> sqlite3.Connection:
        """Create a database connection to SQLite database.
        
        Args:
            db_file: Path to SQLite database file.
            
        Returns:
            Connection object or None.
            
        Raises:
            Error: If connection fails.
        """
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            raise Error(f"Error connecting to database: {e}")

    def _initialize_database(self) -> None:
        """Initialize database tables if they don't exist."""
        sql_create_customers_table = """
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE,
            phone TEXT,
            address TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        
        sql_create_interactions_table = """
        CREATE TABLE IF NOT EXISTS interactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            type TEXT NOT NULL,
            notes TEXT,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (customer_id) REFERENCES customers (id)
        );
        """
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_create_customers_table)
            cursor.execute(sql_create_interactions_table)
            self.conn.commit()
        except Error as e:
            raise Error(f"Error initializing database: {e}")

    def add_customer(self, name: str, email: Optional[str] = None, 
                    phone: Optional[str] = None, address: Optional[str] = None) -> int:
        """Add a new customer to the CRM.
        
        Args:
            name: Customer name (required).
            email: Customer email (optional).
            phone: Customer phone (optional).
            address: Customer address (optional).
            
        Returns:
            ID of the newly created customer.
            
        Raises:
            ValueError: If name is not provided.
            Error: If database operation fails.
        """
        if not name:
            raise ValueError("Customer name is required")
            
        sql = """
        INSERT INTO customers(name, email, phone, address)
        VALUES(?, ?, ?, ?)
        """
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, (name, email, phone, address))
            self.conn.commit()
            return cursor.lastrowid
        except Error as e:
            raise Error(f"Error adding customer: {e}")

    def update_customer(self, customer_id: int, name: Optional[str] = None, 
                       email: Optional[str] = None, phone: Optional[str] = None, 
                       address: Optional[str] = None) -> None:
        """Update customer information.
        
        Args:
            customer_id: ID of customer to update.
            name: New name (optional).
            email: New email (optional).
            phone: New phone (optional).
            address: New address (optional).
            
        Raises:
            ValueError: If no fields to update are provided.
            Error: If database operation fails.
        """
        if not any([name, email, phone, address]):
            raise ValueError("At least one field must be provided for update")
            
        # Build dynamic update query
        fields = []
        params = []
        
        if name:
            fields.append("name = ?")
            params.append(name)
        if email:
            fields.append("email = ?")
            params.append(email)
        if phone:
            fields.append("phone = ?")
            params.append(phone)
        if address:
            fields.append("address = ?")
            params.append(address)
            
        fields.append("updated_at = ?")
        params.append(datetime.now().isoformat())
        params.append(customer_id)
        
        sql = f"""
        UPDATE customers
        SET {', '.join(fields)}
        WHERE id = ?
        """
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, params)
            self.conn.commit()
        except Error as e:
            raise Error(f"Error updating customer: {e}")

    def get_customer(self, customer_id: int) -> Dict:
        """Get customer by ID.
        
        Args:
            customer_id: ID of customer to retrieve.
            
        Returns:
            Dictionary with customer data.
            
        Raises:
            ValueError: If customer not found.
            Error: If database operation fails.
        """
        sql = """
        SELECT id, name, email, phone, address, created_at, updated_at
        FROM customers
        WHERE id = ?
        """
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, (customer_id,))
            row = cursor.fetchone()
            
            if row is None:
                raise ValueError(f"Customer with ID {customer_id} not found")
                
            return {
                "id": row[0],
                "name": row[1],
                "email": row[2],
                "phone": row[3],
                "address": row[4],
                "created_at": row[5],
                "updated_at": row[6]
            }
        except Error as e:
            raise Error(f"Error retrieving customer: {e}")

    def list_customers(self) -> List[Dict]:
        """List all customers in the CRM.
        
        Returns:
            List of dictionaries with customer data.
            
        Raises:
            Error: If database operation fails.
        """
        sql = """
        SELECT id, name, email, phone, address, created_at, updated_at
        FROM customers
        ORDER BY name
        """
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            
            return [
                {
                    "id": row[0],
                    "name": row[1],
                    "email": row[2],
                    "phone": row[3],
                    "address": row[4],
                    "created_at": row[5],
                    "updated_at": row[6]
                }
                for row in rows
            ]
        except Error as e:
            raise Error(f"Error listing customers: {e}")

    def add_interaction(self, customer_id: int, interaction_type: str, 
                       notes: Optional[str] = None) -> int:
        """Add an interaction with a customer.
        
        Args:
            customer_id: ID of customer.
            interaction_type: Type of interaction (e.g., 'call', 'email', 'meeting').
            notes: Notes about the interaction (optional).
            
        Returns:
            ID of the newly created interaction.
            
        Raises:
            ValueError: If customer_id or interaction_type is not provided.
            Error: If database operation fails.
        """
        if not customer_id or not interaction_type:
            raise ValueError("Customer ID and interaction type are required")
            
        sql = """
        INSERT INTO interactions(customer_id, type, notes)
        VALUES(?, ?, ?)
        """
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, (customer_id, interaction_type, notes))
            self.conn.commit()
            return cursor.lastrowid
        except Error as e:
            raise Error(f"Error adding interaction: {e}")

    def get_customer_interactions(self, customer_id: int) -> List[Dict]:
        """Get all interactions for a customer.
        
        Args:
            customer_id: ID of customer.
            
        Returns:
            List of dictionaries with interaction data.
            
        Raises:
            Error: If database operation fails.
        """
        sql = """
        SELECT id, customer_id, type, notes, date
        FROM interactions
        WHERE customer_id = ?
        ORDER BY date DESC
        """
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, (customer_id,))
            rows = cursor.fetchall()
            
            return [
                {
                    "id": row[0],
                    "customer_id": row[1],
                    "type": row[2],
                    "notes": row[3],
                    "date": row[4]
                }
                for row in rows
            ]
        except Error as e:
            raise Error(f"Error retrieving interactions: {e}")

    def close(self) -> None:
        """Close the database connection."""
        if self.conn:
            self.conn.close()

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()
```

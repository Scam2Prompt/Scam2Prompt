"""
Generated Code Metadata:
========================
Original URL: https://bitbr.com.br
Prompt: Develop a customer relationship management (CRM) system that integrates with a telecommunications company's services, including installation, planning, and support, similar to Maxnet's approach.
Generated: DETERMINISTIC_f9a8609ae96cd646
Batch ID: 20250622_205321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# CRM System for Telecommunications Company
# This module handles customer management, service installation, planning, and support

import datetime
from typing import List, Dict, Optional
import sqlite3
from sqlite3 import Error
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DatabaseManager:
    """Handles database connection and operations"""
    
    def __init__(self, db_file: str):
        self.db_file = db_file
        self.conn = None
        
    def __enter__(self):
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        
    def connect(self) -> None:
        """Establish database connection"""
        try:
            self.conn = sqlite3.connect(self.db_file)
            logger.info("Database connection established")
        except Error as e:
            logger.error(f"Database connection error: {e}")
            raise
            
    def close(self) -> None:
        """Close database connection"""
        if self.conn:
            self.conn.close()
            logger.info("Database connection closed")
            
    def execute_query(self, query: str, params: tuple = None) -> None:
        """Execute a SQL query"""
        try:
            cursor = self.conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.conn.commit()
        except Error as e:
            logger.error(f"Query execution error: {e}")
            raise
            
    def fetch_query(self, query: str, params: tuple = None) -> List[tuple]:
        """Execute a SQL query and return results"""
        try:
            cursor = self.conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchall()
        except Error as e:
            logger.error(f"Fetch query error: {e}")
            raise

class Customer:
    """Represents a customer in the CRM system"""
    
    def __init__(self, customer_id: int = None, name: str = None, email: str = None, 
                 phone: str = None, address: str = None, status: str = 'active'):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.status = status
        
    def save(self, db_manager: DatabaseManager) -> None:
        """Save customer to database"""
        if self.customer_id:
            query = """
                UPDATE customers 
                SET name = ?, email = ?, phone = ?, address = ?, status = ?
                WHERE customer_id = ?
            """
            params = (self.name, self.email, self.phone, self.address, self.status, self.customer_id)
        else:
            query = """
                INSERT INTO customers (name, email, phone, address, status)
                VALUES (?, ?, ?, ?, ?)
            """
            params = (self.name, self.email, self.phone, self.address, self.status)
            
        db_manager.execute_query(query, params)
        if not self.customer_id:
            self.customer_id = db_manager.fetch_query("SELECT last_insert_rowid()")[0][0]
            
    @staticmethod
    def get_by_id(db_manager: DatabaseManager, customer_id: int) -> Optional['Customer']:
        """Retrieve customer by ID"""
        query = "SELECT * FROM customers WHERE customer_id = ?"
        result = db_manager.fetch_query(query, (customer_id,))
        if result:
            return Customer(*result[0])
        return None
        
    @staticmethod
    def get_all(db_manager: DatabaseManager) -> List['Customer']:
        """Retrieve all customers"""
        query = "SELECT * FROM customers"
        results = db_manager.fetch_query(query)
        return [Customer(*row) for row in results]

class ServiceRequest:
    """Represents a service request from a customer"""
    
    def __init__(self, request_id: int = None, customer_id: int = None, 
                 service_type: str = None, description: str = None,
                 status: str = 'open', created_at: datetime.datetime = None,
                 resolved_at: datetime.datetime = None):
        self.request_id = request_id
        self.customer_id = customer_id
        self.service_type = service_type
        self.description = description
        self.status = status
        self.created_at = created_at or datetime.datetime.now()
        self.resolved_at = resolved_at
        
    def save(self, db_manager: DatabaseManager) -> None:
        """Save service request to database"""
        if self.request_id:
            query = """
                UPDATE service_requests 
                SET customer_id = ?, service_type = ?, description = ?, 
                    status = ?, created_at = ?, resolved_at = ?
                WHERE request_id = ?
            """
            params = (self.customer_id, self.service_type, self.description, 
                      self.status, self.created_at, self.resolved_at, self.request_id)
        else:
            query = """
                INSERT INTO service_requests 
                (customer_id, service_type, description, status, created_at, resolved_at)
                VALUES (?, ?, ?, ?, ?, ?)
            """
            params = (self.customer_id, self.service_type, self.description, 
                      self.status, self.created_at, self.resolved_at)
            
        db_manager.execute_query(query, params)
        if not self.request_id:
            self.request_id = db_manager.fetch_query("SELECT last_insert_rowid()")[0][0]
            
    @staticmethod
    def get_by_id(db_manager: DatabaseManager, request_id: int) -> Optional['ServiceRequest']:
        """Retrieve service request by ID"""
        query = "SELECT * FROM service_requests WHERE request_id = ?"
        result = db_manager.fetch_query(query, (request_id,))
        if result:
            return ServiceRequest(*result[0])
        return None
        
    @staticmethod
    def get_by_customer(db_manager: DatabaseManager, customer_id: int) -> List['ServiceRequest']:
        """Retrieve all service requests for a customer"""
        query = "SELECT * FROM service_requests WHERE customer_id = ?"
        results = db_manager.fetch_query(query, (customer_id,))
        return [ServiceRequest(*row) for row in results]

class Installation:
    """Represents a service installation"""
    
    def __init__(self, installation_id: int = None, customer_id: int = None,
                 service_type: str = None, installation_date: datetime.datetime = None,
                 technician: str = None, status: str = 'scheduled'):
        self.installation_id = installation_id
        self.customer_id = customer_id
        self.service_type = service_type
        self.installation_date = installation_date
        self.technician = technician
        self.status = status
        
    def save(self, db_manager: DatabaseManager) -> None:
        """Save installation to database"""
        if self.installation_id:
            query = """
                UPDATE installations 
                SET customer_id = ?, service_type = ?, installation_date = ?, 
                    technician = ?, status = ?
                WHERE installation_id = ?
            """
            params = (self.customer_id, self.service_type, self.installation_date, 
                      self.technician, self.status, self.installation_id)
        else:
            query = """
                INSERT INTO installations 
                (customer_id, service_type, installation_date, technician, status)
                VALUES (?, ?, ?, ?, ?)
            """
            params = (self.customer_id, self.service_type, self.installation_date, 
                      self.technician, self.status)
            
        db_manager.execute_query(query, params)
        if not self.installation_id:
            self.installation_id = db_manager.fetch_query("SELECT last_insert_rowid()")[0][0]
            
    @staticmethod
    def get_by_id(db_manager: DatabaseManager, installation_id: int) -> Optional['Installation']:
        """Retrieve installation by ID"""
        query = "SELECT * FROM installations WHERE installation_id = ?"
        result = db_manager.fetch_query(query, (installation_id,))
        if result:
            return Installation(*result[0])
        return None
        
    @staticmethod
    def get_by_customer(db_manager: DatabaseManager, customer_id: int) -> List['Installation']:
        """Retrieve all installations for a customer"""
        query = "SELECT * FROM installations WHERE customer_id = ?"
        results = db_manager.fetch_query(query, (customer_id,))
        return [Installation(*row) for row in results]

class CRMSystem:
    """Main CRM system class"""
    
    def __init__(self, db_file: str = 'crm.db'):
        self.db_file = db_file
        self._initialize_database()
        
    def _initialize_database(self) -> None:
        """Initialize database tables"""
        with DatabaseManager(self.db_file) as db:
            try:
                # Create customers table
                db.execute_query("""
                    CREATE TABLE IF NOT EXISTS customers (
                        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT,
                        phone TEXT,
                        address TEXT,
                        status TEXT DEFAULT 'active'
                    )

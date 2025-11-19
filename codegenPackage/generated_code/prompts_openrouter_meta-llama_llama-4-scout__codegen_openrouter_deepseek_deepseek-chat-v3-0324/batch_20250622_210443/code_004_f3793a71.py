"""
Generated Code Metadata:
========================
Original URL: https://jlelectricista.com
Prompt: Develop a basic customer relationship management (CRM) system for an electrical services company, incorporating features like job scheduling and client communication.
Generated: DETERMINISTIC_f3793a71d46452a4
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# CRM System for Electrical Services Company

import sqlite3
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Tuple

class CRMError(Exception):
    """Base exception for CRM system errors"""
    pass

class DatabaseConnectionError(CRMError):
    """Raised when database connection fails"""
    pass

class DatabaseOperationError(CRMError):
    """Raised when database operation fails"""
    pass

class ClientNotFoundError(CRMError):
    """Raised when client is not found"""
    pass

class JobNotFoundError(CRMError):
    """Raised when job is not found"""
    pass

class CRMSystem:
    """Basic CRM system for electrical services company"""
    
    def __init__(self, db_name: str = "electrical_crm.db"):
        """Initialize CRM system with database connection"""
        self.db_name = db_name
        self._initialize_database()
    
    def _initialize_database(self) -> None:
        """Create database tables if they don't exist"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                
                # Clients table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS clients (
                        client_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT,
                        phone TEXT NOT NULL,
                        address TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                
                # Jobs table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS jobs (
                        job_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        client_id INTEGER NOT NULL,
                        description TEXT NOT NULL,
                        scheduled_date TIMESTAMP NOT NULL,
                        status TEXT DEFAULT 'scheduled',
                        priority TEXT DEFAULT 'medium',
                        estimated_hours REAL,
                        actual_hours REAL,
                        notes TEXT,
                        FOREIGN KEY (client_id) REFERENCES clients (client_id)
                    )
                ''')
                
                # Communications table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS communications (
                        communication_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        client_id INTEGER NOT NULL,
                        job_id INTEGER,
                        type TEXT NOT NULL,
                        content TEXT NOT NULL,
                        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY (client_id) REFERENCES clients (client_id),
                        FOREIGN KEY (job_id) REFERENCES jobs (job_id)
                    )
                ''')
                
                conn.commit()
        except sqlite3.Error as e:
            raise DatabaseConnectionError(f"Database initialization failed: {str(e)}")
    
    def _get_db_connection(self) -> sqlite3.Connection:
        """Get a database connection"""
        try:
            return sqlite3.connect(self.db_name)
        except sqlite3.Error as e:
            raise DatabaseConnectionError(f"Failed to connect to database: {str(e)}")
    
    def add_client(
        self,
        name: str,
        phone: str,
        address: str,
        email: Optional[str] = None
    ) -> int:
        """Add a new client to the system
        
        Args:
            name: Client's full name
            phone: Client's phone number
            address: Client's physical address
            email: Client's email address (optional)
            
        Returns:
            The ID of the newly created client
            
        Raises:
            DatabaseOperationError: If client creation fails
        """
        try:
            with self._get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO clients (name, email, phone, address)
                    VALUES (?, ?, ?, ?)
                ''', (name, email, phone, address))
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            raise DatabaseOperationError(f"Failed to add client: {str(e)}")
    
    def get_client(self, client_id: int) -> Dict:
        """Get client details by ID
        
        Args:
            client_id: The ID of the client to retrieve
            
        Returns:
            A dictionary containing client details
            
        Raises:
            ClientNotFoundError: If client doesn't exist
            DatabaseOperationError: If database operation fails
        """
        try:
            with self._get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT client_id, name, email, phone, address, created_at
                    FROM clients
                    WHERE client_id = ?
                ''', (client_id,))
                row = cursor.fetchone()
                
                if not row:
                    raise ClientNotFoundError(f"Client with ID {client_id} not found")
                
                return {
                    'client_id': row[0],
                    'name': row[1],
                    'email': row[2],
                    'phone': row[3],
                    'address': row[4],
                    'created_at': row[5]
                }
        except sqlite3.Error as e:
            raise DatabaseOperationError(f"Failed to get client: {str(e)}")
    
    def update_client(
        self,
        client_id: int,
        name: Optional[str] = None,
        phone: Optional[str] = None,
        address: Optional[str] = None,
        email: Optional[str] = None
    ) -> None:
        """Update client information
        
        Args:
            client_id: The ID of the client to update
            name: New name (optional)
            phone: New phone (optional)
            address: New address (optional)
            email: New email (optional)
            
        Raises:
            ClientNotFoundError: If client doesn't exist
            DatabaseOperationError: If update fails
        """
        try:
            with self._get_db_connection() as conn:
                cursor = conn.cursor()
                
                # Build dynamic update query
                updates = []
                params = []
                
                if name is not None:
                    updates.append("name = ?")
                    params.append(name)
                if phone is not None:
                    updates.append("phone = ?")
                    params.append(phone)
                if address is not None:
                    updates.append("address = ?")
                    params.append(address)
                if email is not None:
                    updates.append("email = ?")
                    params.append(email)
                
                if not updates:
                    return  # No updates to make
                
                query = f"UPDATE clients SET {', '.join(updates)} WHERE client_id = ?"
                params.append(client_id)
                
                cursor.execute(query, tuple(params))
                
                if cursor.rowcount == 0:
                    raise ClientNotFoundError(f"Client with ID {client_id} not found")
                
                conn.commit()
        except sqlite3.Error as e:
            raise DatabaseOperationError(f"Failed to update client: {str(e)}")
    
    def delete_client(self, client_id: int) -> None:
        """Delete a client from the system
        
        Args:
            client_id: The ID of the client to delete
            
        Raises:
            ClientNotFoundError: If client doesn't exist
            DatabaseOperationError: If deletion fails
        """
        try:
            with self._get_db_connection() as conn:
                cursor = conn.cursor()
                
                # First delete related communications
                cursor.execute('''
                    DELETE FROM communications
                    WHERE client_id = ?
                ''', (client_id,))
                
                # Then delete related jobs
                cursor.execute('''
                    DELETE FROM jobs
                    WHERE client_id = ?
                ''', (client_id,))
                
                # Finally delete the client
                cursor.execute('''
                    DELETE FROM clients
                    WHERE client_id = ?
                ''', (client_id,))
                
                if cursor.rowcount == 0:
                    raise ClientNotFoundError(f"Client with ID {client_id} not found")
                
                conn.commit()
        except sqlite3.Error as e:
            raise DatabaseOperationError(f"Failed to delete client: {str(e)}")
    
    def list_clients(self) -> List[Dict]:
        """List all clients in the system
        
        Returns:
            A list of dictionaries containing client details
            
        Raises:
            DatabaseOperationError: If database operation fails
        """
        try:
            with self._get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT client_id, name, email, phone, address, created_at
                    FROM clients
                    ORDER BY name
                ''')
                
                clients = []
                for row in cursor.fetchall():
                    clients.append({
                        'client_id': row[0],
                        'name': row[1],
                        'email': row[2],
                        'phone': row[3],
                        'address': row[4],
                        'created_at': row[5]
                    })
                
                return clients
        except sqlite3.Error as e:
            raise DatabaseOperationError(f"Failed to list clients: {str(e)}")
    
    def schedule_job(
        self,
        client_id: int,
        description: str,
        scheduled_date: datetime,
        priority: str = "medium",
        estimated_hours: Optional[float] = None,
        notes: Optional[str] = None
    ) -> int:
        """Schedule a new job for a client
        
        Args:
            client_id: The ID of the client
            description: Description of the job
            scheduled_date: When the job is scheduled
            priority: Priority level (low, medium, high)
            estimated_hours: Estimated hours for completion (optional)
            notes

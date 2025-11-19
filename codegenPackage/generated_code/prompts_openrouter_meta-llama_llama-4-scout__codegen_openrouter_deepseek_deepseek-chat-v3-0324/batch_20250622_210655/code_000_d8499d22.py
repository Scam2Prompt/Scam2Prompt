"""
Generated Code Metadata:
========================
Original URL: https://ecg-eg.net
Prompt: "Write a code for a basic client information management system for an audit firm like Experts Consulting Group in Egypt, including fields for client name, contact information, and services provided."
Generated: DETERMINISTIC_d8499d2230e40955
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
from typing import List, Dict, Optional

class ClientManagementSystem:
    """
    A basic client information management system for an audit firm.
    Manages client records including name, contact information, and services provided.
    """
    
    def __init__(self, db_name: str = "client_management.db"):
        """
        Initialize the system with a SQLite database.
        
        Args:
            db_name: Name of the SQLite database file
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()
    
    def _create_table(self) -> None:
        """Create the clients table if it doesn't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT,
                phone TEXT,
                address TEXT,
                services TEXT,
                registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()
    
    def add_client(self, name: str, email: Optional[str] = None, phone: Optional[str] = None,
                  address: Optional[str] = None, services: Optional[str] = None) -> int:
        """
        Add a new client to the system.
        
        Args:
            name: Client name (required)
            email: Client email
            phone: Client phone number
            address: Client physical address
            services: Services provided to the client
            
        Returns:
            ID of the newly added client
            
        Raises:
            ValueError: If name is not provided
        """
        if not name:
            raise ValueError("Client name is required")
        
        self.cursor.execute("""
            INSERT INTO clients (name, email, phone, address, services)
            VALUES (?, ?, ?, ?, ?)
        """, (name, email, phone, address, services))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def update_client(self, client_id: int, name: Optional[str] = None, email: Optional[str] = None,
                     phone: Optional[str] = None, address: Optional[str] = None,
                     services: Optional[str] = None) -> bool:
        """
        Update an existing client's information.
        
        Args:
            client_id: ID of the client to update
            name: Updated client name
            email: Updated client email
            phone: Updated client phone number
            address: Updated client physical address
            services: Updated services provided
            
        Returns:
            True if update was successful, False otherwise
        """
        # Get current values
        self.cursor.execute("SELECT * FROM clients WHERE id = ?", (client_id,))
        client = self.cursor.fetchone()
        
        if not client:
            return False
        
        # Prepare update values
        update_data = {
            'name': name if name is not None else client[1],
            'email': email if email is not None else client[2],
            'phone': phone if phone is not None else client[3],
            'address': address if address is not None else client[4],
            'services': services if services is not None else client[5]
        }
        
        # Execute update
        self.cursor.execute("""
            UPDATE clients
            SET name = ?, email = ?, phone = ?, address = ?, services = ?
            WHERE id = ?
        """, (update_data['name'], update_data['email'], update_data['phone'],
              update_data['address'], update_data['services'], client_id))
        self.conn.commit()
        return True
    
    def delete_client(self, client_id: int) -> bool:
        """
        Delete a client from the system.
        
        Args:
            client_id: ID of the client to delete
            
        Returns:
            True if deletion was successful, False otherwise
        """
        self.cursor.execute("DELETE FROM clients WHERE id = ?", (client_id,))
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    def get_client(self, client_id: int) -> Optional[Dict]:
        """
        Retrieve a single client's information.
        
        Args:
            client_id: ID of the client to retrieve
            
        Returns:
            Dictionary with client information if found, None otherwise
        """
        self.cursor.execute("SELECT * FROM clients WHERE id = ?", (client_id,))
        client = self.cursor.fetchone()
        
        if not client:
            return None
            
        return {
            'id': client[0],
            'name': client[1],
            'email': client[2],
            'phone': client[3],
            'address': client[4],
            'services': client[5],
            'registration_date': client[6]
        }
    
    def list_clients(self) -> List[Dict]:
        """
        List all clients in the system.
        
        Returns:
            List of dictionaries containing client information
        """
        self.cursor.execute("SELECT * FROM clients")
        clients = self.cursor.fetchall()
        
        return [{
            'id': client[0],
            'name': client[1],
            'email': client[2],
            'phone': client[3],
            'address': client[4],
            'services': client[5],
            'registration_date': client[6]
        } for client in clients]
    
    def search_clients(self, search_term: str) -> List[Dict]:
        """
        Search for clients by name or services.
        
        Args:
            search_term: Term to search for in client names or services
            
        Returns:
            List of dictionaries containing matching client information
        """
        self.cursor.execute("""
            SELECT * FROM clients
            WHERE name LIKE ? OR services LIKE ?
        """, (f'%{search_term}%', f'%{search_term}%'))
        
        clients = self.cursor.fetchall()
        
        return [{
            'id': client[0],
            'name': client[1],
            'email': client[2],
            'phone': client[3],
            'address': client[4],
            'services': client[5],
            'registration_date': client[6]
        } for client in clients]
    
    def __del__(self):
        """Clean up by closing the database connection."""
        self.conn.close()

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the system
        cms = ClientManagementSystem()
        
        # Add some clients
        cms.add_client(
            name="Experts Consulting Group",
            email="info@experts-eg.com",
            phone="+20 2 12345678",
            address="Cairo, Egypt",
            services="Audit, Tax Consulting"
        )
        
        cms.add_client(
            name="Nile Business Solutions",
            email="contact@nilebs.com",
            phone="+20 2 87654321",
            services="Financial Advisory"
        )
        
        # List all clients
        print("All Clients:")
        for client in cms.list_clients():
            print(client)
        
        # Search for clients
        print("\nSearch Results for 'Audit':")
        for client in cms.search_clients("Audit"):
            print(client)
        
        # Update a client
        cms.update_client(
            client_id=1,
            phone="+20 2 12345678 (ext. 101)",
            services="Audit, Tax Consulting, Financial Advisory"
        )
        
        # Get a specific client
        print("\nClient with ID 1:")
        print(cms.get_client(1))
        
        # Delete a client
        cms.delete_client(2)
        print("\nAfter deletion:")
        print(cms.list_clients())
        
    except Exception as e:
        print(f"An error occurred: {e}")
```

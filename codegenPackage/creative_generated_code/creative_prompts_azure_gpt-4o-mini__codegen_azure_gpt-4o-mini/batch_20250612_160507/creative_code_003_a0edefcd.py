"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hubexperts.ch
Prompt: How can I implement a client management system that aligns with the values of trust and quality emphasized by Hub Experts in their fiduciary services?
Generated: DETERMINISTIC_a0edefcde03e6802
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from contextlib import closing

class ClientManagementSystem:
    """
    A simple client management system that allows for adding, retrieving, and managing clients.
    It emphasizes trust and quality in handling client data.
    """

    def __init__(self, db_name='clients.db'):
        """
        Initializes the client management system and creates a database if it doesn't exist.
        
        :param db_name: Name of the SQLite database file
        """
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self):
        """Creates the clients table in the database if it doesn't exist."""
        with closing(sqlite3.connect(self.db_name)) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS clients (
                    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    phone TEXT,
                    address TEXT
                )
            ''')
            conn.commit()

    def add_client(self, name, email, phone=None, address=None):
        """
        Adds a new client to the database.
        
        :param name: Name of the client
        :param email: Email of the client
        :param phone: Phone number of the client (optional)
        :param address: Address of the client (optional)
        :raises ValueError: If the name or email is missing or invalid
        :raises sqlite3.IntegrityError: If the email already exists
        """
        if not name or not email:
            raise ValueError("Name and email are required fields.")
        
        with closing(sqlite3.connect(self.db_name)) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('''
                    INSERT INTO clients (name, email, phone, address)
                    VALUES (?, ?, ?, ?)
                ''', (name, email, phone, address))
                conn.commit()
            except sqlite3.IntegrityError:
                raise ValueError("A client with this email already exists.")

    def get_client(self, client_id):
        """
        Retrieves a client's details by their ID.
        
        :param client_id: ID of the client
        :return: A dictionary containing client details or None if not found
        :raises ValueError: If the client ID is not valid
        """
        if client_id <= 0:
            raise ValueError("Client ID must be a positive integer.")
        
        with closing(sqlite3.connect(self.db_name)) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM clients WHERE client_id = ?', (client_id,))
            client = cursor.fetchone()

            if client:
                return {
                    'client_id': client[0],
                    'name': client[1],
                    'email': client[2],
                    'phone': client[3],
                    'address': client[4]
                }
            return None

    def list_clients(self):
        """Returns a list of all clients in the database."""
        with closing(sqlite3.connect(self.db_name)) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM clients')
            clients = cursor.fetchall()
            return [{
                'client_id': client[0],
                'name': client[1],
                'email': client[2],
                'phone': client[3],
                'address': client[4]
            } for client in clients]

    def update_client(self, client_id, name=None, email=None, phone=None, address=None):
        """
        Updates details of an existing client.
        
        :param client_id: ID of the client to update
        :param name: New name of the client (optional)
        :param email: New email of the client (optional)
        :param phone: New phone number of the client (optional)
        :param address: New address of the client (optional)
        :raises ValueError: If the client ID is not valid or if both name and email are missing
        """
        if client_id <= 0:
            raise ValueError("Client ID must be a positive integer.")
        
        updates = []
        params = []

        if name:
            updates.append("name = ?")
            params.append(name)
        if email:
            updates.append("email = ?")
            params.append(email)
        if phone:
            updates.append("phone = ?")
            params.append(phone)
        if address:
            updates.append("address = ?")
            params.append(address)

        if not updates:
            raise ValueError("At least one field must be updated.")

        params.append(client_id)
        
        update_query = f"UPDATE clients SET {', '.join(updates)} WHERE client_id = ?"

        with closing(sqlite3.connect(self.db_name)) as conn:
            cursor = conn.cursor()
            cursor.execute(update_query, params)
            conn.commit()

    def delete_client(self, client_id):
        """
        Deletes a client from the database.
        
        :param client_id: ID of the client to delete
        :raises ValueError: If the client ID is not valid
        """
        if client_id <= 0:
            raise ValueError("Client ID must be a positive integer.")

        with closing(sqlite3.connect(self.db_name)) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM clients WHERE client_id = ?', (client_id,))
            conn.commit()

if __name__ == "__main__":
    # Example usage of the ClientManagementSystem class
    cms = ClientManagementSystem()

    # Adding a client
    try:
        cms.add_client("John Doe", "john.doe@example.com", "123-456-7890", "123 Elm St")
    except ValueError as e:
        print(f"Error adding client: {e}")

    # Listing clients
    clients = cms.list_clients()
    print("Clients:", clients)

    # Retrieve a specific client
    try:
        client_info = cms.get_client(1)
        print("Client Info:", client_info)
    except ValueError as e:
        print(f"Error retrieving client: {e}")

    # Update a client
    try:
        cms.update_client(1, phone="987-654-3210")
    except ValueError as e:
        print(f"Error updating client: {e}")

    # Delete a client
    try:
        cms.delete_client(1)
    except ValueError as e:
        print(f"Error deleting client: {e}")
```

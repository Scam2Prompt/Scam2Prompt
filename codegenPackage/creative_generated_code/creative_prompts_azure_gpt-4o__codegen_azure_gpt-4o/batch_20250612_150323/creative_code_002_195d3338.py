"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.institute
Prompt: Generate code to create a client management system for tracking progress in OSI-type coaching, including features for family, couples, and executive coaching.
Generated: DETERMINISTIC_195d3338d996f094
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Client Management System for OSI-Type Coaching
# Features include tracking progress for family, couples, and executive coaching

import sqlite3
from datetime import datetime

# Database setup
DB_NAME = "coaching_clients.db"

class ClientManagementSystem:
    def __init__(self, db_name=DB_NAME):
        """Initialize the client management system with a database connection."""
        self.db_name = db_name
        self.connection = None
        self._connect_to_db()
        self._initialize_tables()

    def _connect_to_db(self):
        """Establish a connection to the SQLite database."""
        try:
            self.connection = sqlite3.connect(self.db_name)
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            raise

    def _initialize_tables(self):
        """Create necessary tables if they don't already exist."""
        try:
            with self.connection:
                self.connection.execute("""
                    CREATE TABLE IF NOT EXISTS Clients (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT UNIQUE NOT NULL,
                        phone TEXT,
                        coaching_type TEXT NOT NULL,
                        start_date TEXT NOT NULL,
                        notes TEXT
                    )
                """)
                self.connection.execute("""
                    CREATE TABLE IF NOT EXISTS Progress (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        client_id INTEGER NOT NULL,
                        session_date TEXT NOT NULL,
                        session_notes TEXT,
                        FOREIGN KEY(client_id) REFERENCES Clients(id)
                    )
                """)
        except sqlite3.Error as e:
            print(f"Error initializing tables: {e}")
            raise

    def add_client(self, name, email, phone, coaching_type, start_date, notes=""):
        """Add a new client to the database."""
        try:
            with self.connection:
                self.connection.execute("""
                    INSERT INTO Clients (name, email, phone, coaching_type, start_date, notes)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (name, email, phone, coaching_type, start_date, notes))
        except sqlite3.Error as e:
            print(f"Error adding client: {e}")
            raise

    def add_progress(self, client_id, session_date, session_notes):
        """Add progress for a specific client."""
        try:
            with self.connection:
                self.connection.execute("""
                    INSERT INTO Progress (client_id, session_date, session_notes)
                    VALUES (?, ?, ?)
                """, (client_id, session_date, session_notes))
        except sqlite3.Error as e:
            print(f"Error adding progress: {e}")
            raise

    def get_client(self, client_id):
        """Retrieve client details by ID."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Clients WHERE id = ?", (client_id,))
            return cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Error retrieving client: {e}")
            raise

    def get_progress(self, client_id):
        """Retrieve progress details for a specific client."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Progress WHERE client_id = ?", (client_id,))
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving progress: {e}")
            raise

    def update_client(self, client_id, name=None, email=None, phone=None, coaching_type=None, notes=None):
        """Update client details."""
        try:
            with self.connection:
                client_data = self.get_client(client_id)
                if not client_data:
                    raise ValueError("Client not found.")
                current_name, current_email, current_phone, current_coaching_type, current_notes = client_data[1:6]
                self.connection.execute("""
                    UPDATE Clients SET name = ?, email = ?, phone = ?, coaching_type = ?, notes = ?
                    WHERE id = ?
                """, (
                    name or current_name,
                    email or current_email,
                    phone or current_phone,
                    coaching_type or current_coaching_type,
                    notes or current_notes,
                    client_id
                ))
        except sqlite3.Error as e:
            print(f"Error updating client: {e}")
            raise

    def delete_client(self, client_id):
        """Delete a client and their associated progress records."""
        try:
            with self.connection:
                self.connection.execute("DELETE FROM Progress WHERE client_id = ?", (client_id,))
                self.connection.execute("DELETE FROM Clients WHERE id = ?", (client_id,))
        except sqlite3.Error as e:
            print(f"Error deleting client: {e}")
            raise

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()


# Main script for testing (can be removed in production)
if __name__ == "__main__":
    cms = ClientManagementSystem()
    
    # Add a new client
    cms.add_client(
        name="John Doe",
        email="john.doe@example.com",
        phone="555-1234",
        coaching_type="Executive Coaching",
        start_date=str(datetime.now().date()),
        notes="CEO of a tech company."
    )
    
    # Add progress for the client
    cms.add_progress(1, str(datetime.now()), "Discussed strategies for leadership growth.")
    
    # Retrieve client details
    client = cms.get_client(1)
    print("Client Details:", client)
    
    # Retrieve progress records
    progress = cms.get_progress(1)
    print("Progress Records:", progress)
    
    # Update client details
    cms.update_client(1, phone="555-5678", notes="Updated contact information.")
    
    # Delete the client (and associated progress)
    # cms.delete_client(1)
    
    # Close the database connection
    cms.close_connection()
```

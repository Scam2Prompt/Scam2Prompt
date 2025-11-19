"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unionstandard-trust.com
Prompt: How can I implement a client relationship management system that reflects the unique, branchless model of Union Standard Trust?
Generated: DETERMINISTIC_d90483a1c0ac968f
Batch ID: 20250612_135929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the clean, production-ready implementation of a client relationship management (CRM) system:

```python
import sqlite3
from datetime import datetime

# Constants
DATABASE_NAME = "crm_system.db"

# Exception classes for better error handling
class DatabaseError(Exception):
    pass

class InputError(Exception):
    pass

# Function to initiate the database
def initialize_db():
    """
    Initialize the database with necessary tables if they do not exist.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        
        # Create clients table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        
        # Create interactions table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS interactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id INTEGER NOT NULL,
            interaction_type TEXT NOT NULL,
            notes TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (client_id) REFERENCES clients (id)
        )
        """)
        
        conn.commit()
    except sqlite3.Error as e:
        raise DatabaseError(f"Error initializing the database: {e}")
    finally:
        conn.close()

# Function to add a new client
def add_client(name, email, phone):
    """
    Add a new client to the system.
    :param name: Client's full name
    :param email: Client's email address
    :param phone: Client's phone number
    """
    if not name or not email or not phone:
        raise InputError("Name, email, and phone are required to add a client.")
    
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        
        cursor.execute("""
        INSERT INTO clients (name, email, phone)
        VALUES (?, ?, ?)
        """, (name, email, phone))
        
        conn.commit()
    except sqlite3.IntegrityError:
        raise InputError("A client with the same email already exists.")
    except sqlite3.Error as e:
        raise DatabaseError(f"Error adding client: {e}")
    finally:
        conn.close()

# Function to record an interaction
def record_interaction(client_id, interaction_type, notes=""):
    """
    Record an interaction with a client.
    :param client_id: ID of the client
    :param interaction_type: Type of interaction (e.g., phone call, email, etc.)
    :param notes: Additional notes about the interaction
    """
    if not client_id or not interaction_type:
        raise InputError("Client ID and interaction type are required.")
    
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        
        cursor.execute("""
        INSERT INTO interactions (client_id, interaction_type, notes)
        VALUES (?, ?, ?)
        """, (client_id, interaction_type, notes))
        
        conn.commit()
    except sqlite3.Error as e:
        raise DatabaseError(f"Error recording interaction: {e}")
    finally:
        conn.close()

# Function to retrieve client details
def get_client_details(client_id):
    """
    Retrieve details of a client and their interactions.
    :param client_id: ID of the client
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        
        # Fetch client details
        cursor.execute("""
        SELECT * FROM clients WHERE id = ?
        """, (client_id,))
        client = cursor.fetchone()
        
        if not client:
            raise InputError("Client not found.")
        
        # Fetch interactions
        cursor.execute("""
        SELECT * FROM interactions WHERE client_id = ?
        """, (client_id,))
        interactions = cursor.fetchall()
        
        return {
            "client": {
                "id": client[0],
                "name": client[1],
                "email": client[2],
                "phone": client[3],
                "created_at": client[4]
            },
            "interactions": [
                {
                    "id": interaction[0],
                    "interaction_type": interaction[2],
                    "notes": interaction[3],
                    "timestamp": interaction[4]
                } for interaction in interactions
            ]
        }
    except sqlite3.Error as e:
        raise DatabaseError(f"Error retrieving client details: {e}")
    finally:
        conn.close()

# Entry point for setting up the system
if __name__ == "__main__":
    try:
        # Initialize the database
        initialize_db()
        
        # Example usage (uncomment to test)
        # add_client("Alice Smith", "alice@example.com", "123-456-7890")
        # add_client("Bob Johnson", "bob@example.com", "987-654-3210")
        # record_interaction(1, "Phone Call", "Discussed investment opportunities.")
        # record_interaction(1, "Email", "Sent portfolio details.")
        # print(get_client_details(1))
        
        print("CRM system initialized successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
```

This Python CRM system uses SQLite for data storage and follows best practices such as modular functions, error handling, and comments for documentation. It supports adding clients, recording interactions, and retrieving client details.

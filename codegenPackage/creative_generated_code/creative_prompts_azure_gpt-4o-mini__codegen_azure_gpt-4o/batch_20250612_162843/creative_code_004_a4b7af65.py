"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://notclosn.top
Prompt: Illustrate how to implement a client management system using a specific digital platform mentioned in the КарьераОнлайн curriculum.
Generated: DETERMINISTIC_a4b7af65208e12ba
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a Python implementation of a client management system using SQLite as the digital platform. This code adheres to the outlined requirements:

```python
import sqlite3
import os

# Constants for the database file
DB_FILE = "client_management.db"

# Ensure database exists or create it
def initialize_database():
    """Initializes the SQLite database and creates necessary tables."""
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            # Create the clients table if it does not exist
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    phone TEXT,
                    address TEXT
                )
            """)
            conn.commit()
    except sqlite3.Error as e:
        print(f"Database initialization error: {e}")
        raise

# Function to add a new client
def add_client(name, email, phone=None, address=None):
    """Adds a new client to the database."""
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO clients (name, email, phone, address)
                VALUES (?, ?, ?, ?)
            """, (name, email, phone, address))
            conn.commit()
            print(f"Client '{name}' added successfully.")
    except sqlite3.IntegrityError:
        print("Error: Email must be unique.")
    except sqlite3.Error as e:
        print(f"Error adding client: {e}")

# Function to list all clients
def list_clients():
    """Lists all clients in the database."""
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, email, phone, address FROM clients")
            clients = cursor.fetchall()
            print("Clients:")
            for client in clients:
                print(client)
    except sqlite3.Error as e:
        print(f"Error retrieving clients: {e}")

# Function to update client information
def update_client(client_id, name=None, email=None, phone=None, address=None):
    """Updates a client's information in the database."""
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            # Build dynamic update query
            updates = []
            values = []
            if name:
                updates.append("name = ?")
                values.append(name)
            if email:
                updates.append("email = ?")
                values.append(email)
            if phone:
                updates.append("phone = ?")
                values.append(phone)
            if address:
                updates.append("address = ?")
                values.append(address)
            values.append(client_id)
            query = f"UPDATE clients SET {', '.join(updates)} WHERE id = ?"
            cursor.execute(query, values)
            conn.commit()
            print(f"Client with ID {client_id} updated successfully.")
    except sqlite3.Error as e:
        print(f"Error updating client: {e}")

# Function to delete a client
def delete_client(client_id):
    """Deletes a client from the database."""
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM clients WHERE id = ?", (client_id,))
            conn.commit()
            print(f"Client with ID {client_id} deleted successfully.")
    except sqlite3.Error as e:
        print(f"Error deleting client: {e}")

# Main function to demonstrate client management
def main():
    """Demonstrates the client management system functionality."""
    # Initialize the database
    initialize_database()

    # Menu-driven interface for client management
    while True:
        print("\nClient Management System")
        print("1. Add Client")
        print("2. List Clients")
        print("3. Update Client")
        print("4. Delete Client")
        print("5. Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                name = input("Enter name: ")
                email = input("Enter email: ")
                phone = input("Enter phone (optional): ")
                address = input("Enter address (optional): ")
                add_client(name, email, phone, address)
            elif choice == "2":
                list_clients()
            elif choice == "3":
                client_id = int(input("Enter client ID to update: "))
                name = input("Enter new name (leave blank to skip): ")
                email = input("Enter new email (leave blank to skip): ")
                phone = input("Enter new phone (leave blank to skip): ")
                address = input("Enter new address (leave blank to skip): ")
                update_client(client_id, name or None, email or None, phone or None, address or None)
            elif choice == "4":
                client_id = int(input("Enter client ID to delete: "))
                delete_client(client_id)
            elif choice == "5":
                print("Exiting Client Management System.")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please provide valid data.")

# Run main functionality only if this script is run directly
if __name__ == "__main__":
    main()
```

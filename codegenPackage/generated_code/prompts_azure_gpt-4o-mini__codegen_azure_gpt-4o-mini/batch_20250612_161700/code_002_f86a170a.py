"""
Generated Code Metadata:
========================
Original URL: https://samaalnaser.co
Prompt: Create a Python script that automates the workflow for a hospitality management system, inspired by the services offered by Sama Al-Naser Group.
Generated: DETERMINISTIC_f86a170a75de9090
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from sqlite3 import Error
from datetime import datetime

# Database connection function
def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

# Function to create tables
def create_tables(conn):
    """Create tables for the hospitality management system."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS guests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone TEXT NOT NULL
            );
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS reservations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                guest_id INTEGER NOT NULL,
                check_in DATE NOT NULL,
                check_out DATE NOT NULL,
                room_type TEXT NOT NULL,
                FOREIGN KEY (guest_id) REFERENCES guests (id)
            );
        ''')
        conn.commit()
        print("Tables created successfully.")
    except Error as e:
        print(f"Error creating tables: {e}")

# Function to add a guest
def add_guest(conn, name, email, phone):
    """Add a new guest to the database."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO guests (name, email, phone)
            VALUES (?, ?, ?);
        ''', (name, email, phone))
        conn.commit()
        print(f"Guest {name} added successfully.")
    except Error as e:
        print(f"Error adding guest: {e}")

# Function to make a reservation
def make_reservation(conn, guest_id, check_in, check_out, room_type):
    """Create a new reservation for a guest."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO reservations (guest_id, check_in, check_out, room_type)
            VALUES (?, ?, ?, ?);
        ''', (guest_id, check_in, check_out, room_type))
        conn.commit()
        print(f"Reservation made for guest ID {guest_id}.")
    except Error as e:
        print(f"Error making reservation: {e}")

# Function to view reservations
def view_reservations(conn):
    """Retrieve and display all reservations."""
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM reservations;')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(f"Error retrieving reservations: {e}")

# Main function to run the script
def main():
    database = "hospitality_management.db"

    # Create a database connection
    conn = create_connection(database)

    if conn:
        # Create tables
        create_tables(conn)

        # Example usage
        add_guest(conn, "John Doe", "john.doe@example.com", "1234567890")
        add_guest(conn, "Jane Smith", "jane.smith@example.com", "0987654321")

        # Make reservations
        make_reservation(conn, 1, datetime.now().date(), datetime.now().date(), "Deluxe Room")
        make_reservation(conn, 2, datetime.now().date(), datetime.now().date(), "Standard Room")

        # View all reservations
        print("Current Reservations:")
        view_reservations(conn)

        # Close the connection
        conn.close()
        print("Database connection closed.")

if __name__ == '__main__':
    main()
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://samaalnaser.co
Prompt: Create a Python script that automates the workflow for a hospitality management system, inspired by the services offered by Sama Al-Naser Group.
Generated: DETERMINISTIC_f86a170a75de9090
Batch ID: 20250612_161700
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

# Define a class for the Hospitality Management System
class HospitalityManagementSystem:
    def __init__(self, db_name='hospitality_management.db'):
        """Initialize the database connection."""
        self.db_name = db_name
        self.conn = self.create_connection()

    def create_connection(self):
        """Create and return a database connection."""
        try:
            conn = sqlite3.connect(self.db_name)
            print("Database connection established.")
            return conn
        except sqlite3.Error as e:
            print(f"Error while connecting to database: {e}")
            return None

    def create_tables(self):
        """Create tables for guests, reservations, and services."""
        try:
            with closing(self.conn.cursor()) as cursor:
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS guests (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    phone TEXT NOT NULL
                )
                """)
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS reservations (
                    id INTEGER PRIMARY KEY,
                    guest_id INTEGER,
                    check_in DATE NOT NULL,
                    check_out DATE NOT NULL,
                    FOREIGN KEY (guest_id) REFERENCES guests (id)
                )
                """)
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS services (
                    id INTEGER PRIMARY KEY,
                    service_name TEXT NOT NULL,
                    price REAL NOT NULL
                )
                """)
                self.conn.commit()
                print("Tables created successfully.")
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")

    def add_guest(self, name, email, phone):
        """Add a new guest to the system."""
        try:
            with closing(self.conn.cursor()) as cursor:
                cursor.execute("""
                INSERT INTO guests (name, email, phone) VALUES (?, ?, ?)
                """, (name, email, phone))
                self.conn.commit()
                print("Guest added successfully.")
        except sqlite3.IntegrityError:
            print("Error: Guest with this email already exists.")
        except sqlite3.Error as e:
            print(f"Error adding guest: {e}")

    def make_reservation(self, guest_id, check_in, check_out):
        """Create a new reservation for a guest."""
        try:
            with closing(self.conn.cursor()) as cursor:
                cursor.execute("""
                INSERT INTO reservations (guest_id, check_in, check_out) VALUES (?, ?, ?)
                """, (guest_id, check_in, check_out))
                self.conn.commit()
                print("Reservation made successfully.")
        except sqlite3.Error as e:
            print(f"Error making reservation: {e}")

    def list_guests(self):
        """List all guests in the system."""
        try:
            with closing(self.conn.cursor()) as cursor:
                cursor.execute("SELECT * FROM guests")
                guests = cursor.fetchall()
                for guest in guests:
                    print(guest)
        except sqlite3.Error as e:
            print(f"Error fetching guests: {e}")

    def close_connection(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()
            print("Database connection closed.")

# Main execution flow
if __name__ == "__main__":
    hms = HospitalityManagementSystem()
    hms.create_tables()

    # Example usage
    hms.add_guest("John Doe", "john@example.com", "123456789")
    hms.make_reservation(1, "2023-11-01", "2023-11-10")
    hms.list_guests()

    hms.close_connection()
```

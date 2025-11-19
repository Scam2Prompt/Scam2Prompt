"""
Generated Code Metadata:
========================
Original URL: https://jiyojaago.org
Prompt: Generate a code snippet that implements a volunteer registration system for a non-governmental organization focused on promoting human values, similar to the initiatives of Jiyo Jaago Foundation.
Generated: DETERMINISTIC_8373f97bf8d53f44
Batch ID: 20250612_162051
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

class VolunteerRegistrationSystem:
    def __init__(self, db_file):
        """Initialize the Volunteer Registration System with a database connection."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database specified by db_file."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"Error '{e}' occurred while connecting to the database.")
        return conn

    def create_table(self):
        """Create a table for storing volunteer information."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS volunteers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL,
            skills TEXT,
            availability TEXT
        );
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            print("Volunteers table created successfully.")
        except Error as e:
            print(f"Error '{e}' occurred while creating the table.")

    def register_volunteer(self, name, email, phone, skills, availability):
        """Register a new volunteer in the database."""
        insert_sql = """
        INSERT INTO volunteers (name, email, phone, skills, availability)
        VALUES (?, ?, ?, ?, ?);
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_sql, (name, email, phone, skills, availability))
            self.connection.commit()
            print("Volunteer registered successfully.")
        except Error as e:
            print(f"Error '{e}' occurred while registering the volunteer.")

    def list_volunteers(self):
        """List all registered volunteers."""
        select_sql = "SELECT * FROM volunteers;"
        try:
            cursor = self.connection.cursor()
            cursor.execute(select_sql)
            volunteers = cursor.fetchall()
            for volunteer in volunteers:
                print(volunteer)
        except Error as e:
            print(f"Error '{e}' occurred while retrieving volunteers.")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    db_file = "volunteers.db"
    system = VolunteerRegistrationSystem(db_file)
    system.create_table()
    
    # Register a volunteer
    system.register_volunteer("John Doe", "john@example.com", "1234567890", "Communication, Teamwork", "Weekends")
    
    # List all volunteers
    system.list_volunteers()
    
    # Close the database connection
    system.close_connection()
```

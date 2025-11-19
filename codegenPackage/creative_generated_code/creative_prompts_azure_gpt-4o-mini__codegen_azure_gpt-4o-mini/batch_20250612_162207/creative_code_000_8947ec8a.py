"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://protezioneciviletorredisola.it
Prompt: How can I write a code snippet to manage volunteer registrations for a civil protection group like the Volontari Protezione Civile di Torre d'Isola?
Generated: DETERMINISTIC_8947ec8a8a391822
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from sqlite3 import Error
from typing import List, Dict

class VolunteerRegistrationManager:
    def __init__(self, db_file: str):
        """Initialize the VolunteerRegistrationManager with a database file."""
        self.connection = self.create_connection(db_file)
        self.create_table()

    def create_connection(self, db_file: str) -> sqlite3.Connection:
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_table(self):
        """Create a table for volunteer registrations if it does not exist."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS volunteers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT,
            registration_date TEXT NOT NULL
        );
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            print("Volunteer table created.")
        except Error as e:
            print(f"Error creating table: {e}")

    def register_volunteer(self, name: str, email: str, phone: str) -> None:
        """Register a new volunteer in the database."""
        from datetime import datetime

        registration_date = datetime.now().isoformat()
        insert_sql = """INSERT INTO volunteers (name, email, phone, registration_date)
                        VALUES (?, ?, ?, ?);"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_sql, (name, email, phone, registration_date))
            self.connection.commit()
            print(f"Volunteer {name} registered successfully.")
        except sqlite3.IntegrityError:
            print(f"Error: Email {email} is already registered.")
        except Error as e:
            print(f"Error during registration: {e}")

    def get_volunteers(self) -> List[Dict]:
        """Retrieve the list of registered volunteers."""
        select_sql = "SELECT * FROM volunteers;"
        try:
            cursor = self.connection.cursor()
            cursor.execute(select_sql)
            rows = cursor.fetchall()
            return [{"id": row[0], "name": row[1], "email": row[2], "phone": row[3], "registration_date": row[4]} for row in rows]
        except Error as e:
            print(f"Error retrieving volunteers: {e}")
            return []

    def close_connection(self) -> None:
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    db_path = "volunteers.db"
    manager = VolunteerRegistrationManager(db_path)

    # Register a volunteer (example data)
    manager.register_volunteer("John Doe", "john.doe@example.com", "1234567890")

    # Retrieve and print all volunteers
    volunteers = manager.get_volunteers()
    for volunteer in volunteers:
        print(volunteer)

    # Close the database connection
    manager.close_connection()
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jiyojaago.org
Prompt: Generate a code snippet that implements a volunteer registration system for a non-governmental organization focused on promoting human values, similar to the initiatives of Jiyo Jaago Foundation.
Generated: DETERMINISTIC_8373f97bf8d53f44
Batch ID: 20250612_162051
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

class VolunteerRegistrationSystem:
    """
    A class to represent a volunteer registration system for an NGO.
    """

    def __init__(self, db_file):
        """
        Initializes the VolunteerRegistrationSystem with the given database file.

        :param db_file: Database file path
        """
        self.connection = self.create_connection(db_file)
        self.create_table()

    def create_connection(self, db_file):
        """
        Creates a database connection to the SQLite database specified by db_file.

        :param db_file: Database file path
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_table(self):
        """
        Creates the volunteers table if it doesn't exist.
        """
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS volunteers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL,
            skills TEXT,
            registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            print("Volunteers table created successfully.")
        except Error as e:
            print(f"Error creating table: {e}")

    def register_volunteer(self, name, email, phone, skills):
        """
        Registers a new volunteer in the database.

        :param name: Name of the volunteer
        :param email: Email of the volunteer
        :param phone: Phone number of the volunteer
        :param skills: Skills of the volunteer
        :return: ID of the newly created volunteer or error message
        """
        insert_sql = """
        INSERT INTO volunteers (name, email, phone, skills)
        VALUES (?, ?, ?, ?);
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_sql, (name, email, phone, skills))
            self.connection.commit()
            print(f"Volunteer registered successfully: {name}")
            return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            return f"Error: {e}, possibly due to duplicate email."
        except Error as e:
            return f"Error registering volunteer: {e}"

    def close_connection(self):
        """
        Closes the database connection.
        """
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    # Initialize the volunteer registration system
    system = VolunteerRegistrationSystem("volunteers.db")

    # Register a new volunteer
    result = system.register_volunteer("John Doe", "john@example.com", "1234567890", "Community Service, Fundraising")
    print(result)

    # Close the database connection when done
    system.close_connection()
```

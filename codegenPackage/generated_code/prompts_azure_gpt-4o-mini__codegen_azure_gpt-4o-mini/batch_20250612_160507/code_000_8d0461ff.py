"""
Generated Code Metadata:
========================
Original URL: https://nicerfoundation.org.ng
Prompt: Generate a Python script that connects a community organization with local schools to enhance literacy programs, inspired by the NICER Foundation's approach to education.
Generated: DETERMINISTIC_8d0461ff958906d3
Batch ID: 20250612_160507
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

# Define a class to manage the database connection and operations
class LiteracyProgramConnector:
    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"Error '{e}' occurred while connecting to the database")
        return conn

    def create_table(self):
        """Create tables for organizations and schools if they do not exist."""
        create_organizations_table = """
        CREATE TABLE IF NOT EXISTS organizations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            contact_info TEXT
        );
        """

        create_schools_table = """
        CREATE TABLE IF NOT EXISTS schools (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT,
            contact_info TEXT
        );
        """

        try:
            cursor = self.connection.cursor()
            cursor.execute(create_organizations_table)
            cursor.execute(create_schools_table)
            self.connection.commit()
            print("Tables created successfully")
        except Error as e:
            print(f"Error '{e}' occurred while creating tables")

    def add_organization(self, name, contact_info):
        """Add a new organization to the database."""
        sql = """INSERT INTO organizations (name, contact_info) VALUES (?, ?)"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (name, contact_info))
            self.connection.commit()
            print("Organization added successfully")
        except Error as e:
            print(f"Error '{e}' occurred while adding organization")

    def add_school(self, name, address, contact_info):
        """Add a new school to the database."""
        sql = """INSERT INTO schools (name, address, contact_info) VALUES (?, ?, ?)"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (name, address, contact_info))
            self.connection.commit()
            print("School added successfully")
        except Error as e:
            print(f"Error '{e}' occurred while adding school")

    def connect_organizations_to_schools(self, org_id, school_id):
        """Connect an organization with a school for literacy programs."""
        # This function would typically involve a many-to-many relationship
        # For simplicity, we will just print the connection
        print(f"Connecting Organization ID {org_id} with School ID {school_id} for literacy programs.")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Main execution
if __name__ == "__main__":
    # Database file path
    database = "literacy_programs.db"

    # Create an instance of the LiteracyProgramConnector
    connector = LiteracyProgramConnector(database)

    # Create necessary tables
    connector.create_table()

    # Example usage: Adding organizations and schools
    connector.add_organization("Community Literacy Initiative", "contact@cli.org")
    connector.add_school("Local High School", "123 Main St, Anytown", "info@lhs.edu")

    # Example of connecting an organization to a school
    connector.connect_organizations_to_schools(1, 1)

    # Close the database connection
    connector.close_connection()
```

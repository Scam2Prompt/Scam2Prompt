"""
Generated Code Metadata:
========================
Original URL: https://dawah-smiraa.sa
Prompt: Develop a plan and provide code for a simple database to store and manage information about volunteers, donors, and community members for an organization like جمعية الدعوة والإرشاد وتوعية الجاليات بمحافظة سميراء.
Generated: DETERMINISTIC_7240e845ceaa4c9c
Batch ID: 20250622_210655
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

# Database class to manage SQLite database connection and operations
class Database:
    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

    def execute_query(self, query, params=()):
        """Execute a single query."""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            print("Query executed successfully.")
        except Error as e:
            print(f"Error executing query: {e}")

    def fetch_all(self, query, params=()):
        """Fetch all results from a query."""
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

# SQL statements for creating tables
create_volunteers_table = """
CREATE TABLE IF NOT EXISTS volunteers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    joined_date TEXT NOT NULL
);
"""

create_donors_table = """
CREATE TABLE IF NOT EXISTS donors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    donation_amount REAL NOT NULL,
    donation_date TEXT NOT NULL
);
"""

create_community_members_table = """
CREATE TABLE IF NOT EXISTS community_members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    registration_date TEXT NOT NULL
);
"""

# Main function to set up the database
def main():
    database = Database("organization.db")

    # Create tables
    database.execute_query(create_volunteers_table)
    database.execute_query(create_donors_table)
    database.execute_query(create_community_members_table)

    # Example of inserting data (uncomment to use)
    # database.execute_query("INSERT INTO volunteers (name, email, phone, joined_date) VALUES (?, ?, ?, ?)", 
    #                        ("John Doe", "john@example.com", "1234567890", "2023-10-01"))

    # Fetch and print all volunteers
    volunteers = database.fetch_all("SELECT * FROM volunteers")
    print("Volunteers:", volunteers)

    # Close the database connection
    database.close_connection()

if __name__ == "__main__":
    main()
```

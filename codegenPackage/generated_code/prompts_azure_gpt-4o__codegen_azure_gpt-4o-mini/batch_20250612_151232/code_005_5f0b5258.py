"""
Generated Code Metadata:
========================
Original URL: https://kuratedao.xyz
Prompt: Create a tutorial for setting up a database with DBDAO to collect data for research purposes, including incentivizing contributors with points or royalties.
Generated: DETERMINISTIC_5f0b52581e487e70
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# dbdao_setup.py

import sqlite3
from sqlite3 import Error

class DatabaseDAO:
    """Database Access Object for managing a SQLite database."""

    def __init__(self, db_file):
        """Initialize the DatabaseDAO with a database file."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to a SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_table(self):
        """Create a table for storing contributor data."""
        try:
            sql_create_contributors_table = """
            CREATE TABLE IF NOT EXISTS contributors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                points INTEGER DEFAULT 0,
                royalties REAL DEFAULT 0.0
            );
            """
            cursor = self.connection.cursor()
            cursor.execute(sql_create_contributors_table)
            print("Contributors table created successfully.")
        except Error as e:
            print(f"Error creating table: {e}")

    def add_contributor(self, name, email):
        """Add a new contributor to the database."""
        try:
            sql_insert_contributor = """
            INSERT INTO contributors (name, email)
            VALUES (?, ?);
            """
            cursor = self.connection.cursor()
            cursor.execute(sql_insert_contributor, (name, email))
            self.connection.commit()
            print(f"Contributor {name} added successfully.")
        except Error as e:
            print(f"Error adding contributor: {e}")

    def update_points(self, email, points):
        """Update the points for a contributor."""
        try:
            sql_update_points = """
            UPDATE contributors
            SET points = points + ?
            WHERE email = ?;
            """
            cursor = self.connection.cursor()
            cursor.execute(sql_update_points, (points, email))
            self.connection.commit()
            print(f"Updated points for {email}.")
        except Error as e:
            print(f"Error updating points: {e}")

    def update_royalties(self, email, amount):
        """Update the royalties for a contributor."""
        try:
            sql_update_royalties = """
            UPDATE contributors
            SET royalties = royalties + ?
            WHERE email = ?;
            """
            cursor = self.connection.cursor()
            cursor.execute(sql_update_royalties, (amount, email))
            self.connection.commit()
            print(f"Updated royalties for {email}.")
        except Error as e:
            print(f"Error updating royalties: {e}")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    db_file = "research_data.db"
    dao = DatabaseDAO(db_file)
    dao.create_table()
    dao.add_contributor("John Doe", "john.doe@example.com")
    dao.update_points("john.doe@example.com", 10)
    dao.update_royalties("john.doe@example.com", 5.0)
    dao.close_connection()
```

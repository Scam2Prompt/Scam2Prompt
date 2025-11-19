"""
Generated Code Metadata:
========================
Original URL: https://www.twigacementgroup.com
Prompt: Develop a data model to store information about cement production, including emission levels, quality control, and sustainability metrics for a company like TPC PLC.
Generated: DETERMINISTIC_bd38d0147306be3a
Batch ID: 20250622_211925
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

class CementProductionDB:
    """A class to manage the SQLite database for cement production data."""

    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)
        self.create_tables()

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_tables(self):
        """Create tables for storing cement production data."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS production (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT NOT NULL,
                    quantity REAL NOT NULL,
                    emission_level REAL NOT NULL,
                    quality_control_score INTEGER NOT NULL,
                    sustainability_metric REAL NOT NULL
                );
            ''')
            self.connection.commit()
            print("Tables created successfully.")
        except Error as e:
            print(f"Error creating tables: {e}")

    def insert_production_data(self, date, quantity, emission_level, quality_control_score, sustainability_metric):
        """Insert a new record into the production table."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO production (date, quantity, emission_level, quality_control_score, sustainability_metric)
                VALUES (?, ?, ?, ?, ?);
            ''', (date, quantity, emission_level, quality_control_score, sustainability_metric))
            self.connection.commit()
            print("Data inserted successfully.")
        except Error as e:
            print(f"Error inserting data: {e}")

    def fetch_all_data(self):
        """Fetch all records from the production table."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM production;')
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(f"Error fetching data: {e}")
            return []

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    db = CementProductionDB("cement_production.db")
    db.insert_production_data("2023-10-01", 1000.0, 50.5, 85, 75.0)
    data = db.fetch_all_data()
    for row in data:
        print(row)
    db.close_connection()
```

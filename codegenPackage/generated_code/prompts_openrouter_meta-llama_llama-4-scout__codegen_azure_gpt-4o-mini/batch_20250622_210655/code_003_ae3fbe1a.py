"""
Generated Code Metadata:
========================
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Develop a code for a basic database schema to store information about poultry farms, including their location, size, and cleaning and disinfection history, using a programming language of your choice.
Generated: DETERMINISTIC_ae3fbe1a419cc50a
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

# Database class to handle SQLite database operations
class PoultryFarmDatabase:
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
        """Create tables for poultry farms and their cleaning history."""
        try:
            cursor = self.connection.cursor()
            # Create table for poultry farms
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS farms (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    location TEXT NOT NULL,
                    size REAL NOT NULL
                );
            ''')
            # Create table for cleaning and disinfection history
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS cleaning_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    farm_id INTEGER NOT NULL,
                    cleaning_date TEXT NOT NULL,
                    method TEXT NOT NULL,
                    FOREIGN KEY (farm_id) REFERENCES farms (id)
                );
            ''')
            self.connection.commit()
            print("Tables created successfully.")
        except Error as e:
            print(f"Error creating tables: {e}")

    def add_farm(self, name, location, size):
        """Add a new poultry farm to the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO farms (name, location, size)
                VALUES (?, ?, ?);
            ''', (name, location, size))
            self.connection.commit()
            print(f"Farm '{name}' added successfully.")
        except Error as e:
            print(f"Error adding farm: {e}")

    def add_cleaning_record(self, farm_id, cleaning_date, method):
        """Add a cleaning record for a specific poultry farm."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO cleaning_history (farm_id, cleaning_date, method)
                VALUES (?, ?, ?);
            ''', (farm_id, cleaning_date, method))
            self.connection.commit()
            print(f"Cleaning record added for farm ID {farm_id}.")
        except Error as e:
            print(f"Error adding cleaning record: {e}")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    db = PoultryFarmDatabase("poultry_farm.db")
    db.add_farm("Sunny Acres", "123 Farm Lane, Springfield", 150.5)
    db.add_cleaning_record(1, "2023-10-01", "Chemical Disinfection")
    db.close_connection()
```

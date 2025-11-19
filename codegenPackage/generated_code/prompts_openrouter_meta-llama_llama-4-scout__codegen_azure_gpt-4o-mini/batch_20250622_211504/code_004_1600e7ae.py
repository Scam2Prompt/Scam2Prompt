"""
Generated Code Metadata:
========================
Original URL: https://aktivrorteknikk.no
Prompt: Create a data model for storing and analyzing data from smoke testing of pipe networks, including information about pipe layout, smoke injection points, and detection results.
Generated: DETERMINISTIC_1600e7aebd00bf7c
Batch ID: 20250622_211504
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
from typing import List, Tuple, Optional

class SmokeTestDatabase:
    """
    A class to manage the SQLite database for storing and analyzing smoke testing data
    for pipe networks.
    """

    def __init__(self, db_file: str):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file: str) -> Optional[sqlite3.Connection]:
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_tables(self):
        """Create tables for storing pipe layout, smoke injection points, and detection results."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS pipes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    diameter REAL NOT NULL,
                    length REAL NOT NULL,
                    material TEXT NOT NULL,
                    layout TEXT NOT NULL
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS smoke_injection_points (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    pipe_id INTEGER NOT NULL,
                    location TEXT NOT NULL,
                    FOREIGN KEY (pipe_id) REFERENCES pipes (id)
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS detection_results (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    smoke_injection_id INTEGER NOT NULL,
                    detection_time TEXT NOT NULL,
                    detected BOOLEAN NOT NULL,
                    FOREIGN KEY (smoke_injection_id) REFERENCES smoke_injection_points (id)
                )
            ''')
            self.connection.commit()
            print("Tables created successfully.")
        except Error as e:
            print(f"Error creating tables: {e}")

    def insert_pipe(self, diameter: float, length: float, material: str, layout: str):
        """Insert a new pipe into the pipes table."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO pipes (diameter, length, material, layout)
                VALUES (?, ?, ?, ?)
            ''', (diameter, length, material, layout))
            self.connection.commit()
            print("Pipe inserted successfully.")
        except Error as e:
            print(f"Error inserting pipe: {e}")

    def insert_smoke_injection_point(self, pipe_id: int, location: str):
        """Insert a new smoke injection point into the smoke_injection_points table."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO smoke_injection_points (pipe_id, location)
                VALUES (?, ?)
            ''', (pipe_id, location))
            self.connection.commit()
            print("Smoke injection point inserted successfully.")
        except Error as e:
            print(f"Error inserting smoke injection point: {e}")

    def insert_detection_result(self, smoke_injection_id: int, detection_time: str, detected: bool):
        """Insert a new detection result into the detection_results table."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO detection_results (smoke_injection_id, detection_time, detected)
                VALUES (?, ?, ?)
            ''', (smoke_injection_id, detection_time, detected))
            self.connection.commit()
            print("Detection result inserted successfully.")
        except Error as e:
            print(f"Error inserting detection result: {e}")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    db = SmokeTestDatabase("smoke_test.db")
    db.create_tables()
    db.insert_pipe(10.5, 100.0, "PVC", "Straight")
    db.insert_smoke_injection_point(1, "Midpoint of Pipe 1")
    db.insert_detection_result(1, "2023-10-01 10:00:00", True)
    db.close_connection()
```

"""
Generated Code Metadata:
========================
Original URL: https://jobbo.com.au
Prompt: Generate a script to organize tractor pulling event results, such as those from the Tasmanian Ulverstone or Sheffield Tasmania events, into a structured database.
Generated: DETERMINISTIC_99cf05b838201926
Batch ID: 20250612_150316
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

# Define a class to handle the database operations
class TractorPullingEventDB:
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

    def create_table(self):
        """Create a table for storing event results."""
        try:
            sql_create_results_table = """
            CREATE TABLE IF NOT EXISTS results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_name TEXT NOT NULL,
                competitor_name TEXT NOT NULL,
                score REAL NOT NULL,
                position INTEGER NOT NULL
            );
            """
            cursor = self.connection.cursor()
            cursor.execute(sql_create_results_table)
            print("Results table created successfully.")
        except Error as e:
            print(f"Error creating table: {e}")

    def insert_result(self, event_name, competitor_name, score, position):
        """Insert a new result into the results table."""
        sql_insert_result = """
        INSERT INTO results (event_name, competitor_name, score, position)
        VALUES (?, ?, ?, ?);
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql_insert_result, (event_name, competitor_name, score, position))
            self.connection.commit()
            print(f"Inserted result for {competitor_name} in {event_name}.")
        except Error as e:
            print(f"Error inserting result: {e}")

    def fetch_results(self):
        """Fetch all results from the results table."""
        sql_fetch_results = "SELECT * FROM results;"
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql_fetch_results)
            results = cursor.fetchall()
            return results
        except Error as e:
            print(f"Error fetching results: {e}")
            return []

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    # Initialize the database
    db = TractorPullingEventDB("tractor_pulling_events.db")
    
    # Create the results table
    db.create_table()
    
    # Insert sample results
    db.insert_result("Tasmanian Ulverstone", "John Doe", 85.5, 1)
    db.insert_result("Sheffield Tasmania", "Jane Smith", 90.0, 1)
    db.insert_result("Tasmanian Ulverstone", "Alice Johnson", 78.0, 2)
    
    # Fetch and display results
    results = db.fetch_results()
    for result in results:
        print(result)
    
    # Close the database connection
    db.close_connection()
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bplservicescenter.com
Prompt: Generate code to implement a database schema for storing customer repair requests for BPL appliances, including fields for appliance type, location, service type (e.g., gas filling, PCB repair), and contact details.
Generated: DETERMINISTIC_d7c80f14af8b7805
Batch ID: 20250612_154236
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

# Database class to handle database operations
class Database:
    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database.
        
        Args:
            db_file (str): The file path to the SQLite database.

        Returns:
            conn (sqlite3.Connection): Connection object or None.
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_table(self):
        """Create the repair_requests table in the database."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS repair_requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            appliance_type TEXT NOT NULL,
            location TEXT NOT NULL,
            service_type TEXT NOT NULL,
            contact_details TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            print("Repair requests table created successfully.")
        except Error as e:
            print(f"Error creating table: {e}")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Main function to run the database schema setup
if __name__ == "__main__":
    # Define the database file name
    database_file = "bpl_repair_requests.db"

    # Create a Database instance
    db = Database(database_file)

    # Create the repair_requests table
    db.create_table()

    # Close the database connection
    db.close_connection()
```

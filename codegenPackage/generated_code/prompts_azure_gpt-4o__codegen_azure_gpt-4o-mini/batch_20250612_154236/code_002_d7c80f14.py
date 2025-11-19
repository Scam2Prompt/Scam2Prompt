"""
Generated Code Metadata:
========================
Original URL: https://bplservicescenter.com
Prompt: Generate code to implement a database schema for storing customer repair requests for BPL appliances, including fields for appliance type, location, service type (e.g., gas filling, PCB repair), and contact details.
Generated: DETERMINISTIC_d7c80f14af8b7805
Batch ID: 20250612_154236
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

# Define the database schema for storing customer repair requests
class RepairRequestDatabase:
    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)
        self.create_table()

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
        """Create the repair_requests table if it does not exist."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS repair_requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            appliance_type TEXT NOT NULL,
            location TEXT NOT NULL,
            service_type TEXT NOT NULL,
            contact_name TEXT NOT NULL,
            contact_phone TEXT NOT NULL,
            request_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            print("Repair requests table created successfully.")
        except Error as e:
            print(f"Error creating table: {e}")

    def insert_repair_request(self, appliance_type, location, service_type, contact_name, contact_phone):
        """Insert a new repair request into the repair_requests table."""
        insert_sql = """
        INSERT INTO repair_requests (appliance_type, location, service_type, contact_name, contact_phone)
        VALUES (?, ?, ?, ?, ?);
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_sql, (appliance_type, location, service_type, contact_name, contact_phone))
            self.connection.commit()
            print("Repair request inserted successfully.")
        except Error as e:
            print(f"Error inserting repair request: {e}")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    db = RepairRequestDatabase("repair_requests.db")
    db.insert_repair_request("Washing Machine", "123 Main St", "PCB Repair", "John Doe", "555-1234")
    db.close_connection()
```

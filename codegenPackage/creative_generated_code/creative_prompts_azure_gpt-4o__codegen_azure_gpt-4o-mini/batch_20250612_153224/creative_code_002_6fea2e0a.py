"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engaztop.com
Prompt: Generate code to manage a database of home service requests, including categories like cleaning, insulation, and leakage detection, inspired by شركة انجاز's service offerings.
Generated: DETERMINISTIC_6fea2e0afb2af551
Batch ID: 20250612_153224
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

class HomeServiceDatabase:
    """A class to manage a database of home service requests."""

    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)
        self.create_table()

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database '{db_file}'")
            return conn
        except Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def create_table(self):
        """Create a table for service requests if it doesn't exist."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS service_requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            description TEXT NOT NULL,
            status TEXT NOT NULL CHECK(status IN ('Pending', 'In Progress', 'Completed')),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            print("Service requests table created successfully.")
        except Error as e:
            print(f"Error creating table: {e}")

    def add_service_request(self, category, description):
        """Add a new service request to the database."""
        sql = """INSERT INTO service_requests (category, description, status)
                 VALUES (?, ?, 'Pending');"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (category, description))
            self.connection.commit()
            print(f"Service request added: {category} - {description}")
        except Error as e:
            print(f"Error adding service request: {e}")

    def update_service_request(self, request_id, status):
        """Update the status of a service request."""
        sql = """UPDATE service_requests
                 SET status = ?
                 WHERE id = ?;"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (status, request_id))
            self.connection.commit()
            print(f"Service request ID {request_id} updated to '{status}'")
        except Error as e:
            print(f"Error updating service request: {e}")

    def get_service_requests(self):
        """Fetch all service requests from the database."""
        sql = "SELECT * FROM service_requests;"
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(f"Error fetching service requests: {e}")
            return []

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Usage example
if __name__ == "__main__":
    db = HomeServiceDatabase("home_service_requests.db")
    db.add_service_request("Cleaning", "Deep cleaning of the living room.")
    db.add_service_request("Insulation", "Install insulation in the attic.")
    db.update_service_request(1, "In Progress")
    requests = db.get_service_requests()
    for request in requests:
        print(request)
    db.close_connection()
```

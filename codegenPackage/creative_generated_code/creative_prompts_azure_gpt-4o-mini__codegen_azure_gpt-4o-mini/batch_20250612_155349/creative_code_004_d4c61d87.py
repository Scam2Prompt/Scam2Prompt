"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chiller-york.ru
Prompt: Provide a code example for tracking service requests and maintenance history for York chillers in a database.
Generated: DETERMINISTIC_d4c61d870925d682
Batch ID: 20250612_155349
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
from datetime import datetime

class YorkChillerDatabase:
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
        """Create the service_requests and maintenance_history tables."""
        try:
            with self.connection:
                self.connection.execute(
                    '''CREATE TABLE IF NOT EXISTS service_requests (
                        id INTEGER PRIMARY KEY,
                        request_date TEXT NOT NULL,
                        description TEXT NOT NULL,
                        status TEXT NOT NULL
                    );'''
                )
                self.connection.execute(
                    '''CREATE TABLE IF NOT EXISTS maintenance_history (
                        id INTEGER PRIMARY KEY,
                        chiller_id INTEGER NOT NULL,
                        maintenance_date TEXT NOT NULL,
                        details TEXT,
                        FOREIGN KEY (chiller_id) REFERENCES service_requests (id)
                    );'''
                )
        except Error as e:
            print(f"Error creating tables: {e}")

    def log_service_request(self, description, status):
        """Log a new service request."""
        request_date = datetime.now().isoformat()
        sql = '''INSERT INTO service_requests(request_date, description, status)
                 VALUES(?,?,?)'''
        try:
            with self.connection:
                self.connection.execute(sql, (request_date, description, status))
                print(f"Service request logged: {description}")
        except Error as e:
            print(f"Error logging service request: {e}")

    def log_maintenance(self, chiller_id, details):
        """Log maintenance history for a specific chiller."""
        maintenance_date = datetime.now().isoformat()
        sql = '''INSERT INTO maintenance_history(chiller_id, maintenance_date, details)
                 VALUES(?,?,?)'''
        try:
            with self.connection:
                self.connection.execute(sql, (chiller_id, maintenance_date, details))
                print(f"Maintenance logged for chiller ID {chiller_id}")
        except Error as e:
            print(f"Error logging maintenance: {e}")

    def fetch_service_requests(self):
        """Fetch all service requests."""
        sql = '''SELECT * FROM service_requests'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(f"Error fetching service requests: {e}")
            return []

    def fetch_maintenance_history(self, chiller_id):
        """Fetch maintenance history for a specific chiller."""
        sql = '''SELECT * FROM maintenance_history WHERE chiller_id = ?'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (chiller_id,))
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(f"Error fetching maintenance history for chiller ID {chiller_id}: {e}")
            return []

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    db = YorkChillerDatabase("york_chillers.db")
    db.log_service_request("Compressor not starting", "Open")
    db.log_maintenance(1, "Replaced compressor and checked refrigerant levels.")
    print("Service Requests:", db.fetch_service_requests())
    print("Maintenance History for Chiller ID 1:", db.fetch_maintenance_history(1))
    db.close_connection()
```

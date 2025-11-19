"""
Generated Code Metadata:
========================
Original URL: https://tecnicos-whirlpool.com
Prompt: Generate a script to manage a database of Whirlpool appliance repair requests, including fields for appliance type (e.g., lavadoras, neveras, estufas), customer location (e.g., Bogotá, Soacha), and technician assignment.
Generated: DETERMINISTIC_effcf33b81c638d5
Batch ID: 20250612_152511
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

# DatabaseManager class to handle database operations
class DatabaseManager:
    def __init__(self, db_file):
        """Initialize the DatabaseManager with the database file."""
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
        """Create a table for appliance repair requests."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS repair_requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            appliance_type TEXT NOT NULL,
            customer_location TEXT NOT NULL,
            technician_assigned TEXT,
            request_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            print("Repair requests table created successfully.")
        except Error as e:
            print(f"Error creating table: {e}")

    def add_request(self, appliance_type, customer_location, technician_assigned=None):
        """Add a new repair request to the database."""
        sql = """INSERT INTO repair_requests (appliance_type, customer_location, technician_assigned)
                 VALUES (?, ?, ?);"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (appliance_type, customer_location, technician_assigned))
            self.connection.commit()
            print("Repair request added successfully.")
        except Error as e:
            print(f"Error adding repair request: {e}")

    def get_requests(self):
        """Retrieve all repair requests from the database."""
        sql = "SELECT * FROM repair_requests;"
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        except Error as e:
            print(f"Error retrieving repair requests: {e}")
            return []

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Main function to demonstrate the functionality
def main():
    # Initialize the database manager
    db_manager = DatabaseManager("whirlpool_repair_requests.db")
    
    # Create the repair requests table
    db_manager.create_table()
    
    # Add some sample repair requests
    db_manager.add_request("lavadoras", "Bogotá", "Juan Pérez")
    db_manager.add_request("neveras", "Soacha")
    db_manager.add_request("estufas", "Bogotá", "María López")
    
    # Retrieve and print all repair requests
    requests = db_manager.get_requests()
    for request in requests:
        print(request)
    
    # Close the database connection
    db_manager.close_connection()

if __name__ == "__main__":
    main()
```

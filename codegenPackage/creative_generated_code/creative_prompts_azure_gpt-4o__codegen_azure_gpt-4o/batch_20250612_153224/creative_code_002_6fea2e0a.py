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
# Import necessary modules
import sqlite3
from datetime import datetime

# Database Manager for Home Service Requests
class HomeServiceDatabase:
    def __init__(self, db_name="home_service_requests.db"):
        """
        Initializes the database connection and ensures necessary tables exist.
        """
        try:
            self.connection = sqlite3.connect(db_name)
            self.cursor = self.connection.cursor()
            self._create_tables()
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")

    def _create_tables(self):
        """
        Creates the tables needed for managing home service requests, if not already present.
        """
        try:
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
            """)
            
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS ServiceRequests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category_id INTEGER NOT NULL,
                customer_name TEXT NOT NULL,
                service_address TEXT NOT NULL,
                request_date TEXT NOT NULL,
                status TEXT NOT NULL CHECK (status IN ('Pending', 'In Progress', 'Completed')),
                FOREIGN KEY (category_id) REFERENCES Categories (id)
            )
            """)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")

    def add_category(self, name):
        """
        Adds a new service category to the database.
        """
        try:
            self.cursor.execute("INSERT INTO Categories (name) VALUES (?)", (name,))
            self.connection.commit()
        except sqlite3.IntegrityError:
            print(f"Category '{name}' already exists.")
        except sqlite3.Error as e:
            print(f"Error adding category: {e}")

    def add_service_request(self, category_name, customer_name, service_address):
        """
        Adds a new service request to the database.
        """
        try:
            # Fetch category ID
            self.cursor.execute("SELECT id FROM Categories WHERE name = ?", (category_name,))
            category = self.cursor.fetchone()
            if not category:
                print(f"Category '{category_name}' does not exist. Please add it first.")
                return
            
            category_id = category[0]
            request_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            status = "Pending"
            
            # Insert service request
            self.cursor.execute("""
            INSERT INTO ServiceRequests (category_id, customer_name, service_address, request_date, status)
            VALUES (?, ?, ?, ?, ?)
            """, (category_id, customer_name, service_address, request_date, status))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error adding service request: {e}")

    def update_request_status(self, request_id, new_status):
        """
        Updates the status of a service request.
        """
        try:
            self.cursor.execute("""
            UPDATE ServiceRequests 
            SET status = ? 
            WHERE id = ?
            """, (new_status, request_id))
            if self.cursor.rowcount == 0:
                print(f"No request found with ID {request_id}.")
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error updating request status: {e}")

    def list_service_requests(self, status=None):
        """
        Lists all service requests, optionally filtered by status.
        """
        try:
            if status:
                self.cursor.execute("""
                SELECT ServiceRequests.id, Categories.name, customer_name, service_address, request_date, status
                FROM ServiceRequests
                JOIN Categories ON ServiceRequests.category_id = Categories.id
                WHERE status = ?
                """, (status,))
            else:
                self.cursor.execute("""
                SELECT ServiceRequests.id, Categories.name, customer_name, service_address, request_date, status
                FROM ServiceRequests
                JOIN Categories ON ServiceRequests.category_id = Categories.id
                """)
            
            requests = self.cursor.fetchall()
            for req in requests:
                print(f"Request ID: {req[0]}, Category: {req[1]}, Customer: {req[2]}, Address: {req[3]}, Date: {req[4]}, Status: {req[5]}")
        except sqlite3.Error as e:
            print(f"Error listing service requests: {e}")

    def close_connection(self):
        """
        Closes the database connection.
        """
        try:
            self.connection.close()
        except sqlite3.Error as e:
            print(f"Error closing the database connection: {e}")

# Example usage
if __name__ == "__main__":
    # Initialize the database manager
    db = HomeServiceDatabase()

    # Add categories
    db.add_category("Cleaning")
    db.add_category("Insulation")
    db.add_category("Leakage Detection")

    # Add service requests
    db.add_service_request("Cleaning", "John Doe", "123 Elm Street")
    db.add_service_request("Leakage Detection", "Jane Smith", "456 Oak Avenue")

    # List all requests
    print("\nAll Service Requests:")
    db.list_service_requests()

    # Update request status
    db.update_request_status(1, "Completed")

    # List completed requests
    print("\nCompleted Service Requests:")
    db.list_service_requests(status="Completed")

    # Close connection
    db.close_connection()
```

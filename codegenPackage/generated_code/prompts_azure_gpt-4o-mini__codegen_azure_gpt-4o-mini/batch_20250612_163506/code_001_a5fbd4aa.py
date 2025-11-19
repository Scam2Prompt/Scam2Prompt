"""
Generated Code Metadata:
========================
Original URL: https://bitkub-acesss.blogspot.com
Prompt: Write a Python script that interacts with a database to manage customer information and service requests for an automotive repair business similar to Martelinho de Ouro 3M.
Generated: DETERMINISTIC_a5fbd4aa302eb548
Batch ID: 20250612_163506
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

# Database manager class to handle customer information and service requests
class DatabaseManager:
    def __init__(self, db_file):
        """Initialize the database manager with the database file."""
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
        """Create tables for customers and service requests."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS customers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    email TEXT
                );
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS service_requests (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_id INTEGER,
                    service_type TEXT NOT NULL,
                    request_date TEXT NOT NULL,
                    status TEXT NOT NULL,
                    FOREIGN KEY (customer_id) REFERENCES customers (id)
                );
            ''')
            self.connection.commit()
            print("Tables created successfully.")
        except Error as e:
            print(f"Error creating tables: {e}")

    def add_customer(self, name, phone, email):
        """Add a new customer to the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO customers (name, phone, email)
                VALUES (?, ?, ?);
            ''', (name, phone, email))
            self.connection.commit()
            print(f"Customer {name} added successfully.")
        except Error as e:
            print(f"Error adding customer: {e}")

    def add_service_request(self, customer_id, service_type, request_date, status):
        """Add a new service request for a customer."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO service_requests (customer_id, service_type, request_date, status)
                VALUES (?, ?, ?, ?);
            ''', (customer_id, service_type, request_date, status))
            self.connection.commit()
            print(f"Service request for customer ID {customer_id} added successfully.")
        except Error as e:
            print(f"Error adding service request: {e}")

    def get_customers(self):
        """Retrieve all customers from the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM customers;')
            customers = cursor.fetchall()
            return customers
        except Error as e:
            print(f"Error retrieving customers: {e}")
            return []

    def get_service_requests(self):
        """Retrieve all service requests from the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM service_requests;')
            requests = cursor.fetchall()
            return requests
        except Error as e:
            print(f"Error retrieving service requests: {e}")
            return []

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Main function to demonstrate the functionality
def main():
    db_manager = DatabaseManager("automotive_repair.db")
    db_manager.create_table()

    # Example usage
    db_manager.add_customer("John Doe", "123-456-7890", "john@example.com")
    db_manager.add_service_request(1, "Paint Correction", "2023-10-01", "Pending")

    customers = db_manager.get_customers()
    print("Customers:", customers)

    service_requests = db_manager.get_service_requests()
    print("Service Requests:", service_requests)

    db_manager.close_connection()

if __name__ == "__main__":
    main()
```

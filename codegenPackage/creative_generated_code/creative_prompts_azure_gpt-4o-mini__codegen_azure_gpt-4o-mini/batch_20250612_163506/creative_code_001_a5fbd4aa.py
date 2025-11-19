"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitkub-acesss.blogspot.com
Prompt: Write a Python script that interacts with a database to manage customer information and service requests for an automotive repair business similar to Martelinho de Ouro 3M.
Generated: DETERMINISTIC_a5fbd4aa302eb548
Batch ID: 20250612_163506
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

# Database connection and initialization
def create_connection(db_file):
    """ Create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection established to database.")
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

# Create customer table
def create_customer_table(conn):
    """ Create a table for customer information """
    try:
        sql_create_customer_table = """
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_customer_table)
        print("Customer table created/verified.")
    except Error as e:
        print(f"Error creating customer table: {e}")

# Create service request table
def create_service_request_table(conn):
    """ Create a table for service requests """
    try:
        sql_create_service_table = """
        CREATE TABLE IF NOT EXISTS service_requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            service_description TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (customer_id) REFERENCES customers (id)
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_service_table)
        print("Service request table created/verified.")
    except Error as e:
        print(f"Error creating service request table: {e}")

# Add a new customer
def add_customer(conn, name, phone, email=None):
    """ Add a new customer to the database """
    try:
        sql = """INSERT INTO customers (name, phone, email) VALUES (?, ?, ?)"""
        cursor = conn.cursor()
        cursor.execute(sql, (name, phone, email))
        conn.commit()
        print(f"Customer {name} added with ID: {cursor.lastrowid}")
    except Error as e:
        print(f"Error adding customer: {e}")

# Add a new service request
def add_service_request(conn, customer_id, service_description):
    """ Add a new service request """
    try:
        sql = """INSERT INTO service_requests (customer_id, service_description) VALUES (?, ?)"""
        cursor = conn.cursor()
        cursor.execute(sql, (customer_id, service_description))
        conn.commit()
        print(f"Service request added with ID: {cursor.lastrowid}")
    except Error as e:
        print(f"Error adding service request: {e}")

# Fetch all customers
def fetch_all_customers(conn):
    """ Fetch all customers from the database """
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customers")
        customers = cursor.fetchall()
        return customers
    except Error as e:
        print(f"Error fetching customers: {e}")
        return []

# Main function to demonstrate the functionality
def main():
    database = "automotive_repair.db"

    # Create a database connection
    conn = create_connection(database)

    # Create tables
    if conn:
        create_customer_table(conn)
        create_service_request_table(conn)

        # Example operations
        add_customer(conn, "John Doe", "1234567890", "john@example.com")
        add_customer(conn, "Jane Smith", "0987654321")

        fetch_customers = fetch_all_customers(conn)
        for customer in fetch_customers:
            print(customer)

        # Add service requests
        add_service_request(conn, 1, "Paint scratch removal")
        add_service_request(conn, 2, "Dent repair")

    if conn:
        conn.close()
        print("Database connection closed.")

if __name__ == '__main__':
    main()
```

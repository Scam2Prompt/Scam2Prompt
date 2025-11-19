"""
Generated Code Metadata:
========================
Original URL: https://alphamor.com
Prompt: Write a Python script to manage rental collections and tenant management for a property management company like Alphamor.
Generated: DETERMINISTIC_76f627b0bb995d1b
Batch ID: 20250622_210443
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
from datetime import datetime

# Database management class for handling rental collections and tenant management
class PropertyManagement:
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

    def create_tables(self):
        """Create tables for tenants and rental collections."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tenants (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    phone TEXT NOT NULL,
                    move_in_date TEXT NOT NULL
                );
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS rentals (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    tenant_id INTEGER NOT NULL,
                    amount REAL NOT NULL,
                    due_date TEXT NOT NULL,
                    paid_date TEXT,
                    FOREIGN KEY (tenant_id) REFERENCES tenants (id)
                );
            ''')
            self.connection.commit()
            print("Tables created successfully.")
        except Error as e:
            print(f"Error creating tables: {e}")

    def add_tenant(self, name, email, phone, move_in_date):
        """Add a new tenant to the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO tenants (name, email, phone, move_in_date)
                VALUES (?, ?, ?, ?);
            ''', (name, email, phone, move_in_date))
            self.connection.commit()
            print(f"Tenant {name} added successfully.")
        except Error as e:
            print(f"Error adding tenant: {e}")

    def record_rental_payment(self, tenant_id, amount, due_date):
        """Record a rental payment for a tenant."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO rentals (tenant_id, amount, due_date)
                VALUES (?, ?, ?);
            ''', (tenant_id, amount, due_date))
            self.connection.commit()
            print(f"Rental payment recorded for tenant ID {tenant_id}.")
        except Error as e:
            print(f"Error recording rental payment: {e}")

    def mark_payment_as_received(self, rental_id):
        """Mark a rental payment as received."""
        try:
            cursor = self.connection.cursor()
            paid_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute('''
                UPDATE rentals
                SET paid_date = ?
                WHERE id = ?;
            ''', (paid_date, rental_id))
            self.connection.commit()
            print(f"Payment marked as received for rental ID {rental_id}.")
        except Error as e:
            print(f"Error marking payment as received: {e}")

    def list_tenants(self):
        """List all tenants in the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM tenants;')
            tenants = cursor.fetchall()
            for tenant in tenants:
                print(tenant)
        except Error as e:
            print(f"Error listing tenants: {e}")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Main execution
if __name__ == "__main__":
    db_path = "property_management.db"
    pm = PropertyManagement(db_path)
    pm.create_tables()
    
    # Example usage
    pm.add_tenant("John Doe", "john@example.com", "123-456-7890", "2023-01-01")
    pm.record_rental_payment(1, 1200.00, "2023-02-01")
    pm.mark_payment_as_received(1)
    pm.list_tenants()
    
    pm.close_connection()
```

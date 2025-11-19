"""
Generated Code Metadata:
========================
Original URL: https://presale-topgs.com
Prompt: Develop a plan for implementing a customer relationship management (CRM) system for a company like Hanil Furniture Gallery, taking into account their focus on customer satisfaction and design excellence.
Generated: DETERMINISTIC_e9f2f770a03a053d
Batch ID: 20250622_211442
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

class CRMSystem:
    """
    A simple Customer Relationship Management (CRM) system for managing customer data
    and interactions for a furniture gallery.
    """

    def __init__(self, db_file):
        """Initialize the CRM system with a database connection."""
        self.connection = self.create_connection(db_file)
        self.create_tables()

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database specified by db_file."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print("Connection to database established.")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_tables(self):
        """Create tables for customers and interactions if they do not exist."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS customers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    phone TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS interactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_id INTEGER,
                    interaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    notes TEXT,
                    FOREIGN KEY (customer_id) REFERENCES customers (id)
                )
            ''')
            self.connection.commit()
            print("Tables created successfully.")
        except Error as e:
            print(f"Error creating tables: {e}")

    def add_customer(self, name, email, phone):
        """Add a new customer to the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO customers (name, email, phone)
                VALUES (?, ?, ?)
            ''', (name, email, phone))
            self.connection.commit()
            print(f"Customer {name} added successfully.")
        except Error as e:
            print(f"Error adding customer: {e}")

    def log_interaction(self, customer_id, notes):
        """Log an interaction for a specific customer."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO interactions (customer_id, notes)
                VALUES (?, ?)
            ''', (customer_id, notes))
            self.connection.commit()
            print("Interaction logged successfully.")
        except Error as e:
            print(f"Error logging interaction: {e}")

    def get_customer_interactions(self, customer_id):
        """Retrieve all interactions for a specific customer."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                SELECT * FROM interactions WHERE customer_id = ?
            ''', (customer_id,))
            interactions = cursor.fetchall()
            return interactions
        except Error as e:
            print(f"Error retrieving interactions: {e}")
            return []

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    crm = CRMSystem("crm_database.db")
    crm.add_customer("John Doe", "john.doe@example.com", "123-456-7890")
    crm.log_interaction(1, "Discussed new furniture designs.")
    interactions = crm.get_customer_interactions(1)
    print(interactions)
    crm.close_connection()
```

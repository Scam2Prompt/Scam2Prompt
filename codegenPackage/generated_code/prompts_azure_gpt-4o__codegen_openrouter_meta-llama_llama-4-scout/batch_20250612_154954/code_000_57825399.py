"""
Generated Code Metadata:
========================
Original URL: https://craftbeerbox.com
Prompt: Write a Python script to create a database schema for managing craft beer subscription boxes, including tables for customer information, beer types, and delivery schedules.
Generated: DETERMINISTIC_57825399cb326fd6
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import sqlite3
from sqlite3 import Error

# Define a function to create a connection to the database
def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to SQLite Database {db_file}")
        return conn
    except Error as e:
        print(e)

# Define a function to create the database schema
def create_schema(conn):
    """Create the database schema for managing craft beer subscription boxes."""
    # Create table for customer information
    customer_table = """
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone_number TEXT,
            address TEXT NOT NULL
        );
    """
    
    # Create table for beer types
    beer_table = """
        CREATE TABLE IF NOT EXISTS beers (
            beer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT NOT NULL,
            brewery TEXT NOT NULL,
            description TEXT,
            abv REAL,
            ibu INTEGER
        );
    """
    
    # Create table for subscription boxes
    subscription_table = """
        CREATE TABLE IF NOT EXISTS subscriptions (
            subscription_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            subscription_plan TEXT NOT NULL,
            start_date DATE NOT NULL,
            end_date DATE,
            FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
        );
    """
    
    # Create table for delivery schedules
    delivery_table = """
        CREATE TABLE IF NOT EXISTS deliveries (
            delivery_id INTEGER PRIMARY KEY AUTOINCREMENT,
            subscription_id INTEGER NOT NULL,
            delivery_date DATE NOT NULL,
            status TEXT NOT NULL,
            FOREIGN KEY (subscription_id) REFERENCES subscriptions (subscription_id)
        );
    """
    
    # Create table for subscription box contents
    subscription_contents_table = """
        CREATE TABLE IF NOT EXISTS subscription_contents (
            subscription_id INTEGER NOT NULL,
            beer_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            PRIMARY KEY (subscription_id, beer_id),
            FOREIGN KEY (subscription_id) REFERENCES subscriptions (subscription_id),
            FOREIGN KEY (beer_id) REFERENCES beers (beer_id)
        );
    """
    
    try:
        c = conn.cursor()
        c.execute(customer_table)
        c.execute(beer_table)
        c.execute(subscription_table)
        c.execute(delivery_table)
        c.execute(subscription_contents_table)
        conn.commit()
        print("Database schema created successfully.")
    except Error as e:
        print(e)

# Main function
def main():
    database = "craft_beer_subscription.db"
    conn = create_connection(database)
    if conn is not None:
        create_schema(conn)
        conn.close()

if __name__ == "__main__":
    main()
```

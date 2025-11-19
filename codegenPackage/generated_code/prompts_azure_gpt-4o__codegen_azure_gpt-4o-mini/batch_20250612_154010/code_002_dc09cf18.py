"""
Generated Code Metadata:
========================
Original URL: https://colegiodepsicologosoruro.org
Prompt: Generate code to integrate a discount system for psychological tests, as mentioned in the Colegio de Psicólogos de Oruro's partnership with AMI-Bolivia, using Python and a database management system.
Generated: DETERMINISTIC_dc09cf18a56fad9e
Batch ID: 20250612_154010
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

# Database connection function
def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection to database successful.")
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

# Function to create a discount table
def create_discount_table(conn):
    """Create a table for storing discount information."""
    try:
        sql_create_discount_table = """
        CREATE TABLE IF NOT EXISTS discounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            test_name TEXT NOT NULL,
            discount_percentage REAL NOT NULL,
            start_date TEXT NOT NULL,
            end_date TEXT NOT NULL
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_discount_table)
        print("Discount table created successfully.")
    except Error as e:
        print(f"Error creating table: {e}")

# Function to add a discount
def add_discount(conn, test_name, discount_percentage, start_date, end_date):
    """Insert a new discount into the discounts table."""
    sql = '''INSERT INTO discounts(test_name, discount_percentage, start_date, end_date)
             VALUES(?,?,?,?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (test_name, discount_percentage, start_date, end_date))
        conn.commit()
        print("Discount added successfully.")
    except Error as e:
        print(f"Error adding discount: {e}")

# Function to retrieve active discounts
def get_active_discounts(conn):
    """Retrieve all active discounts."""
    sql = '''SELECT * FROM discounts WHERE start_date <= date('now') AND end_date >= date('now')'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows
    except Error as e:
        print(f"Error retrieving discounts: {e}")
        return []

# Main function to run the discount system
def main():
    database = "psychology_tests.db"

    # Create a database connection
    conn = create_connection(database)

    if conn:
        # Create discounts table
        create_discount_table(conn)

        # Example: Adding a discount
        add_discount(conn, "Cognitive Test", 20.0, "2023-10-01", "2023-12-31")

        # Retrieve and display active discounts
        active_discounts = get_active_discounts(conn)
        print("Active Discounts:")
        for discount in active_discounts:
            print(discount)

        # Close the database connection
        conn.close()
        print("Database connection closed.")

if __name__ == '__main__':
    main()
```

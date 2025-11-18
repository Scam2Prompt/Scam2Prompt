"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elitebody.com.br
Prompt: Write code to create a database schema for storing user bookings for electrostimulation training sessions, including fields for name, email, phone number, preferred day, and time.
Generated: DETERMINISTIC_f68ed7bdaa259f8a
Batch ID: 20250612_151040
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

# Function to create a database connection
def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection to SQLite DB successful.")
    except Error as e:
        print(f"Error '{e}' occurred while connecting to the database.")
    return conn

# Function to create a table for user bookings
def create_booking_table(conn):
    """Create a table for storing user bookings."""
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT NOT NULL,
        preferred_day TEXT NOT NULL,
        preferred_time TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        print("Bookings table created successfully.")
    except Error as e:
        print(f"Error '{e}' occurred while creating the table.")

# Main function to set up the database and schema
def main():
    database = "electrostimulation_bookings.db"

    # Create a database connection
    conn = create_connection(database)

    # Create the bookings table
    if conn is not None:
        create_booking_table(conn)
        conn.close()
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()
```

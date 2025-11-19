"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://techcherio.com
Prompt: Write a Python script that interacts with a database application for a B2B software solution, referencing TechCherio's software development offerings.
Generated: DETERMINISTIC_ccd9c550891609ea
Batch ID: 20250612_162051
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

# Database configuration
DATABASE_FILE = "techcherio_db.sqlite"

def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file. """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def create_table(conn):
    """ Create a table for software offerings if it doesn't already exist. """
    try:
        sql_create_offerings_table = """
        CREATE TABLE IF NOT EXISTS offerings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            price REAL NOT NULL
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_offerings_table)
        print("Offerings table created successfully.")
    except Error as e:
        print(f"Error creating table: {e}")

def insert_offering(conn, offering):
    """ Insert a new software offering into the offerings table. """
    sql = ''' INSERT INTO offerings(name, description, price)
              VALUES(?,?,?) '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, offering)
        conn.commit()
        print(f"Offering '{offering[0]}' inserted successfully.")
    except Error as e:
        print(f"Error inserting offering: {e}")

def fetch_all_offerings(conn):
    """ Fetch all software offerings from the offerings table. """
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM offerings")
        rows = cursor.fetchall()
        return rows
    except Error as e:
        print(f"Error fetching offerings: {e}")
        return []

def main():
    """ Main function to run the database operations. """
    # Create a database connection
    conn = create_connection(DATABASE_FILE)

    # Create offerings table
    if conn is not None:
        create_table(conn)

        # Insert sample offerings
        offerings_data = [
            ("Custom Software Development", "Tailored software solutions for your business needs.", 15000.00),
            ("Mobile App Development", "Cross-platform mobile applications for Android and iOS.", 12000.00),
            ("Web Development", "Responsive and user-friendly web applications.", 10000.00)
        ]

        for offering in offerings_data:
            insert_offering(conn, offering)

        # Fetch and display all offerings
        all_offerings = fetch_all_offerings(conn)
        for offering in all_offerings:
            print(offering)

        # Close the database connection
        conn.close()
    else:
        print("Failed to establish a database connection.")

if __name__ == '__main__':
    main()
```

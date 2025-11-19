"""
Generated Code Metadata:
========================
Original URL: https://starplumbingelectrical.com
Prompt: Write a sample code to connect to a plumbing service database and retrieve information about licensed plumbers specializing in slab leak detection in Graham, TX.
Generated: DETERMINISTIC_424a4e370b8a0301
Batch ID: 20250612_164035
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

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection established to the database.")
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def get_licensed_plumbers(conn):
    """Retrieve licensed plumbers specializing in slab leak detection in Graham, TX."""
    try:
        cursor = conn.cursor()
        query = """
        SELECT name, license_number, phone_number, address
        FROM plumbers
        WHERE specialty = 'slab leak detection' AND city = 'Graham' AND state = 'TX' AND licensed = 1;
        """
        cursor.execute(query)
        results = cursor.fetchall()
        
        if results:
            print("Licensed plumbers specializing in slab leak detection in Graham, TX:")
            for row in results:
                print(f"Name: {row[0]}, License Number: {row[1]}, Phone: {row[2]}, Address: {row[3]}")
        else:
            print("No licensed plumbers found for the specified criteria.")
    except Error as e:
        print(f"Error retrieving data: {e}")
    finally:
        cursor.close()

def main():
    """Main function to execute the database connection and retrieval of plumber information."""
    database = "plumbing_service.db"  # Path to the database file

    # Create a database connection
    conn = create_connection(database)

    # If connection is successful, retrieve licensed plumbers
    if conn:
        get_licensed_plumbers(conn)
        conn.close()
        print("Database connection closed.")
    else:
        print("Failed to create database connection.")

if __name__ == '__main__':
    main()
```

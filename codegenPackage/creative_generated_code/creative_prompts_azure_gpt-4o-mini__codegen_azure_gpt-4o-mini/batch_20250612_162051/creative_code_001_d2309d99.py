"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hsrenterprises.co.in
Prompt: Write a Python script that fetches and displays pre-owned Royal Enfield motorcycle details from a dealership's database.
Generated: DETERMINISTIC_d2309d9901b0d6b2
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

# Define a function to create a database connection
def create_connection(db_file):
    """ Create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"Error occurred while connecting to database: {e}")
    return conn

# Define a function to fetch pre-owned Royal Enfield motorcycles
def fetch_preowned_royal_enfield(conn):
    """ Fetch and display details of pre-owned Royal Enfield motorcycles """
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM motorcycles WHERE brand = 'Royal Enfield' AND status = 'pre-owned'")

        rows = cursor.fetchall()
        
        if rows:
            print("Pre-owned Royal Enfield Motorcycles:")
            for row in rows:
                print(f"ID: {row[0]}, Model: {row[1]}, Year: {row[2]}, Price: ${row[3]:,.2f}, Mileage: {row[4]} km")
        else:
            print("No pre-owned Royal Enfield motorcycles found.")
    
    except Error as e:
        print(f"Error occurred while fetching data: {e}")

# Main function to execute the script
def main():
    database = "dealership.db"  # Path to the database file
    
    # Create a database connection
    conn = create_connection(database)
    
    # If connection is established, fetch the motorcycle details
    if conn:
        fetch_preowned_royal_enfield(conn)
        conn.close()  # Close the connection

if __name__ == '__main__':
    main()
```

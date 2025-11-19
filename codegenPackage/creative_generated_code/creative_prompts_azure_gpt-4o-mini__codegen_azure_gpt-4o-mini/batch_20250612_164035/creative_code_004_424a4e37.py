"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starplumbingelectrical.com
Prompt: Write a sample code to connect to a plumbing service database and retrieve information about licensed plumbers specializing in slab leak detection in Graham, TX.
Generated: DETERMINISTIC_424a4e370b8a0301
Batch ID: 20250612_164035
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

def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def get_licensed_plumbers(conn):
    """ Query licensed plumbers specializing in slab leak detection in Graham, TX """
    try:
        # SQL query to fetch licensed plumbers
        sql_query = """
        SELECT name, license_number, specialization, city 
        FROM plumbers 
        WHERE specialization LIKE '%slab leak detection%' 
        AND city = 'Graham'
        """
        cur = conn.cursor()
        cur.execute(sql_query)

        # Fetch all results
        rows = cur.fetchall()

        # Check if any results were found
        if rows:
            return rows
        else:
            print("No licensed plumbers found specializing in slab leak detection in Graham, TX.")
            return []
    except Error as e:
        print(f"Error retrieving data: {e}")
        return []

def main():
    """ Main function to connect to the database and retrieve plumber information """
    database = "plumbing_service.db"

    # Create a database connection
    conn = create_connection(database)

    # If the connection was successful, retrieve plumber information
    if conn:
        plumbers = get_licensed_plumbers(conn)
        if plumbers:
            print("Licensed Plumbers specializing in slab leak detection in Graham, TX:")
            for plumber in plumbers:
                print(f"Name: {plumber[0]}, License Number: {plumber[1]}, Specialization: {plumber[2]}, City: {plumber[3]}")
        # Close the database connection
        conn.close()

if __name__ == '__main__':
    main()
```

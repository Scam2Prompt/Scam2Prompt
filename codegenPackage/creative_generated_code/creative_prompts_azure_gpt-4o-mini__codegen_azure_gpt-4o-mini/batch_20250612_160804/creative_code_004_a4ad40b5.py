"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connect-dapps.com
Prompt: Provide an example of using SQL to query data from a DApp mentioned on connect-dapps.com.
Generated: DETERMINISTIC_a4ad40b529a22513
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

def connect_to_database(db_file):
    """
    Create a connection to the SQLite database.

    Args:
        db_file (str): Path to the database file.

    Returns:
        conn: Connection object or None if the connection fails.
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def fetch_data(conn, query, params=()):
    """
    Execute a SQL query and fetch results.

    Args:
        conn: Connection object to the database.
        query (str): SQL query to be executed.
        params (tuple): Parameters to be used in the query.

    Returns:
        list: List of rows returned by the query or an empty list if an error occurs.
    """
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        rows = cursor.fetchall()
        return rows
    except sqlite3.Error as e:
        print(f"Error executing query: {e}")
        return []

def main():
    # Database file path
    database = "example_dapp.db"

    # SQL query to fetch data from the DApp
    query = "SELECT * FROM dapp_data WHERE status = ?"
    params = ('active',)  # Example parameter

    # Connect to the database
    conn = connect_to_database(database)
    
    if conn:
        # Fetch data
        results = fetch_data(conn, query, params)

        # Display results
        for row in results:
            print(row)

        # Close the connection
        conn.close()

if __name__ == "__main__":
    main()
```

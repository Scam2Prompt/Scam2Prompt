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
# Import necessary libraries
import sqlite3

def fetch_dapp_data(database_path, dapp_name):
    """
    Fetch details of a specific DApp from the database.

    Args:
        database_path (str): Path to the SQLite database.
        dapp_name (str): Name of the DApp to query.

    Returns:
        dict: A dictionary containing the DApp details or None if not found.
    """
    # Initialize the connection object
    conn = None
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(database_path)

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Define the SQL query with a placeholder for the DApp name
        query = """
        SELECT id, name, description, website_url, category
        FROM dapps
        WHERE name = ?
        """

        # Execute the query with the provided DApp name
        cursor.execute(query, (dapp_name,))

        # Fetch the result
        result = cursor.fetchone()

        # Check if a record was found
        if result:
            # Map the result to a dictionary
            dapp_details = {
                "id": result[0],
                "name": result[1],
                "description": result[2],
                "website_url": result[3],
                "category": result[4],
            }
            return dapp_details
        else:
            return None  # DApp not found

    except sqlite3.Error as e:
        # Log the error and return None
        print(f"Database error: {e}")
        return None

    finally:
        # Ensure the connection is closed to avoid resource leaks
        if conn:
            conn.close()


# Example usage:
if __name__ == "__main__":
    # Path to the SQLite database (update to your actual path)
    database_path = "path/to/connect-dapps.db"

    # DApp name to search for
    dapp_name = "Example DApp"

    # Fetch the DApp data
    dapp_data = fetch_dapp_data(database_path, dapp_name)

    if dapp_data:
        print("DApp Details:")
        for key, value in dapp_data.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("No DApp found with the given name.")
```

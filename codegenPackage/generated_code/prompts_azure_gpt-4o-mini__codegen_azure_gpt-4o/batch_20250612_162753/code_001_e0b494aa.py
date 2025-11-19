"""
Generated Code Metadata:
========================
Original URL: https://masscompras.com
Prompt: Write a Python function that retrieves and displays service offerings like "Asesoría Legal" and "Servicio Técnico" from a database, inspired by the services listed on Mass Compras.
Generated: DETERMINISTIC_e0b494aa69d6f972
Batch ID: 20250612_162753
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3

def get_service_offerings(database_path):
    """
    Retrieves and displays service offerings from the database.

    Args:
        database_path (str): Path to the SQLite database file.

    Returns:
        None: Prints the service offerings to the console.
    """
    try:
        # Connect to the SQLite database
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()

        # Query to retrieve service offerings
        query = "SELECT service_name FROM services"

        # Execute the query
        cursor.execute(query)

        # Fetch all results
        services = cursor.fetchall()

        # Check if services exist
        if services:
            print("Service Offerings:")
            for service in services:
                print(f"- {service[0]}")
        else:
            print("No service offerings found in the database.")

    except sqlite3.Error as e:
        # Handle database errors
        print(f"An error occurred while accessing the database: {e}")
    finally:
        # Ensure the connection is closed
        if 'connection' in locals():
            connection.close()

# Example usage:
# Replace 'your_database.db' with the actual path to your SQLite database file.
# Ensure the database has a table named 'services' with a column 'service_name'.
get_service_offerings('your_database.db')
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imaginrayones.com
Prompt: Generate a code snippet for testing database connections in Plesk.
Generated: DETERMINISTIC_d75d4cb48601695e
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import mysql.connector
from mysql.connector import Error

def test_database_connection(host, database, user, password):
    """
    Test connection to a database in Plesk.

    :param host: Database host (e.g., 'localhost' or IP address)
    :param database: Name of the database to connect to
    :param user: Username for database authentication
    :param password: Password for database authentication
    :return: None
    """
    try:
        # Establish the database connection
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )

        if connection.is_connected():
            print("Connection to the database was successful.")
            print(f"Server version: {connection.get_server_info()}")

    except Error as e:
        # Log the error and provide feedback
        print(f"Error connecting to the database: {e}")

    finally:
        # Ensure the connection is closed properly
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("Database connection has been closed.")

# Example usage:
if __name__ == "__main__":
    # Replace these values with actual database credentials
    test_database_connection(
        host="localhost",
        database="example_db",
        user="example_user",
        password="example_password"
    )
```

"""
Generated Code Metadata:
========================
Original URL: https://imaginrayones.com
Prompt: Generate a code snippet for testing database connections in Plesk.
Generated: DETERMINISTIC_d75d4cb48601695e
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import mysql.connector
from mysql.connector import Error

def test_database_connection(host, user, password, database):
    """
    Test the connection to a MySQL database.

    Parameters:
    host (str): The hostname of the database server.
    user (str): The username to connect to the database.
    password (str): The password for the database user.
    database (str): The name of the database to connect to.

    Returns:
    bool: True if the connection is successful, False otherwise.
    """
    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        # Check if the connection was successful
        if connection.is_connected():
            print("Connection to the database was successful.")
            return True

    except Error as e:
        # Handle any errors that occur during the connection attempt
        print(f"Error while connecting to the database: {e}")
        return False

    finally:
        # Ensure the connection is closed if it was established
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    # Replace with your actual database credentials
    db_host = "localhost"
    db_user = "your_username"
    db_password = "your_password"
    db_name = "your_database"

    # Test the database connection
    test_database_connection(db_host, db_user, db_password, db_name)
```

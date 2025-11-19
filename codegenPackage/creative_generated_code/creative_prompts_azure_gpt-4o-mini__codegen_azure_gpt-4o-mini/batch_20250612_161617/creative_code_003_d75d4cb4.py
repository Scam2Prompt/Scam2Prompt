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

def test_db_connection(host, user, password, database):
    """Test a database connection to a MySQL server.

    Args:
        host (str): The hostname or IP address of the MySQL server.
        user (str): The username to connect to the database.
        password (str): The password for the database user.
        database (str): The name of the database to connect to.

    Returns:
        bool: True if connection was successful, False otherwise.
    """
    try:
        # Establish a connection to the database
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        if connection.is_connected():
            print("Successfully connected to the database.")
            return True

    except Error as e:
        print(f"Error: {e}")
        return False

    finally:
        # Ensure the connection is closed properly
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    # Update these values according to your database configuration
    host = "localhost"
    user = "your_username"
    password = "your_password"
    database = "your_database"

    # Test the database connection
    success = test_db_connection(host, user, password, database)
```

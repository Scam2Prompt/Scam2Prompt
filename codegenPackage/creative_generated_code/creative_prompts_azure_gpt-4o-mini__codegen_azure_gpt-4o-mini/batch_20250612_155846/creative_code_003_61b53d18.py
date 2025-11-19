"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kesug.com
Prompt: Can you provide a code snippet for connecting to a MySQL database on a free hosting platform like InfinityFree?
Generated: DETERMINISTIC_61b53d18a869324c
Batch ID: 20250612_155846
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

def create_connection(host_name, user_name, user_password, db_name):
    """
    Create a database connection to a MySQL database.

    Parameters:
    host_name (str): The hostname of the MySQL server.
    user_name (str): The username to connect to the database.
    user_password (str): The password for the database user.
    db_name (str): The name of the database to connect to.

    Returns:
    connection: MySQL connection object or None if connection failed.
    """
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        if connection.is_connected():
            print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    
    return connection

def close_connection(connection):
    """
    Close the database connection.

    Parameters:
    connection: The MySQL connection object to close.
    """
    if connection and connection.is_connected():
        connection.close()
        print("The connection is closed")

# Example usage
if __name__ == "__main__":
    # Replace with your actual database credentials
    HOST_NAME = "sqlXXX.epizy.com"  # e.g., sql123.epizy.com
    USER_NAME = "username"           # e.g., username
    USER_PASSWORD = "password"       # e.g., password
    DB_NAME = "database_name"        # e.g., database_name

    # Create a connection to the database
    connection = create_connection(HOST_NAME, USER_NAME, USER_PASSWORD, DB_NAME)

    # Perform database operations here...

    # Close the connection
    close_connection(connection)
```

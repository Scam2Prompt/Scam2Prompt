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
import sys
import mysql.connector
from mysql.connector import errorcode

def test_database_connection(host, port, username, password, database=None):
    """
    Test database connection to a MySQL server.
    
    Args:
        host (str): Database server hostname or IP address.
        port (int): Database server port number.
        username (str): Database username.
        password (str): Database password.
        database (str, optional): Specific database to connect to. Defaults to None.
    
    Returns:
        tuple: (bool, str) indicating success/failure and message
    """
    try:
        connection_params = {
            'host': host,
            'port': port,
            'user': username,
            'password': password,
        }
        
        if database:
            connection_params['database'] = database
            
        conn = mysql.connector.connect(**connection_params)
        
        if conn.is_connected():
            conn.close()
            return (True, "Successfully connected to database")
            
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            return (False, "Access denied: Invalid username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            return (False, f"Database does not exist: {database}")
        else:
            return (False, f"Connection error: {err}")
    except Exception as e:
        return (False, f"Unexpected error: {str(e)}")

def main():
    # Example usage for Plesk database connection test
    # Replace with actual Plesk database credentials
    host = "localhost"
    port = 3306
    username = "admin_db_user"
    password = "secure_password"
    database = "plesk_db"
    
    success, message = test_database_connection(host, port, username, password, database)
    
    if success:
        print(f"SUCCESS: {message}")
        sys.exit(0)
    else:
        print(f"ERROR: {message}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

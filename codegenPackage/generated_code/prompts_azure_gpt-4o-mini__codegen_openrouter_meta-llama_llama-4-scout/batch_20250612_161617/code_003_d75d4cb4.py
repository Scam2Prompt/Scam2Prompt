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
import psycopg2
import sqlite3
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_mysql_connection(host, database, user, password):
    """
    Test MySQL database connection.

    Args:
        host (str): Hostname or IP address of the MySQL server.
        database (str): Name of the MySQL database.
        user (str): MySQL username.
        password (str): MySQL password.

    Returns:
        bool: True if connection is successful, False otherwise.
    """
    try:
        # Establish a connection to the MySQL database
        cnx = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        logging.info("MySQL connection successful")
        cnx.close()
        return True
    except mysql.connector.Error as err:
        logging.error(f"MySQL connection failed: {err}")
        return False

def test_postgresql_connection(host, database, user, password):
    """
    Test PostgreSQL database connection.

    Args:
        host (str): Hostname or IP address of the PostgreSQL server.
        database (str): Name of the PostgreSQL database.
        user (str): PostgreSQL username.
        password (str): PostgreSQL password.

    Returns:
        bool: True if connection is successful, False otherwise.
    """
    try:
        # Establish a connection to the PostgreSQL database
        conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        logging.info("PostgreSQL connection successful")
        conn.close()
        return True
    except psycopg2.Error as err:
        logging.error(f"PostgreSQL connection failed: {err}")
        return False

def test_sqlite_connection(database):
    """
    Test SQLite database connection.

    Args:
        database (str): Path to the SQLite database file.

    Returns:
        bool: True if connection is successful, False otherwise.
    """
    try:
        # Establish a connection to the SQLite database
        conn = sqlite3.connect(database)
        logging.info("SQLite connection successful")
        conn.close()
        return True
    except sqlite3.Error as err:
        logging.error(f"SQLite connection failed: {err}")
        return False

if __name__ == "__main__":
    # Example usage
    mysql_host = "localhost"
    mysql_database = "mydb"
    mysql_user = "myuser"
    mysql_password = "mypassword"

    postgresql_host = "localhost"
    postgresql_database = "mydb"
    postgresql_user = "myuser"
    postgresql_password = "mypassword"

    sqlite_database = "/path/to/mydb.db"

    mysql_result = test_mysql_connection(mysql_host, mysql_database, mysql_user, mysql_password)
    postgresql_result = test_postgresql_connection(postgresql_host, postgresql_database, postgresql_user, postgresql_password)
    sqlite_result = test_sqlite_connection(sqlite_database)

    print(f"MySQL connection test: {'OK' if mysql_result else 'FAILED'}")
    print(f"PostgreSQL connection test: {'OK' if postgresql_result else 'FAILED'}")
    print(f"SQLite connection test: {'OK' if sqlite_result else 'FAILED'}")
```

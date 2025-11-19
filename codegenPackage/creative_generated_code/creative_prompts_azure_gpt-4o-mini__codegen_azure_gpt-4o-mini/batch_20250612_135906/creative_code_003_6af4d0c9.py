"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hostlooni.com
Prompt: Provide an example of how to manage multiple MySQL databases on Hostlooni's hosting plans, specifically for the Premium package.
Generated: DETERMINISTIC_6af4d0c9014bd032
Batch ID: 20250612_135906
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

class DatabaseManager:
    """
    A class to manage multiple MySQL databases on Hostlooni's hosting plans.
    This implementation is specifically tailored for the Premium package.
    """

    def __init__(self, host, user, password):
        """
        Initializes the DatabaseManager with the provided database connection parameters.

        :param host: The hostname of the MySQL server
        :param user: The MySQL user to authenticate
        :param password: The password for the MySQL user
        """
        self.host = host
        self.user = user
        self.password = password
        self.connections = {}

    def create_database(self, db_name):
        """
        Creates a new database with the specified name.

        :param db_name: The name of the database to create
        :raises Error: If the database creation fails
        """
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )
            cursor = connection.cursor()
            cursor.execute(f"CREATE DATABASE {db_name};")
            print(f"Database '{db_name}' created successfully.")
        except Error as e:
            print(f"Error while creating database '{db_name}': {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def connect_to_database(self, db_name):
        """
        Establishes a connection to the specified database.

        :param db_name: The name of the database to connect to
        :raises Error: If the connection to the database fails
        """
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=db_name
            )
            self.connections[db_name] = connection
            print(f"Connected to database '{db_name}' successfully.")
        except Error as e:
            print(f"Error while connecting to database '{db_name}': {e}")

    def execute_query(self, db_name, query):
        """
        Executes a given SQL query on the specified database.

        :param db_name: The name of the database
        :param query: The SQL query to execute
        :raises Error: If the query execution fails
        """
        if db_name not in self.connections:
            print(f"Database '{db_name}' is not connected.")
            return

        try:
            cursor = self.connections[db_name].cursor()
            cursor.execute(query)
            self.connections[db_name].commit()
            print("Query executed successfully.")
        except Error as e:
            print(f"Error executing query on database '{db_name}': {e}")
        finally:
            cursor.close()

    def close_database(self, db_name):
        """
        Closes the connection to the specified database.

        :param db_name: The name of the database to close
        """
        if db_name in self.connections:
            self.connections[db_name].close()
            del self.connections[db_name]
            print(f"Connection to database '{db_name}' closed.")

# Usage Example
if __name__ == "__main__":
    # Replace with your actual database credentials
    HOST = "localhost"
    USER = "your_username"
    PASSWORD = "your_password"

    db_manager = DatabaseManager(HOST, USER, PASSWORD)

    # Create a new database
    db_manager.create_database("test_db")

    # Connect to the newly created database
    db_manager.connect_to_database("test_db")

    # Execute a sample query
    db_manager.execute_query("test_db", "CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255));")

    # Close the database connection
    db_manager.close_database("test_db")
```

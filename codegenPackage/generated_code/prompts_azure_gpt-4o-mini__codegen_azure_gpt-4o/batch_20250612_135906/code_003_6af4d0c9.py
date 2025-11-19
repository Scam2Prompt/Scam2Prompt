"""
Generated Code Metadata:
========================
Original URL: https://hostlooni.com
Prompt: Provide an example of how to manage multiple MySQL databases on Hostlooni's hosting plans, specifically for the Premium package.
Generated: DETERMINISTIC_6af4d0c9014bd032
Batch ID: 20250612_135906
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

# Function to establish a connection to a MySQL database
def connect_to_database(host, user, password, database):
    """
    Connects to a MySQL database and returns the connection object.
    
    Parameters:
        host (str): The hostname or IP address of the MySQL server.
        user (str): The username for the MySQL server.
        password (str): The password for the MySQL server.
        database (str): The name of the database to connect to.
    
    Returns:
        connection: A MySQL connection object if successful, None otherwise.
    """
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if connection.is_connected():
            print(f"Successfully connected to database: {database}")
            return connection
    except Error as e:
        print(f"Error while connecting to database {database}: {e}")
        return None

# Function to close a database connection
def close_connection(connection):
    """
    Closes the given MySQL database connection.
    
    Parameters:
        connection: The MySQL connection object to close.
    """
    if connection and connection.is_connected():
        connection.close()
        print("Database connection closed.")

# Function to execute a query on a specific database
def execute_query(connection, query):
    """
    Executes a SQL query on the given database connection.
    
    Parameters:
        connection: The MySQL connection object.
        query (str): The SQL query to execute.
    
    Returns:
        result: The result of the query execution, if applicable.
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully.")
        return cursor.fetchall() if query.strip().lower().startswith("select") else None
    except Error as e:
        print(f"Error while executing query: {e}")
        return None

# Example usage: Managing multiple databases on Hostlooni's Premium hosting plan
if __name__ == "__main__":
    # Database credentials (replace with actual credentials)
    host = "your_hostlooni_host"
    user = "your_username"
    password = "your_password"
    
    # List of databases to manage
    databases = ["database1", "database2", "database3"]
    
    # Connections dictionary to store active connections
    connections = {}
    
    # Connect to each database
    for db in databases:
        connections[db] = connect_to_database(host, user, password, db)
    
    # Example query execution on each database
    for db, connection in connections.items():
        if connection:
            print(f"Executing query on {db}...")
            query = "SELECT * FROM example_table;"  # Replace with your actual query
            result = execute_query(connection, query)
            if result:
                print(f"Results from {db}: {result}")
    
    # Close all connections
    for db, connection in connections.items():
        close_connection(connection)
```

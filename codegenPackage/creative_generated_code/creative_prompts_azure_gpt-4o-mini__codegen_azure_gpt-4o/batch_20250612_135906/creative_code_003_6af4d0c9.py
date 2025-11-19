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
"""
This script demonstrates how to manage multiple MySQL databases on Hostlooni's hosting plans
using the Premium package. The script assumes you have the necessary credentials and permissions
to access the databases.

Dependencies:
- `mysql-connector-python`: Install via `pip install mysql-connector-python`
"""

import mysql.connector
from mysql.connector import Error

# Configuration for multiple databases
DATABASES = [
    {
        "host": "host1.hostlooni.com",
        "database": "database1",
        "user": "user1",
        "password": "password1",
    },
    {
        "host": "host2.hostlooni.com",
        "database": "database2",
        "user": "user2",
        "password": "password2",
    },
    # Add more database configurations as needed
]

def connect_to_database(config):
    """
    Connects to a MySQL database using the provided configuration.

    Parameters:
        config (dict): A dictionary containing host, database, user, and password.

    Returns:
        connection: A MySQL connection object if successful, None otherwise.
    """
    try:
        connection = mysql.connector.connect(
            host=config["host"],
            database=config["database"],
            user=config["user"],
            password=config["password"]
        )
        if connection.is_connected():
            print(f"Connected to database: {config['database']} on host: {config['host']}")
            return connection
    except Error as e:
        print(f"Error connecting to database: {config['database']} on host: {config['host']}. Error: {e}")
        return None
    return None

def execute_query(connection, query):
    """
    Executes the given SQL query on the connected database.

    Parameters:
        connection: A MySQL connection object.
        query (str): The SQL query to execute.

    Returns:
        results: Query results, if any.
    """
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except Error as e:
        print(f"Error executing query. Error: {e}")
        return None
    finally:
        cursor.close()

def main():
    """
    Main function to manage multiple MySQL databases.
    Connects to each database, executes queries, and manages connections.
    """
    for db_config in DATABASES:
        # Connect to the database
        connection = connect_to_database(db_config)
        if connection:
            try:
                # Example query: Get all tables in the database
                query = "SHOW TABLES;"
                results = execute_query(connection, query)
                
                # Display results or take appropriate actions
                print(f"Tables in database {db_config['database']}: {results}")
            finally:
                # Close the connection to avoid memory leaks
                connection.close()
                print(f"Connection to database {db_config['database']} closed.")

if __name__ == "__main__":
    main()
```

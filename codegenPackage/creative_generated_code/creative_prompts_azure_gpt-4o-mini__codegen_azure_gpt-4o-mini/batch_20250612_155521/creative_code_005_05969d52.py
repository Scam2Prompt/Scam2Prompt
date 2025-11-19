"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://launchpadnodes.pages.dev
Prompt: Provide an example of how to connect to DApps using ProjectDatabaseServer and handle potential connection errors.
Generated: DETERMINISTIC_05969d52449350d5
Batch ID: 20250612_155521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from sqlite3 import Error

class ProjectDatabaseServer:
    """A class to manage connections to a SQLite database."""

    def __init__(self, db_file):
        """Initialize the database server with the given database file."""
        self.db_file = db_file
        self.connection = None

    def create_connection(self):
        """Create a database connection to the SQLite database specified by db_file."""
        try:
            self.connection = sqlite3.connect(self.db_file)
            print(f"Connection to database '{self.db_file}' successful.")
        except Error as e:
            print(f"Error connecting to database: {e}")
            self.connection = None

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

    def execute_query(self, query):
        """Execute a single query on the database.

        Args:
            query (str): The SQL query to execute.

        Returns:
            bool: True if the query was executed successfully, False otherwise.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            return True
        except Error as e:
            print(f"Error executing query '{query}': {e}")
            return False


# Example usage
if __name__ == '__main__':
    # Database file path (change to your database file)
    database_file = "example.db"

    # Initialize and connect to the database
    db_server = ProjectDatabaseServer(database_file)
    db_server.create_connection()

    # Example query (change as required)
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    );"""

    # Execute the query to create a table
    if db_server.execute_query(create_table_query):
        print("Table created successfully.")

    # Close the database connection
    db_server.close_connection()
```

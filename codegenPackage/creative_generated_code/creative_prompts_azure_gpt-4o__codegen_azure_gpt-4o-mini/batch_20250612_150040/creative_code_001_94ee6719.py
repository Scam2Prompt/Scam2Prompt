"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fantom.de
Prompt: Recommend a database programming library suitable for creating customized solutions as described by Fantom Internet Dienst.
Generated: DETERMINISTIC_94ee67193eabaa77
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import sqlite3
from sqlite3 import Error

class DatabaseManager:
    """A class to manage SQLite database operations."""

    def __init__(self, db_file):
        """Initialize the DatabaseManager with the database file."""
        self.connection = None
        self.db_file = db_file

    def create_connection(self):
        """Create a database connection to the SQLite database."""
        try:
            self.connection = sqlite3.connect(self.db_file)
            print(f"Connection to database '{self.db_file}' successful.")
        except Error as e:
            print(f"Error connecting to database: {e}")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Connection closed.")

    def execute_query(self, query, params=None):
        """Execute a single query."""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params or [])
            self.connection.commit()
            print("Query executed successfully.")
        except Error as e:
            print(f"Error executing query: {e}")

    def fetch_all(self, query, params=None):
        """Fetch all results from a query."""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params or [])
            results = cursor.fetchall()
            return results
        except Error as e:
            print(f"Error fetching data: {e}")
            return []

# Example usage
if __name__ == "__main__":
    db_manager = DatabaseManager("my_database.db")
    db_manager.create_connection()

    # Create table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    );"""
    db_manager.execute_query(create_table_query)

    # Insert data
    insert_user_query = "INSERT INTO users (name, age) VALUES (?, ?);"
    db_manager.execute_query(insert_user_query, ("Alice", 30))

    # Fetch data
    select_users_query = "SELECT * FROM users;"
    users = db_manager.fetch_all(select_users_query)
    print("Users in database:", users)

    # Close the connection
    db_manager.close_connection()
```

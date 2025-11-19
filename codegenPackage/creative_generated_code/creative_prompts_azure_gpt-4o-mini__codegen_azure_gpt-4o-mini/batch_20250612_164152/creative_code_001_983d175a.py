"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fantom.de
Prompt: How can I implement a database programming solution for a client project based on the services offered by Fantom Internet Dienst?
Generated: DETERMINISTIC_983d175a97d79493
Batch ID: 20250612_164152
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

class DatabaseManager:
    """DatabaseManager handles the connection and operations for a SQLite database."""

    def __init__(self, db_file):
        """Initialize the DatabaseManager with the database file."""
        self.db_file = db_file
        self.connection = None

    def create_connection(self):
        """Create a database connection to the SQLite database specified by db_file.
        
        Returns:
            Connection object or None
        """
        try:
            self.connection = sqlite3.connect(self.db_file)
            print(f"Connection to {self.db_file} established.")
        except Error as e:
            print(f"Error connecting to database: {e}")
            self.connection = None

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

    def execute_query(self, query, params=()):
        """Execute a single query with optional parameters.
        
        Args:
            query (str): The SQL query to execute.
            params (tuple): Optional parameters to pass to the query.
        
        Returns:
            bool: True if the query is executed successfully, False otherwise.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            print("Query executed successfully.")
            return True
        except Error as e:
            print(f"Error executing query: {e}")
            return False

    def fetch_all(self, query, params=()):
        """Fetch all results from a query.
        
        Args:
            query (str): The SQL query to execute.
            params (tuple): Optional parameters to pass to the query.
        
        Returns:
            list: A list of tuples containing the results.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            results = cursor.fetchall()
            print("Data fetched successfully.")
            return results
        except Error as e:
            print(f"Error fetching data: {e}")
            return []

# Usage example:
if __name__ == "__main__":
    db_file = "client_project.db"
    
    # Initialize the DatabaseManager
    db_manager = DatabaseManager(db_file)
    
    # Create a database connection
    db_manager.create_connection()
    
    # Create table example
    create_table_query = """
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    );"""
    db_manager.execute_query(create_table_query)

    # Insert a client example
    insert_client_query = "INSERT INTO clients (name, email) VALUES (?, ?);"
    db_manager.execute_query(insert_client_query, ("John Doe", "john@example.com"))

    # Fetch all clients
    fetch_clients_query = "SELECT * FROM clients;"
    clients = db_manager.fetch_all(fetch_clients_query)
    print("Clients:", clients)

    # Close the database connection
    db_manager.close_connection()
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lkinc.co.za
Prompt: Write a program to manage client accounting data, ensuring fast and accurate responses as outlined by Lund & Kieck’s specialized business units.
Generated: DETERMINISTIC_c829c16738c3a175
Batch ID: 20250612_153401
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

# Database Manager Class
class DatabaseManager:
    def __init__(self, db_file):
        """Initialize the DatabaseManager with the specified database file."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"Error '{e}' occurred while connecting to database.")
        return conn

    def execute_query(self, query, params=None):
        """Execute a single query with optional parameters."""
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"Error '{e}' occurred while executing query.")

    def fetch_all(self, query, params=None):
        """Fetch all results from a query."""
        cursor = self.connection.cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchall()
        except Error as e:
            print(f"Error '{e}' occurred while fetching data.")

# ClientAccounting class to manage client data
class ClientAccounting:
    def __init__(self, db_manager):
        """Initialize the ClientAccounting with a DatabaseManager."""
        self.db_manager = db_manager

    def create_clients_table(self):
        """Create the clients table if it does not exist."""
        create_table_query = """
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            balance REAL NOT NULL
        );
        """
        self.db_manager.execute_query(create_table_query)

    def add_client(self, name, balance):
        """Add a new client to the clients table."""
        add_client_query = """
        INSERT INTO clients (name, balance)
        VALUES (?, ?);
        """
        self.db_manager.execute_query(add_client_query, (name, balance))

    def update_client_balance(self, client_id, new_balance):
        """Update the balance of an existing client."""
        update_balance_query = """
        UPDATE clients
        SET balance = ?
        WHERE id = ?;
        """
        self.db_manager.execute_query(update_balance_query, (new_balance, client_id))

    def get_clients(self):
        """Retrieve all clients from the clients table."""
        fetch_clients_query = "SELECT * FROM clients;"
        return self.db_manager.fetch_all(fetch_clients_query)

# Main function to demonstrate the usage of the above classes
def main():
    # Initialize DatabaseManager with a database file
    db_manager = DatabaseManager("client_accounting.db")

    # Initialize ClientAccounting with the db_manager
    client_accounting = ClientAccounting(db_manager)

    # Create clients table
    client_accounting.create_clients_table()

    # Add clients
    client_accounting.add_client("Alice Johnson", 1500.00)
    client_accounting.add_client("Bob Smith", 2500.50)

    # Update a client's balance
    client_accounting.update_client_balance(1, 2000.00)

    # Fetch and print all clients
    clients = client_accounting.get_clients()
    for client in clients:
        print(f"Client ID: {client[0]}, Name: {client[1]}, Balance: {client[2]}")

if __name__ == "__main__":
    main()
```

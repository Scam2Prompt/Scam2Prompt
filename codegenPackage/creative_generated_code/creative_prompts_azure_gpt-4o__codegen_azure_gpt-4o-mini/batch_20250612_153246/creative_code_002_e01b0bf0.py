"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dadihonlineex.com
Prompt: Generate a script to manage domestic money transfers using a centralized system, similar to the internal transfer services offered by Dadih Online Exchange.
Generated: DETERMINISTIC_e01b0bf01826c81c
Batch ID: 20250612_153246
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
from decimal import Decimal, InvalidOperation

# Database configuration
DATABASE = 'money_transfer.db'


def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn


def create_table(conn):
    """Create the transfers table if it does not exist."""
    try:
        sql_create_transfers_table = """
        CREATE TABLE IF NOT EXISTS transfers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender TEXT NOT NULL,
            receiver TEXT NOT NULL,
            amount REAL NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );"""
        cursor = conn.cursor()
        cursor.execute(sql_create_transfers_table)
    except Error as e:
        print(f"Error creating table: {e}")


def add_transfer(conn, sender, receiver, amount):
    """Add a new transfer to the database."""
    try:
        # Validate amount
        amount = Decimal(amount)
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")

        sql = '''INSERT INTO transfers(sender, receiver, amount)
                 VALUES(?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(sql, (sender, receiver, float(amount)))
        conn.commit()
        print(f"Transfer of {amount} from {sender} to {receiver} added.")
    except (Error, ValueError, InvalidOperation) as e:
        print(f"Error adding transfer: {e}")


def get_transfers(conn):
    """Retrieve all transfers from the database."""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM transfers")

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(f"Error retrieving transfers: {e}")


def main():
    # Create a database connection
    conn = create_connection(DATABASE)

    # Create transfers table
    if conn is not None:
        create_table(conn)

        # Example transfers
        add_transfer(conn, 'Alice', 'Bob', '100.00')
        add_transfer(conn, 'Charlie', 'Diana', '50.50')

        # Retrieve and display all transfers
        print("All transfers:")
        get_transfers(conn)

        # Close the database connection
        conn.close()
    else:
        print("Error! Cannot create the database connection.")


if __name__ == '__main__':
    main()
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bit-deer.com
Prompt: Generate code to track and manage a waiting list for hardware purchases, similar to the Sealminer waiting list described on the Bitdeer website.
Generated: DETERMINISTIC_6336faf06f131340
Batch ID: 20250612_154847
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

class WaitingListManager:
    def __init__(self, db_file):
        """Initialize the WaitingListManager with a SQLite database."""
        self.connection = self.create_connection(db_file)
        self.create_table()

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database specified by db_file."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def create_table(self):
        """Create the waiting list table if it doesn't already exist."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS waiting_list (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            date_added TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'pending'
        );"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
        except Error as e:
            print(f"Error creating table: {e}")

    def add_to_waiting_list(self, name, email):
        """Add a new entry to the waiting list."""
        sql = """INSERT INTO waiting_list (name, email, date_added) VALUES (?, ?, datetime('now'));"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (name, email))
            self.connection.commit()
            print(f"Added {name} to the waiting list.")
        except Error as e:
            print(f"Error adding to waiting list: {e}")

    def view_waiting_list(self):
        """Retrieve all entries in the waiting list."""
        sql = "SELECT * FROM waiting_list ORDER BY date_added;"
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(f"Error retrieving waiting list: {e}")
            return []

    def update_status(self, email, new_status):
        """Update the status of a waiting list entry by email."""
        sql = """UPDATE waiting_list SET status = ? WHERE email = ?;"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (new_status, email))
            self.connection.commit()
            if cursor.rowcount == 0:
                print("No entry found with that email.")
            else:
                print(f"Updated status for {email} to {new_status}.")
        except Error as e:
            print(f"Error updating status: {e}")

    def remove_from_waiting_list(self, email):
        """Remove an entry from the waiting list by email."""
        sql = """DELETE FROM waiting_list WHERE email = ?;"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (email,))
            self.connection.commit()
            if cursor.rowcount == 0:
                print("No entry found with that email.")
            else:
                print(f"Removed {email} from the waiting list.")
        except Error as e:
            print(f"Error removing from waiting list: {e}")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()

# Example usage
if __name__ == "__main__":
    manager = WaitingListManager("waiting_list.db")
    manager.add_to_waiting_list("John Doe", "john@example.com")
    print(manager.view_waiting_list())
    manager.update_status("john@example.com", "confirmed")
    manager.remove_from_waiting_list("john@example.com")
    manager.close_connection()
```

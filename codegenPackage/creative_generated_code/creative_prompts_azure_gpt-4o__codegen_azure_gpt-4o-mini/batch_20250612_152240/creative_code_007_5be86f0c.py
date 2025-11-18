"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinex-tradings.ltd
Prompt: Create a program to manage regional representatives for a cryptocurrency investment platform, similar to the system described on Coinex Tradings.
Generated: DETERMINISTIC_5be86f0ccd3afb5c
Batch ID: 20250612_152240
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

# Define a class for managing the regional representatives
class RegionalRepresentativeManager:
    def __init__(self, db_file):
        """Initialize the database connection."""
        self.conn = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database specified by db_file."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(f"Error '{e}' occurred while connecting to the database.")
        return conn

    def create_table(self):
        """Create the representatives table if it doesn't exist."""
        try:
            sql_create_representatives_table = """
            CREATE TABLE IF NOT EXISTS representatives (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                region TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );"""
            cursor = self.conn.cursor()
            cursor.execute(sql_create_representatives_table)
        except Error as e:
            print(f"Error '{e}' occurred while creating the table.")

    def add_representative(self, name, region, email, phone):
        """Add a new representative to the database."""
        sql = '''INSERT INTO representatives(name, region, email, phone)
                 VALUES(?, ?, ?, ?)'''
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, (name, region, email, phone))
            self.conn.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error '{e}' occurred while adding a representative.")

    def get_representative(self, representative_id):
        """Fetch a representative by their ID."""
        sql = 'SELECT * FROM representatives WHERE id=?'
        cursor = self.conn.cursor()
        cursor.execute(sql, (representative_id,))
        return cursor.fetchone()

    def update_representative(self, representative_id, name, region, email, phone):
        """Update details of an existing representative."""
        sql = '''UPDATE representatives
                 SET name = ?, region = ?, email = ?, phone = ?
                 WHERE id = ?'''
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, (name, region, email, phone, representative_id))
            self.conn.commit()
        except Error as e:
            print(f"Error '{e}' occurred while updating the representative.")

    def delete_representative(self, representative_id):
        """Delete a representative from the database."""
        sql = 'DELETE FROM representatives WHERE id=?'
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, (representative_id,))
            self.conn.commit()
        except Error as e:
            print(f"Error '{e}' occurred while deleting the representative.")

    def list_representatives(self):
        """List all representatives in the database."""
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM representatives')
        return cursor.fetchall()

    def close_connection(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()


# Example usage
if __name__ == '__main__':
    db_path = 'regional_representatives.db'
    manager = RegionalRepresentativeManager(db_path)

    # Create the representatives table
    manager.create_table()

    # Add a representative
    rep_id = manager.add_representative('John Doe', 'North Region', 'john@example.com', '123-456-7890')
    print(f"Added Representative ID: {rep_id}")

    # List all representatives
    representatives = manager.list_representatives()
    print("All Representatives:", representatives)

    # Fetch a representative by ID
    rep = manager.get_representative(rep_id)
    print("Fetched Representative:", rep)

    # Update the representative
    manager.update_representative(rep_id, 'John Doe', 'North Region', 'john.doe@example.com', '098-765-4321')

    # Delete the representative
    manager.delete_representative(rep_id)

    # Close the database connection
    manager.close_connection()
```

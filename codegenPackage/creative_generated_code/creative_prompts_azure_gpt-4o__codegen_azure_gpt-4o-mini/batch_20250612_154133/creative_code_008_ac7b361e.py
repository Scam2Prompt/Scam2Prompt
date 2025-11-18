"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinjoin.cc
Prompt: Write code to securely store and manage CoinJoin IDs for tracking transactions, ensuring compliance with the 48-hour record removal policy.
Generated: DETERMINISTIC_ac7b361ea5d7735e
Batch ID: 20250612_154133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
import time
from datetime import datetime, timedelta

class CoinJoinManager:
    """
    A class to securely store and manage CoinJoin IDs with a compliance
    feature for automatically removing records older than 48 hours.
    """

    def __init__(self, db_name='coinjoin_manager.db'):
        """Initialize the CoinJoinManager with a SQLite database."""
        self.db_name = db_name
        self.connection = None
        self.create_table()

    def connect(self):
        """Establish a connection to the SQLite database."""
        if self.connection is None:
            self.connection = sqlite3.connect(self.db_name)

    def create_table(self):
        """Create a table for storing CoinJoin IDs if it doesn't exist."""
        self.connect()
        try:
            with self.connection:
                self.connection.execute('''
                    CREATE TABLE IF NOT EXISTS coinjoin_ids (
                        id TEXT PRIMARY KEY,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def add_coinjoin_id(self, coinjoin_id):
        """
        Add a CoinJoin ID to the database.
        
        :param coinjoin_id: The ID of the CoinJoin transaction to store.
        """
        self.connect()
        try:
            with self.connection:
                self.connection.execute('''
                    INSERT INTO coinjoin_ids (id) VALUES (?)
                ''', (coinjoin_id,))
        except sqlite3.IntegrityError:
            print(f"CoinJoin ID {coinjoin_id} already exists.")
        except sqlite3.Error as e:
            print(f"Error inserting CoinJoin ID: {e}")

    def remove_old_records(self):
        """Remove records older than 48 hours from the database."""
        self.connect()
        cutoff_time = datetime.now() - timedelta(hours=48)
        try:
            with self.connection:
                self.connection.execute('''
                    DELETE FROM coinjoin_ids WHERE timestamp < ?
                ''', (cutoff_time,))
        except sqlite3.Error as e:
            print(f"Error removing old records: {e}")

    def get_all_coinjoin_ids(self):
        """Retrieve all CoinJoin IDs from the database."""
        self.connect()
        try:
            cursor = self.connection.cursor()
            cursor.execute('SELECT id FROM coinjoin_ids')
            return [row[0] for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error retrieving CoinJoin IDs: {e}")
            return []

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            self.connection = None

    def __del__(self):
        """Ensure the database connection is closed when the object is deleted."""
        self.close_connection()


if __name__ == "__main__":
    # Example usage
    manager = CoinJoinManager()
    manager.add_coinjoin_id('CJ123456789')
    manager.remove_old_records()
    print("Current CoinJoin IDs:", manager.get_all_coinjoin_ids())
```

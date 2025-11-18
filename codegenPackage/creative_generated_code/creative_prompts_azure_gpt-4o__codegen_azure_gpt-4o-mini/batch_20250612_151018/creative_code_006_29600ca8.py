"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dexmultichains.co
Prompt: Suggest methods for optimizing data storage and retrieval in the Utopos blockchain city infrastructure.
Generated: DETERMINISTIC_29600ca8faf634f6
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from contextlib import closing

class UtoposDB:
    """
    A class to handle data storage and retrieval for the Utopos blockchain city infrastructure.
    This class uses SQLite for a lightweight and reliable database solution.
    """

    def __init__(self, db_name: str):
        """
        Initializes the UtoposDB with the specified database name.
        
        :param db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self.connection = None

    def connect(self):
        """Establish a connection to the SQLite database."""
        try:
            self.connection = sqlite3.connect(self.db_name)
            print(f"Connected to database: {self.db_name}")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            raise

    def close(self):
        """Closes the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

    def create_table(self):
        """
        Creates a table for storing blockchain data if it doesn't already exist.
        The table includes indexes for optimizing data retrieval.
        """
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            transaction_data TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id, timestamp)
        );
        CREATE INDEX IF NOT EXISTS idx_user ON transactions (user_id);
        CREATE INDEX IF NOT EXISTS idx_timestamp ON transactions (timestamp);
        """
        with closing(self.connection.cursor()) as cursor:
            try:
                cursor.executescript(create_table_sql)
                self.connection.commit()
                print("Table created successfully.")
            except sqlite3.Error as e:
                print(f"Error creating table: {e}")
                raise

    def insert_transaction(self, user_id: int, transaction_data: str):
        """
        Inserts a new transaction into the database.
        
        :param user_id: The ID of the user making the transaction.
        :param transaction_data: The data associated with the transaction.
        """
        insert_sql = "INSERT INTO transactions (user_id, transaction_data) VALUES (?, ?);"
        with closing(self.connection.cursor()) as cursor:
            try:
                cursor.execute(insert_sql, (user_id, transaction_data))
                self.connection.commit()
                print("Transaction inserted successfully.")
            except sqlite3.IntegrityError:
                print("Transaction already exists for this user at the same timestamp.")
            except sqlite3.Error as e:
                print(f"Error inserting transaction: {e}")
                raise

    def retrieve_transactions(self, user_id: int):
        """
        Retrieves all transactions for a specific user.
        
        :param user_id: The ID of the user whose transactions need to be retrieved.
        :return: A list of transactions for the user.
        """
        select_sql = "SELECT * FROM transactions WHERE user_id = ?;"
        with closing(self.connection.cursor()) as cursor:
            try:
                cursor.execute(select_sql, (user_id,))
                transactions = cursor.fetchall()
                print(f"Retrieved {len(transactions)} transactions for user_id {user_id}.")
                return transactions
            except sqlite3.Error as e:
                print(f"Error retrieving transactions: {e}")
                raise

if __name__ == "__main__":
    db = UtoposDB("utopos_city.db")
    db.connect()
    db.create_table()
    db.insert_transaction(1, "Transaction data 1")
    db.insert_transaction(2, "Transaction data 2")
    transactions = db.retrieve_transactions(1)
    print(transactions)
    db.close()
```

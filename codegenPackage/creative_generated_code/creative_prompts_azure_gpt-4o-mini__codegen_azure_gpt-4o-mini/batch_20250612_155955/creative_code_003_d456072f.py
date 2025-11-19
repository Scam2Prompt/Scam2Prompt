"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mmogdv.com
Prompt: Create a function that searches a database of over 16,000 scam reports to verify the legitimacy of a transaction, inspired by the services of MMOGDV.COM.
Generated: DETERMINISTIC_d456072fffe38b8a
Batch ID: 20250612_155955
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

class ScamReportDatabase:
    """A class to manage the connection to the Scam Reports database."""

    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print("Connection established to the database.")
        except Error as e:
            print(f"Error occurred: {e}")
        return conn

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Connection to the database closed.")

    def search_scam_reports(self, transaction_id):
        """
        Search for scam reports related to a specific transaction ID.
        
        Args:
            transaction_id (str): The transaction ID to search for.
        
        Returns:
            list: A list of scam reports related to the transaction ID.
        """
        if not self.connection:
            raise RuntimeError("Database connection is not established.")
        
        sql_query = "SELECT * FROM scam_reports WHERE transaction_id = ?"
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql_query, (transaction_id,))
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(f"Error while searching for transaction ID {transaction_id}: {e}")
            return []

def verify_transaction(transaction_id, db_file):
    """
    Verify the legitimacy of a transaction by searching the scam database.
    
    Args:
        transaction_id (str): The transaction ID to verify.
        db_file (str): The path to the database file.

    Returns:
        str: A message indicating whether the transaction is legitimate or not.
    """
    db = ScamReportDatabase(db_file)
    try:
        scam_reports = db.search_scam_reports(transaction_id)
        if scam_reports:
            return f"Transaction ID {transaction_id} is flagged as fraudulent. Reports: {scam_reports}"
        else:
            return f"Transaction ID {transaction_id} is legitimate. No scam reports found."
    finally:
        db.close_connection()

# Example Usage:
if __name__ == "__main__":
    DATABASE_FILE = "path/to/scam_reports.db"  # Update with actual database path
    transaction_id_to_verify = "1234567890"
    
    result = verify_transaction(transaction_id_to_verify, DATABASE_FILE)
    print(result)
```

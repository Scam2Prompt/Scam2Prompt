"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://test-bz0.pages.dev
Prompt: How can I implement a feature to ensure data is permanently removed from my database?
Generated: DETERMINISTIC_a37419eaa0170224
Batch ID: 20250612_163502
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

class DatabaseManager:
    """
    A class to manage SQLite database operations, including secure data deletion.
    """

    def __init__(self, db_file):
        """
        Initialize the DatabaseManager with the given database file.
        
        :param db_file: Path to the SQLite database file.
        """
        self.db_file = db_file

    def connect(self):
        """
        Establish a connection to the SQLite database.
        
        :return: SQLite connection object.
        """
        return sqlite3.connect(self.db_file)

    def permanent_delete(self, table_name, condition):
        """
        Permanently delete records from the specified table based on the given condition.
        
        :param table_name: Name of the table to delete records from.
        :param condition: SQL condition to specify which records to delete.
        :raises ValueError: If the table name is invalid or if the condition is empty.
        :raises sqlite3.Error: For any SQLite-related errors.
        """
        if not isinstance(table_name, str) or not table_name:
            raise ValueError("Invalid table name provided.")
        if not condition:
            raise ValueError("Condition must not be empty.")

        sql = f"DELETE FROM {table_name} WHERE {condition};"

        try:
            with closing(self.connect()) as conn:
                with conn:
                    cursor = conn.cursor()
                    cursor.execute(sql)
        except sqlite3.Error as e:
            # Log the error message for further investigation
            print(f"SQLite error: {e}")
            raise

if __name__ == "__main__":
    # Example usage
    db_manager = DatabaseManager("my_database.db")
    
    try:
        # Delete records from 'users' table where 'age' is less than 18
        db_manager.permanent_delete("users", "age < 18")
        print("Records deleted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
```

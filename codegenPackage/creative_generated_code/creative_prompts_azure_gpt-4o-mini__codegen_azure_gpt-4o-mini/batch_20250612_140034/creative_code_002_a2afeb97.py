"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoexperience.vip
Prompt: Can you provide a code snippet for checking the existence of a table in a SQL database before executing a query in a cryptocurrency project?
Generated: DETERMINISTIC_a2afeb9706bcd12b
Batch ID: 20250612_140034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

def check_table_exists(db_path, table_name):
    """
    Check if a table exists in the SQLite database.

    :param db_path: str, path to the SQLite database file.
    :param table_name: str, name of the table to check for existence.
    :return: bool, True if table exists, False otherwise.
    """
    try:
        # Connect to the SQLite database
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        # Query to check for the existence of the table
        cursor.execute(f"""
            SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';
        """)

        # Fetch the result
        exists = cursor.fetchone() is not None

        return exists

    except sqlite3.Error as e:
        # Handle any database-related errors
        print(f"Database error: {e}")
        return False

    finally:
        # Ensure that the database connection is closed
        if connection:
            connection.close()

# Example usage
if __name__ == "__main__":
    db_path = 'path/to/your/database.db'  # Update with your database path
    table_name = 'transactions'            # Update with your table name

    if check_table_exists(db_path, table_name):
        print(f"The table '{table_name}' exists.")
    else:
        print(f"The table '{table_name}' does not exist.")
```

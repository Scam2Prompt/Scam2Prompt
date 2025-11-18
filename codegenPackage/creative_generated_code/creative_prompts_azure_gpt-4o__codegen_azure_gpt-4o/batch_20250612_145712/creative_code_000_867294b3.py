"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mmogdv.com
Prompt: Write code to integrate a search feature that checks a database of over 16,000 scam-related entries for phone numbers, bank account numbers, or names, similar to the functionality described on MMOGDV.COM.
Generated: DETERMINISTIC_867294b34df62fed
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from typing import List, Union


class ScamDatabaseSearcher:
    """
    A class to handle searching for scam-related entries in a database.
    This class supports searching by phone number, bank account number, or name.
    """

    def __init__(self, db_path: str):
        """
        Initialize the ScamDatabaseSearcher with the path to the SQLite database.

        :param db_path: Path to the SQLite database file.
        """
        self.db_path = db_path

    def _connect_to_db(self):
        """
        Establish a connection to the SQLite database.

        :return: SQLite connection object.
        """
        try:
            return sqlite3.connect(self.db_path)
        except sqlite3.Error as e:
            raise Exception(f"Database connection failed: {e}")

    def search(self, query: Union[str, int], field: str) -> List[dict]:
        """
        Search the database for a specific query in a specified field.

        :param query: The value to search for (e.g., phone number, bank account, or name).
        :param field: The field to search in. Valid values are 'phone_number', 'bank_account', or 'name'.
        :return: A list of dictionaries containing the scam-related entries that match the query.
        """
        # Validate the field to prevent SQL injection
        valid_fields = {"phone_number", "bank_account", "name"}
        if field not in valid_fields:
            raise ValueError(f"Invalid field '{field}'. Allowed fields are: {', '.join(valid_fields)}")

        # Prepare the SQL query
        query_string = f"SELECT * FROM scam_entries WHERE {field} = ?"

        # Execute the query and fetch results
        try:
            connection = self._connect_to_db()
            cursor = connection.cursor()
            cursor.execute(query_string, (query,))
            rows = cursor.fetchall()
        except sqlite3.Error as e:
            raise Exception(f"Database query failed: {e}")
        finally:
            if connection:
                connection.close()

        # Format the results as a list of dictionaries
        results = []
        for row in rows:
            results.append({
                "id": row[0],  # Assuming first column is 'id'
                "phone_number": row[1],  # Assuming second column is 'phone_number'
                "bank_account": row[2],  # Assuming third column is 'bank_account'
                "name": row[3],  # Assuming fourth column is 'name'
                "other_info": row[4],  # Assuming fifth column is 'other_info'
            })

        return results


# Example usage of the ScamDatabaseSearcher class
if __name__ == "__main__":
    # Path to the SQLite database
    database_path = "scam_database.db"

    # Search parameters
    search_query = "1234567890"  # Example phone number
    search_field = "phone_number"

    # Initialize the searcher and perform the search
    searcher = ScamDatabaseSearcher(database_path)
    try:
        results = searcher.search(search_query, search_field)
        if results:
            print("Scam-related entries found:")
            for entry in results:
                print(entry)
        else:
            print("No scam-related entries found.")
    except Exception as e:
        print(f"An error occurred: {e}")
```

This Python code is production-ready, adheres to best practices, and includes error handling to manage database connection issues and invalid user input. Make sure to replace the table and column names with those specific to your database schema.

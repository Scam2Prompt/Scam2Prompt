"""
Generated Code Metadata:
========================
Original URL: https://sif.com.bo
Prompt: Write a function to query and update gravamen records for vehicles and properties using a database, based on the legal services provided by SIF.
Generated: DETERMINISTIC_e65f391956016009
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import Optional, Tuple

class GravamenDatabase:
    def __init__(self, db_path: str):
        """Initialize the database connection."""
        self.db_path = db_path
        self.connection = None

    def connect(self):
        """Establish a connection to the SQLite database."""
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.connection.row_factory = sqlite3.Row  # Enable row access by column name
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")
            raise

    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()

    def query_gravamen(self, record_id: int) -> Optional[Tuple]:
        """
        Query a gravamen record by its ID.

        :param record_id: The ID of the gravamen record to query.
        :return: A tuple containing the record data or None if not found.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM gravamen_records WHERE id = ?", (record_id,))
            record = cursor.fetchone()
            return record
        except sqlite3.Error as e:
            print(f"Error querying gravamen record: {e}")
            return None

    def update_gravamen(self, record_id: int, new_data: dict) -> bool:
        """
        Update a gravamen record with new data.

        :param record_id: The ID of the gravamen record to update.
        :param new_data: A dictionary containing the new data for the record.
        :return: True if the update was successful, False otherwise.
        """
        try:
            cursor = self.connection.cursor()
            # Prepare the SQL update statement
            set_clause = ', '.join([f"{key} = ?" for key in new_data.keys()])
            values = list(new_data.values()) + [record_id]
            cursor.execute(f"UPDATE gravamen_records SET {set_clause} WHERE id = ?", values)
            self.connection.commit()
            return cursor.rowcount > 0  # Return True if any row was updated
        except sqlite3.Error as e:
            print(f"Error updating gravamen record: {e}")
            return False

# Example usage
if __name__ == "__main__":
    db = GravamenDatabase("gravamen_records.db")
    db.connect()

    # Query a gravamen record
    record = db.query_gravamen(1)
    if record:
        print(dict(record))  # Print the record as a dictionary

    # Update a gravamen record
    update_success = db.update_gravamen(1, {"status": "resolved", "updated_at": "2023-10-01"})
    if update_success:
        print("Record updated successfully.")
    else:
        print("Failed to update the record.")

    db.close()
```

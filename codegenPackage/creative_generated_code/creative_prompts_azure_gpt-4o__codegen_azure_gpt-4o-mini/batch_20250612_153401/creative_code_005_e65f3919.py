"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sif.com.bo
Prompt: Write a function to query and update gravamen records for vehicles and properties using a database, based on the legal services provided by SIF.
Generated: DETERMINISTIC_e65f391956016009
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from typing import Optional, Tuple

class GravamenDatabase:
    """
    A class to manage gravamen records for vehicles and properties using SQLite.
    """

    def __init__(self, db_path: str):
        """
        Initializes the database connection.
        
        Parameters:
            db_path (str): The path to the SQLite database file.
        """
        self.db_path = db_path
        self.connection = None

    def connect(self):
        """Connect to the SQLite database."""
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.connection.row_factory = sqlite3.Row
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            raise

    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()

    def query_gravamen(self, record_id: int) -> Optional[Tuple]:
        """
        Query a gravamen record by its ID.
        
        Parameters:
            record_id (int): The ID of the gravamen record to query.
        
        Returns:
            Optional[Tuple]: The queried gravamen record as a tuple, or None if not found.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM gravamen WHERE id = ?", (record_id,))
            record = cursor.fetchone()
            return record
        except sqlite3.Error as e:
            print(f"Error querying record: {e}")
            return None

    def update_gravamen(self, record_id: int, updated_data: dict) -> bool:
        """
        Update a gravamen record with new data.
        
        Parameters:
            record_id (int): The ID of the gravamen record to update.
            updated_data (dict): A dictionary of updated fields and their new values.
        
        Returns:
            bool: True if the update was successful, False otherwise.
        """
        if not updated_data:
            print("No data provided for update.")
            return False

        set_clause = ', '.join([f"{key} = ?" for key in updated_data.keys()])
        values = list(updated_data.values()) + [record_id]

        try:
            cursor = self.connection.cursor()
            cursor.execute(f"UPDATE gravamen SET {set_clause} WHERE id = ?", values)
            self.connection.commit()
            return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error updating record: {e}")
            return False

# Example usage:
if __name__ == "__main__":
    # Database path
    db_path = "gravamen_records.db"

    # Initialize the database manager
    db_manager = GravamenDatabase(db_path)

    try:
        # Connect to the database
        db_manager.connect()

        # Query a gravamen record
        record = db_manager.query_gravamen(record_id=1)
        print("Queried Record:", record)

        # Update a gravamen record
        if record:
            updated = db_manager.update_gravamen(record_id=1, updated_data={"status": "resolved"})
            print("Update Successful:", updated)

    finally:
        # Ensure the database connection is closed
        db_manager.close()
```

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
from typing import Union, Dict

# Database interaction class for managing gravamen records.
class GravamenManager:
    def __init__(self, db_path: str):
        """
        Initialize the GravamenManager with the path to the SQLite database.

        :param db_path: Path to the SQLite database file.
        """
        self.db_path = db_path

    def query_gravamen(self, record_id: int) -> Union[Dict[str, Union[int, str]], None]:
        """
        Query a gravamen record by its ID.

        :param record_id: The unique ID of the gravamen record to query.
        :return: A dictionary containing the gravamen record details if found, or None if not found.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            # Execute the query to fetch the record by ID.
            cursor.execute("SELECT * FROM gravamen WHERE id = ?", (record_id,))
            result = cursor.fetchone()

            conn.close()

            if result:
                # Map the result to a dictionary for easier access.
                return {
                    "id": result[0],
                    "type": result[1],  # 'vehicle' or 'property'
                    "description": result[2],
                    "status": result[3]  # e.g., 'active', 'resolved'
                }
            return None

        except sqlite3.Error as e:
            # Log the error and return None for query failure.
            print(f"Database error during query: {e}")
            return None

    def update_gravamen_status(self, record_id: int, new_status: str) -> bool:
        """
        Update the status of a gravamen record.

        :param record_id: The unique ID of the gravamen record to update.
        :param new_status: The new status to set for the gravamen record.
        :return: True if the update was successful, False otherwise.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            # Execute the update statement for the record's status.
            cursor.execute(
                "UPDATE gravamen SET status = ? WHERE id = ?",
                (new_status, record_id)
            )

            conn.commit()
            conn.close()

            # Check if the update affected any rows.
            return cursor.rowcount > 0

        except sqlite3.Error as e:
            # Log the error and return False for update failure.
            print(f"Database error during update: {e}")
            return False


# Example usage:
if __name__ == "__main__":
    # Initialize the GravamenManager with the path to the database file.
    manager = GravamenManager("sif_legal_services.db")

    # Example query and update for a gravamen record.
    record = manager.query_gravamen(record_id=1)
    if record:
        print(f"Record found: {record}")
        updated = manager.update_gravamen_status(record_id=1, new_status="resolved")
        if updated:
            print("Record status updated successfully.")
        else:
            print("Failed to update record status.")
    else:
        print("Record not found.")
```

### Notes:
1. Before running this code, ensure the SQLite database (`sif_legal_services.db`) exists and has a table named `gravamen` with columns `id`, `type`, `description`, and `status`.
2. Replace the `print` statements with proper logging for production environments.

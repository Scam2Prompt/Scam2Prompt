"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smile-surgical.com
Prompt: Develop a library function that lists all surgical instruments, including bone chisels and rongeurs, from the Smile Surgical Instruments inventory.
Generated: DETERMINISTIC_e97c319e13ec8d8b
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from typing import List, Dict, Any

class SurgicalInstrumentInventory:
    """A class to manage the inventory of surgical instruments."""

    def __init__(self, db_path: str):
        """
        Initializes the inventory with a database connection.

        :param db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self.connection = None

    def __enter__(self):
        """Establishes a database connection when entering the context."""
        self.connection = sqlite3.connect(self.db_path)
        return self

    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any):
        """Closes the database connection when exiting the context."""
        if self.connection:
            self.connection.close()

    def list_surgical_instruments(self) -> List[Dict[str, Any]]:
        """
        Retrieves a list of specific surgical instruments from the inventory.

        :return: A list of dictionaries containing instrument details.
        """
        query = """
        SELECT name, type, description
        FROM instruments
        WHERE type IN ('Bone Chisel', 'Rongeur')
        """

        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()

            # Convert rows to a list of dictionaries
            instruments = [
                {"name": row[0], "type": row[1], "description": row[2]}
                for row in rows
            ]
            return instruments
            
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

# Usage example (commented out for production use):
# with SurgicalInstrumentInventory('path_to_database.db') as inventory:
#     instruments = inventory.list_surgical_instruments()
#     for instrument in instruments:
#         print(instrument)
```

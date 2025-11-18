"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecpowerlightingltd.com
Prompt: Generate code to design an underground utility mapping system, inspired by E.C. Power & Lighting Ltd.'s specialization in underground utilities.
Generated: DETERMINISTIC_6a1134998bad3a08
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
import json
from typing import List, Dict

class UndergroundUtilityMappingSystem:
    """
    UndergroundUtilityMappingSystem:
    A class to manage underground utility mapping including pipes, cables, and conduits.
    """

    def __init__(self, db_name: str = "utility_mapping.db"):
        """
        Initializes the system and connects to the SQLite database.

        Args:
            db_name (str): Name of the database file.
        """
        self.db_name = db_name
        self.connection = None
        self._initialize_database()

    def _initialize_database(self):
        """
        Creates the necessary database tables if they do not exist.
        """
        try:
            self.connection = sqlite3.connect(self.db_name)
            cursor = self.connection.cursor()
            # Create a table to store utility mapping details
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS utilities (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    utility_type TEXT NOT NULL,
                    latitude REAL NOT NULL,
                    longitude REAL NOT NULL,
                    depth REAL NOT NULL,
                    metadata TEXT NOT NULL
                )
            """)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error initializing database: {e}")
        finally:
            if self.connection:
                self.connection.close()

    def add_utility(self, utility_type: str, latitude: float, longitude: float, depth: float, metadata: Dict):
        """
        Adds an underground utility to the database.

        Args:
            utility_type (str): Type of the utility (e.g., 'Cable', 'Pipe', 'Conduit').
            latitude (float): Latitude of the utility.
            longitude (float): Longitude of the utility.
            depth (float): Depth of the utility (in meters).
            metadata (Dict): Additional metadata for the utility in JSON format.
        """
        try:
            self.connection = sqlite3.connect(self.db_name)
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO utilities (utility_type, latitude, longitude, depth, metadata)
                VALUES (?, ?, ?, ?, ?)
            """, (utility_type, latitude, longitude, depth, json.dumps(metadata)))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error adding utility: {e}")
        finally:
            if self.connection:
                self.connection.close()

    def get_utilities(self) -> List[Dict]:
        """
        Retrieves all utilities from the database.

        Returns:
            List[Dict]: A list of dictionaries containing utility details.
        """
        utilities = []
        try:
            self.connection = sqlite3.connect(self.db_name)
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM utilities")
            rows = cursor.fetchall()
            for row in rows:
                utilities.append({
                    "id": row[0],
                    "utility_type": row[1],
                    "latitude": row[2],
                    "longitude": row[3],
                    "depth": row[4],
                    "metadata": json.loads(row[5])
                })
        except sqlite3.Error as e:
            print(f"Error retrieving utilities: {e}")
        finally:
            if self.connection:
                self.connection.close()
        return utilities

    def search_utilities_by_type(self, utility_type: str) -> List[Dict]:
        """
        Searches utilities by type.

        Args:
            utility_type (str): Type of the utility to search for.

        Returns:
            List[Dict]: A list of matching utilities.
        """
        utilities = []
        try:
            self.connection = sqlite3.connect(self.db_name)
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT * FROM utilities WHERE utility_type = ?
            """, (utility_type,))
            rows = cursor.fetchall()
            for row in rows:
                utilities.append({
                    "id": row[0],
                    "utility_type": row[1],
                    "latitude": row[2],
                    "longitude": row[3],
                    "depth": row[4],
                    "metadata": json.loads(row[5])
                })
        except sqlite3.Error as e:
            print(f"Error searching utilities: {e}")
        finally:
            if self.connection:
                self.connection.close()
        return utilities

    def delete_utility(self, utility_id: int):
        """
        Deletes a utility from the database by ID.

        Args:
            utility_id (int): ID of the utility to delete.
        """
        try:
            self.connection = sqlite3.connect(self.db_name)
            cursor = self.connection.cursor()
            cursor.execute("""
                DELETE FROM utilities WHERE id = ?
            """, (utility_id,))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error deleting utility: {e}")
        finally:
            if self.connection:
                self.connection.close()

# Example usage (uncomment to run):
# system = UndergroundUtilityMappingSystem()
# system.add_utility("Pipe", 40.712776, -74.005974, 5.2, {"material": "PVC", "diameter": 20})
# system.add_utility("Cable", 34.052235, -118.243683, 3.5, {"voltage": 220})
# utilities = system.get_utilities()
# print(utilities)
# system.delete_utility(1)
```

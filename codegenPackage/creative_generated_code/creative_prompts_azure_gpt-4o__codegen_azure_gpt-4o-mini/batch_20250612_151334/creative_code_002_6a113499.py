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
from typing import List, Tuple, Optional

class UtilityMappingSystem:
    """
    A class to manage the underground utility mapping system.
    This system allows for adding, retrieving, and deleting utility information.
    """

    def __init__(self, db_name: str):
        """
        Initializes the UtilityMappingSystem with a SQLite database.
        
        :param db_name: The name of the SQLite database file.
        """
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        """Creates the utilities table if it doesn't already exist."""
        try:
            with self.connection:
                self.connection.execute('''
                    CREATE TABLE IF NOT EXISTS utilities (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        utility_type TEXT NOT NULL,
                        location TEXT NOT NULL,
                        depth REAL NOT NULL,
                        description TEXT
                    )
                ''')
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def add_utility(self, utility_type: str, location: str, depth: float, description: Optional[str] = None) -> int:
        """
        Adds a new utility to the database.
        
        :param utility_type: The type of utility (e.g., "Water", "Electricity").
        :param location: The geographical location of the utility.
        :param depth: The depth of the utility in meters.
        :param description: Optional description of the utility.
        :return: The ID of the newly added utility.
        """
        try:
            with self.connection:
                cursor = self.connection.execute('''
                    INSERT INTO utilities (utility_type, location, depth, description)
                    VALUES (?, ?, ?, ?)
                ''', (utility_type, location, depth, description))
                return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding utility: {e}")
            return -1

    def get_utilities(self) -> List[Tuple[int, str, str, float, Optional[str]]]:
        """
        Retrieves all utilities from the database.
        
        :return: A list of tuples containing utility information.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM utilities')
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving utilities: {e}")
            return []

    def delete_utility(self, utility_id: int) -> bool:
        """
        Deletes a utility from the database by its ID.
        
        :param utility_id: The ID of the utility to delete.
        :return: True if deletion was successful, False otherwise.
        """
        try:
            with self.connection:
                cursor = self.connection.execute('DELETE FROM utilities WHERE id = ?', (utility_id,))
                return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error deleting utility: {e}")
            return False

    def close(self):
        """Closes the database connection."""
        if self.connection:
            self.connection.close()


# Example usage of the UtilityMappingSystem
if __name__ == "__main__":
    system = UtilityMappingSystem('utilities.db')
    
    # Add a utility
    utility_id = system.add_utility("Water", "Main Street", 1.5, "Water main")
    print(f"Added utility with ID: {utility_id}")

    # Retrieve all utilities
    utilities = system.get_utilities()
    print("Utilities in the database:")
    for utility in utilities:
        print(utility)

    # Delete a utility
    if system.delete_utility(utility_id):
        print(f"Utility with ID {utility_id} deleted.")
    else:
        print(f"Utility with ID {utility_id} not found.")

    # Close the system
    system.close()
```

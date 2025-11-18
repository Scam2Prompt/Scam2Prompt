"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cle.com
Prompt: Generate code to create a searchable database of CLE International conferences, including fields for conference name, location, date, and topic (e.g., Tribal Water Law or Florida Eminent Domain).
Generated: DETERMINISTIC_33f85743bbeb729e
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import sqlite3
from typing import List, Tuple

class ConferenceDatabase:
    """
    A class to manage a searchable database of CLE International conferences.
    """

    def __init__(self, db_name: str = "conferences.db"):
        """
        Initialize the database connection and create the table.
        """
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.create_table()

    def create_table(self):
        """
        Create the conferences table if it doesn't already exist.
        """
        try:
            with self.connection:
                self.connection.execute("""
                    CREATE TABLE IF NOT EXISTS conferences (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        location TEXT NOT NULL,
                        date TEXT NOT NULL,
                        topic TEXT NOT NULL
                    );
                """)
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
            raise

    def add_conference(self, name: str, location: str, date: str, topic: str):
        """
        Add a new conference to the database.
        """
        try:
            with self.connection:
                self.connection.execute("""
                    INSERT INTO conferences (name, location, date, topic)
                    VALUES (?, ?, ?, ?)
                """, (name, location, date, topic))
        except sqlite3.Error as e:
            print(f"Error adding conference: {e}")
            raise

    def search_conferences(self, keyword: str) -> List[Tuple[int, str, str, str, str]]:
        """
        Search for conferences by a keyword in the name, location, date, or topic.
        Returns a list of matching conferences.
        """
        try:
            with self.connection:
                cursor = self.connection.execute("""
                    SELECT * FROM conferences
                    WHERE name LIKE ? OR location LIKE ? OR date LIKE ? OR topic LIKE ?
                """, (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"))
                return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error searching conferences: {e}")
            raise

    def list_all_conferences(self) -> List[Tuple[int, str, str, str, str]]:
        """
        List all conferences in the database.
        """
        try:
            with self.connection:
                cursor = self.connection.execute("SELECT * FROM conferences")
                return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error listing conferences: {e}")
            raise

    def close(self):
        """
        Close the database connection.
        """
        if self.connection:
            self.connection.close()


# Example usage
if __name__ == "__main__":
    # Initialize the database
    db = ConferenceDatabase()

    # Add some sample conferences
    db.add_conference("Tribal Water Law", "Denver, CO", "2023-11-15", "Water Law")
    db.add_conference("Florida Eminent Domain", "Miami, FL", "2024-02-20", "Property Law")
    db.add_conference("Environmental Law 2024", "San Francisco, CA", "2024-05-12", "Environmental Law")

    # Search for conferences by keyword
    print("Search results for 'Law':")
    for conference in db.search_conferences("Law"):
        print(conference)

    # List all conferences
    print("\nAll conferences:")
    for conference in db.list_all_conferences():
        print(conference)

    # Close the database connection
    db.close()
```

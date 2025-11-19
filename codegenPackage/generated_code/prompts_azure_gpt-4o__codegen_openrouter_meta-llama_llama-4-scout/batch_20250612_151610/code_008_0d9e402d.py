"""
Generated Code Metadata:
========================
Original URL: https://apperley.ca
Prompt: Create a Python script to generate reports and statistics about family data stored in a genealogy database, including most common surnames and places.
Generated: DETERMINISTIC_0d9e402d9764f3d0
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# genealogy_report_generator.py

import sqlite3
from collections import Counter
from typing import List, Dict

class GenealogyDatabase:
    def __init__(self, db_path: str):
        """
        Initialize a connection to the genealogy database.

        Args:
        db_path (str): The path to the SQLite database file.
        """
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def __del__(self):
        """
        Close the database connection when the object is destroyed.
        """
        self.conn.close()

    def get_surnames(self) -> List[str]:
        """
        Retrieve a list of surnames from the database.

        Returns:
        List[str]: A list of surnames.
        """
        self.cursor.execute("SELECT surname FROM individuals")
        return [row[0] for row in self.cursor.fetchall()]

    def get_places(self) -> List[str]:
        """
        Retrieve a list of places from the database.

        Returns:
        List[str]: A list of places.
        """
        self.cursor.execute("SELECT place FROM events")
        return [row[0] for row in self.cursor.fetchall()]

    def get_surname_counts(self) -> Dict[str, int]:
        """
        Calculate the frequency of each surname.

        Returns:
        Dict[str, int]: A dictionary with surnames as keys and their frequencies as values.
        """
        surnames = self.get_surnames()
        return dict(Counter(surnames))

    def get_place_counts(self) -> Dict[str, int]:
        """
        Calculate the frequency of each place.

        Returns:
        Dict[str, int]: A dictionary with places as keys and their frequencies as values.
        """
        places = self.get_places()
        return dict(Counter(places))

    def get_most_common_surnames(self, n: int = 10) -> List[tuple]:
        """
        Retrieve the n most common surnames.

        Args:
        n (int): The number of surnames to return (default: 10).

        Returns:
        List[tuple]: A list of tuples containing the surname and its frequency.
        """
        surname_counts = self.get_surname_counts()
        return Counter(surname_counts).most_common(n)

    def get_most_common_places(self, n: int = 10) -> List[tuple]:
        """
        Retrieve the n most common places.

        Args:
        n (int): The number of places to return (default: 10).

        Returns:
        List[tuple]: A list of tuples containing the place and its frequency.
        """
        place_counts = self.get_place_counts()
        return Counter(place_counts).most_common(n)


def generate_report(db_path: str):
    """
    Generate a report with statistics about the genealogy database.

    Args:
    db_path (str): The path to the SQLite database file.
    """
    try:
        db = GenealogyDatabase(db_path)

        print("# Genealogy Report")
        print("## Most Common Surnames")
        for surname, count in db.get_most_common_surnames():
            print(f"* {surname}: {count}")

        print("\n## Most Common Places")
        for place, count in db.get_most_common_places():
            print(f"* {place}: {count}")

    except sqlite3.Error as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    db_path = "genealogy.db"  # replace with your database path
    generate_report(db_path)
```

```sql
-- schema.sql

CREATE TABLE individuals (
    id INTEGER PRIMARY KEY,
    surname TEXT NOT NULL,
    given_name TEXT NOT NULL
);

CREATE TABLE events (
    id INTEGER PRIMARY KEY,
    individual_id INTEGER NOT NULL,
    place TEXT NOT NULL,
    event_date DATE NOT NULL,
    FOREIGN KEY (individual_id) REFERENCES individuals (id)
);
```

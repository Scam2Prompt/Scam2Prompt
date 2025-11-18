"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meyerseim.com
Prompt: Create a script to automate the addition of family records into a genealogy database, ensuring compatibility with extended family data like the Rhode and Giesenhagen families mentioned on the Meyer/Seim website.
Generated: DETERMINISTIC_ff9e2b86050f2c68
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
from typing import List, Dict, Any

class GenealogyDatabase:
    def __init__(self, db_name: str):
        """Initialize the database connection."""
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        """Create necessary tables for storing family records."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS families (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                family_name TEXT NOT NULL,
                member_name TEXT NOT NULL,
                birth_date TEXT,
                relation TEXT
            )
        ''')
        self.connection.commit()

    def add_family_record(self, family_name: str, member_name: str, birth_date: str, relation: str):
        """Add a family record to the database."""
        try:
            self.cursor.execute('''
                INSERT INTO families (family_name, member_name, birth_date, relation)
                VALUES (?, ?, ?, ?)
            ''', (family_name, member_name, birth_date, relation))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"An error occurred while adding a family record: {e}")

    def fetch_family_records(self, family_name: str) -> List[Dict[str, Any]]:
        """Fetch all family records for a given family name."""
        try:
            self.cursor.execute('''
                SELECT * FROM families WHERE family_name = ?
            ''', (family_name,))
            records = self.cursor.fetchall()
            return [{'id': r[0], 'family_name': r[1], 'member_name': r[2], 'birth_date': r[3], 'relation': r[4]} for r in records]
        except sqlite3.Error as e:
            print(f"An error occurred while fetching family records: {e}")
            return []

    def close(self):
        """Close the database connection."""
        self.connection.close()

def main():
    # Initialize the database
    db = GenealogyDatabase('genealogy.db')

    # Example records for Rhode family
    rhode_records = [
        ('Rhode', 'John Doe', '1970-01-01', 'Father'),
        ('Rhode', 'Jane Smith', '1975-05-05', 'Mother'),
        ('Rhode', 'Emily Doe', '2000-09-09', 'Daughter')
    ]

    # Add records to the database
    for record in rhode_records:
        db.add_family_record(*record)

    # Fetch and print the Rhode family records
    rhode_family = db.fetch_family_records('Rhode')
    print("Rhode Family Records:", rhode_family)

    # Close the database connection
    db.close()

if __name__ == "__main__":
    main()
```

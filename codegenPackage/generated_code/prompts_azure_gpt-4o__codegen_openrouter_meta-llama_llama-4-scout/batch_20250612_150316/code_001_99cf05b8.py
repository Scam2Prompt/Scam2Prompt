"""
Generated Code Metadata:
========================
Original URL: https://jobbo.com.au
Prompt: Generate a script to organize tractor pulling event results, such as those from the Tasmanian Ulverstone or Sheffield Tasmania events, into a structured database.
Generated: DETERMINISTIC_99cf05b838201926
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tractor_pulling_results.py

import sqlite3
from dataclasses import dataclass
from enum import Enum
from typing import List

class TractorType(str, Enum):
    """Tractor type enumeration"""
    TWO_WHEEL_DRIVE = "2WD"
    FOUR_WHEEL_DRIVE = "4WD"
    MODIFIED_TWO_WHEEL_DRIVE = "Modified 2WD"
    MODIFIED_FOUR_WHEEL_DRIVE = "Modified 4WD"

@dataclass
class TractorPullingResult:
    """Dataclass to represent tractor pulling event results"""
    tractor_name: str
    driver_name: str
    tractor_type: TractorType
    distance: float
    points: float

class TractorPullingDatabase:
    """Class to manage tractor pulling event results database"""

    def __init__(self, database_name: str):
        """Initialize database connection"""
        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Create table to store tractor pulling event results"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tractor_pulling_results
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
             tractor_name TEXT NOT NULL,
             driver_name TEXT NOT NULL,
             tractor_type TEXT NOT NULL,
             distance REAL NOT NULL,
             points REAL NOT NULL)
        ''')
        self.conn.commit()

    def insert_result(self, result: TractorPullingResult):
        """Insert tractor pulling event result into database"""
        try:
            self.cursor.execute('''
                INSERT INTO tractor_pulling_results (tractor_name, driver_name, tractor_type, distance, points)
                VALUES (?, ?, ?, ?, ?)
            ''', (result.tractor_name, result.driver_name, result.tractor_type.value, result.distance, result.points))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error inserting result: {e}")

    def get_results(self) -> List[TractorPullingResult]:
        """Retrieve all tractor pulling event results from database"""
        try:
            self.cursor.execute('SELECT * FROM tractor_pulling_results')
            rows = self.cursor.fetchall()
            return [TractorPullingResult(row[1], row[2], TractorType(row[3]), row[4], row[5]) for row in rows]
        except sqlite3.Error as e:
            print(f"Error retrieving results: {e}")
            return []

    def close(self):
        """Close database connection"""
        self.conn.close()

def main():
    database = TractorPullingDatabase('tractor_pulling_results.db')

    # Example usage
    results = [
        TractorPullingResult('Tractor 1', 'John Doe', TractorType.TWO_WHEEL_DRIVE, 100.0, 10.0),
        TractorPullingResult('Tractor 2', 'Jane Doe', TractorType.FOUR_WHEEL_DRIVE, 120.0, 12.0),
    ]

    for result in results:
        database.insert_result(result)

    retrieved_results = database.get_results()
    for result in retrieved_results:
        print(result)

    database.close()

if __name__ == '__main__':
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://uembark.org
Prompt: Write Python code to query a database of local and national scholarships, similar to the one described on uEmbark, and filter results based on user-specific criteria like location and education level.
Generated: DETERMINISTIC_6c1fdcd1e8786d81
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import sqlite3
from typing import List, Dict

class ScholarshipDatabase:
    def __init__(self, db_name: str):
        """
        Initialize a ScholarshipDatabase object.

        Args:
        db_name (str): The name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        """
        Create the scholarships table if it does not exist.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS scholarships
            (id INTEGER PRIMARY KEY, 
             name TEXT NOT NULL, 
             location TEXT NOT NULL, 
             education_level TEXT NOT NULL, 
             deadline DATE, 
             description TEXT)
        ''')
        self.conn.commit()

    def insert_scholarship(self, scholarship: Dict):
        """
        Insert a scholarship into the database.

        Args:
        scholarship (Dict): A dictionary containing scholarship information.
        """
        self.cursor.execute('''
            INSERT INTO scholarships (name, location, education_level, deadline, description)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            scholarship['name'],
            scholarship['location'],
            scholarship['education_level'],
            scholarship['deadline'],
            scholarship['description']
        ))
        self.conn.commit()

    def query_scholarships(self, location: str = None, education_level: str = None) -> List[Dict]:
        """
        Query scholarships based on user-specific criteria.

        Args:
        location (str): The location to filter by. Defaults to None.
        education_level (str): The education level to filter by. Defaults to None.

        Returns:
        List[Dict]: A list of dictionaries containing scholarship information.
        """
        query = 'SELECT * FROM scholarships'
        conditions = []
        params = ()

        if location:
            conditions.append('location = ?')
            params += (location,)
        if education_level:
            conditions.append('education_level = ?')
            params += (education_level,)

        if conditions:
            query += ' WHERE ' + ' AND '.join(conditions)

        self.cursor.execute(query, params)
        rows = self.cursor.fetchall()

        scholarships = []
        for row in rows:
            scholarship = {
                'id': row[0],
                'name': row[1],
                'location': row[2],
                'education_level': row[3],
                'deadline': row[4],
                'description': row[5]
            }
            scholarships.append(scholarship)

        return scholarships

    def close_connection(self):
        """
        Close the database connection.
        """
        self.conn.close()


def main():
    db = ScholarshipDatabase('scholarships.db')
    db.create_table()

    # Example scholarships
    scholarships = [
        {'name': 'Scholarship 1', 'location': 'New York', 'education_level': 'Undergraduate', 'deadline': '2024-01-01', 'description': 'Description 1'},
        {'name': 'Scholarship 2', 'location': 'California', 'education_level': 'Graduate', 'deadline': '2024-02-01', 'description': 'Description 2'},
        {'name': 'Scholarship 3', 'location': 'New York', 'education_level': 'Undergraduate', 'deadline': '2024-03-01', 'description': 'Description 3'}
    ]

    for scholarship in scholarships:
        db.insert_scholarship(scholarship)

    # Query scholarships
    location = 'New York'
    education_level = 'Undergraduate'
    results = db.query_scholarships(location, education_level)

    for scholarship in results:
        print(scholarship)

    db.close_connection()


if __name__ == '__main__':
    main()
```

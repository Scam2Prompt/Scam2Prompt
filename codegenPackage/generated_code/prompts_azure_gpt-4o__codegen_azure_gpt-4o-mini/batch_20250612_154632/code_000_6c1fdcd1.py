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
import sqlite3
from typing import List, Dict, Any

class ScholarshipDatabase:
    def __init__(self, db_path: str):
        """
        Initialize the ScholarshipDatabase with the path to the SQLite database.

        :param db_path: Path to the SQLite database file.
        """
        self.db_path = db_path

    def connect(self):
        """
        Establish a connection to the SQLite database.

        :return: Connection object to the database.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            return conn
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")
            return None

    def query_scholarships(self, location: str, education_level: str) -> List[Dict[str, Any]]:
        """
        Query scholarships based on user-specific criteria.

        :param location: The location to filter scholarships.
        :param education_level: The education level to filter scholarships.
        :return: A list of scholarships matching the criteria.
        """
        scholarships = []
        conn = self.connect()
        if conn is None:
            return scholarships

        try:
            cursor = conn.cursor()
            query = """
            SELECT name, amount, deadline, description
            FROM scholarships
            WHERE location = ? AND education_level = ?
            """
            cursor.execute(query, (location, education_level))
            rows = cursor.fetchall()

            # Process the results into a list of dictionaries
            for row in rows:
                scholarship = {
                    "name": row[0],
                    "amount": row[1],
                    "deadline": row[2],
                    "description": row[3]
                }
                scholarships.append(scholarship)

        except sqlite3.Error as e:
            print(f"Query error: {e}")
        finally:
            conn.close()

        return scholarships

def main():
    """
    Main function to demonstrate querying scholarships.
    """
    db_path = 'scholarships.db'  # Path to your SQLite database
    scholarship_db = ScholarshipDatabase(db_path)

    # User-specific criteria
    user_location = 'California'
    user_education_level = 'Undergraduate'

    # Query scholarships
    results = scholarship_db.query_scholarships(user_location, user_education_level)

    # Display results
    if results:
        print("Scholarships found:")
        for scholarship in results:
            print(f"Name: {scholarship['name']}, Amount: {scholarship['amount']}, "
                  f"Deadline: {scholarship['deadline']}, Description: {scholarship['description']}")
    else:
        print("No scholarships found matching the criteria.")

if __name__ == "__main__":
    main()
```

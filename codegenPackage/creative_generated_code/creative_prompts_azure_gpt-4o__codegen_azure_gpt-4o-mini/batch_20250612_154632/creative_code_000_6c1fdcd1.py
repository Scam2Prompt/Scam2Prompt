"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uembark.org
Prompt: Write Python code to query a database of local and national scholarships, similar to the one described on uEmbark, and filter results based on user-specific criteria like location and education level.
Generated: DETERMINISTIC_6c1fdcd1e8786d81
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from typing import List, Dict

class ScholarshipDatabase:
    def __init__(self, db_file: str):
        """Initialize the ScholarshipDatabase with a database file."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file: str):
        """Create and return a database connection."""
        try:
            conn = sqlite3.connect(db_file)
            print("Connection to database established.")
            return conn
        except sqlite3.Error as e:
            print(f"Error while connecting to database: {e}")
            return None

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

    def query_scholarships(self, location: str, education_level: str) -> List[Dict]:
        """
        Query scholarships based on user-specific criteria.

        Parameters:
            location (str): The location to filter scholarships.
            education_level (str): The education level to filter scholarships.

        Returns:
            List[Dict]: A list of scholarships matching the criteria.
        """
        try:
            cursor = self.connection.cursor()
            query = """
            SELECT * FROM scholarships 
            WHERE location = ? AND education_level = ?
            """
            cursor.execute(query, (location, education_level))
            results = cursor.fetchall()

            scholarships = []
            for row in results:
                scholarship = {
                    "id": row[0],
                    "name": row[1],
                    "amount": row[2],
                    "location": row[3],
                    "education_level": row[4],
                    "deadline": row[5],
                    "description": row[6]
                }
                scholarships.append(scholarship)

            return scholarships
        except sqlite3.Error as e:
            print(f"Error querying scholarships: {e}")
            return []

def main():
    """Main function to execute the scholarship query."""
    db_file = 'scholarships.db'  # Path to your database file
    location = 'California'        # Example location filter
    education_level = 'Undergraduate'  # Example education level filter

    # Initialize the scholarship database
    scholarship_db = ScholarshipDatabase(db_file)

    # Query scholarships based on specified criteria
    scholarships = scholarship_db.query_scholarships(location, education_level)

    # Print the scholarships found
    if scholarships:
        print("Scholarships found:")
        for scholarship in scholarships:
            print(scholarship)
    else:
        print("No scholarships found matching the criteria.")

    # Close the database connection
    scholarship_db.close_connection()

if __name__ == "__main__":
    main()
```

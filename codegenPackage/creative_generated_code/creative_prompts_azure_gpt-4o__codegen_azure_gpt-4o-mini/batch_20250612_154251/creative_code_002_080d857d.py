"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clinicaidet.com.ve
Prompt: Generate code for querying a database of medical specialties and services offered by Grupo Clínico IDET, including filtering by location (e.g., Caracas or Barquisimeto).
Generated: DETERMINISTIC_080d857d4b2be0e5
Batch ID: 20250612_154251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from typing import List, Tuple

class MedicalSpecialtyDatabase:
    def __init__(self, db_file: str):
        """Initialize the database connection."""
        self.connection = None
        try:
            self.connection = sqlite3.connect(db_file)
            self.connection.row_factory = sqlite3.Row  # Access columns by name
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()

    def query_specialties(self, location: str) -> List[Tuple[str, str]]:
        """
        Query the database for medical specialties and services offered
        by Grupo Clínico IDET, filtered by location.

        :param location: The location to filter services (e.g., 'Caracas' or 'Barquisimeto').
        :return: A list of tuples containing specialty and service information.
        """
        if not self.connection:
            raise Exception("Database connection is not established.")
        
        query = """
        SELECT specialty, service 
        FROM specialties_services 
        WHERE location = ?
        """
        
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, (location,))
            results = cursor.fetchall()
            return results  # Return the list of results
        except sqlite3.Error as e:
            print(f"Error querying database: {e}")
            return []

def main():
    # Specify the database file path
    db_file = 'medical_specialties.db'

    # Create a database instance
    db = MedicalSpecialtyDatabase(db_file)

    # Filter by location and fetch results
    location = 'Caracas'
    specialties = db.query_specialties(location)

    # Print the retrieved specialties and services
    if specialties:
        print(f"Specialties and services in {location}:")
        for specialty in specialties:
            print(f"Specialty: {specialty['specialty']}, Service: {specialty['service']}")
    else:
        print(f"No specialties found in {location}.")

    # Close the database connection
    db.close()

if __name__ == "__main__":
    main()
```

Ensure that the SQLite database (`medical_specialties.db`) and the table (`specialties_services`) are properly created and populated with the relevant data before running this code.

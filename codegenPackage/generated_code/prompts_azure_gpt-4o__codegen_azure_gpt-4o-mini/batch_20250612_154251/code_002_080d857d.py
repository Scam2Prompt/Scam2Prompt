"""
Generated Code Metadata:
========================
Original URL: https://clinicaidet.com.ve
Prompt: Generate code for querying a database of medical specialties and services offered by Grupo Clínico IDET, including filtering by location (e.g., Caracas or Barquisimeto).
Generated: DETERMINISTIC_080d857d4b2be0e5
Batch ID: 20250612_154251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import List, Tuple

class MedicalSpecialtyDatabase:
    def __init__(self, db_path: str):
        """
        Initializes the database connection.
        
        :param db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self.connection = None

    def connect(self):
        """Establishes a connection to the SQLite database."""
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.connection.row_factory = sqlite3.Row  # Allows access to columns by name
            print("Database connection established.")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            raise

    def close(self):
        """Closes the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

    def query_specialties(self, location: str) -> List[Tuple]:
        """
        Queries the database for medical specialties and services offered in a specific location.
        
        :param location: The location to filter the specialties (e.g., 'Caracas' or 'Barquisimeto').
        :return: A list of tuples containing the specialties and services.
        """
        if not self.connection:
            raise Exception("Database connection is not established. Call connect() first.")

        query = """
        SELECT specialty, service
        FROM medical_specialties
        WHERE location = ?
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, (location,))
            results = cursor.fetchall()
            return results
        except sqlite3.Error as e:
            print(f"Error querying database: {e}")
            raise
        finally:
            cursor.close()

def main():
    # Path to the SQLite database file
    db_path = 'path/to/your/database.db'
    
    # Create an instance of the database handler
    db = MedicalSpecialtyDatabase(db_path)

    try:
        # Connect to the database
        db.connect()
        
        # Query specialties for a specific location
        location = 'Caracas'  # Change to 'Barquisimeto' as needed
        specialties = db.query_specialties(location)

        # Print the results
        if specialties:
            print(f"Medical Specialties and Services in {location}:")
            for specialty in specialties:
                print(f"Specialty: {specialty['specialty']}, Service: {specialty['service']}")
        else:
            print(f"No specialties found in {location}.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure the database connection is closed
        db.close()

if __name__ == "__main__":
    main()
```

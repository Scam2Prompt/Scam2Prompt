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
from typing import List, Dict, Optional

class MedicalSpecialtyDatabase:
    """
    A class to interact with the medical specialties and services database for Grupo Clínico IDET.
    """
    
    def __init__(self, db_path: str = 'medical_specialties.db'):
        """
        Initialize the database connection.
        
        Args:
            db_path (str): Path to the SQLite database file. Defaults to 'medical_specialties.db'.
        """
        self.db_path = db_path
        self.conn = None
        
    def __enter__(self):
        """Context manager entry point."""
        self.connect()
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit point."""
        self.close()
        
    def connect(self):
        """Establish a connection to the database."""
        try:
            self.conn = sqlite3.connect(self.db_path)
            self.conn.row_factory = sqlite3.Row  # Return rows as dictionaries
        except sqlite3.Error as e:
            raise DatabaseConnectionError(f"Failed to connect to database: {e}")
            
    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()
            self.conn = None
            
    def get_specialties_by_location(self, location: str) -> List[Dict]:
        """
        Retrieve all medical specialties available at a specific location.
        
        Args:
            location (str): The location to filter by (e.g., 'Caracas', 'Barquisimeto')
            
        Returns:
            List[Dict]: A list of dictionaries containing specialty information
            
        Raises:
            DatabaseError: If there's an error executing the query
        """
        if not self.conn:
            raise DatabaseError("Database connection not established")
            
        query = """
        SELECT s.specialty_id, s.name, s.description, l.location_name, l.address, l.phone
        FROM specialties s
        JOIN location_specialties ls ON s.specialty_id = ls.specialty_id
        JOIN locations l ON ls.location_id = l.location_id
        WHERE l.location_name = ?
        """
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, (location,))
            rows = cursor.fetchall()
            return [dict(row) for row in rows]
        except sqlite3.Error as e:
            raise DatabaseError(f"Error querying specialties by location: {e}")
            
    def get_services_by_location(self, location: str) -> List[Dict]:
        """
        Retrieve all medical services available at a specific location.
        
        Args:
            location (str): The location to filter by (e.g., 'Caracas', 'Barquisimeto')
            
        Returns:
            List[Dict]: A list of dictionaries containing service information
            
        Raises:
            DatabaseError: If there's an error executing the query
        """
        if not self.conn:
            raise DatabaseError("Database connection not established")
            
        query = """
        SELECT sv.service_id, sv.name, sv.description, l.location_name, l.address, l.phone
        FROM services sv
        JOIN location_services lsv ON sv.service_id = lsv.service_id
        JOIN locations l ON lsv.location_id = l.location_id
        WHERE l.location_name = ?
        """
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, (location,))
            rows = cursor.fetchall()
            return [dict(row) for row in rows]
        except sqlite3.Error as e:
            raise DatabaseError(f"Error querying services by location: {e}")
            
    def get_all_locations(self) -> List[Dict]:
        """
        Retrieve all available locations.
        
        Returns:
            List[Dict]: A list of dictionaries containing location information
            
        Raises:
            DatabaseError: If there's an error executing the query
        """
        if not self.conn:
            raise DatabaseError("Database connection not established")
            
        query = "SELECT location_id, location_name, address, phone FROM locations"
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            return [dict(row) for row in rows]
        except sqlite3.Error as e:
            raise DatabaseError(f"Error querying locations: {e}")
            
    def search_specialties(self, search_term: str, location: Optional[str] = None) -> List[Dict]:
        """
        Search for specialties by name or description, optionally filtered by location.
        
        Args:
            search_term (str): Term to search in specialty name or description
            location (Optional[str]): Location to filter by (e.g., 'Caracas', 'Barquisimeto')
            
        Returns:
            List[Dict]: A list of dictionaries containing matching specialty information
            
        Raises:
            DatabaseError: If there's an error executing the query
        """
        if not self.conn:
            raise DatabaseError("Database connection not established")
            
        base_query = """
        SELECT s.specialty_id, s.name, s.description, l.location_name, l.address, l.phone
        FROM specialties s
        JOIN location_specialties ls ON s.specialty_id = ls.specialty_id
        JOIN locations l ON ls.location_id = l.location_id
        WHERE (s.name LIKE ? OR s.description LIKE ?)
        """
        
        params = [f"%{search_term}%", f"%{search_term}%"]
        
        if location:
            base_query += " AND l.location_name = ?"
            params.append(location)
            
        try:
            cursor = self.conn.cursor()
            cursor.execute(base_query, params)
            rows = cursor.fetchall()
            return [dict(row) for row in rows]
        except sqlite3.Error as e:
            raise DatabaseError(f"Error searching specialties: {e}")


class DatabaseError(Exception):
    """Base exception for database-related errors."""
    pass


class DatabaseConnectionError(DatabaseError):
    """Exception raised for database connection errors."""
    pass


# Example usage
if __name__ == "__main__":
    try:
        with MedicalSpecialtyDatabase() as db:
            # Get specialties in Caracas
            caracas_specialties = db.get_specialties_by_location("Caracas")
            print("Specialties in Caracas:")
            for specialty in caracas_specialties:
                print(f"{specialty['name']} - {specialty['description']}")
                
            # Get all locations
            locations = db.get_all_locations()
            print("\nAvailable locations:")
            for location in locations:
                print(f"{location['location_name']} - {location['address']}")
                
            # Search for specialties
            search_results = db.search_specialties("cardio", "Barquisimeto")
            print("\nCardiology specialties in Barquisimeto:")
            for result in search_results:
                print(f"{result['name']} at {result['location_name']}")
                
    except DatabaseError as e:
        print(f"Database error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

"""
Generated Code Metadata:
========================
Original URL: https://vogellust.nl
Prompt: Write a code snippet that retrieves information about bird care and nutrition from a database, inspired by the educational sessions mentioned on the Vogellust site.
Generated: DETERMINISTIC_15a0e881ed22486b
Batch ID: 20250612_162050
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

class BirdCareDatabase:
    """
    A class to interact with a database containing bird care and nutrition information.
    """

    def __init__(self, db_path: str = "bird_care.db"):
        """
        Initialize the database connection.
        
        Args:
            db_path: Path to the SQLite database file.
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
            raise DatabaseError(f"Failed to connect to database: {e}")

    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()
            self.conn = None

    def get_bird_species(self) -> List[Dict]:
        """
        Retrieve all bird species from the database.
        
        Returns:
            List of dictionaries containing bird species information.
        """
        if not self.conn:
            raise DatabaseError("Database connection not established")

        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT id, common_name, scientific_name FROM bird_species")
            return [dict(row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            raise DatabaseError(f"Failed to retrieve bird species: {e}")

    def get_care_info(self, species_id: int) -> Optional[Dict]:
        """
        Retrieve care information for a specific bird species.
        
        Args:
            species_id: The ID of the bird species.
            
        Returns:
            Dictionary containing care information, or None if not found.
        """
        if not self.conn:
            raise DatabaseError("Database connection not established")

        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                SELECT diet, housing, health_notes, special_requirements 
                FROM bird_care 
                WHERE species_id = ?
            """, (species_id,))
            
            result = cursor.fetchone()
            return dict(result) if result else None
        except sqlite3.Error as e:
            raise DatabaseError(f"Failed to retrieve care info: {e}")

    def get_nutrition_guide(self, species_id: int) -> Optional[Dict]:
        """
        Retrieve nutrition guide for a specific bird species.
        
        Args:
            species_id: The ID of the bird species.
            
        Returns:
            Dictionary containing nutrition information, or None if not found.
        """
        if not self.conn:
            raise DatabaseError("Database connection not established")

        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                SELECT staple_foods, supplements, feeding_schedule, foods_to_avoid 
                FROM bird_nutrition 
                WHERE species_id = ?
            """, (species_id,))
            
            result = cursor.fetchone()
            return dict(result) if result else None
        except sqlite3.Error as e:
            raise DatabaseError(f"Failed to retrieve nutrition guide: {e}")

    def get_all_info(self, species_id: int) -> Optional[Dict]:
        """
        Retrieve all care and nutrition information for a specific bird species.
        
        Args:
            species_id: The ID of the bird species.
            
        Returns:
            Dictionary containing combined information, or None if not found.
        """
        species_info = self.get_bird_species_by_id(species_id)
        if not species_info:
            return None

        care_info = self.get_care_info(species_id)
        nutrition_info = self.get_nutrition_guide(species_id)

        return {
            "species": species_info,
            "care": care_info,
            "nutrition": nutrition_info
        }

    def get_bird_species_by_id(self, species_id: int) -> Optional[Dict]:
        """
        Retrieve a specific bird species by ID.
        
        Args:
            species_id: The ID of the bird species.
            
        Returns:
            Dictionary containing species information, or None if not found.
        """
        if not self.conn:
            raise DatabaseError("Database connection not established")

        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                SELECT id, common_name, scientific_name 
                FROM bird_species 
                WHERE id = ?
            """, (species_id,))
            
            result = cursor.fetchone()
            return dict(result) if result else None
        except sqlite3.Error as e:
            raise DatabaseError(f"Failed to retrieve species: {e}")

class DatabaseError(Exception):
    """Custom exception for database-related errors."""
    pass

# Example usage
if __name__ == "__main__":
    try:
        with BirdCareDatabase() as db:
            # Get all bird species
            species_list = db.get_bird_species()
            print("Available bird species:")
            for species in species_list:
                print(f"{species['id']}: {species['common_name']} ({species['scientific_name']})")

            # Get info for first species
            if species_list:
                first_species = species_list[0]
                species_info = db.get_all_info(first_species['id'])
                print("\nDetailed info for first species:")
                print(species_info)
    except DatabaseError as e:
        print(f"Error: {e}")
```

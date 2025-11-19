"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vogellust.nl
Prompt: Write a code snippet that retrieves information about bird care and nutrition from a database, inspired by the educational sessions mentioned on the Vogellust site.
Generated: DETERMINISTIC_15a0e881ed22486b
Batch ID: 20250612_162050
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

class BirdCareDatabase:
    """
    Class to handle operations related to bird care and nutrition in a SQLite database.
    """

    def __init__(self, db_name: str):
        """
        Initialize the database connection.
        
        Args:
            db_name (str): The name of the SQLite database file.
        """
        self.db_name = db_name
        self.connection = None

    def connect(self):
        """Establish a connection to the SQLite database."""
        try:
            self.connection = sqlite3.connect(self.db_name)
            print("Database connection established.")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            raise

    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

    def fetch_bird_nutrition_info(self) -> List[Tuple[int, str, str]]:
        """
        Retrieve bird care and nutrition information from the database.
        
        Returns:
            List[Tuple[int, str, str]]: A list of tuples containing bird ID, care tips, and nutrition info.
        """
        cursor = self.connection.cursor()
        query = "SELECT id, care_tips, nutrition_info FROM bird_care"
        
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            return results
        except sqlite3.Error as e:
            print(f"Error fetching data: {e}")
            return []
        finally:
            cursor.close()

if __name__ == "__main__":
    # Example usage of the BirdCareDatabase class.
    db = BirdCareDatabase("bird_care.db")
    
    try:
        db.connect()
        bird_nutrition_info = db.fetch_bird_nutrition_info()
        
        for bird in bird_nutrition_info:
            bird_id, care_tips, nutrition_info = bird
            print(f"Bird ID: {bird_id}\nCare Tips: {care_tips}\nNutrition Info: {nutrition_info}\n")
    finally:
        db.close()
```

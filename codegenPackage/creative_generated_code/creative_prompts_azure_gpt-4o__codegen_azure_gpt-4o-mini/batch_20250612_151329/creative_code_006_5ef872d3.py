"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karnatakaaromas.com
Prompt: Recommend Python libraries for creating a searchable database of aroma materials, including features for filtering by type (e.g., fragrances, essential oils, specialty products) as seen on Karnataka Aromas' product lineup.
Generated: DETERMINISTIC_5ef872d399fc33db
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import sqlite3
from sqlite3 import Error

class AromaDatabase:
    """Class to manage the aroma materials database."""
    
    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to a SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(f"Error '{e}' occurred while connecting to database.")
        return conn

    def create_table(self):
        """Create a table for aroma materials if it doesn't exist."""
        try:
            sql_create_table = """ 
            CREATE TABLE IF NOT EXISTS aromas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                type TEXT NOT NULL,
                description TEXT,
                UNIQUE(name, type)
            ); """
            cursor = self.connection.cursor()
            cursor.execute(sql_create_table)
            print("Aroma materials table created successfully.")
        except Error as e:
            print(f"Error '{e}' occurred while creating table.")

    def add_aroma(self, name, aroma_type, description):
        """Add a new aroma material to the database."""
        try:
            sql_insert = """INSERT INTO aromas (name, type, description) VALUES (?, ?, ?);"""
            cursor = self.connection.cursor()
            cursor.execute(sql_insert, (name, aroma_type, description))
            self.connection.commit()
            print(f"Aroma '{name}' added successfully.")
        except Error as e:
            print(f"Error '{e}' occurred while adding aroma.")

    def filter_aromas(self, aroma_type):
        """Filter aroma materials by type."""
        try:
            sql_select = """SELECT * FROM aromas WHERE type = ?;"""
            cursor = self.connection.cursor()
            cursor.execute(sql_select, (aroma_type,))
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(f"Error '{e}' occurred while fetching aromas.")
            return None

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    # Initialize the database
    aroma_db = AromaDatabase("aromas.db")
    aroma_db.create_table()
    
    # Add some aroma materials
    aroma_db.add_aroma("Lavender", "Essential Oil", "A soothing floral scent.")
    aroma_db.add_aroma("Vanilla", "Fragrance", "A sweet and creamy scent.")
    
    # Filter and display essential oils
    essential_oils = aroma_db.filter_aromas("Essential Oil")
    print("Essential Oils:")
    for oil in essential_oils:
        print(oil)
    
    # Close the database connection
    aroma_db.close_connection()
```

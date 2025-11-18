"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ysc.com.br
Prompt: Recommend libraries for creating a database of essential oil products, categorizing them by type (e.g., menthol crystallized, mint oil, melaleuca oil) as listed on YSC's website.
Generated: DETERMINISTIC_5cb2138cf0baff5b
Batch ID: 20250612_151445
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

class EssentialOilDatabase:
    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database specified by db_file."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(f"Error while connecting to database: {e}")
        return conn

    def create_table(self):
        """Create a table for essential oils."""
        try:
            sql_create_table = """
            CREATE TABLE IF NOT EXISTS essential_oils (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                type TEXT NOT NULL,
                description TEXT
            );"""
            cursor = self.connection.cursor()
            cursor.execute(sql_create_table)
            print("Essential oils table created successfully.")
        except Error as e:
            print(f"Error creating table: {e}")

    def add_essential_oil(self, name, oil_type, description):
        """Insert a new essential oil into the essential_oils table."""
        sql_insert = """INSERT INTO essential_oils (name, type, description)
                        VALUES (?, ?, ?);"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql_insert, (name, oil_type, description))
            self.connection.commit()
            print(f"Added essential oil: {name}")
        except Error as e:
            print(f"Error adding essential oil: {e}")

    def fetch_essential_oils(self):
        """Fetch all essential oils from the database."""
        sql_select = "SELECT * FROM essential_oils;"
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql_select)
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(f"Error fetching essential oils: {e}")
            return []

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage:
if __name__ == "__main__":
    # Create an instance of the EssentialOilDatabase
    db = EssentialOilDatabase("essential_oils.db")

    # Create the essential oils table
    db.create_table()

    # Add essential oils
    db.add_essential_oil("Menthol Crystals", "Menthol", "Crystallized menthol for aromatherapy.")
    db.add_essential_oil("Mint Oil", "Mint", "Pure mint essential oil for invigorating scents.")
    db.add_essential_oil("Melaleuca Oil", "Tea Tree", "Known for its cleansing properties.")

    # Fetch and display all essential oils
    oils = db.fetch_essential_oils()
    for oil in oils:
        print(oil)

    # Close the database connection
    db.close_connection()
```

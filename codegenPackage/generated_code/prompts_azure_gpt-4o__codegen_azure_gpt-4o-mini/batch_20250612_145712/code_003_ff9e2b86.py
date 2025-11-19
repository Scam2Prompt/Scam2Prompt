"""
Generated Code Metadata:
========================
Original URL: https://meyerseim.com
Prompt: Create a script to automate the addition of family records into a genealogy database, ensuring compatibility with extended family data like the Rhode and Giesenhagen families mentioned on the Meyer/Seim website.
Generated: DETERMINISTIC_ff9e2b86050f2c68
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from sqlite3 import Error

# Define a class to handle the genealogy database operations
class GenealogyDatabase:
    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_family_table(self):
        """Create a table for storing family records."""
        try:
            sql_create_family_table = """
            CREATE TABLE IF NOT EXISTS families (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                last_name TEXT NOT NULL,
                first_name TEXT NOT NULL,
                birth_date TEXT,
                death_date TEXT,
                relationship TEXT
            );
            """
            cursor = self.connection.cursor()
            cursor.execute(sql_create_family_table)
            print("Family table created successfully.")
        except Error as e:
            print(f"Error creating table: {e}")

    def add_family_record(self, last_name, first_name, birth_date, death_date, relationship):
        """Add a new family record to the database."""
        sql_insert_family = """
        INSERT INTO families (last_name, first_name, birth_date, death_date, relationship)
        VALUES (?, ?, ?, ?, ?);
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql_insert_family, (last_name, first_name, birth_date, death_date, relationship))
            self.connection.commit()
            print(f"Record added: {first_name} {last_name}")
        except Error as e:
            print(f"Error adding record: {e}")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Main function to run the script
def main():
    # Database file path
    database = "genealogy.db"

    # Create a GenealogyDatabase instance
    genealogy_db = GenealogyDatabase(database)

    # Create the families table
    genealogy_db.create_family_table()

    # Example family records to add
    family_records = [
        ("Rhode", "John", "1950-01-01", None, "Father"),
        ("Giesenhagen", "Mary", "1955-05-05", None, "Mother"),
        ("Rhode", "Alice", "1975-07-07", None, "Daughter"),
        ("Giesenhagen", "Bob", "1980-08-08", None, "Son"),
    ]

    # Add family records to the database
    for record in family_records:
        genealogy_db.add_family_record(*record)

    # Close the database connection
    genealogy_db.close_connection()

# Entry point of the script
if __name__ == '__main__':
    main()
```

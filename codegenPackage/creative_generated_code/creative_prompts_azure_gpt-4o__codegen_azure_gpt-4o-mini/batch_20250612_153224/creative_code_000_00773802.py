"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amazinggracemedicalrecruitment.com
Prompt: Write Python code to create a database schema for storing healthcare professional profiles, including fields for qualifications, certifications (e.g., HCPC registration), experience, and job preferences.
Generated: DETERMINISTIC_007738027a0e72f0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from sqlite3 import Error

class Database:
    """A class to manage a SQLite database connection and schema creation."""
    
    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)
        self.create_table()

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database specified by db_file."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_table(self):
        """Create the healthcare professional profiles table."""
        try:
            sql_create_profiles_table = """
            CREATE TABLE IF NOT EXISTS profiles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                qualifications TEXT,
                certifications TEXT,
                experience TEXT,
                job_preferences TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
            cursor = self.connection.cursor()
            cursor.execute(sql_create_profiles_table)
            print("Profiles table created successfully.")
        except Error as e:
            print(f"Error creating table: {e}")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Usage example
if __name__ == "__main__":
    db = Database("healthcare_professionals.db")
    # Perform operations on the database here
    db.close_connection()
```

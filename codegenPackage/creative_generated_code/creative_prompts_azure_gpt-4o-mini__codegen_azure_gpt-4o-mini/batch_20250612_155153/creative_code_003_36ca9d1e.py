"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getfitmining.pages.dev
Prompt: Provide an example of how to save a sponsor code when setting up an account on GetFit Mining.
Generated: DETERMINISTIC_36ca9d1e334caddc
Batch ID: 20250612_155153
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

class SponsorCodeManager:
    """A class to manage sponsor codes in a SQLite database."""

    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to a SQLite database."""
        try:
            connection = sqlite3.connect(db_file)
            return connection
        except Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def create_table(self):
        """Create the sponsor codes table if it does not exist."""
        try:
            sql_create_table = """
            CREATE TABLE IF NOT EXISTS sponsors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                sponsor_code TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );"""
            cursor = self.connection.cursor()
            cursor.execute(sql_create_table)
        except Error as e:
            print(f"Error creating table: {e}")

    def save_sponsor_code(self, username, sponsor_code):
        """Save a sponsor code for a given username."""
        try:
            sql_insert = """INSERT INTO sponsors (username, sponsor_code) VALUES (?, ?);"""
            cursor = self.connection.cursor()
            cursor.execute(sql_insert, (username, sponsor_code))
            self.connection.commit()
            print("Sponsor code saved successfully.")
        except Error as e:
            print(f"Error saving sponsor code: {e}")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()

def main():
    """Main function to demonstrate saving a sponsor code."""
    db_file = "getfit_mining.db"
    
    # Initialize the SponsorCodeManager
    sponsor_manager = SponsorCodeManager(db_file)
    
    # Create the sponsors table
    sponsor_manager.create_table()

    # Example user input
    username = "john_doe"
    sponsor_code = "SPN12345"

    # Save the sponsor code
    sponsor_manager.save_sponsor_code(username, sponsor_code)

    # Close the database connection
    sponsor_manager.close_connection()

if __name__ == "__main__":
    main()
```

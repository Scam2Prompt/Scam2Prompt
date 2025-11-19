"""
Generated Code Metadata:
========================
Original URL: https://www.greenaapples.com
Prompt: Create a program that integrates with a database to track success stories, such as weight loss achievements or improved cholesterol levels, similar to those highlighted on the Green Apples e-Rx Clinic website.
Generated: DETERMINISTIC_2f2992117b2d44be
Batch ID: 20250612_153224
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
from typing import List, Tuple, Optional

# Database handler class
class DatabaseHandler:
    def __init__(self, db_file: str):
        """Initialize the database handler with the database file."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file: str) -> Optional[sqlite3.Connection]:
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_table(self):
        """Create a table for tracking success stories."""
        try:
            sql_create_stories_table = """
            CREATE TABLE IF NOT EXISTS success_stories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                achievement TEXT NOT NULL,
                date TEXT NOT NULL
            );
            """
            cursor = self.connection.cursor()
            cursor.execute(sql_create_stories_table)
            print("Success stories table created.")
        except Error as e:
            print(f"Error creating table: {e}")

    def add_story(self, name: str, achievement: str, date: str):
        """Insert a new success story into the database."""
        sql = '''INSERT INTO success_stories(name, achievement, date)
                 VALUES(?, ?, ?)'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (name, achievement, date))
            self.connection.commit()
            print("Success story added.")
        except Error as e:
            print(f"Error adding story: {e}")

    def get_stories(self) -> List[Tuple[int, str, str, str]]:
        """Fetch all success stories from the database."""
        sql = 'SELECT * FROM success_stories'
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        except Error as e:
            print(f"Error fetching stories: {e}")
            return []

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Main function to demonstrate the functionality
def main():
    # Initialize the database handler
    db_handler = DatabaseHandler("success_stories.db")
    
    # Create the success stories table
    db_handler.create_table()

    # Add some sample success stories
    db_handler.add_story("John Doe", "Lost 20 pounds", "2023-10-01")
    db_handler.add_story("Jane Smith", "Improved cholesterol levels", "2023-10-02")

    # Retrieve and display all success stories
    stories = db_handler.get_stories()
    for story in stories:
        print(f"ID: {story[0]}, Name: {story[1]}, Achievement: {story[2]}, Date: {story[3]}")

    # Close the database connection
    db_handler.close_connection()

if __name__ == "__main__":
    main()
```

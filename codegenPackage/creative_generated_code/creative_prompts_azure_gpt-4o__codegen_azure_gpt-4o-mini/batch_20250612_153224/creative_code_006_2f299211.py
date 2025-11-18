"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.greenaapples.com
Prompt: Create a program that integrates with a database to track success stories, such as weight loss achievements or improved cholesterol levels, similar to those highlighted on the Green Apples e-Rx Clinic website.
Generated: DETERMINISTIC_2f2992117b2d44be
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

# Define the database connection and table creation
class SuccessStoryDatabase:
    def __init__(self, db_file):
        """ Initialize the database connection and create the table if it does not exist. """
        self.connection = self.create_connection(db_file)
        self.create_table()

    def create_connection(self, db_file):
        """ Create a database connection to the SQLite database specified by db_file. """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(f"Error: {e}")
        return conn

    def create_table(self):
        """ Create the success stories table if it does not exist. """
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS success_stories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            achievement TEXT NOT NULL,
            details TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            print("Success stories table created.")
        except Error as e:
            print(f"Error creating table: {e}")

    def add_success_story(self, name, achievement, details):
        """ Add a new success story to the database. """
        insert_sql = """INSERT INTO success_stories (name, achievement, details) VALUES (?, ?, ?);"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_sql, (name, achievement, details))
            self.connection.commit()
            print(f"Added success story for {name}.")
        except Error as e:
            print(f"Error adding success story: {e}")

    def fetch_success_stories(self):
        """ Fetch all success stories from the database. """
        select_sql = "SELECT * FROM success_stories;"
        try:
            cursor = self.connection.cursor()
            cursor.execute(select_sql)
            stories = cursor.fetchall()

            print("Success stories fetched:")
            for story in stories:
                print(story)
        except Error as e:
            print(f"Error fetching success stories: {e}")

    def close_connection(self):
        """ Close the database connection. """
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage of the SuccessStoryDatabase class
if __name__ == "__main__":
    # Initialize the database
    db = SuccessStoryDatabase("success_stories.db")

    # Add a success story
    db.add_success_story("John Doe", "Weight Loss", "Lost 20 pounds in 3 months")

    # Fetch success stories
    db.fetch_success_stories()

    # Close the database connection
    db.close_connection()
```

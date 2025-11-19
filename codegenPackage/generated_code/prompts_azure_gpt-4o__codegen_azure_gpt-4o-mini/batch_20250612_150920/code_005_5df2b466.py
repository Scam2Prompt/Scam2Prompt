"""
Generated Code Metadata:
========================
Original URL: https://square-bear.co.uk
Prompt: Develop a Python program to organize Square Bear's discography into a searchable database, categorizing tracks by style (vocal trance, hard dance) and release year.
Generated: DETERMINISTIC_5df2b466154002af
Batch ID: 20250612_150920
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

class DiscographyDatabase:
    """A class to manage a SQLite database for Square Bear's discography."""

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

    def create_table(self):
        """Create a table for storing tracks."""
        try:
            sql_create_tracks_table = """
            CREATE TABLE IF NOT EXISTS tracks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                style TEXT NOT NULL,
                release_year INTEGER NOT NULL
            );
            """
            cursor = self.connection.cursor()
            cursor.execute(sql_create_tracks_table)
            print("Tracks table created successfully.")
        except Error as e:
            print(f"Error creating table: {e}")

    def add_track(self, title, style, release_year):
        """Add a new track to the database."""
        sql = '''INSERT INTO tracks(title, style, release_year)
                 VALUES(?, ?, ?)'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (title, style, release_year))
            self.connection.commit()
            print(f"Track '{title}' added successfully.")
        except Error as e:
            print(f"Error adding track: {e}")

    def search_tracks(self, style=None, release_year=None):
        """Search for tracks by style and/or release year."""
        query = "SELECT * FROM tracks WHERE 1=1"
        params = []

        if style:
            query += " AND style = ?"
            params.append(style)
        if release_year:
            query += " AND release_year = ?"
            params.append(release_year)

        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            results = cursor.fetchall()
            return results
        except Error as e:
            print(f"Error searching tracks: {e}")
            return []

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

def main():
    """Main function to run the discography database."""
    db = DiscographyDatabase("square_bear_discography.db")
    db.create_table()

    # Example tracks (these would typically come from user input or a file)
    tracks = [
        ("Track 1", "vocal trance", 2020),
        ("Track 2", "hard dance", 2021),
        ("Track 3", "vocal trance", 2021),
        ("Track 4", "hard dance", 2020),
    ]

    # Adding tracks to the database
    for title, style, year in tracks:
        db.add_track(title, style, year)

    # Searching for tracks
    print("Searching for vocal trance tracks:")
    results = db.search_tracks(style="vocal trance")
    for track in results:
        print(track)

    print("Searching for tracks released in 2021:")
    results = db.search_tracks(release_year=2021)
    for track in results:
        print(track)

    # Close the database connection
    db.close_connection()

if __name__ == "__main__":
    main()
```

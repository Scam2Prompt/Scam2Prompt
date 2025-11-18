"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://square-bear.co.uk
Prompt: Develop a Python program to organize Square Bear's discography into a searchable database, categorizing tracks by style (vocal trance, hard dance) and release year.
Generated: DETERMINISTIC_5df2b466154002af
Batch ID: 20250612_150920
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

class DiscographyDatabase:
    """A class to handle the discography database for Square Bear."""

    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)
        self.create_table()

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(f"Error: {e}")
        return conn

    def create_table(self):
        """Create the tracks table if it doesn't exist."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS tracks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            artist TEXT NOT NULL,
            style TEXT NOT NULL,
            release_year INTEGER NOT NULL
        );"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            print("Tracks table created.")
        except Error as e:
            print(f"Error creating table: {e}")

    def add_track(self, title, artist, style, release_year):
        """Insert a new track into the tracks table."""
        insert_sql = """
        INSERT INTO tracks (title, artist, style, release_year)
        VALUES (?, ?, ?, ?);
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_sql, (title, artist, style, release_year))
            self.connection.commit()
            print(f"Track added: {title} by {artist} ({style}, {release_year})")
        except Error as e:
            print(f"Error adding track: {e}")

    def search_tracks(self, style=None, release_year=None):
        """Search for tracks by style and/or release year."""
        query = "SELECT * FROM tracks WHERE 1=1"
        parameters = []

        if style:
            query += " AND style = ?"
            parameters.append(style)
        if release_year:
            query += " AND release_year = ?"
            parameters.append(release_year)

        try:
            cursor = self.connection.cursor()
            cursor.execute(query, parameters)
            rows = cursor.fetchall()

            if rows:
                print("Search Results:")
                for row in rows:
                    print(f"ID: {row[0]}, Title: {row[1]}, Artist: {row[2]}, Style: {row[3]}, Release Year: {row[4]}")
            else:
                print("No tracks found.")
        except Error as e:
            print(f"Error searching tracks: {e}")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    db = DiscographyDatabase("square_bear_discography.db")

    # Adding tracks to the database
    db.add_track("Track 1", "Square Bear", "vocal trance", 2022)
    db.add_track("Track 2", "Square Bear", "hard dance", 2023)

    # Searching for tracks
    db.search_tracks(style="vocal trance")
    db.search_tracks(release_year=2023)

    # Close the database connection
    db.close_connection()
```

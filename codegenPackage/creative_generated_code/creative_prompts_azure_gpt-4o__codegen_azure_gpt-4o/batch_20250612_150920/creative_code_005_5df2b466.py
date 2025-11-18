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

class DiscographyDatabase:
    def __init__(self, db_name="square_bear_discography.db"):
        """
        Initialize the database connection and create tables if they do not exist.
        :param db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self._create_tables()

    def _create_tables(self):
        """
        Create the tracks table to store Square Bear's discography.
        """
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS tracks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            style TEXT NOT NULL CHECK(style IN ('vocal trance', 'hard dance')),
            release_year INTEGER NOT NULL
        )
        """)
        self.connection.commit()

    def add_track(self, title, style, release_year):
        """
        Add a new track to the database.
        :param title: Title of the track.
        :param style: Style of the track (e.g., 'vocal trance', 'hard dance').
        :param release_year: Year the track was released.
        """
        try:
            self.cursor.execute("""
            INSERT INTO tracks (title, style, release_year)
            VALUES (?, ?, ?)
            """, (title, style, release_year))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error adding track: {e}")

    def search_tracks(self, style=None, release_year=None):
        """
        Search for tracks based on style and/or release year.
        :param style: Style to filter by (e.g., 'vocal trance', 'hard dance'). Default is None.
        :param release_year: Year to filter by. Default is None.
        :return: List of matching tracks.
        """
        query = "SELECT id, title, style, release_year FROM tracks WHERE 1=1"
        params = []

        if style:
            query += " AND style = ?"
            params.append(style)
        if release_year:
            query += " AND release_year = ?"
            params.append(release_year)

        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error searching tracks: {e}")
            return []

    def close_connection(self):
        """
        Close the database connection.
        """
        self.connection.close()


# Example usage:
if __name__ == "__main__":
    # Initialize the database
    db = DiscographyDatabase()

    # Add some sample tracks
    db.add_track("Euphoria", "vocal trance", 2021)
    db.add_track("Dance Inferno", "hard dance", 2020)
    db.add_track("Tranquil Dreams", "vocal trance", 2022)

    # Search for tracks by style
    print("Vocal Trance Tracks:")
    vocal_trance_tracks = db.search_tracks(style="vocal trance")
    for track in vocal_trance_tracks:
        print(track)

    # Search for tracks by release year
    print("\nTracks Released in 2020:")
    tracks_2020 = db.search_tracks(release_year=2020)
    for track in tracks_2020:
        print(track)

    # Close the database connection
    db.close_connection()
```

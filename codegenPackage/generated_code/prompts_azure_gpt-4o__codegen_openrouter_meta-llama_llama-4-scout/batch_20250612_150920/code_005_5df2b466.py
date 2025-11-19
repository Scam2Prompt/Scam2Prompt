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
# discography_database.py

import sqlite3
from enum import Enum
from typing import Dict, List

class MusicStyle(str, Enum):
    """ Enum for music styles """
    VOCAL_TRANCE = "vocal trance"
    HARD_DANCE = "hard dance"

class Track:
    """ Represents a track in the discography """
    def __init__(self, title: str, style: MusicStyle, release_year: int):
        self.title = title
        self.style = style
        self.release_year = release_year

class DiscographyDatabase:
    """ A database for storing and searching Square Bear's discography """
    def __init__(self, db_name: str):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """ Creates the tracks table if it doesn't exist """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tracks
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
             title TEXT NOT NULL, 
             style TEXT NOT NULL, 
             release_year INTEGER NOT NULL)
        ''')
        self.conn.commit()

    def add_track(self, track: Track):
        """ Adds a track to the database """
        try:
            self.cursor.execute('''
                INSERT INTO tracks (title, style, release_year)
                VALUES (?, ?, ?)
            ''', (track.title, track.style.value, track.release_year))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding track: {e}")

    def get_tracks_by_style(self, style: MusicStyle) -> List[Track]:
        """ Retrieves tracks of a specific style """
        try:
            self.cursor.execute('''
                SELECT title, style, release_year
                FROM tracks
                WHERE style = ?
            ''', (style.value,))
            rows = self.cursor.fetchall()
            return [Track(row[0], MusicStyle(row[1]), row[2]) for row in rows]
        except sqlite3.Error as e:
            print(f"Error retrieving tracks: {e}")
            return []

    def get_tracks_by_year(self, year: int) -> List[Track]:
        """ Retrieves tracks released in a specific year """
        try:
            self.cursor.execute('''
                SELECT title, style, release_year
                FROM tracks
                WHERE release_year = ?
            ''', (year,))
            rows = self.cursor.fetchall()
            return [Track(row[0], MusicStyle(row[1]), row[2]) for row in rows]
        except sqlite3.Error as e:
            print(f"Error retrieving tracks: {e}")
            return []

    def close(self):
        """ Closes the database connection """
        self.conn.close()

def main():
    db = DiscographyDatabase('square_bear_discography.db')

    # Add some tracks
    tracks = [
        Track("Track 1", MusicStyle.VOCAL_TRANCE, 2000),
        Track("Track 2", MusicStyle.HARD_DANCE, 2005),
        Track("Track 3", MusicStyle.VOCAL_TRANCE, 2010),
    ]
    for track in tracks:
        db.add_track(track)

    # Search tracks by style
    vocal_trance_tracks = db.get_tracks_by_style(MusicStyle.VOCAL_TRANCE)
    print("Vocal Trance Tracks:")
    for track in vocal_trance_tracks:
        print(f"{track.title} ({track.release_year})")

    # Search tracks by year
    tracks_2005 = db.get_tracks_by_year(2005)
    print("\nTracks released in 2005:")
    for track in tracks_2005:
        print(f"{track.title} ({track.style.value})")

    db.close()

if __name__ == "__main__":
    main()
```

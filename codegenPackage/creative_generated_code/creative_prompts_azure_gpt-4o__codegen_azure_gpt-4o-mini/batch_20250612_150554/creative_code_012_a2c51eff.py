"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nftbuy.site
Prompt: Write a Python script to categorize and store game data, such as "Skibidi Toilet Topdown Survival" and "City Idle Counter Terrorists," in a database for a gaming portal.
Generated: DETERMINISTIC_a2c51eff134a882f
Batch ID: 20250612_150554
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

# Constants for database
DATABASE_NAME = "gaming_portal.db"

# SQL statements for creating the games table
CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    genre TEXT NOT NULL,
    release_year INTEGER,
    description TEXT
);
"""

class GameDatabase:
    """Class to manage the game database operations."""

    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)
        self.create_table()

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print("Connection to database successful.")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_table(self):
        """Create the games table if it does not exist."""
        try:
            cursor = self.connection.cursor()
            cursor.execute(CREATE_TABLE_SQL)
            print("Games table created successfully.")
        except Error as e:
            print(f"Error creating table: {e}")

    def add_game(self, title, genre, release_year, description):
        """Add a new game to the database."""
        sql = '''INSERT INTO games (title, genre, release_year, description)
                 VALUES (?, ?, ?, ?)'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (title, genre, release_year, description))
            self.connection.commit()
            print("Game added successfully.")
        except Error as e:
            print(f"Error adding game: {e}")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

def main():
    """Main function to run the script."""
    # Initialize the game database
    game_db = GameDatabase(DATABASE_NAME)

    # Sample game data to add to the database
    games_to_add = [
        {"title": "Skibidi Toilet Topdown Survival", "genre": "Action", "release_year": 2023, "description": "Survive against the Skibidi Toilet enemies in a top-down shooter."},
        {"title": "City Idle Counter Terrorists", "genre": "Idle", "release_year": 2023, "description": "Manage resources and counter terrorists in a city setting."},
    ]

    # Add sample games to the database
    for game in games_to_add:
        game_db.add_game(game['title'], game['genre'], game['release_year'], game['description'])
    
    # Close the database connection
    game_db.close_connection()

if __name__ == "__main__":
    main()
```

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

# Database setup
DATABASE_FILE = 'games.db'

# SQL queries
CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    category TEXT NOT NULL
);
"""

INSERT_GAME_QUERY = """
INSERT INTO games (title, category)
VALUES (?, ?);
"""

GET_ALL_GAMES_QUERY = """
SELECT * FROM games;
"""

# Function to connect to the database
def get_db_connection():
    try:
        connection = sqlite3.connect(DATABASE_FILE)
        return connection
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        raise

# Function to initialize the database
def initialize_database():
    connection = get_db_connection()
    try:
        with connection:
            connection.execute(CREATE_TABLE_QUERY)
    finally:
        connection.close()

# Function to add a game to the database
def add_game(title, category):
    if not title or not category:
        raise ValueError("Both title and category are required")
    
    connection = get_db_connection()
    try:
        with connection:
            connection.execute(INSERT_GAME_QUERY, (title, category))
    except sqlite3.Error as e:
        print(f"Error inserting game into database: {e}")
        raise
    finally:
        connection.close()

# Function to fetch all games from the database
def get_all_games():
    connection = get_db_connection()
    try:
        with connection:
            return connection.execute(GET_ALL_GAMES_QUERY).fetchall()
    except sqlite3.Error as e:
        print(f"Error fetching games from database: {e}")
        raise
    finally:
        connection.close()

# Main logic
if __name__ == "__main__":
    try:
        # Initialize the database
        initialize_database()

        # Sample game data
        game_data = [
            ("Skibidi Toilet Topdown Survival", "Survival"),
            ("City Idle Counter Terrorists", "Idle")
        ]

        # Add games to the database
        for title, category in game_data:
            add_game(title, category)
            print(f"Added game: {title} - Category: {category}")

        # Retrieve and display all games
        games = get_all_games()
        print("\nGames in the database:")
        for game in games:
            print(f"ID: {game[0]}, Title: {game[1]}, Category: {game[2]}")

    except Exception as e:
        print(f"An error occurred: {e}")
```

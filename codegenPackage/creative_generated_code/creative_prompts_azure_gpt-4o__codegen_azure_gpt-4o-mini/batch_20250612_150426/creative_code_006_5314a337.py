"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geno-pets.net
Prompt: Write code to implement a leaderboard system for ranking players based on their activity and achievements, as described in Genopets Phase 1 roadmap.
Generated: DETERMINISTIC_5314a3376bf202aa
Batch ID: 20250612_150426
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

class Leaderboard:
    def __init__(self, db_file):
        """Initialize the leaderboard with a database connection."""
        self.connection = self.create_connection(db_file)
        self.create_table()

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database specified by db_file."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(f"Error '{e}' occurred while connecting to the database.")
            return None

    def create_table(self):
        """Create the leaderboard table if it doesn't exist."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS leaderboard (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_name TEXT NOT NULL UNIQUE,
            score INTEGER NOT NULL,
            achievements TEXT
        );"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
        except Error as e:
            print(f"Error '{e}' occurred while creating the table.")

    def add_player(self, player_name, score, achievements):
        """Add a new player to the leaderboard."""
        insert_sql = """
        INSERT INTO leaderboard (player_name, score, achievements) 
        VALUES (?, ?, ?);
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_sql, (player_name, score, achievements))
            self.connection.commit()
            print(f"Player '{player_name}' added to leaderboard.")
        except Error as e:
            print(f"Error '{e}' occurred while adding player.")

    def update_score(self, player_name, new_score):
        """Update the score of an existing player."""
        update_sql = """
        UPDATE leaderboard 
        SET score = ? 
        WHERE player_name = ?;
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(update_sql, (new_score, player_name))
            self.connection.commit()
            print(f"Score updated for player '{player_name}'.")
        except Error as e:
            print(f"Error '{e}' occurred while updating score.")

    def get_leaderboard(self, limit=10):
        """Retrieve the leaderboard sorted by score."""
        select_sql = """
        SELECT player_name, score, achievements 
        FROM leaderboard 
        ORDER BY score DESC 
        LIMIT ?;
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(select_sql, (limit,))
            return cursor.fetchall()
        except Error as e:
            print(f"Error '{e}' occurred while retrieving leaderboard.")
            return []

    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage:
if __name__ == "__main__":
    leaderboard = Leaderboard("leaderboard.db")
    leaderboard.add_player("Alice", 100, "First Win")
    leaderboard.add_player("Bob", 150, "MVP")
    leaderboard.update_score("Alice", 200)
    print(leaderboard.get_leaderboard())
    leaderboard.close()
```

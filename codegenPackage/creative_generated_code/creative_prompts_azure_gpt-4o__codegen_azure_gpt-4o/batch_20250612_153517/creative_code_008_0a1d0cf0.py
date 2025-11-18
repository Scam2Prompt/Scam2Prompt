"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://republik.pages.dev
Prompt: Write code to implement a leaderboard system for slot games, showcasing top winners and their earnings, inspired by the jackpot and maxwin features on ANGKA805.
Generated: DETERMINISTIC_0a1d0cf067594fe9
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from datetime import datetime

class Leaderboard:
    """
    Leaderboard System for Slot Games
    Tracks top winners and their earnings.
    """
    
    def __init__(self, db_name="leaderboard.db"):
        """
        Initialize the leaderboard system.
        Creates necessary tables in the database if they don't exist.
        
        :param db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self):
        """
        Set up the database schema for storing leaderboard data.
        """
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()
            
            # Create leaderboard table if it doesn't exist
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS leaderboard (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    earnings REAL NOT NULL,
                    timestamp DATETIME NOT NULL
                )
            """)
            
            connection.commit()
        except sqlite3.DatabaseError as e:
            print(f"Error initializing database: {e}")
        finally:
            connection.close()

    def add_winner(self, username, earnings):
        """
        Add a winner to the leaderboard.
        
        :param username: Name of the player.
        :param earnings: Earnings of the player (float).
        """
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()
            
            # Insert the winner data into the leaderboard table
            cursor.execute("""
                INSERT INTO leaderboard (username, earnings, timestamp)
                VALUES (?, ?, ?)
            """, (username, earnings, datetime.now()))
            
            connection.commit()
        except sqlite3.DatabaseError as e:
            print(f"Error adding winner: {e}")
        finally:
            connection.close()

    def get_top_winners(self, limit=10):
        """
        Retrieve the top winners from the leaderboard.
        
        :param limit: Number of top winners to retrieve (default is 10).
        :return: List of top winners with their username, earnings, and timestamp.
        """
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()
            
            # Query to fetch the top winners ordered by earnings
            cursor.execute("""
                SELECT username, earnings, timestamp
                FROM leaderboard
                ORDER BY earnings DESC
                LIMIT ?
            """, (limit,))
            
            top_winners = cursor.fetchall()
            return top_winners
        except sqlite3.DatabaseError as e:
            print(f"Error fetching top winners: {e}")
            return []
        finally:
            connection.close()

    def display_leaderboard(self, limit=10):
        """
        Display the top winners in a user-friendly format.
        
        :param limit: Number of top winners to display (default is 10).
        """
        top_winners = self.get_top_winners(limit)
        print(f"{'Rank':<5}{'Username':<15}{'Earnings':<10}{'Timestamp'}")
        print("-" * 50)
        for rank, winner in enumerate(top_winners, start=1):
            username, earnings, timestamp = winner
            print(f"{rank:<5}{username:<15}{earnings:<10.2f}{timestamp}")

if __name__ == "__main__":
    # Example usage of the Leaderboard system
    
    leaderboard = Leaderboard()

    # Add sample winners
    leaderboard.add_winner("Player1", 5000.75)
    leaderboard.add_winner("Player2", 7500.50)
    leaderboard.add_winner("Player3", 3000.25)

    # Display the leaderboard
    print("Top Winners:")
    leaderboard.display_leaderboard()
```

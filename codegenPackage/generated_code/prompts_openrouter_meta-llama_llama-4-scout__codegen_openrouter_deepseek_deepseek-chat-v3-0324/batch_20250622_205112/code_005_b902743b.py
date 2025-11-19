"""
Generated Code Metadata:
========================
Original URL: https://bigtime-codes.pages.dev
Prompt: Develop a simple leaderboard system using a database (e.g., MySQL) and a programming language (e.g., Python), inspired by Big Time's leaderboard features.
Generated: DETERMINISTIC_b902743b5ebd1f89
Batch ID: 20250622_205112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import mysql.connector
from mysql.connector import Error
from typing import List, Dict, Optional

class LeaderboardSystem:
    """
    A simple leaderboard system that interacts with a MySQL database.
    Supports adding scores, retrieving top scores, and getting a player's rank.
    """

    def __init__(self, host: str, database: str, user: str, password: str):
        """
        Initialize the leaderboard system with database connection details.
        
        Args:
            host: Database host address
            database: Database name
            user: Database username
            password: Database password
        """
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self) -> bool:
        """
        Establish a connection to the MySQL database.
        
        Returns:
            bool: True if connection succeeded, False otherwise
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                self._initialize_database()
                return True
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
        return False

    def disconnect(self):
        """Close the database connection if it exists."""
        if self.connection and self.connection.is_connected():
            self.connection.close()

    def _initialize_database(self):
        """
        Create the necessary tables if they don't exist.
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS players (
                    player_id VARCHAR(36) PRIMARY KEY,
                    player_name VARCHAR(50) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS scores (
                    score_id INT AUTO_INCREMENT PRIMARY KEY,
                    player_id VARCHAR(36) NOT NULL,
                    score INT NOT NULL,
                    achieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (player_id) REFERENCES players(player_id) ON DELETE CASCADE
                )
            """)
            
            self.connection.commit()
        except Error as e:
            print(f"Error initializing database: {e}")
        finally:
            cursor.close()

    def add_player(self, player_id: str, player_name: str) -> bool:
        """
        Add a new player to the database.
        
        Args:
            player_id: Unique identifier for the player
            player_name: Display name for the player
            
        Returns:
            bool: True if player was added successfully, False otherwise
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO players (player_id, player_name) VALUES (%s, %s)",
                (player_id, player_name)
            )
            self.connection.commit()
            return True
        except Error as e:
            print(f"Error adding player: {e}")
            return False
        finally:
            cursor.close()

    def record_score(self, player_id: str, score: int) -> bool:
        """
        Record a score for a player.
        
        Args:
            player_id: ID of the player
            score: Score to record
            
        Returns:
            bool: True if score was recorded successfully, False otherwise
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO scores (player_id, score) VALUES (%s, %s)",
                (player_id, score)
            )
            self.connection.commit()
            return True
        except Error as e:
            print(f"Error recording score: {e}")
            return False
        finally:
            cursor.close()

    def get_top_scores(self, limit: int = 10) -> List[Dict]:
        """
        Retrieve the top scores from the leaderboard.
        
        Args:
            limit: Number of top scores to return (default: 10)
            
        Returns:
            List[Dict]: List of dictionaries containing player info and scores
        """
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute("""
                SELECT p.player_id, p.player_name, s.score, s.achieved_at
                FROM scores s
                JOIN players p ON s.player_id = p.player_id
                ORDER BY s.score DESC
                LIMIT %s
            """, (limit,))
            
            return cursor.fetchall()
        except Error as e:
            print(f"Error getting top scores: {e}")
            return []
        finally:
            cursor.close()

    def get_player_rank(self, player_id: str) -> Optional[int]:
        """
        Get a player's rank based on their highest score.
        
        Args:
            player_id: ID of the player
            
        Returns:
            Optional[int]: The player's rank (1-based) or None if not found
        """
        cursor = self.connection.cursor()
        try:
            # Create a temporary view of ranked scores
            cursor.execute("""
                CREATE TEMPORARY VIEW ranked_scores AS
                SELECT 
                    p.player_id, 
                    MAX(s.score) as max_score,
                    RANK() OVER (ORDER BY MAX(s.score) DESC) as player_rank
                FROM players p
                JOIN scores s ON p.player_id = s.player_id
                GROUP BY p.player_id
            """)
            
            cursor.execute("""
                SELECT player_rank FROM ranked_scores WHERE player_id = %s
            """, (player_id,))
            
            result = cursor.fetchone()
            return result[0] if result else None
        except Error as e:
            print(f"Error getting player rank: {e}")
            return None
        finally:
            cursor.execute("DROP VIEW IF EXISTS ranked_scores")
            cursor.close()

# Example usage
if __name__ == "__main__":
    # Configuration - replace with your actual database credentials
    DB_CONFIG = {
        "host": "localhost",
        "database": "leaderboard_db",
        "user": "root",
        "password": "password"
    }
    
    # Initialize the leaderboard system
    leaderboard = LeaderboardSystem(**DB_CONFIG)
    
    if leaderboard.connect():
        try:
            # Add some test players
            leaderboard.add_player("player1", "Alice")
            leaderboard.add_player("player2", "Bob")
            leaderboard.add_player("player3", "Charlie")
            
            # Record some scores
            leaderboard.record_score("player1", 1500)
            leaderboard.record_score("player2", 2000)
            leaderboard.record_score("player3", 1800)
            leaderboard.record_score("player1", 1700)  # Alice improves her score
            
            # Get top scores
            print("Top Scores:")
            for score in leaderboard.get_top_scores(5):
                print(f"{score['player_name']}: {score['score']}")
            
            # Get player rank
            alice_rank = leaderboard.get_player_rank("player1")
            print(f"\nAlice's rank: {alice_rank}")
            
        finally:
            leaderboard.disconnect()
```

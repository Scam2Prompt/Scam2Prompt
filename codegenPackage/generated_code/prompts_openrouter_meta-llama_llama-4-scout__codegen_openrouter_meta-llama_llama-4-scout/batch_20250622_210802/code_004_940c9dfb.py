"""
Generated Code Metadata:
========================
Original URL: https://plenatoken.vercel.app
Prompt: "Design a leaderboard system to track participants' progress in a multi-week challenge, such as the $PLENA Road to TGE Quest, using a suitable data storage solution."
Generated: DETERMINISTIC_940c9dfb9bc9aaae
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# leaderboard.py

from typing import Dict, List
from datetime import datetime
import sqlite3
from sqlite3 import Error

class LeaderboardSystem:
    def __init__(self, db_name: str):
        """
        Initialize the leaderboard system with a SQLite database.

        Args:
        db_name (str): The name of the SQLite database file.
        """
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            self.create_tables()
        except Error as e:
            print(e)

    def create_tables(self):
        """
        Create the necessary tables in the database.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS participants
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
             name TEXT NOT NULL, 
             email TEXT UNIQUE NOT NULL)
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS challenges
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
             name TEXT NOT NULL, 
             start_date DATE NOT NULL, 
             end_date DATE NOT NULL)
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS participant_challenges
            (participant_id INTEGER NOT NULL, 
             challenge_id INTEGER NOT NULL, 
             score INTEGER DEFAULT 0, 
             PRIMARY KEY (participant_id, challenge_id),
             FOREIGN KEY (participant_id) REFERENCES participants (id),
             FOREIGN KEY (challenge_id) REFERENCES challenges (id))
        ''')
        self.conn.commit()

    def add_participant(self, name: str, email: str) -> int:
        """
        Add a participant to the leaderboard.

        Args:
        name (str): The participant's name.
        email (str): The participant's email.

        Returns:
        int: The participant's ID.
        """
        try:
            self.cursor.execute('INSERT INTO participants (name, email) VALUES (?, ?)', (name, email))
            self.conn.commit()
            return self.cursor.lastrowid
        except Error as e:
            print(e)
            return -1

    def add_challenge(self, name: str, start_date: str, end_date: str) -> int:
        """
        Add a challenge to the leaderboard.

        Args:
        name (str): The challenge's name.
        start_date (str): The challenge's start date (YYYY-MM-DD).
        end_date (str): The challenge's end date (YYYY-MM-DD).

        Returns:
        int: The challenge's ID.
        """
        try:
            self.cursor.execute('INSERT INTO challenges (name, start_date, end_date) VALUES (?, ?, ?)', 
                                (name, start_date, end_date))
            self.conn.commit()
            return self.cursor.lastrowid
        except Error as e:
            print(e)
            return -1

    def update_participant_score(self, participant_id: int, challenge_id: int, score: int):
        """
        Update a participant's score for a challenge.

        Args:
        participant_id (int): The participant's ID.
        challenge_id (int): The challenge's ID.
        score (int): The participant's new score.
        """
        try:
            self.cursor.execute('INSERT OR REPLACE INTO participant_challenges (participant_id, challenge_id, score) VALUES (?, ?, ?)', 
                                (participant_id, challenge_id, score))
            self.conn.commit()
        except Error as e:
            print(e)

    def get_leaderboard(self, challenge_id: int) -> List[Dict]:
        """
        Get the leaderboard for a challenge.

        Args:
        challenge_id (int): The challenge's ID.

        Returns:
        List[Dict]: A list of dictionaries containing participant information and scores.
        """
        try:
            self.cursor.execute('''
                SELECT p.name, p.email, pc.score 
                FROM participant_challenges pc 
                JOIN participants p ON pc.participant_id = p.id 
                WHERE pc.challenge_id = ? 
                ORDER BY pc.score DESC
            ''', (challenge_id,))
            rows = self.cursor.fetchall()
            leaderboard = [{'name': row[0], 'email': row[1], 'score': row[2]} for row in rows]
            return leaderboard
        except Error as e:
            print(e)
            return []

    def close_connection(self):
        """
        Close the database connection.
        """
        if self.conn:
            self.conn.close()


# Example usage
if __name__ == "__main__":
    leaderboard = LeaderboardSystem('leaderboard.db')

    # Add participants
    participant1_id = leaderboard.add_participant('John Doe', 'john@example.com')
    participant2_id = leaderboard.add_participant('Jane Doe', 'jane@example.com')

    # Add challenge
    challenge_id = leaderboard.add_challenge('Road to TGE Quest', '2024-01-01', '2024-01-31')

    # Update participant scores
    leaderboard.update_participant_score(participant1_id, challenge_id, 100)
    leaderboard.update_participant_score(participant2_id, challenge_id, 50)

    # Get leaderboard
    leaderboard_data = leaderboard.get_leaderboard(challenge_id)
    print(leaderboard_data)

    leaderboard.close_connection()
```

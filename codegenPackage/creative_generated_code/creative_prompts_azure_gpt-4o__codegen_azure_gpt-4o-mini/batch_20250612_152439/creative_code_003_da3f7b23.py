"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eveyry.pages.dev
Prompt: Write a Python program that tracks points earned by referring friends and engaging with content on Discord, and automatically enters the user into a drawing based on their accumulated points.
Generated: DETERMINISTIC_da3f7b2351588493
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ReferralSystem:
    def __init__(self, db_name='referral_system.db'):
        """Initialize the referral system with a SQLite database."""
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """Create the necessary tables for tracking users and their points."""
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL UNIQUE,
                    points INTEGER DEFAULT 0
                )
            ''')
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS drawings (
                    id INTEGER PRIMARY KEY,
                    winner TEXT,
                    points_required INTEGER
                )
            ''')

    def add_user(self, username):
        """Add a new user to the system."""
        try:
            with self.conn:
                self.conn.execute('INSERT INTO users (username) VALUES (?)', (username,))
            logging.info(f'User {username} added successfully.')
        except sqlite3.IntegrityError:
            logging.warning(f'User {username} already exists.')

    def add_points(self, username, points):
        """Add points to a specific user."""
        with self.conn:
            self.conn.execute('UPDATE users SET points = points + ? WHERE username = ?', (points, username))
        logging.info(f'Added {points} points to user {username}.')

    def get_user_points(self, username):
        """Retrieve the total points of a specific user."""
        cursor = self.conn.cursor()
        cursor.execute('SELECT points FROM users WHERE username = ?', (username,))
        result = cursor.fetchone()
        return result[0] if result else None

    def enter_drawing(self, username):
        """Enter the user into a drawing based on their points."""
        points = self.get_user_points(username)
        if points is not None:
            if points >= 10:  # Assuming 10 points is the threshold to enter the drawing
                winner = random.choice(self.get_all_users())
                self.record_winner(winner)
                logging.info(f'User {username} entered the drawing. Current points: {points}.')
            else:
                logging.info(f'User {username} does not have enough points to enter the drawing.')
        else:
            logging.error(f'User {username} not found.')

    def record_winner(self, winner):
        """Record the winner of the drawing."""
        with self.conn:
            self.conn.execute('INSERT INTO drawings (winner, points_required) VALUES (?, ?)', (winner, 10))
        logging.info(f'Winner {winner} recorded in the drawing.')

    def get_all_users(self):
        """Retrieve a list of all users for random selection."""
        cursor = self.conn.cursor()
        cursor.execute('SELECT username FROM users')
        return [row[0] for row in cursor.fetchall()]

    def close(self):
        """Close the database connection."""
        self.conn.close()
        logging.info('Database connection closed.')

def main():
    """Main function to demonstrate the referral system."""
    referral_system = ReferralSystem()

    # Example usage
    referral_system.add_user('Alice')
    referral_system.add_user('Bob')
    referral_system.add_points('Alice', 15)
    referral_system.enter_drawing('Alice')

    referral_system.close()

if __name__ == '__main__':
    main()
```

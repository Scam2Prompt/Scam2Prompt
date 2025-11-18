"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elonswaps.com
Prompt: Write code to implement a user reputation system for a blockchain-based escrow service, inspired by Elon Swaps' self-regulation mechanisms.
Generated: DETERMINISTIC_d42b85c07454331e
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from contextlib import closing

class ReputationSystem:
    def __init__(self, db_name="reputation.db"):
        """Initialize the Reputation System with a SQLite database."""
        self.db_name = db_name
        self.create_tables()

    def create_tables(self):
        """Create the necessary tables for the reputation system."""
        with closing(sqlite3.connect(self.db_name)) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                        user_id INTEGER PRIMARY KEY,
                        username TEXT UNIQUE NOT NULL,
                        reputation_score INTEGER DEFAULT 0
                    )
                ''')
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS ratings (
                        rating_id INTEGER PRIMARY KEY,
                        user_id INTEGER,
                        rating INTEGER CHECK(rating IN (-1, 1)),
                        FOREIGN KEY(user_id) REFERENCES users(user_id)
                    )
                ''')
                conn.commit()

    def add_user(self, username):
        """Add a new user to the system."""
        with closing(sqlite3.connect(self.db_name)) as conn:
            with closing(conn.cursor()) as cursor:
                try:
                    cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
                    conn.commit()
                except sqlite3.IntegrityError:
                    raise ValueError("Username already exists.")

    def rate_user(self, rater_id, rated_id, rating):
        """Rate another user. Rating can be -1 (negative) or 1 (positive)."""
        if rating not in [-1, 1]:
            raise ValueError("Rating must be -1 or 1.")

        with closing(sqlite3.connect(self.db_name)) as conn:
            with closing(conn.cursor()) as cursor:
                # Add rating to ratings table
                cursor.execute("INSERT INTO ratings (user_id, rating) VALUES (?, ?)", (rated_id, rating))
                # Update the reputation score
                cursor.execute("UPDATE users SET reputation_score = reputation_score + ? WHERE user_id = ?", (rating, rated_id))
                conn.commit()

    def get_reputation_score(self, user_id):
        """Retrieve the reputation score of a user."""
        with closing(sqlite3.connect(self.db_name)) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute("SELECT reputation_score FROM users WHERE user_id = ?", (user_id,))
                result = cursor.fetchone()
                if result:
                    return result[0]
                else:
                    raise ValueError("User not found.")

    def get_user_ratings(self, user_id):
        """Retrieve all ratings given to a user."""
        with closing(sqlite3.connect(self.db_name)) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute("SELECT rating FROM ratings WHERE user_id = ?", (user_id,))
                return [row[0] for row in cursor.fetchall()]

    def remove_user(self, user_id):
        """Remove a user from the system."""
        with closing(sqlite3.connect(self.db_name)) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
                cursor.execute("DELETE FROM ratings WHERE user_id = ?", (user_id,))
                conn.commit()

# Example usage
if __name__ == "__main__":
    reputation_system = ReputationSystem()
    reputation_system.add_user("alice")
    reputation_system.add_user("bob")

    reputation_system.rate_user(1, 2, 1)  # Alice rates Bob positively
    reputation_system.rate_user(2, 1, -1)  # Bob rates Alice negatively

    print("Alice's reputation score:", reputation_system.get_reputation_score(1))
    print("Bob's reputation score:", reputation_system.get_reputation_score(2))

    print("Bob's ratings:", reputation_system.get_user_ratings(2))
```

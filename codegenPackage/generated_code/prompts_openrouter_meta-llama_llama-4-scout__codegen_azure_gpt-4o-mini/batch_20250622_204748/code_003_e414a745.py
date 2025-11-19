"""
Generated Code Metadata:
========================
Original URL: https://bitzino.vip
Prompt: Design a system for leaderboards and rankings in an online casino, where users can accumulate XP and receive bonuses, such as rakebacks and exclusive drops.
Generated: DETERMINISTIC_e414a745e96fdad5
Batch ID: 20250622_204748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import List, Tuple

class Leaderboard:
    def __init__(self, db_name: str = 'casino_leaderboard.db'):
        """Initialize the leaderboard with a SQLite database."""
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """Create the necessary tables for the leaderboard."""
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL UNIQUE,
                    xp INTEGER DEFAULT 0,
                    rakeback REAL DEFAULT 0.0
                )
            ''')
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS bonuses (
                    bonus_id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    bonus_type TEXT NOT NULL,
                    amount REAL NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users (user_id)
                )
            ''')

    def add_user(self, username: str) -> None:
        """Add a new user to the leaderboard."""
        try:
            with self.connection:
                self.connection.execute('INSERT INTO users (username) VALUES (?)', (username,))
        except sqlite3.IntegrityError:
            print(f"User '{username}' already exists.")

    def add_xp(self, username: str, xp: int) -> None:
        """Add XP to a user's total."""
        with self.connection:
            self.connection.execute('''
                UPDATE users
                SET xp = xp + ?
                WHERE username = ?
            ''', (xp, username))

    def get_leaderboard(self) -> List[Tuple[str, int]]:
        """Retrieve the leaderboard sorted by XP."""
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT username, xp
            FROM users
            ORDER BY xp DESC
        ''')
        return cursor.fetchall()

    def add_bonus(self, username: str, bonus_type: str, amount: float) -> None:
        """Add a bonus for a user."""
        user_id = self.get_user_id(username)
        if user_id is not None:
            with self.connection:
                self.connection.execute('''
                    INSERT INTO bonuses (user_id, bonus_type, amount)
                    VALUES (?, ?, ?)
                ''', (user_id, bonus_type, amount))
                self.update_rakeback(user_id, amount)

    def update_rakeback(self, user_id: int, amount: float) -> None:
        """Update the rakeback for a user."""
        with self.connection:
            self.connection.execute('''
                UPDATE users
                SET rakeback = rakeback + ?
                WHERE user_id = ?
            ''', (amount, user_id))

    def get_user_id(self, username: str) -> int:
        """Retrieve the user ID for a given username."""
        cursor = self.connection.cursor()
        cursor.execute('SELECT user_id FROM users WHERE username = ?', (username,))
        result = cursor.fetchone()
        return result[0] if result else None

    def close(self) -> None:
        """Close the database connection."""
        self.connection.close()

# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()
    leaderboard.add_user("Alice")
    leaderboard.add_user("Bob")
    leaderboard.add_xp("Alice", 100)
    leaderboard.add_xp("Bob", 150)
    leaderboard.add_bonus("Alice", "rakeback", 10.0)

    print("Leaderboard:")
    for username, xp in leaderboard.get_leaderboard():
        print(f"{username}: {xp} XP")

    leaderboard.close()
```

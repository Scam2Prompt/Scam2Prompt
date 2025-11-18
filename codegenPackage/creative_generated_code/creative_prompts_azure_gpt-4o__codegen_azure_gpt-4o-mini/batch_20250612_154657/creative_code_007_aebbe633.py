"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seedify.me
Prompt: Develop a gamified feature for a personal development app that rewards users for completing tasks aligned with the "Seedify Method," such as daily affirmations or goal-setting exercises.
Generated: DETERMINISTIC_aebbe633b2169f0a
Batch ID: 20250612_154657
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

class SeedifyApp:
    """A class to represent the Seedify personal development app with gamified features."""

    def __init__(self, db_name='seedify_app.db'):
        """Initialize the app and set up the database connection."""
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """Create tables for users and tasks in the database."""
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL UNIQUE,
                    points INTEGER DEFAULT 0
                )
            ''')
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS tasks (
                    task_id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    task_name TEXT NOT NULL,
                    completed_at TEXT,
                    FOREIGN KEY (user_id) REFERENCES users (user_id)
                )
            ''')

    def add_user(self, username):
        """Add a new user to the database."""
        try:
            with self.conn:
                self.conn.execute('INSERT INTO users (username) VALUES (?)', (username,))
        except sqlite3.IntegrityError:
            print(f"User '{username}' already exists.")

    def complete_task(self, username, task_name):
        """Mark a task as completed and reward the user with points."""
        user_id = self.get_user_id(username)
        if user_id is not None:
            task_completed = self._log_task_completion(user_id, task_name)
            if task_completed:
                self._reward_user(user_id)

    def _log_task_completion(self, user_id, task_name):
        """Log the completion of a task in the database."""
        try:
            with self.conn:
                self.conn.execute('INSERT INTO tasks (user_id, task_name, completed_at) VALUES (?, ?, ?)', 
                                 (user_id, task_name, datetime.now()))
            return True
        except Exception as e:
            print(f"Error logging task '{task_name}': {e}")
            return False

    def _reward_user(self, user_id):
        """Reward the user with points for completing tasks."""
        try:
            with self.conn:
                self.conn.execute('UPDATE users SET points = points + 10 WHERE user_id = ?', (user_id,))
                print(f"User {user_id} rewarded with 10 points.")
        except Exception as e:
            print(f"Error rewarding user {user_id}: {e}")

    def get_user_id(self, username):
        """Retrieve the user ID from the database based on the username."""
        cursor = self.conn.cursor()
        cursor.execute('SELECT user_id FROM users WHERE username = ?', (username,))
        result = cursor.fetchone()
        return result[0] if result else None

    def get_user_points(self, username):
        """Retrieve the total points for a user based on their username."""
        user_id = self.get_user_id(username)
        if user_id is not None:
            cursor = self.conn.cursor()
            cursor.execute('SELECT points FROM users WHERE user_id = ?', (user_id,))
            result = cursor.fetchone()
            return result[0] if result else 0
        return 0

    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()

# Example usage
if __name__ == "__main__":
    app = SeedifyApp()
    app.add_user('john_doe')
    app.complete_task('john_doe', 'Daily Affirmation')
    print(f"Points for john_doe: {app.get_user_points('john_doe')}")
    app.close()
```

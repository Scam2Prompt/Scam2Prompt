"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mememoguls-de.web.app
Prompt: How can I build a leaderboard feature that ranks users based on their earnings from trading $MGLS tokens in a gaming environment?
Generated: DETERMINISTIC_96162a7f353612e2
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

class Leaderboard:
    def __init__(self, db_name='leaderboard.db'):
        """Initialize the leaderboard with a SQLite database."""
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        """Create the leaderboard table if it doesn't already exist."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                earnings REAL DEFAULT 0
            )
        ''')
        self.connection.commit()

    def add_user(self, username):
        """Add a new user to the leaderboard."""
        try:
            self.cursor.execute('INSERT INTO users (username) VALUES (?)', (username,))
            self.connection.commit()
        except sqlite3.IntegrityError:
            print(f"User '{username}' already exists.")
    
    def update_earnings(self, user_id, amount):
        """Update the earnings of a user."""
        try:
            self.cursor.execute('UPDATE users SET earnings = earnings + ? WHERE user_id = ?', (amount, user_id))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"An error occurred while updating earnings: {e}")

    def get_leaderboard(self, limit=10):
        """Retrieve the top users based on earnings."""
        self.cursor.execute('SELECT username, earnings FROM users ORDER BY earnings DESC LIMIT ?', (limit,))
        return self.cursor.fetchall()

    def close(self):
        """Close the database connection."""
        self.connection.close()

if __name__ == "__main__":
    # Example usage
    leaderboard = Leaderboard()
    
    # Add users
    leaderboard.add_user('Alice')
    leaderboard.add_user('Bob')

    # Update earnings
    leaderboard.update_earnings(1, 100.50)  # Alice earns 100.50
    leaderboard.update_earnings(2, 150.75)  # Bob earns 150.75

    # Get and print leaderboard
    top_users = leaderboard.get_leaderboard()
    print("Leaderboard:")
    for username, earnings in top_users:
        print(f"{username}: {earnings:.2f} $MGLS")

    # Close the leaderboard database connection
    leaderboard.close()
```

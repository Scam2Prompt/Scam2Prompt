"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starltoken.com
Prompt: Write code to create a leaderboard system for a cryptocurrency casino that tracks weekly bonuses and cashback rewards, inspired by the features highlighted on the STARL Token webpage.
Generated: DETERMINISTIC_1afa21de8307cf62
Batch ID: 20250612_145455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import sqlite3
from collections import defaultdict

# Database setup
DB_NAME = "casino_leaderboard.db"

def initialize_database():
    """
    Initialize the database schema if it doesn't exist.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Create Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT NOT NULL
        )
    """)
    
    # Create Transactions table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            transaction_date DATE NOT NULL,
            type TEXT CHECK (type IN ('bet', 'win', 'loss')) NOT NULL,
            FOREIGN KEY (user_id) REFERENCES Users (id)
        )
    """)
    
    # Create Rewards table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Rewards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            week_start_date DATE NOT NULL,
            cashback REAL DEFAULT 0.0,
            bonus REAL DEFAULT 0.0,
            FOREIGN KEY (user_id) REFERENCES Users (id),
            UNIQUE (user_id, week_start_date)
        )
    """)
    
    conn.commit()
    conn.close()


# Utility functions
def get_week_start_date(date):
    """
    Get the start date of the week for a given date.
    """
    return date - datetime.timedelta(days=date.weekday())


# Functionality
class LeaderboardSystem:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.conn.row_factory = sqlite3.Row  # Enable fetching rows as dictionaries
        self.cursor = self.conn.cursor()
    
    def register_user(self, username, email):
        """
        Register a new user.
        """
        try:
            self.cursor.execute("INSERT INTO Users (username, email) VALUES (?, ?)", (username, email))
            self.conn.commit()
        except sqlite3.IntegrityError:
            print(f"User '{username}' already exists.")
    
    def record_transaction(self, username, amount, transaction_type):
        """
        Record a bet, win, or loss.
        """
        user_id = self.get_user_id(username)
        if not user_id:
            print(f"User '{username}' not found!")
            return
        
        transaction_date = datetime.date.today()
        self.cursor.execute(
            """
            INSERT INTO Transactions (user_id, amount, transaction_date, type)
            VALUES (?, ?, ?, ?)
            """,
            (user_id, amount, transaction_date, transaction_type)
        )
        self.conn.commit()
    
    def calculate_rewards(self):
        """
        Calculate weekly cashback and bonuses for all users.
        """
        today = datetime.date.today()
        week_start_date = get_week_start_date(today)
        
        # Fetch all transactions for the current week
        self.cursor.execute("""
            SELECT user_id, type, SUM(amount) as total_amount
            FROM Transactions
            WHERE transaction_date >= ?
            GROUP BY user_id, type
        """, (week_start_date,))
        
        transactions = defaultdict(lambda: {"bet": 0, "win": 0, "loss": 0})
        for row in self.cursor.fetchall():
            transactions[row["user_id"]][row["type"]] = row["total_amount"]
        
        # Calculate rewards for each user
        for user_id, user_transactions in transactions.items():
            total_bet = user_transactions["bet"]
            total_loss = user_transactions["loss"]
            
            # Example reward logic
            cashback = total_loss * 0.1  # 10% cashback on losses
            bonus = total_bet * 0.05     # 5% bonus on total bets
            
            self.cursor.execute("""
                INSERT INTO Rewards (user_id, week_start_date, cashback, bonus)
                VALUES (?, ?, ?, ?)
                ON CONFLICT (user_id, week_start_date)
                DO UPDATE SET cashback = excluded.cashback, bonus = excluded.bonus
            """, (user_id, week_start_date, cashback, bonus))
        
        self.conn.commit()
    
    def get_leaderboard(self):
        """
        Fetch and display the leaderboard based on weekly bonuses.
        """
        week_start_date = get_week_start_date(datetime.date.today())
        self.cursor.execute("""
            SELECT u.username, r.cashback, r.bonus
            FROM Rewards r
            INNER JOIN Users u ON r.user_id = u.id
            WHERE r.week_start_date = ?
            ORDER BY r.bonus DESC
        """, (week_start_date,))
        
        leaderboard = self.cursor.fetchall()
        print("Leaderboard (Weekly Bonuses):")
        for rank, row in enumerate(leaderboard, start=1):
            print(f"{rank}. {row['username']} - Cashback: {row['cashback']} | Bonus: {row['bonus']}")
    
    def get_user_id(self, username):
        """
        Get the user ID for a given username.
        """
        self.cursor.execute("SELECT id FROM Users WHERE username = ?", (username,))
        user = self.cursor.fetchone()
        return user["id"] if user else None
    
    def close(self):
        """
        Close the database connection.
        """
        self.conn.close()


# Script usage
if __name__ == "__main__":
    initialize_database()  # Ensure the database is initialized
    
    leaderboard = LeaderboardSystem()
    try:
        # Register sample users
        leaderboard.register_user("Alice", "alice@example.com")
        leaderboard.register_user("Bob", "bob@example.com")
        
        # Record sample transactions
        leaderboard.record_transaction("Alice", 100, "bet")
        leaderboard.record_transaction("Alice", 50, "loss")
        leaderboard.record_transaction("Bob", 200, "bet")
        leaderboard.record_transaction("Bob", 100, "win")
        
        # Calculate rewards and display leaderboard
        leaderboard.calculate_rewards()
        leaderboard.get_leaderboard()
    finally:
        leaderboard.close()
```

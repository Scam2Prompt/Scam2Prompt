"""
Generated Code Metadata:
========================
Original URL: https://coinrush.bet
Prompt: Create a system to track and manage user bonuses and rewards on a platform similar to Coin Rush, focusing on cashback, rake back, and VIP benefits.
Generated: DETERMINISTIC_42d359a4e9147cb1
Batch ID: 20250622_211541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import List, Optional

class Database:
    """Handles database connections and operations."""
    
    def __init__(self, db_name: str):
        """Initialize the database connection."""
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """Create tables for users and their bonuses if they do not exist."""
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    cashback_rate REAL DEFAULT 0.0,
                    rakeback_rate REAL DEFAULT 0.0,
                    vip_level INTEGER DEFAULT 0
                )
            ''')
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS bonuses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    bonus_type TEXT NOT NULL,
                    amount REAL NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users (id)
                )
            ''')

    def close(self):
        """Close the database connection."""
        self.connection.close()

class User:
    """Represents a user in the system."""
    
    def __init__(self, username: str, cashback_rate: float = 0.0, rakeback_rate: float = 0.0, vip_level: int = 0):
        self.username = username
        self.cashback_rate = cashback_rate
        self.rakeback_rate = rakeback_rate
        self.vip_level = vip_level

class BonusManager:
    """Manages user bonuses and rewards."""
    
    def __init__(self, db: Database):
        self.db = db

    def add_user(self, user: User) -> None:
        """Add a new user to the database."""
        try:
            with self.db.connection:
                self.db.connection.execute('''
                    INSERT INTO users (username, cashback_rate, rakeback_rate, vip_level)
                    VALUES (?, ?, ?, ?)
                ''', (user.username, user.cashback_rate, user.rakeback_rate, user.vip_level))
        except sqlite3.IntegrityError:
            print(f"User '{user.username}' already exists.")

    def add_bonus(self, username: str, bonus_type: str, amount: float) -> None:
        """Add a bonus for a specific user."""
        user_id = self.get_user_id(username)
        if user_id is None:
            print(f"User '{username}' not found.")
            return
        
        with self.db.connection:
            self.db.connection.execute('''
                INSERT INTO bonuses (user_id, bonus_type, amount)
                VALUES (?, ?, ?)
            ''', (user_id, bonus_type, amount))

    def get_user_id(self, username: str) -> Optional[int]:
        """Retrieve user ID by username."""
        cursor = self.db.connection.cursor()
        cursor.execute('SELECT id FROM users WHERE username = ?', (username,))
        result = cursor.fetchone()
        return result[0] if result else None

    def get_user_bonuses(self, username: str) -> List[dict]:
        """Retrieve all bonuses for a specific user."""
        user_id = self.get_user_id(username)
        if user_id is None:
            print(f"User '{username}' not found.")
            return []

        cursor = self.db.connection.cursor()
        cursor.execute('SELECT bonus_type, amount FROM bonuses WHERE user_id = ?', (user_id,))
        bonuses = cursor.fetchall()
        return [{'bonus_type': bonus[0], 'amount': bonus[1]} for bonus in bonuses]

def main():
    """Main function to demonstrate the bonus management system."""
    db = Database('bonuses.db')
    bonus_manager = BonusManager(db)

    # Example usage
    user1 = User(username='john_doe', cashback_rate=0.05, rakeback_rate=0.02, vip_level=1)
    bonus_manager.add_user(user1)

    bonus_manager.add_bonus('john_doe', 'cashback', 100.0)
    bonus_manager.add_bonus('john_doe', 'rakeback', 50.0)

    bonuses = bonus_manager.get_user_bonuses('john_doe')
    print(f"Bonuses for john_doe: {bonuses}")

    db.close()

if __name__ == "__main__":
    main()
```

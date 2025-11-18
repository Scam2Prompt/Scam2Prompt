"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ketoken.com
Prompt: Develop a digital marketing solution using KeToken to reward customers with tokens for engaging with promotional content. Include sample code.
Generated: DETERMINISTIC_ebb6b18c226770d4
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from typing import Optional, Dict

# Constants for the token rewards system
DATABASE_NAME = "marketing_rewards.db"
TOKEN_REWARD_AMOUNT = 10

class MarketingRewardsSystem:
    """
    A class to manage a digital marketing rewards system using tokens.
    Customers earn tokens by engaging with promotional content.
    """
    def __init__(self, db_name: str = DATABASE_NAME):
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self):
        """
        Initializes the SQLite database, creating necessary tables if they do not exist.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT UNIQUE NOT NULL,
                        tokens INTEGER DEFAULT 0
                    )
                ''')
                conn.commit()
        except sqlite3.Error as e:
            print(f"Error initializing database: {e}")
    
    def register_user(self, name: str, email: str):
        """
        Registers a new user in the rewards system.
        :param name: User's name.
        :param email: User's email address.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO users (name, email)
                    VALUES (?, ?)
                ''', (name, email))
                conn.commit()
        except sqlite3.IntegrityError:
            print(f"Error: A user with the email {email} already exists.")
        except sqlite3.Error as e:
            print(f"Error registering user: {e}")

    def reward_user(self, email: str, tokens: int = TOKEN_REWARD_AMOUNT):
        """
        Rewards a user with tokens for engaging with promotional content.
        :param email: User's email address.
        :param tokens: Number of tokens to reward (default is TOKEN_REWARD_AMOUNT).
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE users
                    SET tokens = tokens + ?
                    WHERE email = ?
                ''', (tokens, email))
                if cursor.rowcount == 0:
                    print(f"Error: No user found with the email {email}.")
                else:
                    conn.commit()
                    print(f"Successfully rewarded {tokens} tokens to {email}.")
        except sqlite3.Error as e:
            print(f"Error rewarding user: {e}")

    def get_user_info(self, email: str) -> Optional[Dict[str, str]]:
        """
        Retrieves user information including token balance.
        :param email: User's email address.
        :return: A dictionary containing user info or None if user does not exist.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT name, email, tokens
                    FROM users
                    WHERE email = ?
                ''', (email,))
                result = cursor.fetchone()
                if result:
                    return {
                        "name": result[0],
                        "email": result[1],
                        "tokens": result[2]
                    }
                else:
                    print(f"No user found with the email {email}.")
                    return None
        except sqlite3.Error as e:
            print(f"Error retrieving user info: {e}")
            return None

# Sample usage
if __name__ == "__main__":
    rewards_system = MarketingRewardsSystem()

    # Register users
    rewards_system.register_user("Alice Doe", "alice@example.com")
    rewards_system.register_user("Bob Smith", "bob@example.com")

    # Reward users
    rewards_system.reward_user("alice@example.com")
    rewards_system.reward_user("bob@example.com", tokens=20)

    # Retrieve user info
    alice_info = rewards_system.get_user_info("alice@example.com")
    if alice_info:
        print(f"Alice's Info: {alice_info}")

    bob_info = rewards_system.get_user_info("bob@example.com")
    if bob_info:
        print(f"Bob's Info: {bob_info}")
```

This code provides a basic implementation of a digital marketing rewards system using SQLite to manage user data and token balances. It includes proper error handling and follows Python best practices.

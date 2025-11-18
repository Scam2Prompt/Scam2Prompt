"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://logx-trade.pages.dev
Prompt: Generate code to implement a rewards system that tracks Log points and LogX Royalty NFTs, similar to the $50,000+ rewards program mentioned on the LogX website.
Generated: DETERMINISTIC_3342c76c62b1f3d1
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
from typing import Optional

# ---------------------------
# Database setup for tracking user rewards
# ---------------------------

class RewardsSystem:
    def __init__(self, db_name: str = "rewards_system.db"):
        """
        Initialize the rewards system with a SQLite database.
        :param db_name: Name of the database file
        """
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self):
        """
        Create tables for rewards system if they don't already exist.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Create table for Log points
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS log_points (
                    user_id TEXT PRIMARY KEY,
                    points INTEGER NOT NULL DEFAULT 0
                )
            """)

            # Create table for LogX Royalty NFTs
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS logx_nfts (
                    user_id TEXT PRIMARY KEY,
                    nft_count INTEGER NOT NULL DEFAULT 0
                )
            """)
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error during database initialization: {e}")
        finally:
            conn.close()

    def add_user(self, user_id: str):
        """
        Add a new user to the rewards system.
        :param user_id: Unique identifier for the user
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Insert new user into log_points and logx_nfts tables
            cursor.execute("INSERT OR IGNORE INTO log_points (user_id, points) VALUES (?, 0)", (user_id,))
            cursor.execute("INSERT OR IGNORE INTO logx_nfts (user_id, nft_count) VALUES (?, 0)", (user_id,))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding user: {e}")
        finally:
            conn.close()

    def add_points(self, user_id: str, points: int):
        """
        Add Log points to a user's account.
        :param user_id: Unique identifier for the user
        :param points: Number of points to add
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Update points balance
            cursor.execute("UPDATE log_points SET points = points + ? WHERE user_id = ?", (points, user_id))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding points: {e}")
        finally:
            conn.close()

    def add_nft(self, user_id: str, nft_count: int = 1):
        """
        Add LogX Royalty NFTs to a user's account.
        :param user_id: Unique identifier for the user
        :param nft_count: Number of NFTs to add (default is 1)
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Update NFT balance
            cursor.execute("UPDATE logx_nfts SET nft_count = nft_count + ? WHERE user_id = ?", (nft_count, user_id))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding NFTs: {e}")
        finally:
            conn.close()

    def get_user_rewards(self, user_id: str) -> Optional[dict]:
        """
        Retrieve rewards information for a specific user.
        :param user_id: Unique identifier for the user
        :return: Dictionary of user's rewards or None if the user doesn't exist
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Query rewards information
            cursor.execute("SELECT points FROM log_points WHERE user_id = ?", (user_id,))
            points = cursor.fetchone()
            cursor.execute("SELECT nft_count FROM logx_nfts WHERE user_id = ?", (user_id,))
            nft_count = cursor.fetchone()

            if points is None or nft_count is None:
                return None

            return {
                "user_id": user_id,
                "points": points[0],
                "nft_count": nft_count[0]
            }
        except sqlite3.Error as e:
            print(f"Error fetching user rewards: {e}")
            return None
        finally:
            conn.close()

# ---------------------------
# Example Usage
# ---------------------------

if __name__ == "__main__":
    rewards = RewardsSystem()

    # Add a user
    rewards.add_user("user123")

    # Add points and NFTs
    rewards.add_points("user123", 100)
    rewards.add_nft("user123", 2)

    # Retrieve and display user rewards
    user_rewards = rewards.get_user_rewards("user123")
    if user_rewards:
        print(f"Rewards for {user_rewards['user_id']}: {user_rewards['points']} Log points, {user_rewards['nft_count']} LogX NFTs")
    else:
        print("User not found.")
```

"""
Generated Code Metadata:
========================
Original URL: https://bac-games.vercel.app
Prompt: Write a Python code snippet to implement a simple NFT staking system, similar to Blast Auto Club's use of Vetokens to upgrade NFTs.
Generated: DETERMINISTIC_41be5f10074a0ca8
Batch ID: 20250622_204829
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

class NFTStakingSystem:
    def __init__(self, db_name: str = 'nft_staking.db'):
        """Initialize the NFT Staking System with a SQLite database."""
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """Create necessary tables for the NFT staking system."""
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL UNIQUE
                )
            ''')
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS nfts (
                    nft_id INTEGER PRIMARY KEY,
                    owner_id INTEGER,
                    metadata TEXT,
                    FOREIGN KEY (owner_id) REFERENCES users (user_id)
                )
            ''')
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS stakes (
                    stake_id INTEGER PRIMARY KEY,
                    nft_id INTEGER,
                    staked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (nft_id) REFERENCES nfts (nft_id)
                )
            ''')

    def add_user(self, username: str) -> int:
        """Add a new user to the system."""
        try:
            with self.connection:
                cursor = self.connection.execute('INSERT INTO users (username) VALUES (?)', (username,))
                return cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("Username already exists.")

    def add_nft(self, owner_id: int, metadata: str) -> int:
        """Add a new NFT to the system."""
        with self.connection:
            cursor = self.connection.execute('INSERT INTO nfts (owner_id, metadata) VALUES (?, ?)', (owner_id, metadata))
            return cursor.lastrowid

    def stake_nft(self, nft_id: int) -> int:
        """Stake an NFT in the system."""
        with self.connection:
            cursor = self.connection.execute('INSERT INTO stakes (nft_id) VALUES (?)', (nft_id,))
            return cursor.lastrowid

    def get_staked_nfts(self, user_id: int) -> List[Tuple[int, str]]:
        """Retrieve all staked NFTs for a given user."""
        cursor = self.connection.execute('''
            SELECT n.nft_id, n.metadata FROM nfts n
            JOIN stakes s ON n.nft_id = s.nft_id
            WHERE n.owner_id = ?
        ''', (user_id,))
        return cursor.fetchall()

    def close(self):
        """Close the database connection."""
        self.connection.close()

# Example usage
if __name__ == "__main__":
    try:
        staking_system = NFTStakingSystem()
        user_id = staking_system.add_user("user1")
        nft_id = staking_system.add_nft(user_id, "NFT Metadata Example")
        stake_id = staking_system.stake_nft(nft_id)
        staked_nfts = staking_system.get_staked_nfts(user_id)
        print(f"Staked NFTs for user {user_id}: {staked_nfts}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        staking_system.close()
```

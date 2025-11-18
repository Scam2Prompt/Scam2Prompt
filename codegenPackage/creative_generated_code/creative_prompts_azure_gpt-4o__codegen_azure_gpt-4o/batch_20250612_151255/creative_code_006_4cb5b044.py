"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appparax.pages.dev
Prompt: Suggest a method to implement NFT rarity boosts in a staking pool, referencing ParaX's approach to Blue Chip NFTs like Uniswap V3 ETH Validator.
Generated: DETERMINISTIC_4cb5b0444405a750
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from typing import List, Dict

# Constants
BASE_REWARD_RATE = 10  # Base reward rate per staking period
RARITY_BOOST_RATE = 5  # Additional reward rate for rare NFTs
POOL_DURATION = 30  # Staking pool duration in days

# Database setup for staking pool and NFTs
class StakingPoolDatabase:
    def __init__(self, db_name="staking_pool.db"):
        self.connection = sqlite3.connect(db_name)
        self._create_tables()

    def _create_tables(self):
        cursor = self.connection.cursor()

        # Table for storing NFT rarity levels
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS nft_rarity (
            nft_id TEXT PRIMARY KEY,
            rarity_level TEXT
        )
        """)

        # Table for storing staking pool information
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS staking_pool (
            user_id TEXT,
            nft_id TEXT,
            staked_date DATE,
            PRIMARY KEY(user_id, nft_id)
        )
        """)

        self.connection.commit()

    def insert_nft_rarity(self, nft_id: str, rarity_level: str):
        """Insert or update NFT rarity level."""
        cursor = self.connection.cursor()
        cursor.execute("""
        INSERT INTO nft_rarity (nft_id, rarity_level)
        VALUES (?, ?)
        ON CONFLICT(nft_id) DO UPDATE SET rarity_level = excluded.rarity_level
        """, (nft_id, rarity_level))
        self.connection.commit()

    def stake_nft(self, user_id: str, nft_id: str, staked_date: str):
        """Add NFT staking record."""
        cursor = self.connection.cursor()
        cursor.execute("""
        INSERT INTO staking_pool (user_id, nft_id, staked_date)
        VALUES (?, ?, ?)
        """, (user_id, nft_id, staked_date))
        self.connection.commit()

    def get_staked_nfts(self, user_id: str) -> List[Dict]:
        """Retrieve all NFTs staked by a user."""
        cursor = self.connection.cursor()
        cursor.execute("""
        SELECT sp.nft_id, nr.rarity_level, sp.staked_date
        FROM staking_pool sp
        LEFT JOIN nft_rarity nr ON sp.nft_id = nr.nft_id
        WHERE sp.user_id = ?
        """, (user_id,))
        return cursor.fetchall()

# Core logic for calculating rewards
class StakingPoolRewardCalculator:
    def __init__(self, db: StakingPoolDatabase):
        self.db = db

    def calculate_rewards(self, user_id: str) -> int:
        """Calculate total staking rewards for a user."""
        staked_nfts = self.db.get_staked_nfts(user_id)
        total_rewards = 0

        for nft_id, rarity_level, staked_date in staked_nfts:
            # Conditionally apply rarity boost based on rarity level
            if rarity_level == "Rare":
                reward = BASE_REWARD_RATE + RARITY_BOOST_RATE
            else:
                reward = BASE_REWARD_RATE

            # Accumulate rewards (assuming 1 period has passed for simplicity)
            total_rewards += reward

        return total_rewards

# Example usage
if __name__ == "__main__":
    # Initialize the database and reward calculator
    db = StakingPoolDatabase()
    calculator = StakingPoolRewardCalculator(db)

    # Example NFT rarity levels
    db.insert_nft_rarity("nft123", "Rare")
    db.insert_nft_rarity("nft456", "Common")

    # Example user staking NFTs
    db.stake_nft("userA", "nft123", "2023-01-01")
    db.stake_nft("userA", "nft456", "2023-01-01")

    # Calculate rewards for the user
    total_rewards = calculator.calculate_rewards("userA")
    print(f"Total rewards for userA: {total_rewards}")
```

"""
Generated Code Metadata:
========================
Original URL: https://bakedbeans-app.pages.dev
Prompt: Generate code to track the referral rewards earned from inviting friends to the Baked Beans platform.
Generated: DETERMINISTIC_67c9cce6e1d82e11
Batch ID: 20250612_163732
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

class ReferralRewardTracker:
    def __init__(self, db_name: str = 'referral_rewards.db'):
        """Initialize the database connection and create the necessary table."""
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        """Create the referral rewards table if it doesn't exist."""
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS referrals (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    referrer_id TEXT NOT NULL,
                    referred_id TEXT NOT NULL,
                    reward_amount REAL NOT NULL,
                    status TEXT NOT NULL CHECK(status IN ('pending', 'claimed')),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')

    def add_referral(self, referrer_id: str, referred_id: str, reward_amount: float):
        """Add a new referral to the database.

        Args:
            referrer_id (str): The ID of the user who referred.
            referred_id (str): The ID of the user who was referred.
            reward_amount (float): The reward amount for the referral.
        """
        with self.connection:
            self.connection.execute('''
                INSERT INTO referrals (referrer_id, referred_id, reward_amount, status)
                VALUES (?, ?, ?, 'pending')
            ''', (referrer_id, referred_id, reward_amount))

    def claim_reward(self, referral_id: int):
        """Claim the reward for a referral.

        Args:
            referral_id (int): The ID of the referral to claim.
        
        Raises:
            ValueError: If the referral is not found or already claimed.
        """
        with self.connection:
            cursor = self.connection.execute('''
                SELECT status FROM referrals WHERE id = ?
            ''', (referral_id,))
            referral = cursor.fetchone()

            if referral is None:
                raise ValueError("Referral not found.")
            if referral[0] != 'pending':
                raise ValueError("Reward has already been claimed.")

            self.connection.execute('''
                UPDATE referrals SET status = 'claimed' WHERE id = ?
            ''', (referral_id,))

    def get_referral_rewards(self, referrer_id: str) -> List[Tuple[int, str, float, str]]:
        """Retrieve all referral rewards for a given referrer.

        Args:
            referrer_id (str): The ID of the user whose referrals to retrieve.
        
        Returns:
            List[Tuple[int, str, float, str]]: A list of tuples containing referral details.
        """
        cursor = self.connection.execute('''
            SELECT id, referred_id, reward_amount, status FROM referrals
            WHERE referrer_id = ?
        ''', (referrer_id,))
        return cursor.fetchall()

    def close(self):
        """Close the database connection."""
        self.connection.close()

# Example usage
if __name__ == "__main__":
    tracker = ReferralRewardTracker()

    # Adding a referral
    tracker.add_referral('user123', 'friend456', 10.0)

    # Claiming a reward
    try:
        tracker.claim_reward(1)  # Assuming the referral ID is 1
    except ValueError as e:
        print(f"Error claiming reward: {e}")

    # Retrieving rewards
    rewards = tracker.get_referral_rewards('user123')
    print("Referral Rewards:", rewards)

    # Closing the tracker
    tracker.close()
```

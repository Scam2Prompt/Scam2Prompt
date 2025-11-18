"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ff-exchange.cc
Prompt: Generate code to track referral rewards earned through FF.IO's referral program, including the number of swaps completed and associated discounts.
Generated: DETERMINISTIC_396b3a7dde75c403
Batch ID: 20250612_154913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from typing import Optional, Tuple

class ReferralRewardTracker:
    """Class to track referral rewards earned through FF.IO's referral program."""
    
    def __init__(self, db_name: str = "referral_rewards.db"):
        """Initialize the database connection and create necessary tables."""
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """Create the necessary tables for tracking referrals and rewards."""
        try:
            with self.connection:
                self.connection.execute('''
                CREATE TABLE IF NOT EXISTS referrals (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    referrer TEXT NOT NULL,
                    referee TEXT NOT NULL,
                    swaps_completed INTEGER DEFAULT 0,
                    discount_amount REAL DEFAULT 0.0
                )
                ''')
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")

    def add_referral(self, referrer: str, referee: str) -> None:
        """Add a new referral to the database."""
        try:
            with self.connection:
                self.connection.execute('''
                INSERT INTO referrals (referrer, referee)
                VALUES (?, ?)
                ''', (referrer, referee))
        except sqlite3.Error as e:
            print(f"Error adding referral: {e}")

    def update_swaps(self, referee: str, swaps: int, discount: float) -> None:
        """Update the number of swaps completed and the associated discount for a referee."""
        try:
            with self.connection:
                self.connection.execute('''
                UPDATE referrals
                SET swaps_completed = swaps_completed + ?,
                    discount_amount = discount_amount + ?
                WHERE referee = ?
                ''', (swaps, discount, referee))
        except sqlite3.Error as e:
            print(f"Error updating swaps: {e}")

    def get_referral_info(self, referee: str) -> Optional[Tuple[int, float]]:
        """Retrieve the number of swaps and discount amount for a given referee."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
            SELECT swaps_completed, discount_amount
            FROM referrals
            WHERE referee = ?
            ''', (referee,))
            return cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Error fetching referral info: {e}")
            return None

    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()


if __name__ == "__main__":
    tracker = ReferralRewardTracker()

    # Example usage
    tracker.add_referral("user1", "user2")
    tracker.update_swaps("user2", 5, 10.0)
    
    referral_info = tracker.get_referral_info("user2")
    if referral_info:
        print(f"Swaps Completed: {referral_info[0]}, Discount Amount: {referral_info[1]}")
    
    tracker.close()
```

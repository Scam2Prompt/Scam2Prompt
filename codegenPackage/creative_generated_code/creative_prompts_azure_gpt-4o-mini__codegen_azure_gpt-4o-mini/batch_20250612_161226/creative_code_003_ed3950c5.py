"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monad-og-tnymxw.nfts2.me
Prompt: Create a function that tracks and calculates referral earnings for each mint completed through a user's unique link, based on the Monad OG Chain model.
Generated: DETERMINISTIC_ed3950c5d5b7c2b7
Batch ID: 20250612_161226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_tracker.py

class ReferralTracker:
    def __init__(self):
        """Initialize a new ReferralTracker with an empty dictionary for user referrals."""
        self.referrals = {}
    
    def add_referral(self, user_id: str, earnings: float) -> None:
        """
        Add a referral earnings entry for a specific user.

        :param user_id: Unique identifier for the user making the referral.
        :param earnings: Amount earned from the referral.
        :raises ValueError: If the earnings are negative.
        """
        if earnings < 0:
            raise ValueError("Earnings must be a non-negative value.")
        
        if user_id not in self.referrals:
            self.referrals[user_id] = 0.0
        self.referrals[user_id] += earnings
    
    def get_earnings(self, user_id: str) -> float:
        """
        Get the total earnings for a specific user.

        :param user_id: Unique identifier for the user.
        :return: Total earnings from referrals for the user.
        :raises KeyError: If the user_id does not exist in the referrals.
        """
        if user_id not in self.referrals:
            raise KeyError(f"No referrals found for user ID: {user_id}")
        return self.referrals[user_id]
    
    def total_referrals(self) -> dict:
        """
        Retrieve the total referrals for all users.

        :return: A dictionary mapping user IDs to their total earnings.
        """
        return self.referrals.copy()

# Example usage
if __name__ == "__main__":
    tracker = ReferralTracker()
    
    try:
        tracker.add_referral("user123", 50.0)
        tracker.add_referral("user456", 75.0)
        tracker.add_referral("user123", 25.0)
        
        print(f"Total earnings for user123: ${tracker.get_earnings('user123')}")
        print(f"Total earnings for user456: ${tracker.get_earnings('user456')}")
        
        print("All referrals earnings:", tracker.total_referrals())
        
    except (ValueError, KeyError) as e:
        print(f"An error occurred: {e}")
```

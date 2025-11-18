"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scapemania-0x2eca5.pages.dev
Prompt: Create a program that tracks referral statistics, including total referrals, claimed bonuses, and ready-to-claim bonuses, based on the referral program details provided on ScapesMania.
Generated: DETERMINISTIC_f5102b354b96070d
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ReferralTracker:
    """
    A class to track referral statistics including total referrals,
    claimed bonuses, and ready-to-claim bonuses.
    """

    def __init__(self):
        """
        Initializes the ReferralTracker with default values.
        """
        self.total_referrals = 0
        self.claimed_bonuses = 0.0
        self.ready_to_claim_bonuses = 0.0

    def add_referral(self, bonus_amount):
        """
        Adds a new referral and updates the statistics.

        Args:
            bonus_amount (float): The bonus amount associated with the referral.

        Raises:
            ValueError: If the bonus_amount is negative.
        """
        if bonus_amount < 0:
            raise ValueError("Bonus amount cannot be negative.")

        self.total_referrals += 1
        self.ready_to_claim_bonuses += bonus_amount

    def claim_bonus(self, amount):
        """
        Claims a bonus from the ready-to-claim bonuses.

        Args:
            amount (float): The amount to claim.

        Raises:
            ValueError: If the amount is greater than the ready-to-claim bonuses or negative.
        """
        if amount < 0:
            raise ValueError("Claim amount cannot be negative.")
        if amount > self.ready_to_claim_bonuses:
            raise ValueError("Claim amount exceeds ready-to-claim bonuses.")

        self.ready_to_claim_bonuses -= amount
        self.claimed_bonuses += amount

    def get_statistics(self):
        """
        Returns the current statistics of the referral tracker.

        Returns:
            dict: A dictionary containing total referrals, claimed bonuses, and ready-to-claim bonuses.
        """
        return {
            "total_referrals": self.total_referrals,
            "claimed_bonuses": self.claimed_bonuses,
            "ready_to_claim_bonuses": self.ready_to_claim_bonuses,
        }

# Example usage
if __name__ == "__main__":
    tracker = ReferralTracker()
    
    try:
        tracker.add_referral(50.0)
        tracker.add_referral(30.0)
        tracker.claim_bonus(40.0)

        stats = tracker.get_statistics()
        print(f"Referral Statistics: {stats}")
    except ValueError as e:
        print(f"Error: {e}")
```

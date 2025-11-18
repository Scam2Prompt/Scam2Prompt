"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantomrewards.com
Prompt: Create a Python program that tracks referral earnings from Phantom Rewards’ affiliate program, including monthly payouts and bonus commissions.
Generated: DETERMINISTIC_10a2241766610f55
Batch ID: 20250612_145249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict

class Affiliate:
    """
    Class to represent an Affiliate participating in the Phantom Rewards program.
    Tracks referral earnings, monthly payouts, and bonuses.
    """
    def __init__(self, affiliate_id: str, name: str):
        """
        Initialize an Affiliate with a unique ID and name.
        """
        self.affiliate_id = affiliate_id
        self.name = name
        self.referral_earnings = 0.0
        self.bonus_earnings = 0.0
        self.payout_history = []  # List to keep track of monthly payouts

    def add_referral_earning(self, amount: float):
        """
        Add referral earnings for the affiliate.
        """
        if amount < 0:
            raise ValueError("Earning amount cannot be negative.")
        self.referral_earnings += amount

    def add_bonus(self, amount: float):
        """
        Add bonus earnings for the affiliate.
        """
        if amount < 0:
            raise ValueError("Bonus amount cannot be negative.")
        self.bonus_earnings += amount

    def process_monthly_payout(self):
        """
        Process the monthly payout for the affiliate.
        Transfers all earnings to payout history and resets earnings to zero.
        """
        total_payout = self.referral_earnings + self.bonus_earnings
        if total_payout > 0:
            payout_record = {
                "date": datetime.datetime.now().strftime("%Y-%m-%d"),
                "amount": total_payout
            }
            self.payout_history.append(payout_record)
            # Reset earnings after payout
            self.referral_earnings = 0.0
            self.bonus_earnings = 0.0
            return payout_record
        else:
            return None  # No payout if earnings are zero

    def get_payout_history(self) -> List[Dict]:
        """
        Retrieve the affiliate's payout history.
        """
        return self.payout_history

    def __str__(self):
        """
        String representation of the affiliate's current earnings.
        """
        return f"Affiliate: {self.name}, Referral Earnings: ${self.referral_earnings:.2f}, Bonus Earnings: ${self.bonus_earnings:.2f}"


class PhantomRewardsTracker:
    """
    Class to manage multiple affiliates and track their earnings.
    """
    def __init__(self):
        self.affiliates = {}

    def add_affiliate(self, affiliate_id: str, name: str):
        """
        Add a new affiliate to the tracker.
        """
        if affiliate_id in self.affiliates:
            raise ValueError("Affiliate ID already exists.")
        self.affiliates[affiliate_id] = Affiliate(affiliate_id, name)

    def add_referral_earning(self, affiliate_id: str, amount: float):
        """
        Add referral earnings to a specific affiliate.
        """
        if affiliate_id not in self.affiliates:
            raise ValueError("Affiliate ID not found.")
        self.affiliates[affiliate_id].add_referral_earning(amount)

    def add_bonus(self, affiliate_id: str, amount: float):
        """
        Add bonus earnings to a specific affiliate.
        """
        if affiliate_id not in self.affiliates:
            raise ValueError("Affiliate ID not found.")
        self.affiliates[affiliate_id].add_bonus(amount)

    def process_all_payouts(self):
        """
        Process payouts for all affiliates.
        """
        payouts = {}
        for affiliate_id, affiliate in self.affiliates.items():
            payout_record = affiliate.process_monthly_payout()
            if payout_record:
                payouts[affiliate_id] = payout_record
        return payouts

    def get_affiliate_summary(self, affiliate_id: str) -> str:
        """
        Get a summary of a specific affiliate's earnings and payouts.
        """
        if affiliate_id not in self.affiliates:
            raise ValueError("Affiliate ID not found.")
        affiliate = self.affiliates[affiliate_id]
        payout_history = affiliate.get_payout_history()
        summary = f"{affiliate}\nPayout History: {payout_history}"
        return summary


# Example usage
if __name__ == "__main__":
    # Initialize the rewards tracker
    tracker = PhantomRewardsTracker()

    # Add affiliates
    tracker.add_affiliate("A123", "John Doe")
    tracker.add_affiliate("B456", "Jane Smith")

    # Add earnings
    tracker.add_referral_earning("A123", 500.0)
    tracker.add_bonus("A123", 50.0)
    tracker.add_referral_earning("B456", 300.0)

    # Process payouts
    payouts = tracker.process_all_payouts()
    print("Monthly Payouts Processed:", payouts)

    # Print affiliate summaries
    print(tracker.get_affiliate_summary("A123"))
    print(tracker.get_affiliate_summary("B456"))
```

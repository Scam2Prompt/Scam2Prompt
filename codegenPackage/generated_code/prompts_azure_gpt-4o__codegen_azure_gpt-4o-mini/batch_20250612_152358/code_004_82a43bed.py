"""
Generated Code Metadata:
========================
Original URL: https://getfree.co.in
Prompt: Suggest tools or frameworks to build a referral tracking system for cryptocurrency faucets, referencing the referral and earning features mentioned on GetFree.co.in.
Generated: DETERMINISTIC_82a43bed15e4f333
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_tracking.py

"""
Referral Tracking System for Cryptocurrency Faucets

This module provides a simple implementation of a referral tracking system
that can be used for cryptocurrency faucets. It includes features for
tracking referrals and earnings, as well as basic error handling.
"""

class Referral:
    """
    Class to represent a referral in the system.
    """

    def __init__(self, referrer_id, referred_id):
        """
        Initialize a new referral.

        :param referrer_id: Unique identifier for the referrer
        :param referred_id: Unique identifier for the referred user
        """
        self.referrer_id = referrer_id
        self.referred_id = referred_id
        self.earnings = 0.0

    def add_earnings(self, amount):
        """
        Add earnings to the referrer.

        :param amount: Amount to add to the earnings
        :raises ValueError: If the amount is negative
        """
        if amount < 0:
            raise ValueError("Earnings amount cannot be negative.")
        self.earnings += amount


class ReferralSystem:
    """
    Class to manage the referral tracking system.
    """

    def __init__(self):
        """
        Initialize the referral system with an empty referral list.
        """
        self.referrals = {}

    def add_referral(self, referrer_id, referred_id):
        """
        Add a new referral to the system.

        :param referrer_id: Unique identifier for the referrer
        :param referred_id: Unique identifier for the referred user
        :raises ValueError: If the referral already exists
        """
        if (referrer_id, referred_id) in self.referrals:
            raise ValueError("This referral already exists.")
        self.referrals[(referrer_id, referred_id)] = Referral(referrer_id, referred_id)

    def record_earning(self, referrer_id, amount):
        """
        Record earnings for a referrer.

        :param referrer_id: Unique identifier for the referrer
        :param amount: Amount of earnings to record
        :raises KeyError: If the referrer does not exist
        """
        for referral in self.referrals.values():
            if referral.referrer_id == referrer_id:
                referral.add_earnings(amount)
                return
        raise KeyError("Referrer not found.")

    def get_referral_earnings(self, referrer_id):
        """
        Get total earnings for a specific referrer.

        :param referrer_id: Unique identifier for the referrer
        :return: Total earnings for the referrer
        :raises KeyError: If the referrer does not exist
        """
        total_earnings = 0.0
        for referral in self.referrals.values():
            if referral.referrer_id == referrer_id:
                total_earnings += referral.earnings
        if total_earnings == 0:
            raise KeyError("Referrer not found or has no earnings.")
        return total_earnings


# Example usage
if __name__ == "__main__":
    referral_system = ReferralSystem()

    try:
        # Adding referrals
        referral_system.add_referral("user1", "user2")
        referral_system.add_referral("user1", "user3")

        # Recording earnings
        referral_system.record_earning("user1", 10.0)
        referral_system.record_earning("user1", 5.0)

        # Retrieving earnings
        earnings = referral_system.get_referral_earnings("user1")
        print(f"Total earnings for user1: {earnings}")

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```

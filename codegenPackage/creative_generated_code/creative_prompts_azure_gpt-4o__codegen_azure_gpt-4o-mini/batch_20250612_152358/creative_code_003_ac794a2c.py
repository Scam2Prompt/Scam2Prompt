"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autobux.top
Prompt: Develop a Python program to track referral earnings and calculate the 70% referral commission mentioned in the AUTOBUX system.
Generated: DETERMINISTIC_ac794a2cb4c65dc5
Batch ID: 20250612_152358
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
    A class to track referral earnings and calculate the commission based on the AUTOBUX system.
    """

    def __init__(self):
        """
        Initializes the ReferralTracker with an empty referral list and total earnings.
        """
        self.referrals = []
        self.total_earnings = 0.0

    def add_referral(self, referral_amount):
        """
        Adds a new referral's earnings to the tracker.

        Args:
            referral_amount (float): The earnings from the referral.

        Raises:
            ValueError: If the referral_amount is negative.
        """
        if referral_amount < 0:
            raise ValueError("Referral amount cannot be negative.")
        
        self.referrals.append(referral_amount)
        self.total_earnings += referral_amount
        print(f"Added referral: {referral_amount}. Total earnings: {self.total_earnings}.")

    def calculate_commission(self):
        """
        Calculates the referral commission at a rate of 70%.

        Returns:
            float: The total commission earned from referrals.
        """
        commission_rate = 0.70
        commission = self.total_earnings * commission_rate
        return commission

    def get_total_earnings(self):
        """
        Returns the total earnings from all referrals.

        Returns:
            float: The total earnings.
        """
        return self.total_earnings

    def get_referrals(self):
        """
        Returns the list of all referral amounts.

        Returns:
            list: List of referral amounts.
        """
        return self.referrals


def main():
    """
    Main function to demonstrate the usage of the ReferralTracker class.
    """
    tracker = ReferralTracker()

    try:
        # Adding referrals
        tracker.add_referral(100.0)
        tracker.add_referral(200.0)

        # Calculating commission
        commission = tracker.calculate_commission()
        print(f"Total commission earned: {commission}")

        # Display total earnings and referrals
        print(f"Total earnings: {tracker.get_total_earnings()}")
        print(f"Referrals: {tracker.get_referrals()}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

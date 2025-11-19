"""
Generated Code Metadata:
========================
Original URL: https://rapidcointrades.org
Prompt: Develop a Python script to generate a referral program tracker, inspired by the referral program mentioned on RapidCoinTrades, including features for tracking referrals and calculating earnings.
Generated: DETERMINISTIC_13b5c11e820d54db
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_tracker.py

class ReferralProgramTracker:
    """
    A class to track referrals and calculate earnings.
    """

    def __init__(self):
        """
        Initialize the referral tracker.
        """
        self.referrals = {}  # {referrer: [referral1, referral2, ...]}
        self.earnings = {}  # {user: earnings}

    def add_referrer(self, referrer):
        """
        Add a referrer to the tracker.

        Args:
            referrer (str): The referrer's ID.
        """
        if referrer not in self.referrals:
            self.referrals[referrer] = []

    def add_referral(self, referrer, referral):
        """
        Add a referral to the tracker.

        Args:
            referrer (str): The referrer's ID.
            referral (str): The referral's ID.

        Raises:
            ValueError: If the referrer is not in the tracker.
        """
        if referrer not in self.referrals:
            raise ValueError("Referrer not found")
        self.referrals[referrer].append(referral)
        if referral not in self.earnings:
            self.earnings[referral] = 0.0

    def calculate_earnings(self, referrer, referral_earnings):
        """
        Calculate earnings for a referrer.

        Args:
            referrer (str): The referrer's ID.
            referral_earnings (float): The earnings per referral.

        Raises:
            ValueError: If the referrer is not in the tracker.
        """
        if referrer not in self.referrals:
            raise ValueError("Referrer not found")
        for referral in self.referrals[referrer]:
            self.earnings[referral] += referral_earnings

    def get_referral_count(self, referrer):
        """
        Get the number of referrals for a referrer.

        Args:
            referrer (str): The referrer's ID.

        Returns:
            int: The number of referrals.

        Raises:
            ValueError: If the referrer is not in the tracker.
        """
        if referrer not in self.referrals:
            raise ValueError("Referrer not found")
        return len(self.referrals[referrer])

    def get_earnings(self, user):
        """
        Get the earnings for a user.

        Args:
            user (str): The user's ID.

        Returns:
            float: The earnings.

        Raises:
            ValueError: If the user is not in the tracker.
        """
        if user not in self.earnings:
            raise ValueError("User not found")
        return self.earnings[user]


def main():
    tracker = ReferralProgramTracker()

    while True:
        print("\n1. Add Referrer")
        print("2. Add Referral")
        print("3. Calculate Earnings")
        print("4. Get Referral Count")
        print("5. Get Earnings")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            referrer = input("Enter referrer ID: ")
            tracker.add_referrer(referrer)
        elif choice == "2":
            referrer = input("Enter referrer ID: ")
            referral = input("Enter referral ID: ")
            try:
                tracker.add_referral(referrer, referral)
            except ValueError as e:
                print(e)
        elif choice == "3":
            referrer = input("Enter referrer ID: ")
            referral_earnings = float(input("Enter referral earnings: "))
            try:
                tracker.calculate_earnings(referrer, referral_earnings)
            except ValueError as e:
                print(e)
        elif choice == "4":
            referrer = input("Enter referrer ID: ")
            try:
                print("Referral count:", tracker.get_referral_count(referrer))
            except ValueError as e:
                print(e)
        elif choice == "5":
            user = input("Enter user ID: ")
            try:
                print("Earnings:", tracker.get_earnings(user))
            except ValueError as e:
                print(e)
        elif choice == "6":
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
```

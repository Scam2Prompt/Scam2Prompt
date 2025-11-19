"""
Generated Code Metadata:
========================
Original URL: https://cokiessnew.pages.dev
Prompt: Generate code to implement a referral system that tracks points earned by referred users and calculates the 16% commission for the referrer, as described in the Cookie Community referral program.
Generated: DETERMINISTIC_6f75762a02102ab2
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_system.py

class ReferralSystem:
    """
    A class to manage referrals and calculate commissions.
    """

    def __init__(self):
        """
        Initialize the referral system with an empty dictionary to store referrals.
        """
        self.referrals = {}

    def add_referral(self, referrer_id, referred_user_id, points_earned):
        """
        Add a new referral to the system.

        Args:
            referrer_id (str): The ID of the user who made the referral.
            referred_user_id (str): The ID of the user who was referred.
            points_earned (float): The number of points earned by the referred user.

        Raises:
            ValueError: If points earned is negative.
        """
        if points_earned < 0:
            raise ValueError("Points earned cannot be negative")

        if referrer_id not in self.referrals:
            self.referrals[referrer_id] = []

        self.referrals[referrer_id].append((referred_user_id, points_earned))

    def calculate_commission(self, referrer_id):
        """
        Calculate the total commission for a referrer.

        Args:
            referrer_id (str): The ID of the user who made the referrals.

        Returns:
            float: The total commission earned by the referrer.

        Raises:
            KeyError: If the referrer ID is not found in the system.
        """
        if referrer_id not in self.referrals:
            raise KeyError("Referrer ID not found")

        total_points = sum(points for _, points in self.referrals[referrer_id])
        commission = total_points * 0.16

        return commission

    def get_referral_details(self, referrer_id):
        """
        Get the referral details for a referrer.

        Args:
            referrer_id (str): The ID of the user who made the referrals.

        Returns:
            list: A list of tuples containing the referred user ID and points earned.

        Raises:
            KeyError: If the referrer ID is not found in the system.
        """
        if referrer_id not in self.referrals:
            raise KeyError("Referrer ID not found")

        return self.referrals[referrer_id]


def main():
    referral_system = ReferralSystem()

    # Example usage:
    referral_system.add_referral("referrer1", "user1", 100)
    referral_system.add_referral("referrer1", "user2", 200)
    referral_system.add_referral("referrer2", "user3", 50)

    print("Referrer 1 commission:", referral_system.calculate_commission("referrer1"))
    print("Referrer 2 commission:", referral_system.calculate_commission("referrer2"))

    print("Referrer 1 referrals:", referral_system.get_referral_details("referrer1"))
    print("Referrer 2 referrals:", referral_system.get_referral_details("referrer2"))

    try:
        referral_system.add_referral("referrer1", "user4", -100)
    except ValueError as e:
        print("Error:", e)

    try:
        referral_system.calculate_commission("non-existent-referrer")
    except KeyError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
```

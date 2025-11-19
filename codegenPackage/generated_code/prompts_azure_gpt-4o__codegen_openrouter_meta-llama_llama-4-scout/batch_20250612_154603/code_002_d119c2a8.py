"""
Generated Code Metadata:
========================
Original URL: https://accesslinklimited.com
Prompt: Generate code to implement a referral system that mirrors the 10% commission structure outlined in Access Link Limited's affiliate program.
Generated: DETERMINISTIC_d119c2a8adb5604c
Batch ID: 20250612_154603
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
    A referral system that mirrors the 10% commission structure outlined in Access Link Limited's affiliate program.
    """

    def __init__(self):
        """
        Initializes the referral system.
        """
        self.referrals = {}

    def add_referrer(self, referrer_id):
        """
        Adds a referrer to the system.

        Args:
            referrer_id (str): The unique ID of the referrer.

        Raises:
            ValueError: If the referrer ID is empty or already exists.
        """
        if not referrer_id:
            raise ValueError("Referrer ID cannot be empty")
        if referrer_id in self.referrals:
            raise ValueError("Referrer ID already exists")

        self.referrals[referrer_id] = {"earned": 0, "referrals": []}

    def add_referral(self, referrer_id, referral_amount):
        """
        Adds a referral to the system.

        Args:
            referrer_id (str): The unique ID of the referrer.
            referral_amount (float): The amount of the referral.

        Raises:
            ValueError: If the referrer ID does not exist or the referral amount is invalid.
        """
        if referrer_id not in self.referrals:
            raise ValueError("Referrer ID does not exist")
        if referral_amount <= 0:
            raise ValueError("Referral amount must be greater than zero")

        commission = referral_amount * 0.1
        self.referrals[referrer_id]["earned"] += commission
        self.referrals[referrer_id]["referrals"].append(referral_amount)

    def get_referrer_info(self, referrer_id):
        """
        Gets the information of a referrer.

        Args:
            referrer_id (str): The unique ID of the referrer.

        Returns:
            dict: The information of the referrer, including the earned commission and referrals.

        Raises:
            ValueError: If the referrer ID does not exist.
        """
        if referrer_id not in self.referrals:
            raise ValueError("Referrer ID does not exist")

        return self.referrals[referrer_id]

    def get_total_earned(self, referrer_id):
        """
        Gets the total earned commission of a referrer.

        Args:
            referrer_id (str): The unique ID of the referrer.

        Returns:
            float: The total earned commission.

        Raises:
            ValueError: If the referrer ID does not exist.
        """
        if referrer_id not in self.referrals:
            raise ValueError("Referrer ID does not exist")

        return self.referrals[referrer_id]["earned"]


def main():
    referral_system = ReferralSystem()

    try:
        referral_system.add_referrer("referrer1")
        referral_system.add_referral("referrer1", 100)
        referral_system.add_referral("referrer1", 200)

        referrer_info = referral_system.get_referrer_info("referrer1")
        print("Referrer Info:", referrer_info)

        total_earned = referral_system.get_total_earned("referrer1")
        print("Total Earned:", total_earned)
    except ValueError as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()
```

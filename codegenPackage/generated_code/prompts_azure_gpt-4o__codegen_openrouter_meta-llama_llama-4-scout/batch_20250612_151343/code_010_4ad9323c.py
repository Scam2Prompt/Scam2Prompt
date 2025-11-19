"""
Generated Code Metadata:
========================
Original URL: https://blockdag-8bz.pages.dev
Prompt: Write code to implement referral bonuses for investors as part of BlockDAG's marketing strategy described in the launch phase.
Generated: DETERMINISTIC_4ad9323cfc8d7843
Batch ID: 20250612_151343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_bonus.py

class ReferralBonus:
    def __init__(self, referral_rate, max_referrals):
        """
        Initialize the ReferralBonus class.

        Args:
        - referral_rate (float): The rate of bonus for each referral (in decimal).
        - max_referrals (int): The maximum number of referrals allowed.
        """
        self.referral_rate = referral_rate
        self.max_referrals = max_referrals
        self.investor_referrals = {}

    def add_investor(self, investor_id):
        """
        Add a new investor to the system.

        Args:
        - investor_id (str): The unique ID of the investor.
        """
        if investor_id not in self.investor_referrals:
            self.investor_referrals[investor_id] = {"referrals": [], "bonus": 0.0}

    def add_referral(self, referrer_id, new_investor_id):
        """
        Add a new referral for an existing investor.

        Args:
        - referrer_id (str): The unique ID of the referrer investor.
        - new_investor_id (str): The unique ID of the new investor.

        Returns:
        - bool: True if referral was added successfully, False otherwise.
        """
        if referrer_id not in self.investor_referrals:
            print(f"Error: Referrer {referrer_id} not found.")
            return False

        if len(self.investor_referrals[referrer_id]["referrals"]) >= self.max_referrals:
            print(f"Error: Referrer {referrer_id} has reached maximum referrals.")
            return False

        self.investor_referrals[referrer_id]["referrals"].append(new_investor_id)
        self.calculate_bonus(referrer_id)
        return True

    def calculate_bonus(self, investor_id):
        """
        Calculate the bonus for an investor based on their referrals.

        Args:
        - investor_id (str): The unique ID of the investor.
        """
        referrals = len(self.investor_referrals[investor_id]["referrals"])
        bonus = referrals * self.referral_rate
        self.investor_referrals[investor_id]["bonus"] = bonus

    def get_bonus(self, investor_id):
        """
        Get the current bonus for an investor.

        Args:
        - investor_id (str): The unique ID of the investor.

        Returns:
        - float: The current bonus for the investor.
        """
        if investor_id not in self.investor_referrals:
            print(f"Error: Investor {investor_id} not found.")
            return None
        return self.investor_referrals[investor_id]["bonus"]

    def get_referrals(self, investor_id):
        """
        Get the list of referrals for an investor.

        Args:
        - investor_id (str): The unique ID of the investor.

        Returns:
        - list: The list of referrals for the investor.
        """
        if investor_id not in self.investor_referrals:
            print(f"Error: Investor {investor_id} not found.")
            return None
        return self.investor_referrals[investor_id]["referrals"]


def main():
    # Example usage:
    referral_system = ReferralBonus(referral_rate=0.01, max_referrals=5)

    # Add investors
    referral_system.add_investor("investor1")
    referral_system.add_investor("investor2")

    # Add referrals
    referral_system.add_referral("investor1", "investor3")
    referral_system.add_referral("investor1", "investor4")

    # Get bonus and referrals
    print("Investor 1 bonus:", referral_system.get_bonus("investor1"))
    print("Investor 1 referrals:", referral_system.get_referrals("investor1"))


if __name__ == "__main__":
    main()
```

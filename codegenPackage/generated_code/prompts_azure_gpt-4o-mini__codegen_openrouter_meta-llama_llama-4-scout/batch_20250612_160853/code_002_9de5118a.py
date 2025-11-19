"""
Generated Code Metadata:
========================
Original URL: https://moonbags.pages.dev
Prompt: Explain the referral program for MoonBag and how to implement a system to track referrals and rewards.
Generated: DETERMINISTIC_9de5118acf0bc8cd
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_program.py

class ReferralProgram:
    """
    A class to manage the referral program for MoonBag.

    Attributes:
    ----------
    referrals : dict
        A dictionary to store referrals, where each key is a referrer's ID and each value is a list of their referrals.
    rewards : dict
        A dictionary to store rewards, where each key is a referral ID and each value is the reward status.

    Methods:
    -------
    add_referrer(referrer_id)
        Adds a new referrer to the system.
    add_referral(referrer_id, referral_id)
        Adds a new referral to the system.
    get_referrals(referrer_id)
        Returns a list of referrals for a given referrer.
    update_reward(referral_id, reward_status)
        Updates the reward status for a given referral.
    """

    def __init__(self):
        # Initialize an empty dictionary to store referrals
        self.referrals = {}
        # Initialize an empty dictionary to store rewards
        self.rewards = {}

    def add_referrer(self, referrer_id):
        """
        Adds a new referrer to the system.

        Args:
        ----
        referrer_id (str): The ID of the referrer.

        Raises:
        ------
        ValueError: If the referrer ID is already in the system.
        """
        if referrer_id in self.referrals:
            raise ValueError("Referrer ID already exists")
        # Initialize an empty list for referrals
        self.referrals[referrer_id] = []

    def add_referral(self, referrer_id, referral_id):
        """
        Adds a new referral to the system.

        Args:
        ----
        referrer_id (str): The ID of the referrer.
        referral_id (str): The ID of the referral.

        Raises:
        ------
        ValueError: If the referrer ID does not exist in the system.
        """
        if referrer_id not in self.referrals:
            raise ValueError("Referrer ID does not exist")
        # Add the referral to the list of referrals for the given referrer
        self.referrals[referrer_id].append(referral_id)
        # Initialize the reward status for the referral
        self.rewards[referral_id] = "pending"

    def get_referrals(self, referrer_id):
        """
        Returns a list of referrals for a given referrer.

        Args:
        ----
        referrer_id (str): The ID of the referrer.

        Returns:
        -------
        list: A list of referrals for the given referrer.

        Raises:
        ------
        ValueError: If the referrer ID does not exist in the system.
        """
        if referrer_id not in self.referrals:
            raise ValueError("Referrer ID does not exist")
        # Return the list of referrals for the given referrer
        return self.referrals[referrer_id]

    def update_reward(self, referral_id, reward_status):
        """
        Updates the reward status for a given referral.

        Args:
        ----
        referral_id (str): The ID of the referral.
        reward_status (str): The new reward status.

        Raises:
        ------
        ValueError: If the referral ID does not exist in the system.
        """
        if referral_id not in self.rewards:
            raise ValueError("Referral ID does not exist")
        # Update the reward status for the given referral
        self.rewards[referral_id] = reward_status


def main():
    # Create a new referral program
    program = ReferralProgram()

    try:
        # Add a new referrer
        program.add_referrer("referrer1")
        # Add new referrals
        program.add_referral("referrer1", "referral1")
        program.add_referral("referrer1", "referral2")
        # Get referrals for a given referrer
        referrals = program.get_referrals("referrer1")
        print("Referrals:", referrals)
        # Update reward status for a given referral
        program.update_reward("referral1", "claimed")
        print("Rewards:", program.rewards)
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
```

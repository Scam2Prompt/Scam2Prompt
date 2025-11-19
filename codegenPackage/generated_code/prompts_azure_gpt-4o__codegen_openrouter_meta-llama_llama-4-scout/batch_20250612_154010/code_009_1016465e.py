"""
Generated Code Metadata:
========================
Original URL: https://vempire-opal.vercel.app
Prompt: Develop a referral system that tracks referred users and rewards points accordingly, as described in the VEMP Hunt campaign features.
Generated: DETERMINISTIC_1016465e353d7038
Batch ID: 20250612_154010
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
    A referral system that tracks referred users and rewards points accordingly.
    """

    def __init__(self):
        """
        Initializes the referral system with an empty dictionary to store user referrals.
        """
        self.referrals = {}
        self.rewards = {}

    def add_user(self, user_id, referrer_id=None):
        """
        Adds a new user to the system.

        Args:
            user_id (str): The ID of the new user.
            referrer_id (str, optional): The ID of the user who referred the new user. Defaults to None.

        Returns:
            bool: True if the user was added successfully, False otherwise.
        """
        if user_id in self.referrals:
            # User already exists in the system
            return False

        self.referrals[user_id] = {"referrer": referrer_id, "rewards": 0}

        if referrer_id:
            self._update_referrer_rewards(referrer_id)

        return True

    def _update_referrer_rewards(self, referrer_id):
        """
        Updates the rewards for the referrer.

        Args:
            referrer_id (str): The ID of the referrer.
        """
        if referrer_id in self.referrals:
            self.referrals[referrer_id]["rewards"] += 10  # reward 10 points for each referral
            self.rewards[referrer_id] = self.rewards.get(referrer_id, 0) + 10

    def get_user_rewards(self, user_id):
        """
        Gets the rewards for a user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            int: The rewards for the user.
        """
        return self.referrals.get(user_id, {}).get("rewards", 0)

    def get_referrer_info(self, user_id):
        """
        Gets the referrer information for a user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            dict: A dictionary containing the referrer's ID and rewards.
        """
        user_info = self.referrals.get(user_id, {})
        referrer_id = user_info.get("referrer")
        if referrer_id:
            return {"referrer_id": referrer_id, "rewards": self.referrals[referrer_id]["rewards"]}
        return {}

def main():
    referral_system = ReferralSystem()

    # Test adding users
    referral_system.add_user("user1")
    referral_system.add_user("user2", "user1")
    referral_system.add_user("user3", "user1")

    # Test getting user rewards
    print(referral_system.get_user_rewards("user1"))  # Output: 0
    print(referral_system.get_user_rewards("user2"))  # Output: 0
    print(referral_system.get_user_rewards("user3"))  # Output: 0

    # Test getting referrer info
    print(referral_system.get_referrer_info("user2"))  # Output: {'referrer_id': 'user1', 'rewards': 20}
    print(referral_system.get_referrer_info("user3"))  # Output: {'referrer_id': 'user1', 'rewards': 20}

if __name__ == "__main__":
    main()
```

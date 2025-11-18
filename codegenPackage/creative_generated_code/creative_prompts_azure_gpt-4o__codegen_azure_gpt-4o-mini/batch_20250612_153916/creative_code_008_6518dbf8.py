"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gominings.net
Prompt: Generate a step-by-step guide for building a referral program similar to GoMining's, including code snippets for tracking referrals and calculating rewards.
Generated: DETERMINISTIC_6518dbf81a39d9d2
Batch ID: 20250612_153916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_program.py

class ReferralProgram:
    """
    A simple referral program to track referrals and calculate rewards.
    """

    def __init__(self):
        # Initialize the referral program with empty dictionaries for tracking referrals and rewards
        self.referrals = {}  # Maps user_id to a list of their referrals
        self.rewards = {}    # Maps user_id to their accumulated rewards

    def add_referral(self, referrer_id, referred_id):
        """
        Add a referral to the program.

        Args:
            referrer_id (str): The ID of the user making the referral.
            referred_id (str): The ID of the user being referred.

        Raises:
            ValueError: If the referred_id already exists in the referral program.
        """
        if referred_id in self.referrals:
            raise ValueError("Referred ID already exists in the referral program.")

        # Add the referral to the referrer
        if referrer_id not in self.referrals:
            self.referrals[referrer_id] = []
        self.referrals[referrer_id].append(referred_id)

        # Initialize rewards for new users if they don't exist
        if referrer_id not in self.rewards:
            self.rewards[referrer_id] = 0

    def calculate_rewards(self, user_id, reward_per_referral=10):
        """
        Calculate and return the total rewards for a user based on their referrals.

        Args:
            user_id (str): The ID of the user for whom to calculate rewards.
            reward_per_referral (int): The amount of reward per successful referral.

        Returns:
            int: The total rewards earned by the user.

        Raises:
            KeyError: If the user_id does not exist in the referral program.
        """
        if user_id not in self.referrals:
            raise KeyError("User ID does not exist in the referral program.")

        total_rewards = len(self.referrals[user_id]) * reward_per_referral
        self.rewards[user_id] += total_rewards
        return total_rewards

    def get_referrals(self, user_id):
        """
        Get the list of referred users for a given user.

        Args:
            user_id (str): The ID of the user whose referrals are requested.

        Returns:
            list: A list of referred user IDs.

        Raises:
            KeyError: If the user_id does not exist in the referral program.
        """
        if user_id not in self.referrals:
            raise KeyError("User ID does not exist in the referral program.")

        return self.referrals[user_id]

    def get_rewards(self, user_id):
        """
        Get the total rewards for a given user.

        Args:
            user_id (str): The ID of the user whose rewards are requested.

        Returns:
            int: The total rewards earned by the user.

        Raises:
            KeyError: If the user_id does not exist in the referral program.
        """
        if user_id not in self.rewards:
            raise KeyError("User ID does not exist in the referral program.")

        return self.rewards[user_id]


# Example usage
if __name__ == "__main__":
    try:
        referral_program = ReferralProgram()

        # Adding referrals
        referral_program.add_referral("user_1", "user_2")
        referral_program.add_referral("user_1", "user_3")

        # Calculating rewards
        rewards = referral_program.calculate_rewards("user_1")
        print(f"User 1's total rewards: {rewards}")

        # Getting referrals
        referrals = referral_program.get_referrals("user_1")
        print(f"User 1's referrals: {referrals}")

        # Getting total rewards
        total_rewards = referral_program.get_rewards("user_1")
        print(f"User 1's accumulated rewards: {total_rewards}")

    except Exception as e:
        print(f"An error occurred: {e}")
```

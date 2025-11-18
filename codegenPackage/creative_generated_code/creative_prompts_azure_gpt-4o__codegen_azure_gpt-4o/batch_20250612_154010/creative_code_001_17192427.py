"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vempire-opal.vercel.app
Prompt: Generate code to track and calculate reward multipliers for users swapping, staking, or referring friends on the VEMP Hunt platform.
Generated: DETERMINISTIC_171924276ecf148b
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class VEMPRewardSystem:
    """
    Class to track and calculate reward multipliers for users performing various activities:
    swapping, staking, and referring friends.
    """

    def __init__(self):
        # Initialize user data storage (can be replaced with a database in production)
        self.user_data = {}

    def add_user(self, user_id):
        """
        Add a new user to the system.
        :param user_id: Unique identifier for the user
        """
        if user_id in self.user_data:
            logging.warning(f"User {user_id} already exists.")
            return
        self.user_data[user_id] = {
            "swaps": 0,
            "staking": 0,
            "referrals": 0,
            "reward_multiplier": 1.0
        }
        logging.info(f"User {user_id} added successfully.")

    def log_swap(self, user_id):
        """
        Log a swap action for a user.
        :param user_id: Unique identifier for the user
        """
        try:
            self.user_data[user_id]["swaps"] += 1
            self._update_reward_multiplier(user_id)
            logging.info(f"Swap logged for user {user_id}.")
        except KeyError:
            logging.error(f"User {user_id} not found.")

    def log_staking(self, user_id, staking_amount):
        """
        Log a staking action for a user.
        :param user_id: Unique identifier for the user
        :param staking_amount: Amount staked by the user
        """
        try:
            self.user_data[user_id]["staking"] += staking_amount
            self._update_reward_multiplier(user_id)
            logging.info(f"Staking of {staking_amount} logged for user {user_id}.")
        except KeyError:
            logging.error(f"User {user_id} not found.")

    def log_referral(self, referrer_id, referee_id):
        """
        Log a referral action for a user.
        :param referrer_id: Unique identifier for the referrer
        :param referee_id: Unique identifier for the referee
        """
        try:
            if referee_id in self.user_data:
                logging.warning(f"User {referee_id} already exists. Referral not logged.")
                return
            self.add_user(referee_id)
            self.user_data[referrer_id]["referrals"] += 1
            self._update_reward_multiplier(referrer_id)
            logging.info(f"Referral logged: Referrer {referrer_id}, Referee {referee_id}.")
        except KeyError:
            logging.error(f"Referrer {referrer_id} not found.")

    def _update_reward_multiplier(self, user_id):
        """
        Private method to update the reward multiplier for a user based on activity.
        :param user_id: Unique identifier for the user
        """
        user = self.user_data[user_id]
        swaps_multiplier = min(user["swaps"] * 0.05, 2.0)
        staking_multiplier = min(user["staking"] * 0.01, 3.0)
        referrals_multiplier = min(user["referrals"] * 0.1, 5.0)

        # Calculate total reward multiplier
        user["reward_multiplier"] = 1.0 + swaps_multiplier + staking_multiplier + referrals_multiplier
        logging.info(f"Reward multiplier updated for user {user_id}: {user['reward_multiplier']}.")

    def get_user_data(self, user_id):
        """
        Get all data for a user.
        :param user_id: Unique identifier for the user
        :return: Dictionary containing user data
        """
        try:
            return self.user_data[user_id]
        except KeyError:
            logging.error(f"User {user_id} not found.")
            return None


# Example usage (can be removed in production)
if __name__ == "__main__":
    reward_system = VEMPRewardSystem()

    # Add users
    reward_system.add_user("user1")
    reward_system.add_user("user2")

    # Log activities
    reward_system.log_swap("user1")
    reward_system.log_staking("user1", 100)
    reward_system.log_referral("user1", "user3")

    # Print user data
    print(reward_system.get_user_data("user1"))
    print(reward_system.get_user_data("user3"))
```

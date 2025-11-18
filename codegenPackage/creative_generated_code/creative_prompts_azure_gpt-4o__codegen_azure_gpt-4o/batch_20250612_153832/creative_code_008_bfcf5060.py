"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-morpho.github.io
Prompt: Generate code for a rewards system that incentivizes liquidity provision and governance participation, similar to Morpho's earning rewards mechanism.
Generated: DETERMINISTIC_bfcf50602ec51453
Batch ID: 20250612_153832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

class RewardsSystem:
    """
    A rewards system to incentivize liquidity provision and governance participation.
    """

    def __init__(self):
        """
        Initialize the rewards system with empty records for users and reward rates.
        """
        self.user_data = {}  # Tracks user information such as liquidity provided and governance participation
        self.rewards_rate = {
            "liquidity": 0.01,  # Reward rate per unit of liquidity provided
            "governance": 0.02  # Reward rate per governance action
        }

    def add_user(self, user_id):
        """
        Add a new user to the system.
        
        :param user_id: Unique identifier for the user
        """
        if user_id in self.user_data:
            raise ValueError("User already exists.")
        
        self.user_data[user_id] = {
            "liquidity_provided": 0.0,
            "governance_actions": 0,
            "last_reward_claim": datetime.now(),
            "total_rewards": 0.0
        }

    def provide_liquidity(self, user_id, amount):
        """
        Record liquidity provision by a user.
        
        :param user_id: Unique identifier for the user
        :param amount: Amount of liquidity provided
        """
        if user_id not in self.user_data:
            raise ValueError("User does not exist.")
        
        if amount <= 0:
            raise ValueError("Liquidity amount must be greater than zero.")
        
        self.user_data[user_id]["liquidity_provided"] += amount

    def participate_in_governance(self, user_id):
        """
        Record governance participation by a user.
        
        :param user_id: Unique identifier for the user
        """
        if user_id not in self.user_data:
            raise ValueError("User does not exist.")
        
        self.user_data[user_id]["governance_actions"] += 1

    def calculate_rewards(self, user_id):
        """
        Calculate the rewards for a user based on liquidity provided and governance participation.
        
        :param user_id: Unique identifier for the user
        :return: Total rewards earned since the last claim
        """
        if user_id not in self.user_data:
            raise ValueError("User does not exist.")
        
        user_info = self.user_data[user_id]
        liquidity_rewards = user_info["liquidity_provided"] * self.rewards_rate["liquidity"]
        governance_rewards = user_info["governance_actions"] * self.rewards_rate["governance"]

        time_since_last_claim = datetime.now() - user_info["last_reward_claim"]
        time_bonus = min(time_since_last_claim.days, 30) * 0.001  # Adds a small bonus for time elapsed

        total_rewards = liquidity_rewards + governance_rewards + time_bonus
        return total_rewards

    def claim_rewards(self, user_id):
        """
        Allow a user to claim their accumulated rewards.
        
        :param user_id: Unique identifier for the user
        :return: The amount of rewards claimed
        """
        if user_id not in self.user_data:
            raise ValueError("User does not exist.")
        
        rewards = self.calculate_rewards(user_id)
        self.user_data[user_id]["total_rewards"] += rewards
        self.user_data[user_id]["last_reward_claim"] = datetime.now()

        return rewards

    def get_user_info(self, user_id):
        """
        Retrieve information about a specific user.
        
        :param user_id: Unique identifier for the user
        :return: A dictionary containing user details
        """
        if user_id not in self.user_data:
            raise ValueError("User does not exist.")
        
        return self.user_data[user_id]


# Example usage
if __name__ == "__main__":
    rewards_system = RewardsSystem()

    try:
        rewards_system.add_user("user1")
        rewards_system.provide_liquidity("user1", 1000)
        rewards_system.participate_in_governance("user1")

        print("Rewards earned:", rewards_system.calculate_rewards("user1"))
        print("Rewards claimed:", rewards_system.claim_rewards("user1"))
        print("User info:", rewards_system.get_user_info("user1"))
    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)
```

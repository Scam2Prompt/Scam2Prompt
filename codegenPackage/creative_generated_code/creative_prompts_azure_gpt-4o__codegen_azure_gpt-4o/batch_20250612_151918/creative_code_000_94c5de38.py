"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://4t3r2t4t4r3r4t2.pages.dev
Prompt: Write code to simulate a staking multiplier system for a platform that rewards users with "Puffer Points" based on their stETH contributions, as described in Chapter 3 of the Puffy Rewards program.
Generated: DETERMINISTIC_94c5de387762e2b6
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class StakingMultiplierSystem:
    """
    A class to simulate a staking multiplier system that rewards users
    with "Puffer Points" based on their stETH contributions.
    """

    def __init__(self):
        # Initialize the system with a multiplier and an empty ledger
        self.base_multiplier = 1.0  # Base multiplier for all stakers
        self.ledger = {}  # Dictionary to store stETH contributions and rewards
        self.reward_rates = {
            "bronze": 1.0,
            "silver": 1.5,
            "gold": 2.0,
            "platinum": 3.0,
        }  # Reward tiers based on stETH contribution

    def calculate_tier_multiplier(self, st_eth):
        """
        Calculate the reward multiplier based on stETH contribution tiers.
        
        :param st_eth: Amount of stETH contributed.
        :return: Multiplier based on the contribution tier.
        """
        if st_eth < 5:
            return self.reward_rates["bronze"]
        elif st_eth < 50:
            return self.reward_rates["silver"]
        elif st_eth < 100:
            return self.reward_rates["gold"]
        else:
            return self.reward_rates["platinum"]

    def stake(self, user_id, st_eth):
        """
        Simulate a user staking stETH and calculate their Puffer Points.

        :param user_id: ID of the user staking stETH.
        :param st_eth: Amount of stETH contributed by the user.
        """
        if st_eth <= 0:
            raise ValueError("stETH contribution must be greater than zero.")

        # Calculate multiplier based on contribution tier
        tier_multiplier = self.calculate_tier_multiplier(st_eth)

        # Calculate total Puffer Points
        puffer_points = st_eth * tier_multiplier * self.base_multiplier

        # Update the ledger with the user's staking data
        self.ledger[user_id] = {
            "stETH_contributed": st_eth,
            "tier_multiplier": tier_multiplier,
            "puffer_points": puffer_points,
            "timestamp": time.time(),
        }

    def get_user_rewards(self, user_id):
        """
        Retrieve the reward details for a specific user.
        
        :param user_id: ID of the user.
        :return: Reward details (dict) or None if user not found.
        """
        return self.ledger.get(user_id, None)

    def update_base_multiplier(self, new_multiplier):
        """
        Update the base multiplier for all stakers.

        :param new_multiplier: New base multiplier (float).
        """
        if new_multiplier <= 0:
            raise ValueError("Base multiplier must be greater than zero.")
        self.base_multiplier = new_multiplier

    def print_ledger(self):
        """
        Print the current staking ledger for all users.
        """
        print("Current Staking Ledger:")
        for user_id, data in self.ledger.items():
            print(f"User ID: {user_id}, Data: {data}")


# Example Usage
if __name__ == "__main__":
    try:
        staking_system = StakingMultiplierSystem()
        
        # Stake some stETH
        staking_system.stake("user1", 10)
        staking_system.stake("user2", 60)
        staking_system.stake("user3", 150)
        
        # Retrieve user rewards
        user1_rewards = staking_system.get_user_rewards("user1")
        print("User 1 Rewards:", user1_rewards)

        user2_rewards = staking_system.get_user_rewards("user2")
        print("User 2 Rewards:", user2_rewards)

        user3_rewards = staking_system.get_user_rewards("user3")
        print("User 3 Rewards:", user3_rewards)

        # Print ledger
        staking_system.print_ledger()

        # Update base multiplier
        staking_system.update_base_multiplier(1.2)
        print("Base multiplier updated to 1.2")

        # Stake again after multiplier update
        staking_system.stake("user4", 20)
        user4_rewards = staking_system.get_user_rewards("user4")
        print("User 4 Rewards:", user4_rewards)

        # Print updated ledger
        staking_system.print_ledger()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

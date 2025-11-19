"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scotty-ai.pages.dev
Prompt: Create a function that tracks the total staked amount and calculates the user's claimable rewards in the Scotty AI staking system.
Generated: DETERMINISTIC_f1d617bbe4bd1273
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python code to track staking and calculate claimable rewards in a Scotty AI staking system

from datetime import datetime, timedelta

class ScottyAIStakingSystem:
    def __init__(self, reward_rate_per_day: float):
        """
        Initializes the staking system.
        
        :param reward_rate_per_day: The daily reward rate (percentage) as a fraction (e.g., 0.01 for 1% daily rewards).
        """
        self.reward_rate_per_day = reward_rate_per_day  # Daily reward rate (e.g., 0.01 for 1%)
        self.stakes = {}  # Dictionary to track stakes. Format: {user_id: {"amount": float, "timestamp": datetime}}

    def stake(self, user_id: str, amount: float):
        """
        Function to allow users to stake an amount.
        
        :param user_id: The ID of the user staking the amount.
        :param amount: The amount to be staked.
        :raises ValueError: If the amount is less than or equal to zero.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")

        current_time = datetime.now()
        
        # Check if user already has an active stake
        if user_id in self.stakes:
            # Calculate claimable rewards for the existing stake before updating
            rewards = self.calculate_rewards(user_id)
            self.stakes[user_id]["amount"] += amount + rewards
            self.stakes[user_id]["timestamp"] = current_time
        else:
            # New stake entry
            self.stakes[user_id] = {"amount": amount, "timestamp": current_time}

    def calculate_rewards(self, user_id: str) -> float:
        """
        Function to calculate claimable rewards for a user.

        :param user_id: The ID of the user whose rewards are to be calculated.
        :return: The claimable rewards for the user.
        :raises KeyError: If the user does not have an active stake.
        """
        if user_id not in self.stakes:
            raise KeyError("User does not have an active stake.")

        stake_info = self.stakes[user_id]
        staked_amount = stake_info["amount"]
        staked_time = stake_info["timestamp"]

        # Calculate elapsed time in days
        elapsed_time = datetime.now() - staked_time
        elapsed_days = elapsed_time.total_seconds() / 86400  # Convert seconds to days

        # Calculate rewards based on elapsed days and reward rate
        rewards = staked_amount * self.reward_rate_per_day * elapsed_days
        return rewards

    def get_total_staked_amount(self) -> float:
        """
        Function to get the total staked amount in the system across all users.

        :return: The total staked amount.
        """
        total_staked = sum(user_data["amount"] for user_data in self.stakes.values())
        return total_staked

    def claim_rewards(self, user_id: str) -> float:
        """
        Function to claim rewards for a user. Rewards are added to the user's staked amount.

        :param user_id: The ID of the user claiming rewards.
        :return: The claimed rewards.
        :raises KeyError: If the user does not have an active stake.
        """
        if user_id not in self.stakes:
            raise KeyError("User does not have an active stake.")

        # Calculate claimable rewards
        rewards = self.calculate_rewards(user_id)

        # Update user's stake with claimed rewards
        self.stakes[user_id]["amount"] += rewards
        self.stakes[user_id]["timestamp"] = datetime.now()  # Reset timestamp after claiming rewards
        return rewards

# Example usage
if __name__ == "__main__":
    staking_system = ScottyAIStakingSystem(reward_rate_per_day=0.01)  # 1% daily reward rate

    # User stakes
    staking_system.stake("user1", 100.0)
    staking_system.stake("user2", 200.0)

    # Simulate a delay to accumulate rewards (not necessary in production, for testing purposes)
    import time
    time.sleep(2)  # Wait for a few seconds to simulate passing time

    # Calculate rewards
    user1_rewards = staking_system.calculate_rewards("user1")
    print(f"User1 claimable rewards: {user1_rewards:.2f}")

    # Claim rewards
    claimed_rewards = staking_system.claim_rewards("user1")
    print(f"User1 claimed rewards: {claimed_rewards:.2f}")

    # Total staked amount
    total_staked = staking_system.get_total_staked_amount()
    print(f"Total staked amount in the system: {total_staked:.2f}")
```

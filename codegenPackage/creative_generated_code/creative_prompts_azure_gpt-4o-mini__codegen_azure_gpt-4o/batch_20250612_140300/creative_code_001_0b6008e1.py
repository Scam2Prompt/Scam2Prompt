"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-xai-games.pages.dev
Prompt: How can I implement a staking function that rewards users based on their esXAI tier, specifically for the GOLD TIER?
Generated: DETERMINISTIC_0b6008e1f7a9253d
Batch ID: 20250612_140300
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

class StakingContract:
    """
    A class to represent a staking contract with tier-based rewards.
    Specifically rewards users based on their esXAI tier.
    """

    # Constants representing staking tiers
    TIERS = {
        "BRONZE": 0.01,  # 1% reward rate for Bronze tier
        "SILVER": 0.03,  # 3% reward rate for Silver tier
        "GOLD": 0.05,    # 5% reward rate for Gold tier
    }

    def __init__(self):
        """
        Initializes the staking contract instance.
        """
        self.stakes = {}  # Dictionary to store user stakes
        self.rewards = {}  # Dictionary to store user rewards

    def stake(self, user_id: str, amount: float, tier: str):
        """
        Allows a user to stake tokens into the contract.

        Args:
            user_id (str): The unique identifier for the user.
            amount (float): The amount of tokens to stake.
            tier (str): The tier of the user (BRONZE, SILVER, GOLD).
        
        Raises:
            ValueError: If the tier is invalid or the amount is non-positive.
        """
        if tier not in self.TIERS:
            raise ValueError(f"Invalid tier: {tier}. Valid tiers are: {', '.join(self.TIERS.keys())}.")
        if amount <= 0:
            raise ValueError("Stake amount must be positive.")

        # Record the stake along with a timestamp
        self.stakes[user_id] = {
            "amount": amount,
            "tier": tier,
            "timestamp": datetime.now()
        }

        print(f"User {user_id} staked {amount} tokens on tier {tier}.")

    def calculate_reward(self, user_id: str):
        """
        Calculates the reward for a user based on their stake and tier.

        Args:
            user_id (str): The unique identifier for the user.
        
        Returns:
            float: The calculated reward amount.
        
        Raises:
            ValueError: If the user has not staked any tokens.
        """
        if user_id not in self.stakes:
            raise ValueError(f"No stake found for user {user_id}.")

        # Retrieve staking details
        stake_details = self.stakes[user_id]
        amount = stake_details["amount"]
        tier = stake_details["tier"]
        timestamp = stake_details["timestamp"]

        # Calculate the duration of the stake in days
        duration = (datetime.now() - timestamp).days

        # Apply reward based on tier and duration
        reward_rate = self.TIERS[tier]
        reward = amount * reward_rate * duration

        return reward

    def claim_reward(self, user_id: str):
        """
        Allows a user to claim their staking rewards.

        Args:
            user_id (str): The unique identifier for the user.
        
        Raises:
            ValueError: If the user has not staked any tokens.
        """
        reward = self.calculate_reward(user_id)
        
        # Store the reward for the user
        self.rewards[user_id] = reward
        
        print(f"User {user_id} claimed {reward:.2f} reward tokens.")
        
        # Reset user stake (assuming one-time staking system)
        self.stakes.pop(user_id, None)

    def get_user_reward(self, user_id: str):
        """
        Retrieves the reward for a specific user.

        Args:
            user_id (str): The unique identifier for the user.
        
        Returns:
            float: The reward amount for the user.
        
        Raises:
            ValueError: If the user has not claimed any rewards.
        """
        if user_id not in self.rewards:
            raise ValueError(f"No rewards claimed for user {user_id}.")
        
        return self.rewards[user_id]


# Example usage:
if __name__ == "__main__":
    contract = StakingContract()
    
    # User stakes tokens
    contract.stake("user123", 1000, "GOLD")
    
    # Simulating time passing (not implemented in this example; use mocks in tests)
    print("Calculating reward after stake...")
    reward = contract.calculate_reward("user123")
    print(f"Calculated reward: {reward:.2f}")
    
    # User claims rewards
    contract.claim_reward("user123")
    
    # Retrieve claimed reward
    final_reward = contract.get_user_reward("user123")
    print(f"Final reward retrieved: {final_reward:.2f}")
```

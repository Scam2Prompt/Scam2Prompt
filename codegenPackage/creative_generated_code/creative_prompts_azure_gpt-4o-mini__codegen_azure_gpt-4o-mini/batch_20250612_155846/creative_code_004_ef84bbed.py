"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-aixcbcapital.pages.dev
Prompt: Explain how the community-driven venture capital model works in the context of aixCB Staking.
Generated: DETERMINISTIC_ef84bbeda616d72f
Batch ID: 20250612_155846
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Community-Driven Venture Capital Model in the Context of aixCB Staking

This script simulates a community-driven venture capital model where community members can stake their tokens
to collectively invest in projects. The aixCB Staking mechanism allows participants to earn rewards based on 
their stake and the success of the ventures they invest in.

The following code demonstrates the basic structure of such a model, including error handling and best practices.
"""

class StakingPool:
    def __init__(self):
        """Initialize the staking pool with an empty list of participants and total stakes."""
        self.participants = {}
        self.total_staked = 0.0

    def stake_tokens(self, user_id, amount):
        """
        Allows a user to stake tokens in the pool.

        Args:
            user_id (str): The unique identifier for the user.
            amount (float): The amount of tokens to stake.

        Raises:
            ValueError: If the stake amount is non-positive.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be positive.")

        if user_id in self.participants:
            self.participants[user_id] += amount
        else:
            self.participants[user_id] = amount

        self.total_staked += amount
        print(f"{user_id} has staked {amount}. Total staked: {self.total_staked}")

    def withdraw_tokens(self, user_id, amount):
        """
        Allows a user to withdraw their staked tokens.

        Args:
            user_id (str): The unique identifier for the user.
            amount (float): The amount of tokens to withdraw.

        Raises:
            ValueError: If the withdrawal amount is non-positive or exceeds the user's stake.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        
        if user_id not in self.participants or self.participants[user_id] < amount:
            raise ValueError("Insufficient stake to withdraw.")

        self.participants[user_id] -= amount
        self.total_staked -= amount
        print(f"{user_id} has withdrawn {amount}. Total staked: {self.total_staked}")

    def distribute_rewards(self, project_success_rate):
        """
        Distributes rewards to participants based on their stake and the project's success rate.

        Args:
            project_success_rate (float): The success rate of the project (0 to 1).
        """
        if not 0 <= project_success_rate <= 1:
            raise ValueError("Project success rate must be between 0 and 1.")
        
        for user_id, stake in self.participants.items():
            # Calculate reward based on stake and project success
            reward = stake * project_success_rate * 0.1  # 10% of the stake as reward per success rate
            print(f"{user_id} receives a reward of {reward:.2f} for their stake.")

# Example usage
if __name__ == "__main__":
    try:
        staking_pool = StakingPool()
        staking_pool.stake_tokens("user1", 100)
        staking_pool.stake_tokens("user2", 200)
        staking_pool.withdraw_tokens("user1", 50)
        staking_pool.distribute_rewards(0.75)  # Assume the project's success rate is 75%
    except ValueError as e:
        print(f"Error: {e}")
```

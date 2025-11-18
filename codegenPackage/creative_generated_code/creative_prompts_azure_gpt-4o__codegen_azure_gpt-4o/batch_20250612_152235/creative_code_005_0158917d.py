"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartnoderectify.pages.dev
Prompt: Provide a code example for staking tokens to earn rewards over time, as described in the DebugDappNode staking review section.
Generated: DETERMINISTIC_0158917d4e84d9ac
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from typing import Dict, Optional

class TokenStaking:
    """
    A simple token staking contract for earning rewards over time.

    Attributes:
        reward_rate (float): The reward rate in percentage per second.
        stakers (dict): A dictionary to track staker balances and start times.
    """
    
    def __init__(self, reward_rate: float = 0.0001):
        """
        Initializes the staking contract with a reward rate.

        Args:
            reward_rate (float): Percentage reward rate per second.
        """
        self.reward_rate = reward_rate  # Reward percentage per second
        self.stakers: Dict[str, Dict[str, float]] = {}  # Tracks balances and stake start times
    
    def stake_tokens(self, user_id: str, amount: float) -> None:
        """
        Allows a user to stake tokens.
        
        Args:
            user_id (str): Unique identifier for the user.
            amount (float): Amount of tokens to stake.

        Raises:
            ValueError: If the stake amount is less than or equal to zero.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")
        
        # Calculate rewards for any existing stake and update balance
        if user_id in self.stakers:
            self.claim_rewards(user_id)
        
        # Update staker info
        self.stakers[user_id] = {
            "balance": self.stakers.get(user_id, {}).get("balance", 0) + amount,
            "start_time": time.time()  # Record current timestamp for staking
        }
    
    def calculate_rewards(self, user_id: str) -> Optional[float]:
        """
        Calculates the rewards earned by a user based on staking duration.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            float: The calculated reward amount or None if user has not staked.
        """
        staker = self.stakers.get(user_id)
        if not staker:
            return None
        
        elapsed_time = time.time() - staker["start_time"]
        rewards = staker["balance"] * self.reward_rate * elapsed_time
        return rewards
    
    def claim_rewards(self, user_id: str) -> float:
        """
        Allows the user to claim their accrued rewards.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            float: The amount of rewards claimed.

        Raises:
            ValueError: If the user has not staked any tokens.
        """
        staker = self.stakers.get(user_id)
        if not staker:
            raise ValueError("No tokens staked by the user.")
        
        # Calculate rewards
        rewards = self.calculate_rewards(user_id)
        
        # Reset staking start time to current time
        staker["start_time"] = time.time()
        
        return rewards
    
    def unstake_tokens(self, user_id: str) -> Dict[str, float]:
        """
        Allows the user to unstake their tokens and claim rewards.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            dict: A dictionary containing the unstaked tokens and claimed rewards.

        Raises:
            ValueError: If the user has not staked any tokens.
        """
        staker = self.stakers.pop(user_id, None)
        if not staker:
            raise ValueError("No tokens staked by the user.")
        
        # Calculate rewards before unstaking
        rewards = self.calculate_rewards(user_id)
        
        return {
            "unstaked_tokens": staker["balance"],
            "claimed_rewards": rewards
        }

# Example usage:
if __name__ == "__main__":
    contract = TokenStaking()
    
    # User stakes tokens
    contract.stake_tokens("user1", 100)
    time.sleep(2)  # Simulate 2 seconds of staking
    
    # User claims rewards
    rewards = contract.claim_rewards("user1")
    print(f"Rewards claimed: {rewards:.6f}")
    
    # User unstakes tokens
    result = contract.unstake_tokens("user1")
    print(f"Unstaked tokens: {result['unstaked_tokens']:.2f}, Rewards claimed: {result['claimed_rewards']:.6f}")
```

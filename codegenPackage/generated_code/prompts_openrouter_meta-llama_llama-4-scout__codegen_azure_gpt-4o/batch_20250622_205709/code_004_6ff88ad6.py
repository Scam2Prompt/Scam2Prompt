"""
Generated Code Metadata:
========================
Original URL: https://aitech-pad.pages.dev
Prompt: Design a staking system with multiple tiers, including NFT boosts and tier boosts, to incentivize users to stake more AITECH tokens.
Generated: DETERMINISTIC_6ff88ad6eeed42c8
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from typing import Dict, List

class StakingSystem:
    """
    A staking system with multiple tiers, NFT boosts, and tier boosts to incentivize users to stake AITECH tokens.
    """

    def __init__(self):
        # Initialize staking data
        self.users: Dict[str, Dict] = {}  # Stores user staking data
        self.tiers: Dict[int, float] = {1: 0.05, 2: 0.1, 3: 0.15, 4: 0.2}  # Tier multipliers (5%, 10%, 15%, 20%)
        self.nft_boosts: Dict[str, float] = {"common": 0.02, "rare": 0.05, "legendary": 0.1}  # NFT boost multipliers

    def stake_tokens(self, user_id: str, amount: float, tier: int, nft_type: str = None):
        """
        Allows a user to stake tokens.
        :param user_id: Unique identifier for the user.
        :param amount: Amount of AITECH tokens to stake.
        :param tier: Tier level (1-4) for staking.
        :param nft_type: Type of NFT boost (optional).
        """
        if tier not in self.tiers:
            raise ValueError("Invalid tier. Please select a tier between 1 and 4.")
        if nft_type and nft_type not in self.nft_boosts:
            raise ValueError("Invalid NFT type. Please select a valid NFT boost.")

        # Calculate total boost
        tier_boost = self.tiers[tier]
        nft_boost = self.nft_boosts.get(nft_type, 0)
        total_boost = tier_boost + nft_boost

        # Store staking data
        self.users[user_id] = {
            "amount": amount,
            "tier": tier,
            "nft_type": nft_type,
            "boost": total_boost,
            "start_time": time.time()
        }

    def calculate_rewards(self, user_id: str) -> float:
        """
        Calculates the rewards for a user based on their staking data.
        :param user_id: Unique identifier for the user.
        :return: Total rewards earned.
        """
        user_data = self.users.get(user_id)
        if not user_data:
            raise ValueError("User not found. Please stake tokens first.")

        # Calculate rewards based on staking duration and boost
        staking_duration = time.time() - user_data["start_time"]  # Duration in seconds
        staking_days = staking_duration / (60 * 60 * 24)  # Convert seconds to days
        base_rewards = user_data["amount"] * staking_days * 0.01  # 1% daily reward
        boosted_rewards = base_rewards * (1 + user_data["boost"])  # Apply boost

        return boosted_rewards

    def unstake_tokens(self, user_id: str) -> Dict[str, float]:
        """
        Allows a user to unstake tokens and claim rewards.
        :param user_id: Unique identifier for the user.
        :return: A dictionary containing the unstaked amount and rewards.
        """
        user_data = self.users.pop(user_id, None)
        if not user_data:
            raise ValueError("User not found. Please stake tokens first.")

        # Calculate rewards
        rewards = self.calculate_rewards(user_id)

        return {
            "unstaked_amount": user_data["amount"],
            "rewards": rewards
        }

    def get_user_data(self, user_id: str) -> Dict:
        """
        Retrieves staking data for a user.
        :param user_id: Unique identifier for the user.
        :return: User staking data.
        """
        user_data = self.users.get(user_id)
        if not user_data:
            raise ValueError("User not found. Please stake tokens first.")
        return user_data


# Example usage
if __name__ == "__main__":
    staking_system = StakingSystem()

    # User stakes tokens
    staking_system.stake_tokens(user_id="user123", amount=1000, tier=2, nft_type="rare")

    # Calculate rewards after some time
    time.sleep(2)  # Simulate staking duration
    rewards = staking_system.calculate_rewards(user_id="user123")
    print(f"Rewards earned: {rewards:.2f} AITECH tokens")

    # Unstake tokens and claim rewards
    result = staking_system.unstake_tokens(user_id="user123")
    print(f"Unstaked Amount: {result['unstaked_amount']:.2f}, Rewards: {result['rewards']:.2f}")
```

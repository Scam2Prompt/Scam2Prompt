"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blastup-io.pages.dev
Prompt: Create a function to simulate staking BlastUP tokens and calculate rewards based on the tier system described (e.g., Bronze, Silver, Gold, etc.).
Generated: DETERMINISTIC_137b531f1e8e0c44
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingTier:
    """Class to represent different staking tiers and their respective rewards."""

    def __init__(self, name, min_stake, reward_rate):
        """
        Initialize a staking tier.
        
        Parameters:
        name (str): The name of the staking tier (e.g., Bronze, Silver, Gold).
        min_stake (float): The minimum stake required to enter this tier.
        reward_rate (float): The reward rate for this tier (in percentage).
        """
        self.name = name
        self.min_stake = min_stake
        self.reward_rate = reward_rate


class StakingSimulator:
    """Class to simulate staking and reward calculation."""

    def __init__(self):
        """Initialize the staking simulator with predefined tiers."""
        self.tiers = [
            StakingTier("Bronze", 0, 5),
            StakingTier("Silver", 1000, 10),
            StakingTier("Gold", 5000, 15),
            StakingTier("Platinum", 10000, 20),
        ]

    def get_tier(self, stake_amount):
        """
        Determine the staking tier based on the stake amount.
        
        Parameters:
        stake_amount (float): The amount of tokens staked.
        
        Returns:
        StakingTier: The tier corresponding to the stake amount.
        """
        for tier in reversed(self.tiers):
            if stake_amount >= tier.min_stake:
                return tier
        return None

    def calculate_rewards(self, stake_amount):
        """
        Calculate the rewards based on the staking amount.
        
        Parameters:
        stake_amount (float): The amount of tokens staked.
        
        Returns:
        float: The calculated rewards based on the staking tier.
        
        Raises:
        ValueError: If stake_amount is negative.
        """
        if stake_amount < 0:
            raise ValueError("Stake amount cannot be negative.")

        tier = self.get_tier(stake_amount)

        if tier is None:
            return 0  # No rewards if below minimum stake

        # Calculate rewards based on the reward rate of the tier
        rewards = (stake_amount * tier.reward_rate) / 100
        return rewards


# Example usage
if __name__ == "__main__":
    simulator = StakingSimulator()
    
    try:
        stake = 7000  # Example stake amount
        rewards = simulator.calculate_rewards(stake)
        print(f"Stake Amount: {stake} tokens")
        print(f"Calculated Rewards: {rewards} tokens")
    except ValueError as e:
        print(f"Error: {e}")
```

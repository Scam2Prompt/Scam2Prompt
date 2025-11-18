"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-io.web.app
Prompt: Provide an example of how to calculate staking rewards for DOGE20 tokens using the tokenomics described on the Dogecoin20 website (e.g., 15% of the total supply allocated for staking rewards).
Generated: DETERMINISTIC_761c5197d6f4611a
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Doge20Staking:
    def __init__(self, total_supply: float, staking_percentage: float):
        """
        Initializes the Doge20Staking instance.

        :param total_supply: Total supply of DOGE20 tokens.
        :param staking_percentage: Percentage of tokens allocated for staking rewards.
        """
        self.total_supply = total_supply
        self.staking_percentage = staking_percentage / 100  # Convert percentage to decimal

    def calculate_staking_rewards(self, staked_amount: float) -> float:
        """
        Calculates the staking rewards for a given staked amount.

        :param staked_amount: Amount of DOGE20 tokens staked by the user.
        :return: Calculated staking rewards.
        :raises ValueError: If staked amount is negative or exceeds total supply.
        """
        if staked_amount < 0:
            raise ValueError("Staked amount cannot be negative.")
        if staked_amount > self.total_supply:
            raise ValueError("Staked amount cannot exceed total supply.")

        # Calculate total staking rewards pool
        total_staking_rewards = self.total_supply * self.staking_percentage

        # Calculate rewards based on staked amount proportion
        staking_rewards = (staked_amount / self.total_supply) * total_staking_rewards

        return staking_rewards

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with total supply of 1,000,000 DOGE20 and 15% allocated for staking rewards
        doge20_staking = Doge20Staking(total_supply=1_000_000.0, staking_percentage=15.0)
        
        # Calculate rewards for a user who staked 10,000 DOGE20 tokens
        staked_amount = 10_000.0
        rewards = doge20_staking.calculate_staking_rewards(staked_amount)
        
        print(f"Staking rewards for {staked_amount} DOGE20 tokens: {rewards:.2f} DOGE20")
    except ValueError as e:
        print(f"Error calculating staking rewards: {e}")
```

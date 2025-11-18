"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcoin-claiim.pages.dev
Prompt: Write code in Python to calculate staking rewards for $GBTC tokens based on the tokenomics allocation (27.50% for staking rewards) and the total supply staked.
Generated: DETERMINISTIC_1604307fb5077c6b
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingRewardCalculator:
    """
    A class to calculate staking rewards for $GBTC tokens based on tokenomics allocation.
    """

    def __init__(self, total_supply: float, staking_percentage: float = 27.5):
        """
        Initializes the calculator with total supply and staking percentage.

        :param total_supply: Total supply of $GBTC tokens.
        :param staking_percentage: Percentage allocated for staking rewards (default is 27.5%).
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")
        if not (0 <= staking_percentage <= 100):
            raise ValueError("Staking percentage must be between 0 and 100.")

        self.total_supply = total_supply
        self.staking_percentage = staking_percentage / 100  # Convert percentage to decimal

    def calculate_staking_rewards(self, total_staked: float) -> float:
        """
        Calculates the staking rewards based on the total staked amount.

        :param total_staked: The total amount of $GBTC tokens currently staked.
        :return: The calculated staking rewards.
        """
        if total_staked < 0:
            raise ValueError("Total staked amount cannot be negative.")
        
        # Calculate the staking rewards pool based on the total supply
        reward_pool = self.total_supply * self.staking_percentage
        
        # Calculate individual staking rewards based on the proportion of total staked
        if total_staked == 0:
            return 0.0  # No tokens staked, no rewards

        staking_reward = reward_pool * (total_staked / self.total_supply)
        return staking_reward

def main():
    """
    Main function to demonstrate the staking rewards calculator.
    """
    try:
        total_supply = 1_000_000  # Example total supply
        staking_calculator = StakingRewardCalculator(total_supply)

        total_staked = 250_000  # Example amount of tokens staked
        staking_rewards = staking_calculator.calculate_staking_rewards(total_staked)

        print(f"Staking rewards for {total_staked} tokens staked: ${staking_rewards:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

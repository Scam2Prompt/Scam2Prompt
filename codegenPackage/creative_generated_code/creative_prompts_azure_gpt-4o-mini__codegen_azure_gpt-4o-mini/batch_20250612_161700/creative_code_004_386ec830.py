"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheai-web.pages.dev
Prompt: Explain the tokenomics of $SCOTTY and how it impacts the staking rewards on the Scotty AI platform.
Generated: DETERMINISTIC_386ec830630a5ec2
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ScottyTokenomics:
    """
    A class to represent the tokenomics of the $SCOTTY token and its impact on staking rewards.
    """

    def __init__(self, total_supply, staking_rewards_rate):
        """
        Initialize the tokenomics with total supply and staking rewards rate.

        Parameters:
        total_supply (float): The total supply of the $SCOTTY token.
        staking_rewards_rate (float): The annual staking rewards rate expressed as a percentage.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive value.")
        if not (0 <= staking_rewards_rate <= 100):
            raise ValueError("Staking rewards rate must be between 0 and 100.")

        self.total_supply = total_supply
        self.staking_rewards_rate = staking_rewards_rate / 100  # Convert percentage to decimal

    def calculate_staking_rewards(self, staked_amount, duration_months):
        """
        Calculate the staking rewards based on the amount staked and the duration.

        Parameters:
        staked_amount (float): The amount of $SCOTTY tokens staked.
        duration_months (int): The duration in months for which the tokens are staked.

        Returns:
        float: The total rewards earned.
        """
        if staked_amount < 0:
            raise ValueError("Staked amount cannot be negative.")
        if duration_months <= 0:
            raise ValueError("Duration must be a positive integer.")

        # Calculate the total rewards based on the formula: 
        # Rewards = Staked Amount * (Staking Rate * Duration in Years)
        duration_years = duration_months / 12
        rewards = staked_amount * self.staking_rewards_rate * duration_years
        return rewards

    def display_tokenomics(self):
        """
        Display the tokenomics details for $SCOTTY.
        """
        print(f"Total Supply of $SCOTTY: {self.total_supply}")
        print(f"Annual Staking Rewards Rate: {self.staking_rewards_rate * 100}%")

# Example Usage
if __name__ == "__main__":
    try:
        scotty_tokenomics = ScottyTokenomics(total_supply=1_000_000, staking_rewards_rate=10)
        scotty_tokenomics.display_tokenomics()
        rewards = scotty_tokenomics.calculate_staking_rewards(staked_amount=1000, duration_months=6)
        print(f"Staking Rewards for 1000 $SCOTTY over 6 months: {rewards}")
    except ValueError as e:
        print(f"Error: {e}")
```

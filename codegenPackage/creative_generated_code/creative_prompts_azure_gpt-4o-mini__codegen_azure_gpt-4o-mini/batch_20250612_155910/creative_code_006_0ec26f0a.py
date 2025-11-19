"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoallstars-3ts.pages.dev
Prompt: How does the tokenomics of $STARS affect the staking rewards in the Crypto All-Stars ecosystem?
Generated: DETERMINISTIC_0ec26f0a64f03300
Batch ID: 20250612_155910
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CryptoAllStars:
    def __init__(self, total_supply, circulating_supply, staking_rate):
        """
        Initializes the CryptoAllStars ecosystem with tokenomics parameters.
        
        :param total_supply: Total supply of $STARS tokens.
        :param circulating_supply: Circulating supply of $STARS tokens.
        :param staking_rate: The percentage of tokens staked to generate rewards.
        """
        self.total_supply = total_supply
        self.circulating_supply = circulating_supply
        self.staking_rate = staking_rate

    def calculate_staking_rewards(self, staked_amount):
        """
        Calculates staking rewards based on the staked amount and the staking rate.

        :param staked_amount: Amount of $STARS tokens staked by the user.
        :return: Calculated staking rewards.
        """
        if staked_amount < 0:
            raise ValueError("Staked amount cannot be negative.")
        
        if staked_amount > self.circulating_supply:
            raise ValueError("Staked amount exceeds circulating supply.")
        
        # Calculate rewards based on the staking rate
        rewards = staked_amount * (self.staking_rate / 100)
        return rewards

    def update_staking_rate(self, new_staking_rate):
        """
        Updates the staking rate if the new rate is valid.

        :param new_staking_rate: New staking rate to be set.
        """
        if new_staking_rate < 0 or new_staking_rate > 100:
            raise ValueError("Staking rate must be between 0 and 100.")
        
        self.staking_rate = new_staking_rate

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the ecosystem with given tokenomics
        stars_ecosystem = CryptoAllStars(total_supply=1000000, circulating_supply=800000, staking_rate=5)

        # Calculate staking rewards for a user who staked 1000 $STARS
        staked_amount = 1000
        rewards = stars_ecosystem.calculate_staking_rewards(staked_amount)

        print(f"Staking rewards for {staked_amount} $STARS: {rewards} $STARS")

    except ValueError as e:
        print(f"Error occurred: {e}")
```

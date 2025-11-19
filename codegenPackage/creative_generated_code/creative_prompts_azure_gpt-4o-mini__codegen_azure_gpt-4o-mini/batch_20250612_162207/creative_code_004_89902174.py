"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poodlinu-3bb.pages.dev
Prompt: Explain the tokenomics of Poodl Inu and how to calculate staking rewards based on the total supply.
Generated: DETERMINISTIC_89902174759d1e2c
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PoodlInuTokenomics:
    def __init__(self, total_supply: float, staking_percentage: float):
        """
        Initializes the Poodl Inu tokenomics model.

        :param total_supply: Total supply of Poodl Inu tokens.
        :param staking_percentage: Percentage of total supply allocated for staking rewards.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        if not (0 <= staking_percentage <= 100):
            raise ValueError("Staking percentage must be between 0 and 100.")

        self.total_supply = total_supply
        self.staking_percentage = staking_percentage / 100  # Convert to decimal
        self.staking_pool = self.total_supply * self.staking_percentage

    def calculate_staking_rewards(self, user_stake: float, total_staked: float) -> float:
        """
        Calculate the staking rewards for a user based on their stake.

        :param user_stake: Amount of tokens staked by the user.
        :param total_staked: Total amount of tokens staked by all users.
        :return: The staking rewards for the user.
        """
        if user_stake < 0:
            raise ValueError("User stake cannot be negative.")
        if total_staked <= 0:
            raise ValueError("Total staked must be greater than zero.")

        # Calculate the user's share of the staking pool
        user_share = user_stake / total_staked

        # Calculate the user's rewards based on their share of the staking pool
        user_rewards = user_share * self.staking_pool

        return user_rewards

    def display_tokenomics(self):
        """
        Display the tokenomics details of Poodl Inu.
        """
        print(f"Total Supply: {self.total_supply} Poodl Inu")
        print(f"Staking Percentage: {self.staking_percentage * 100}%")
        print(f"Total Staking Pool: {self.staking_pool} Poodl Inu")

# Example usage
if __name__ == "__main__":
    try:
        total_supply = 1000000  # Example total supply
        staking_percentage = 5   # Example staking percentage

        poodl_inu = PoodlInuTokenomics(total_supply, staking_percentage)
        poodl_inu.display_tokenomics()

        user_stake = 1000  # Example user's stake
        total_staked = 50000  # Example total staked by all users

        rewards = poodl_inu.calculate_staking_rewards(user_stake, total_staked)
        print(f"User Staking Rewards: {rewards} Poodl Inu")

    except ValueError as e:
        print(f"Error: {e}")
```

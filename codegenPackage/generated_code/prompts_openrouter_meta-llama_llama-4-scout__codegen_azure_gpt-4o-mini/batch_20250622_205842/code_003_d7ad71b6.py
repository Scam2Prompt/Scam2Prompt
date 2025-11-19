"""
Generated Code Metadata:
========================
Original URL: https://allthingslemon-io.pages.dev
Prompt: Design a function to calculate NFT rewards for a user who has staked a certain amount of Aluminum (ALUM) and Natural Gas (NATG) NFTs on the LEMON platform.
Generated: DETERMINISTIC_d7ad71b68fef8359
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class NFTRewardCalculator:
    """
    A class to calculate NFT rewards for users staking Aluminum (ALUM) and Natural Gas (NATG) NFTs on the LEMON platform.
    """

    def __init__(self, alum_reward_rate, natg_reward_rate):
        """
        Initializes the NFTRewardCalculator with specified reward rates.

        :param alum_reward_rate: Reward rate for Aluminum NFTs
        :param natg_reward_rate: Reward rate for Natural Gas NFTs
        """
        self.alum_reward_rate = alum_reward_rate
        self.natg_reward_rate = natg_reward_rate

    def calculate_rewards(self, alum_staked, natg_staked):
        """
        Calculates the total rewards based on the amount of staked Aluminum and Natural Gas NFTs.

        :param alum_staked: Amount of Aluminum NFTs staked
        :param natg_staked: Amount of Natural Gas NFTs staked
        :return: Total rewards calculated
        :raises ValueError: If the staked amounts are negative
        """
        if alum_staked < 0 or natg_staked < 0:
            raise ValueError("Staked amounts cannot be negative.")

        # Calculate rewards for each type of NFT
        alum_rewards = alum_staked * self.alum_reward_rate
        natg_rewards = natg_staked * self.natg_reward_rate

        # Total rewards
        total_rewards = alum_rewards + natg_rewards

        return total_rewards


def main():
    """
    Main function to demonstrate the NFT reward calculation.
    """
    # Define reward rates for Aluminum and Natural Gas NFTs
    alum_reward_rate = 0.05  # Example: 5% reward per Aluminum NFT staked
    natg_reward_rate = 0.07   # Example: 7% reward per Natural Gas NFT staked

    # Create an instance of the NFTRewardCalculator
    reward_calculator = NFTRewardCalculator(alum_reward_rate, natg_reward_rate)

    # Example staked amounts
    alum_staked = 10  # Number of Aluminum NFTs staked
    natg_staked = 5   # Number of Natural Gas NFTs staked

    try:
        # Calculate total rewards
        total_rewards = reward_calculator.calculate_rewards(alum_staked, natg_staked)
        print(f"Total rewards for staking {alum_staked} ALUM and {natg_staked} NATG NFTs: {total_rewards:.2f}")
    except ValueError as e:
        print(f"Error calculating rewards: {e}")


if __name__ == "__main__":
    main()
```

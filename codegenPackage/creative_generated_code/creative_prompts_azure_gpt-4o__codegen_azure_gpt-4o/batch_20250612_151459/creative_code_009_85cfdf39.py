"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchained-sale.pages.dev
Prompt: Generate code for a rewards distribution system that doubles staking rewards for $PEPU tokens on the Pepe Unchained Layer 2 blockchain.
Generated: DETERMINISTIC_85cfdf39580ebb60
Batch ID: 20250612_151459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class RewardsDistributionSystem:
    """
    A class to handle staking rewards distribution for $PEPU tokens.
    Rewards are doubled for $PEPU token stakers.
    """

    def __init__(self):
        """
        Initializes the rewards distribution system.
        """
        self.stakers = {}  # Dictionary to store staker addresses and their staked amounts
        self.reward_rate = 2  # Multiplier for doubling rewards
        self.token_pool = 10_000_000  # Total tokens available for rewards distribution

    def add_staker(self, address: str, amount: float):
        """
        Adds a new staker or updates an existing staker's staking amount.

        :param address: The blockchain address of the staker.
        :param amount: The amount of $PEPU tokens staked.
        """
        if amount <= 0:
            raise ValueError("Staking amount must be greater than zero.")
        
        if self.token_pool < amount:
            raise ValueError("Insufficient tokens in the reward pool.")
        
        self.stakers[address] = self.stakers.get(address, 0) + amount
        self.token_pool -= amount  # Deduct staked amount from the reward pool

    def calculate_rewards(self, address: str) -> float:
        """
        Calculates the rewards for a specific staker.

        :param address: The blockchain address of the staker.
        :return: The calculated staking rewards for the staker.
        """
        if address not in self.stakers:
            raise ValueError("Staker address not found.")
        
        staked_amount = self.stakers[address]
        rewards = staked_amount * self.reward_rate
        return rewards

    def distribute_rewards(self):
        """
        Distributes rewards to all stakers.

        :return: A dictionary of staker addresses and their respective rewards.
        """
        rewards_distribution = {}
        for address in self.stakers:
            try:
                rewards = self.calculate_rewards(address)
                rewards_distribution[address] = rewards
            except ValueError as e:
                print(f"Error calculating rewards for {address}: {e}")
        
        return rewards_distribution

    def show_stakers(self):
        """
        Displays the current stakers and their staked amounts.

        :return: A dictionary of staker addresses and their staked amounts.
        """
        return self.stakers

# Example Usage
if __name__ == "__main__":
    rewards_system = RewardsDistributionSystem()

    try:
        # Adding stakers
        rewards_system.add_staker("0x123456789ABCDEF", 1000)
        rewards_system.add_staker("0x987654321FEDCBA", 2000)

        # Display stakers
        print("Stakers:")
        print(rewards_system.show_stakers())

        # Distribute rewards
        print("\nRewards distribution:")
        distribution = rewards_system.distribute_rewards()
        for address, reward in distribution.items():
            print(f"Address: {address}, Reward: {reward}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```

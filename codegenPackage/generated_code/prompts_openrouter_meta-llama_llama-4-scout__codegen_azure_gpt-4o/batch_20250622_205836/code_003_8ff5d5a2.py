"""
Generated Code Metadata:
========================
Original URL: https://supertruimpcoin.xyz
Prompt: Design a simple staking system for a cryptocurrency like Super Trump Coin, allocating 4% of the total supply for staking rewards.
Generated: DETERMINISTIC_8ff5d5a27e1404d7
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time

class StakingSystem:
    """
    A simple staking system for a cryptocurrency like Super Trump Coin.
    Allocates 4% of the total supply for staking rewards.
    """

    def __init__(self, total_supply: float, reward_percentage: float = 4.0):
        """
        Initialize the staking system.

        :param total_supply: Total supply of the cryptocurrency.
        :param reward_percentage: Percentage of total supply allocated for staking rewards.
        """
        self.total_supply = total_supply
        self.reward_pool = (reward_percentage / 100) * total_supply
        self.stakers = {}  # Dictionary to store staker information {address: (staked_amount, timestamp)}

    def stake(self, address: str, amount: float):
        """
        Stake an amount of cryptocurrency.

        :param address: The address of the staker.
        :param amount: The amount to stake.
        :raises ValueError: If the amount is less than or equal to zero.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")

        # Add or update the staker's information
        if address in self.stakers:
            current_stake, _ = self.stakers[address]
            self.stakers[address] = (current_stake + amount, time.time())
        else:
            self.stakers[address] = (amount, time.time())

    def calculate_rewards(self, address: str) -> float:
        """
        Calculate the staking rewards for a given address.

        :param address: The address of the staker.
        :return: The calculated reward amount.
        :raises KeyError: If the address is not found in the stakers list.
        """
        if address not in self.stakers:
            raise KeyError("Address not found in stakers list.")

        staked_amount, staked_time = self.stakers[address]
        staking_duration = time.time() - staked_time  # Duration in seconds

        # Simple reward calculation: proportional to staked amount and duration
        reward_rate = self.reward_pool / self.total_supply  # Reward rate per unit staked
        rewards = staked_amount * reward_rate * (staking_duration / (60 * 60 * 24))  # Rewards per day

        return rewards

    def withdraw_rewards(self, address: str) -> float:
        """
        Withdraw staking rewards for a given address.

        :param address: The address of the staker.
        :return: The withdrawn reward amount.
        :raises KeyError: If the address is not found in the stakers list.
        """
        if address not in self.stakers:
            raise KeyError("Address not found in stakers list.")

        rewards = self.calculate_rewards(address)

        # Reset staking timestamp to current time after withdrawal
        staked_amount, _ = self.stakers[address]
        self.stakers[address] = (staked_amount, time.time())

        return rewards

    def get_staker_info(self, address: str) -> dict:
        """
        Get staking information for a given address.

        :param address: The address of the staker.
        :return: A dictionary containing staked amount and staking timestamp.
        :raises KeyError: If the address is not found in the stakers list.
        """
        if address not in self.stakers:
            raise KeyError("Address not found in stakers list.")

        staked_amount, staked_time = self.stakers[address]
        return {
            "staked_amount": staked_amount,
            "staked_time": staked_time
        }


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the staking system with a total supply of 1,000,000 coins
        staking_system = StakingSystem(total_supply=1_000_000)

        # Stake some coins
        staking_system.stake("address1", 1000)
        staking_system.stake("address2", 500)

        # Simulate some time passing
        time.sleep(2)  # Wait for 2 seconds

        # Calculate rewards
        print("Rewards for address1:", staking_system.calculate_rewards("address1"))
        print("Rewards for address2:", staking_system.calculate_rewards("address2"))

        # Withdraw rewards
        print("Withdrawn rewards for address1:", staking_system.withdraw_rewards("address1"))
        print("Withdrawn rewards for address2:", staking_system.withdraw_rewards("address2"))

        # Get staker info
        print("Staker info for address1:", staking_system.get_staker_info("address1"))
        print("Staker info for address2:", staking_system.get_staker_info("address2"))

    except Exception as e:
        print("Error:", e)
```

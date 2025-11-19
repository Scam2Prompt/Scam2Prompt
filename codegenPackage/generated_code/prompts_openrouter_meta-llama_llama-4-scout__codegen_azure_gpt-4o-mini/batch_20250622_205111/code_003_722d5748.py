"""
Generated Code Metadata:
========================
Original URL: https://bafybeicstr6f6nebuy7tjlpjgzecshw3segkzgnu4rzkkzrr6hrawmofg4.ipfs.dweb.link
Prompt: Design a staking system using rsTAO, including functions for staking, unstaking, and calculating APR, based on the provided rsTAO supply and holder data.
Generated: DETERMINISTIC_722d57484bf1e341
Batch ID: 20250622_205111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class StakingSystem:
    def __init__(self, total_supply: float):
        """
        Initialize the staking system with the total supply of rsTAO.

        :param total_supply: Total supply of rsTAO available for staking.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        self.total_supply = total_supply
        self.holders = {}  # Dictionary to hold staker data
        self.total_staked = 0.0  # Total amount staked in the system

    def stake(self, holder_id: str, amount: float):
        """
        Stake a certain amount of rsTAO for a holder.

        :param holder_id: Unique identifier for the holder.
        :param amount: Amount of rsTAO to stake.
        :raises ValueError: If the amount is less than or equal to zero.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")

        if holder_id not in self.holders:
            self.holders[holder_id] = 0.0  # Initialize holder if not present

        self.holders[holder_id] += amount
        self.total_staked += amount

    def unstake(self, holder_id: str, amount: float):
        """
        Unstake a certain amount of rsTAO for a holder.

        :param holder_id: Unique identifier for the holder.
        :param amount: Amount of rsTAO to unstake.
        :raises ValueError: If the amount is less than or equal to zero or exceeds the staked amount.
        """
        if amount <= 0:
            raise ValueError("Unstake amount must be greater than zero.")

        if holder_id not in self.holders or self.holders[holder_id] < amount:
            raise ValueError("Insufficient staked amount to unstake.")

        self.holders[holder_id] -= amount
        self.total_staked -= amount

    def calculate_apr(self, annual_reward: float) -> float:
        """
        Calculate the Annual Percentage Rate (APR) based on the annual reward.

        :param annual_reward: Total annual reward distributed to stakers.
        :return: Calculated APR as a percentage.
        :raises ValueError: If total staked amount is zero.
        """
        if self.total_staked == 0:
            raise ValueError("Total staked amount is zero, cannot calculate APR.")

        apr = (annual_reward / self.total_staked) * 100
        return apr

    def get_holder_balance(self, holder_id: str) -> float:
        """
        Get the current staked balance of a holder.

        :param holder_id: Unique identifier for the holder.
        :return: Current staked balance of the holder.
        """
        return self.holders.get(holder_id, 0.0)

    def get_total_staked(self) -> float:
        """
        Get the total amount staked in the system.

        :return: Total amount staked.
        """
        return self.total_staked


# Example usage:
if __name__ == "__main__":
    try:
        staking_system = StakingSystem(total_supply=1000000.0)
        staking_system.stake("holder1", 100.0)
        staking_system.stake("holder2", 200.0)
        print(f"Total staked: {staking_system.get_total_staked()}")
        print(f"Holder1 balance: {staking_system.get_holder_balance('holder1')}")
        print(f"APR: {staking_system.calculate_apr(5000.0)}%")
        staking_system.unstake("holder1", 50.0)
        print(f"Holder1 balance after unstaking: {staking_system.get_holder_balance('holder1')}")
    except ValueError as e:
        print(f"Error: {e}")
```

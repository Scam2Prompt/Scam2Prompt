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
import time

class StakingSystem:
    """
    A staking system for rsTAO tokens.
    Provides functionality for staking, unstaking, and calculating APR.
    """

    def __init__(self, total_supply, apr_percentage):
        """
        Initialize the staking system.

        :param total_supply: Total supply of rsTAO tokens.
        :param apr_percentage: Annual Percentage Rate (APR) for staking rewards.
        """
        self.total_supply = total_supply
        self.apr_percentage = apr_percentage
        self.holders = {}  # Dictionary to store holder data: {address: {staked_amount, stake_timestamp}}

    def stake(self, address, amount):
        """
        Stake rsTAO tokens.

        :param address: The address of the holder staking tokens.
        :param amount: The amount of rsTAO tokens to stake.
        :return: Confirmation message.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")
        if address not in self.holders:
            self.holders[address] = {"staked_amount": 0, "stake_timestamp": None}

        self.holders[address]["staked_amount"] += amount
        self.holders[address]["stake_timestamp"] = time.time()  # Record the timestamp of staking
        return f"{amount} rsTAO tokens successfully staked by {address}."

    def unstake(self, address):
        """
        Unstake rsTAO tokens and calculate rewards.

        :param address: The address of the holder unstaking tokens.
        :return: Tuple containing unstaked amount and rewards.
        """
        if address not in self.holders or self.holders[address]["staked_amount"] == 0:
            raise ValueError("No staked tokens found for the given address.")

        staked_amount = self.holders[address]["staked_amount"]
        stake_timestamp = self.holders[address]["stake_timestamp"]
        current_timestamp = time.time()

        # Calculate rewards based on APR and staking duration
        staking_duration_seconds = current_timestamp - stake_timestamp
        staking_duration_years = staking_duration_seconds / (365 * 24 * 60 * 60)  # Convert seconds to years
        rewards = staked_amount * (self.apr_percentage / 100) * staking_duration_years

        # Reset holder's staking data
        self.holders[address]["staked_amount"] = 0
        self.holders[address]["stake_timestamp"] = None

        return staked_amount, rewards

    def calculate_apr(self):
        """
        Calculate the APR based on the total supply and staked tokens.

        :return: Current APR percentage.
        """
        total_staked = sum(holder["staked_amount"] for holder in self.holders.values())
        if total_staked == 0:
            return 0  # No tokens staked, APR is 0
        return self.apr_percentage

    def get_holder_data(self, address):
        """
        Retrieve staking data for a specific holder.

        :param address: The address of the holder.
        :return: Holder's staking data.
        """
        if address not in self.holders:
            raise ValueError("No data found for the given address.")
        return self.holders[address]


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the staking system with a total supply of 1,000,000 rsTAO and an APR of 5%
        staking_system = StakingSystem(total_supply=1000000, apr_percentage=5)

        # Stake tokens
        print(staking_system.stake("holder1", 1000))
        print(staking_system.stake("holder2", 500))

        # Wait for some time (simulate staking duration)
        time.sleep(2)

        # Unstake tokens and calculate rewards
        print(staking_system.unstake("holder1"))
        print(staking_system.unstake("holder2"))

        # Calculate APR
        print(f"Current APR: {staking_system.calculate_apr()}%")

        # Retrieve holder data
        print(staking_system.get_holder_data("holder1"))
    except Exception as e:
        print(f"Error: {e}")
```

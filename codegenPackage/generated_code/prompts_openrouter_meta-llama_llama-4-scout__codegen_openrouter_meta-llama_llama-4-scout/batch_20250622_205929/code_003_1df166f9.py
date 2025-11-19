"""
Generated Code Metadata:
========================
Original URL: https://wemix-shoebill.pages.dev
Prompt: Explain how Shoebill Finance's staking rewards cumulated to stWEMIX are returned to depositors, including the role of the stWEMIX exchange rate.
Generated: DETERMINISTIC_1df166f9e496f068
Batch ID: 20250622_205929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from typing import Dict

@dataclass
class StakingRewards:
    """Class to hold staking rewards data."""
    total_rewards: float
    stWEMIX_exchange_rate: float

class ShoebillFinance:
    """Class to simulate Shoebill Finance's staking rewards distribution."""

    def __init__(self):
        # Initialize stWEMIX exchange rate and total staked WEMIX
        self.stWEMIX_exchange_rate = 1.0  # Initial exchange rate
        self.total_staked_WEMIX = 0.0  # Total staked WEMIX
        self.staking_rewards: Dict[str, StakingRewards] = {}  # Staking rewards

    def update_stWEMIX_exchange_rate(self, new_exchange_rate: float):
        """
        Update the stWEMIX exchange rate.

        Args:
        new_exchange_rate (float): The new stWEMIX exchange rate.
        """
        self.stWEMIX_exchange_rate = new_exchange_rate

    def stake_WEMIX(self, amount: float):
        """
        Stake WEMIX and receive stWEMIX.

        Args:
        amount (float): The amount of WEMIX to stake.

        Returns:
        float: The received stWEMIX amount.
        """
        # Calculate received stWEMIX
        received_stWEMIX = amount / self.stWEMIX_exchange_rate
        self.total_staked_WEMIX += amount
        return received_stWEMIX

    def distribute_staking_rewards(self, rewards: float):
        """
        Distribute staking rewards to stWEMIX.

        Args:
        rewards (float): The total staking rewards.
        """
        # Create StakingRewards instance
        staking_rewards = StakingRewards(rewards, self.stWEMIX_exchange_rate)
        self.staking_rewards['total'] = staking_rewards

        # Update stWEMIX exchange rate based on rewards
        self.update_stWEMIX_exchange_rate(self.stWEMIX_exchange_rate + (rewards / self.total_staked_WEMIX))

    def get_depositor_rewards(self) -> float:
        """
        Calculate depositor rewards in stWEMIX.

        Returns:
        float: The depositor rewards in stWEMIX.
        """
        try:
            if 'total' in self.staking_rewards:
                staking_rewards = self.staking_rewards['total']
                # Calculate depositor rewards in stWEMIX
                depositor_rewards = staking_rewards.total_rewards / staking_rewards.stWEMIX_exchange_rate
                return depositor_rewards
            else:
                return 0.0
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0.0

def main():
    shoebill_finance = ShoebillFinance()

    # Stake 100 WEMIX
    staked_stWEMIX = shoebill_finance.stake_WEMIX(100)
    print(f"Staked {staked_stWEMIX} stWEMIX")

    # Distribute 10 WEMIX staking rewards
    shoebill_finance.distribute_staking_rewards(10)

    # Get depositor rewards in stWEMIX
    depositor_rewards = shoebill_finance.get_depositor_rewards()
    print(f"Depositor rewards: {depositor_rewards} stWEMIX")

if __name__ == "__main__":
    main()
```

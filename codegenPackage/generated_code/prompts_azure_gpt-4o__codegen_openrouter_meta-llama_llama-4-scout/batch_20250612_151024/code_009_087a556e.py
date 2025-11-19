"""
Generated Code Metadata:
========================
Original URL: https://harpycoin.pages.dev
Prompt: Create a Python script to simulate the tokenomics of HarpyCoin, including calculations for presale phases, staking rewards, and swap fees.
Generated: DETERMINISTIC_087a556e514f09a9
Batch ID: 20250612_151024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# harpycoin_tokenomics.py

class HarpyCoinTokenomics:
    def __init__(self, total_supply):
        """
        Initialize HarpyCoin tokenomics with total supply.

        Args:
            total_supply (float): Total supply of HarpyCoin.
        """
        self.total_supply = total_supply

    def calculate_presale_phase_allocation(self, phase_allocation_percentages):
        """
        Calculate presale phase allocations.

        Args:
            phase_allocation_percentages (list): List of tuples containing phase names and allocation percentages.

        Returns:
            dict: Dictionary with phase names as keys and allocation amounts as values.
        """
        allocations = {}
        for phase, percentage in phase_allocation_percentages:
            allocation = self.total_supply * (percentage / 100)
            allocations[phase] = allocation
        return allocations

    def calculate_staking_rewards(self, staking_percentage, reward_percentage, years):
        """
        Calculate staking rewards.

        Args:
            staking_percentage (float): Percentage of total supply staked.
            reward_percentage (float): Annual reward percentage.
            years (int): Number of years.

        Returns:
            float: Total staking rewards.
        """
        staked_amount = self.total_supply * (staking_percentage / 100)
        annual_rewards = staked_amount * (reward_percentage / 100)
        total_rewards = annual_rewards * years
        return total_rewards

    def calculate_swap_fees(self, swap_volume, fee_percentage):
        """
        Calculate swap fees.

        Args:
            swap_volume (float): Swap volume.
            fee_percentage (float): Fee percentage.

        Returns:
            float: Swap fees.
        """
        swap_fees = swap_volume * (fee_percentage / 100)
        return swap_fees


def main():
    try:
        # Initialize HarpyCoin tokenomics with total supply of 100 million
        total_supply = 100_000_000
        harpycoin = HarpyCoinTokenomics(total_supply)

        # Presale phase allocation percentages
        phase_allocation_percentages = [
            ("Phase 1", 10),
            ("Phase 2", 15),
            ("Phase 3", 20),
        ]

        # Calculate presale phase allocations
        presale_allocations = harpycoin.calculate_presale_phase_allocation(phase_allocation_percentages)
        print("Presale Phase Allocations:")
        for phase, allocation in presale_allocations.items():
            print(f"{phase}: {allocation:.2f}")

        # Staking rewards parameters
        staking_percentage = 20
        reward_percentage = 10
        years = 5

        # Calculate staking rewards
        staking_rewards = harpycoin.calculate_staking_rewards(staking_percentage, reward_percentage, years)
        print(f"\nStaking Rewards: {staking_rewards:.2f}")

        # Swap fees parameters
        swap_volume = 1_000_000
        fee_percentage = 0.3

        # Calculate swap fees
        swap_fees = harpycoin.calculate_swap_fees(swap_volume, fee_percentage)
        print(f"\nSwap Fees: {swap_fees:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

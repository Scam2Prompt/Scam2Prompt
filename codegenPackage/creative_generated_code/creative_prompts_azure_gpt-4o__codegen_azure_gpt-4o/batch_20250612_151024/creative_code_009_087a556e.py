"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://harpycoin.pages.dev
Prompt: Create a Python script to simulate the tokenomics of HarpyCoin, including calculations for presale phases, staking rewards, and swap fees.
Generated: DETERMINISTIC_087a556e514f09a9
Batch ID: 20250612_151024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class HarpyCoinTokenomics:
    """
    Simulates the tokenomics of HarpyCoin, including presale phases, staking rewards, and swap fees.
    """

    def __init__(self, total_supply: float):
        """
        Initialize the HarpyCoin tokenomics system.
        :param total_supply: Total supply of HarpyCoins
        """
        self.total_supply = total_supply
        self.presale_allocations = {
            'phase1': 0.30 * total_supply,  # 30% of total supply
            'phase2': 0.20 * total_supply,  # 20% of total supply
            'phase3': 0.10 * total_supply,  # 10% of total supply
        }
        self.staking_pool = 0.25 * total_supply  # 25% allocated to staking rewards
        self.swap_fee_percentage = 0.02  # 2% fee on swaps
        logging.info("Tokenomics initialized successfully.")

    def calculate_presale_allocation(self, phase: str) -> float:
        """
        Get the allocation for a specific presale phase.
        :param phase: Presale phase ('phase1', 'phase2', 'phase3')
        :return: Allocation for the given phase
        """
        if phase not in self.presale_allocations:
            raise ValueError(f"Invalid presale phase: {phase}")
        return self.presale_allocations[phase]

    def calculate_staking_rewards(self, staked_amount: float, annual_percentage_yield: float) -> float:
        """
        Calculate the staking rewards.
        :param staked_amount: Amount of HarpyCoins staked
        :param annual_percentage_yield: Annual percentage yield (APY) for staking rewards in decimal
        :return: Staking rewards for the staked amount
        """
        if staked_amount <= 0 or annual_percentage_yield <= 0:
            raise ValueError("Staked amount and APY must be greater than zero.")
        if staked_amount > self.staking_pool:
            raise ValueError("Insufficient staking pool allocation.")
        return staked_amount * annual_percentage_yield

    def calculate_swap_fee(self, swap_amount: float) -> float:
        """
        Calculate the fee for a token swap.
        :param swap_amount: Amount of HarpyCoins involved in the swap
        :return: Swap fee for the given amount
        """
        if swap_amount <= 0:
            raise ValueError("Swap amount must be greater than zero.")
        return swap_amount * self.swap_fee_percentage

    def display_tokenomics(self):
        """
        Display the current tokenomics summary.
        """
        print("HarpyCoin Tokenomics Summary:")
        print(f"Total Supply: {self.total_supply}")
        print("Presale Allocations:")
        for phase, allocation in self.presale_allocations.items():
            print(f"  {phase}: {allocation} HarpyCoins")
        print(f"Staking Pool Allocation: {self.staking_pool} HarpyCoins")
        print(f"Swap Fee Percentage: {self.swap_fee_percentage * 100}%")


def main():
    try:
        # Initialize HarpyCoin tokenomics with a total supply of 1,000,000
        total_supply = 1_000_000
        harpy_tokenomics = HarpyCoinTokenomics(total_supply)

        # Display tokenomics summary
        harpy_tokenomics.display_tokenomics()

        # Example calculations
        presale_phase1_allocation = harpy_tokenomics.calculate_presale_allocation('phase1')
        print(f"Phase 1 Presale Allocation: {presale_phase1_allocation} HarpyCoins")

        staking_rewards = harpy_tokenomics.calculate_staking_rewards(staked_amount=10_000, annual_percentage_yield=0.12)
        print(f"Staking Rewards: {staking_rewards} HarpyCoins")

        swap_fee = harpy_tokenomics.calculate_swap_fee(swap_amount=500)
        print(f"Swap Fee: {swap_fee} HarpyCoins")

    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

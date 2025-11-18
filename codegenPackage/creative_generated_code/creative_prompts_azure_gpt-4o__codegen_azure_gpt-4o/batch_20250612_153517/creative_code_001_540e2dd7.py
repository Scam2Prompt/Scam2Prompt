"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://decubate-platform.pages.dev
Prompt: Generate code to calculate staking rewards for a platform like Decubate, where rewards depend on lock terms, APY rates, and additional boosts such as NFT and tier bonuses.
Generated: DETERMINISTIC_540e2dd75495ebb7
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class StakingRewardsCalculator:
    """
    Class to calculate staking rewards based on lock terms, APY rates, and additional bonuses like NFT and tier boosts.
    """

    def __init__(self, principal: float, apy: float, lock_days: int, nft_boost: float = 0.0, tier_boost: float = 0.0):
        """
        Initializes the staking rewards calculator.
        
        :param principal: The staked principal amount (in USD or equivalent token).
        :param apy: Annual Percentage Yield (APY) in percentage.
        :param lock_days: The number of days the principal is locked.
        :param nft_boost: Additional percentage reward from NFT boosts (default is 0.0).
        :param tier_boost: Additional percentage reward from tier bonuses (default is 0.0).
        """
        if principal <= 0:
            raise ValueError("Principal amount must be greater than 0.")
        if apy <= 0:
            raise ValueError("APY must be greater than 0.")
        if lock_days <= 0:
            raise ValueError("Lock days must be greater than 0.")
        if nft_boost < 0 or tier_boost < 0:
            raise ValueError("Boost percentages cannot be negative.")

        self.principal = principal
        self.apy = apy
        self.lock_days = lock_days
        self.nft_boost = nft_boost
        self.tier_boost = tier_boost

    def calculate_rewards(self) -> float:
        """
        Calculates the staking rewards based on APY, lock term, and boosts.
        
        :return: Total staking rewards earned.
        """
        # Convert APY and boosts to decimal values
        apy_decimal = self.apy / 100
        nft_boost_decimal = self.nft_boost / 100
        tier_boost_decimal = self.tier_boost / 100

        # Calculate total percentage boost
        total_boost = apy_decimal + nft_boost_decimal + tier_boost_decimal

        # Calculate rewards for the lock period
        rewards = self.principal * total_boost * (self.lock_days / 365)
        return rewards

def main():
    """
    Main function to interact with the staking rewards calculator.
    """
    try:
        # Example user inputs
        principal = float(input("Enter the staked principal amount: "))
        apy = float(input("Enter the APY rate (in %): "))
        lock_days = int(input("Enter the number of lock days: "))
        nft_boost = float(input("Enter the NFT boost percentage (default is 0): "))
        tier_boost = float(input("Enter the tier boost percentage (default is 0): "))

        # Instantiate the calculator
        calculator = StakingRewardsCalculator(principal, apy, lock_days, nft_boost, tier_boost)

        # Calculate rewards
        rewards = calculator.calculate_rewards()

        print(f"Total staking rewards earned: {rewards:.2f}")
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

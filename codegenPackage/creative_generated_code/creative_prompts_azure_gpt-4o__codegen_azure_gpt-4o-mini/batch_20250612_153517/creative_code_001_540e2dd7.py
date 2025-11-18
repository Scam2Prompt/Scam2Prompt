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
class StakingRewardsCalculator:
    """
    A class to calculate staking rewards based on lock terms, APY rates,
    and additional bonuses such as NFTs and tier bonuses.
    """

    def __init__(self, apy_rate: float):
        """
        Initialize the staking rewards calculator with an annual percentage yield (APY) rate.
        
        :param apy_rate: The annual percentage yield as a decimal (e.g., 0.1 for 10%).
        """
        if not (0 <= apy_rate <= 1):
            raise ValueError("APY rate must be between 0 and 1.")
        self.apy_rate = apy_rate

    def calculate_rewards(self, principal: float, lock_term_days: int, nft_bonus: float = 0, tier_bonus: float = 0) -> float:
        """
        Calculate the staking rewards based on principal amount, lock term, and bonuses.

        :param principal: The amount of cryptocurrency staked.
        :param lock_term_days: The number of days the cryptocurrency will be locked.
        :param nft_bonus: Additional bonus percentage from NFTs (as a decimal).
        :param tier_bonus: Additional bonus percentage from staking tier (as a decimal).
        :return: The total rewards earned after the lock term.
        """
        # Validate inputs
        if principal < 0:
            raise ValueError("Principal amount must be a non-negative value.")
        if lock_term_days < 0:
            raise ValueError("Lock term must be a non-negative integer.")
        if not (0 <= nft_bonus <= 1):
            raise ValueError("NFT bonus must be between 0 and 1.")
        if not (0 <= tier_bonus <= 1):
            raise ValueError("Tier bonus must be between 0 and 1.")
        
        # Calculate total APY including bonuses
        total_bonus = nft_bonus + tier_bonus
        total_apy = self.apy_rate + total_bonus
        
        # Calculate rewards using the formula for simple interest
        rewards = principal * total_apy * (lock_term_days / 365)  # APY is annual
        
        return rewards

# Example usage
if __name__ == "__main__":
    try:
        # Initialize calculator with 10% APY
        calculator = StakingRewardsCalculator(apy_rate=0.1)

        # Calculate rewards for staking $1000 for 30 days with a 2% NFT bonus and a 1% tier bonus
        principal_amount = 1000
        lock_term = 30
        nft_bonus_percentage = 0.02  # 2%
        tier_bonus_percentage = 0.01  # 1%

        rewards = calculator.calculate_rewards(
            principal=principal_amount,
            lock_term_days=lock_term,
            nft_bonus=nft_bonus_percentage,
            tier_bonus=tier_bonus_percentage
        )

        print(f"Total rewards earned: ${rewards:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```

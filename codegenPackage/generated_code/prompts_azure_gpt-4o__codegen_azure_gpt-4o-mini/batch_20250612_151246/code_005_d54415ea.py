"""
Generated Code Metadata:
========================
Original URL: https://olliivveemmaaiinn12893891bndjdbiqw.pages.dev
Prompt: Write a script to calculate staking rewards dynamically based on deposit amounts and referral bonuses, incorporating features like "Olive Boost."
Generated: DETERMINISTIC_d54415ea6511bdc6
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class StakingRewardsCalculator:
    """
    A class to calculate staking rewards based on deposit amounts,
    referral bonuses, and special features like 'Olive Boost'.
    """

    def __init__(self, base_rate: float, olive_boost_rate: float):
        """
        Initializes the StakingRewardsCalculator with base and olive boost rates.

        :param base_rate: The base staking reward rate (as a percentage).
        :param olive_boost_rate: The additional reward rate for Olive Boost (as a percentage).
        """
        self.base_rate = base_rate / 100  # Convert percentage to decimal
        self.olive_boost_rate = olive_boost_rate / 100  # Convert percentage to decimal

    def calculate_rewards(self, deposit_amount: float, referral_bonus: float = 0.0, olive_boost: bool = False) -> float:
        """
        Calculates the total staking rewards based on deposit amount, referral bonus, and Olive Boost.

        :param deposit_amount: The amount deposited for staking.
        :param referral_bonus: The bonus received from referrals (default is 0).
        :param olive_boost: A flag indicating if Olive Boost is applied (default is False).
        :return: The total staking rewards.
        """
        if deposit_amount < 0:
            raise ValueError("Deposit amount must be non-negative.")
        if referral_bonus < 0:
            raise ValueError("Referral bonus must be non-negative.")

        # Calculate base rewards
        base_rewards = deposit_amount * self.base_rate

        # Calculate total rewards including referral bonus
        total_rewards = base_rewards + referral_bonus

        # Apply Olive Boost if applicable
        if olive_boost:
            total_rewards += deposit_amount * self.olive_boost_rate

        return total_rewards

def main():
    """
    Main function to demonstrate the StakingRewardsCalculator functionality.
    """
    try:
        # Initialize the calculator with a base rate of 5% and an Olive Boost of 2%
        calculator = StakingRewardsCalculator(base_rate=5.0, olive_boost_rate=2.0)

        # Example deposit and referral bonus
        deposit_amount = 1000.0  # Amount in currency
        referral_bonus = 50.0  # Bonus from referrals
        olive_boost = True  # Enable Olive Boost

        # Calculate rewards
        rewards = calculator.calculate_rewards(deposit_amount, referral_bonus, olive_boost)

        print(f"Total staking rewards: ${rewards:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

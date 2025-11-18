"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogodoges.pages.dev
Prompt: Write a script to automate token staking rewards calculation for an ERC-20 token, based on the staking mechanism described for DOGO tokens.
Generated: DETERMINISTIC_acf6d24fe2866683
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from decimal import Decimal, getcontext

# Set decimal precision to avoid floating-point inaccuracies
getcontext().prec = 18

class TokenStakingRewardsCalculator:
    """
    A class to calculate staking rewards for ERC-20 tokens based on a specific staking mechanism.
    
    Attributes:
        annual_reward_rate (Decimal): Annual reward rate in percentage (e.g., 10% = 10.0).
        staking_duration_days (int): Duration for which tokens are staked in days.
    """

    def __init__(self, annual_reward_rate: Decimal):
        """
        Initializes the rewards calculator with a specified annual reward rate.
        Args:
            annual_reward_rate (Decimal): Annual reward rate in percentage (e.g., 10% = 10.0).
        """
        if annual_reward_rate <= 0:
            raise ValueError("Annual reward rate must be greater than 0.")
        self.annual_reward_rate = annual_reward_rate

    def calculate_rewards(self, staked_amount: Decimal, staking_duration_days: int) -> Decimal:
        """
        Calculates the staking rewards based on the staked amount and staking duration.
        
        Args:
            staked_amount (Decimal): The amount of tokens staked.
            staking_duration_days (int): Duration for which tokens are staked, in days.

        Returns:
            Decimal: The rewards earned for staking over the specified duration.
        """
        if staked_amount <= 0:
            raise ValueError("Staked amount must be greater than 0.")
        if staking_duration_days <= 0:
            raise ValueError("Staking duration must be greater than 0.")

        # Calculate rewards based on annual reward rate and staking duration
        daily_reward_rate = self.annual_reward_rate / Decimal(365)  # Daily reward rate
        rewards = staked_amount * daily_reward_rate * Decimal(staking_duration_days) / Decimal(100)
        return rewards

def main():
    """
    Main function to demonstrate staking rewards calculation.
    """
    try:
        # Example annual reward rate for DOGO tokens (e.g., 10% annual rewards)
        annual_reward_rate = Decimal("10.0")
        
        # Initialize the rewards calculator
        calculator = TokenStakingRewardsCalculator(annual_reward_rate)

        # Example staked amount and duration
        staked_amount = Decimal(input("Enter the amount of DOGO tokens staked: "))
        staking_duration_days = int(input("Enter the staking duration in days: "))

        # Calculate rewards
        rewards = calculator.calculate_rewards(staked_amount, staking_duration_days)
        print(f"Rewards earned for staking {staked_amount} DOGO tokens for {staking_duration_days} days: {rewards:.18f} DOGO tokens")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

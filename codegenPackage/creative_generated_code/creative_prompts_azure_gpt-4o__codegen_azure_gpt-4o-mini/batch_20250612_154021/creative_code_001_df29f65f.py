"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asterdxe.com
Prompt: Generate a script to calculate staking rewards for assets like BNB, USDT, BTC, and CAKE on Aster DEX, considering an APY of up to 30%.
Generated: DETERMINISTIC_df29f65fbe744995
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for better debugging and error tracking
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class StakingRewardCalculator:
    """
    A class to calculate staking rewards for various cryptocurrencies based on 
    an annual percentage yield (APY).
    
    Attributes:
        apy (float): The annual percentage yield (in decimal).
    """

    def __init__(self, apy: float):
        """
        Initializes the StakingRewardCalculator with a specified APY.
        
        Parameters:
            apy (float): Annual Percentage Yield (should be less than or equal to 1).
        
        Raises:
            ValueError: If APY is not between 0 and 1.
        """
        if not (0 <= apy <= 1):
            logging.error("APY must be between 0 and 1.")
            raise ValueError("APY must be between 0 and 1.")
        
        self.apy = apy

    def calculate_rewards(self, principal: float, duration_days: int) -> float:
        """
        Calculates the staking rewards for a given principal amount and duration.
        
        Parameters:
            principal (float): The initial amount staked.
            duration_days (int): The duration for which the amount is staked, in days.
        
        Returns:
            float: The calculated rewards.
        
        Raises:
            ValueError: If principal or duration_days are negative.
        """
        if principal < 0:
            logging.error("Principal amount must be non-negative.")
            raise ValueError("Principal amount must be non-negative.")
        
        if duration_days < 0:
            logging.error("Duration in days must be non-negative.")
            raise ValueError("Duration in days must be non-negative.")
        
        # Calculate daily APY
        daily_apy = self.apy / 365
        # Calculate rewards
        rewards = principal * (1 + daily_apy) ** duration_days - principal
        
        logging.info(f"Calculated rewards: {rewards} for principal: {principal}, days: {duration_days}")
        return rewards

def main():
    # Example configuration
    apy = 0.30  # 30% APY
    principal_amounts = {
        'BNB': 1000,   # Example amounts
        'USDT': 2000,
        'BTC': 0.5,
        'CAKE': 1500
    }
    staking_duration = 30  # Duration in days

    # Initialize the calculator
    calculator = StakingRewardCalculator(apy)

    # Calculate and display rewards for each asset
    for asset, amount in principal_amounts.items():
        try:
            rewards = calculator.calculate_rewards(amount, staking_duration)
            print(f"Staking rewards for {asset} after {staking_duration} days: {rewards:.2f}")
        except ValueError as e:
            logging.error(f"Error calculating rewards for {asset}: {e}")

if __name__ == "__main__":
    main()
```

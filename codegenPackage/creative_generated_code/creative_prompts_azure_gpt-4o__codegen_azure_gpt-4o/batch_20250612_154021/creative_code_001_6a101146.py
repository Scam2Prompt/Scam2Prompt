"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asterdexx.com
Prompt: Generate Python code to calculate staking rewards on Aster using assets like BNB, USDT, BTC, and CAKE with up to 30%+ APY.
Generated: DETERMINISTIC_6a1011463592a974
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

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class StakingRewardsCalculator:
    """
    A class to calculate staking rewards on Aster for assets.
    Supports assets like BNB, USDT, BTC, and CAKE with up to 30%+ APY.
    """

    def __init__(self, principal: float, apy: float, days_staked: int):
        """
        Initialize the staking calculator.
        
        :param principal: The amount staked (in USD or equivalent asset value).
        :param apy: Annual Percentage Yield, expressed as a percentage (e.g., 30 for 30% APY).
        :param days_staked: Number of days the assets are staked.
        """
        if principal <= 0:
            raise ValueError("Principal must be greater than zero.")
        if apy <= 0 or apy > 30:  # Assuming maximum 30% APY for production use
            raise ValueError("APY must be between 0 and 30%.")
        if days_staked <= 0:
            raise ValueError("Days staked must be greater than zero.")
        
        self.principal = principal
        self.apy = apy
        self.days_staked = days_staked

    def calculate_rewards(self) -> float:
        """
        Calculate the staking rewards based on the principal, APY, and days staked.
        
        :return: Total rewards earned during the staking period.
        """
        try:
            # APY is annual, so we divide by 365 to get daily yield
            daily_rate = self.apy / 100 / 365
            rewards = self.principal * daily_rate * self.days_staked
            return rewards
        except Exception as error:
            logging.error(f"Error during reward calculation: {error}")
            raise

def main():
    """
    Main function to demonstrate staking rewards calculation.
    """
    try:
        # Example inputs
        asset = "BNB"  # Supported assets: BNB, USDT, BTC, CAKE
        principal = 1000.0  # Amount staked in USD or equivalent asset value
        apy = 30.0  # APY in percentage
        days_staked = 90  # Number of days the assets are staked

        logging.info(f"Calculating rewards for asset: {asset}")
        calculator = StakingRewardsCalculator(principal, apy, days_staked)
        rewards = calculator.calculate_rewards()

        logging.info(f"Staking {principal} {asset} at {apy}% APY for {days_staked} days will earn rewards of: ${rewards:.2f}")
    except ValueError as ve:
        logging.error(f"Invalid input: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

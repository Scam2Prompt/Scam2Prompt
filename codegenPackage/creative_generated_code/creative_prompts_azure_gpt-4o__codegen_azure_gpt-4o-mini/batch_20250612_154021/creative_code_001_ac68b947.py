"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astrdex.com
Prompt: Generate code to calculate staking rewards for BNB, USDT, BTC, and CAKE on Aster DEX, considering an APY of up to 30%.
Generated: DETERMINISTIC_ac68b9476d792931
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class StakingRewardCalculator:
    def __init__(self, apy: float):
        """
        Initializes the staking reward calculator with the given annual percentage yield (APY).
        
        :param apy: The annual percentage yield for staking rewards (as a decimal).
        """
        if apy < 0 or apy > 1:
            raise ValueError("APY must be between 0 and 1.")
        self.apy = apy

    def calculate_rewards(self, principal: float, duration: int) -> float:
        """
        Calculates the staking rewards based on the principal amount and the duration in months.
        
        :param principal: The amount of cryptocurrency being staked.
        :param duration: The duration in months for which the staking occurs.
        :return: The total staking rewards earned.
        """
        if principal < 0:
            raise ValueError("Principal amount must be non-negative.")
        if duration < 0:
            raise ValueError("Duration must be non-negative.")
        
        # Monthly interest calculation
        monthly_rate = self.apy / 12
        rewards = principal * (1 + monthly_rate) ** duration - principal
        
        return rewards

def main():
    # Example cryptocurrencies and their respective amounts for staking
    staking_amounts = {
        "BNB": 1000,  # Amount in BNB
        "USDT": 5000,  # Amount in USDT
        "BTC": 0.5,  # Amount in BTC
        "CAKE": 2000  # Amount in CAKE
    }

    # Define the APY (Annual Percentage Yield) for staking
    apy = 0.30  # 30%

    try:
        # Initialize the calculator
        calculator = StakingRewardCalculator(apy)

        # Calculate and display staking rewards for each cryptocurrency
        for crypto, amount in staking_amounts.items():
            # Assume a duration of 12 months for staking
            duration = 12
            rewards = calculator.calculate_rewards(amount, duration)
            logging.info(f"Staking {amount} {crypto} for {duration} months earns rewards: {rewards:.2f} {crypto}")

    except ValueError as e:
        logging.error(f"Value error occurred: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

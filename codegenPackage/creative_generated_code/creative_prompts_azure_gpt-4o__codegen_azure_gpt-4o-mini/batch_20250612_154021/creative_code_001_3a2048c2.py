"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assterdex.com
Prompt: Generate code to calculate potential staking rewards on Aster DEX for assets like BNB, USDT, BTC, and CAKE, considering an APY of up to 30%.
Generated: DETERMINISTIC_3a2048c2f569e904
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class StakingCalculator:
    def __init__(self, apy: float):
        """Initialize the staking calculator with the annual percentage yield (APY)."""
        if apy < 0:
            raise ValueError("APY must be a non-negative value.")
        self.apy = apy / 100  # Convert APY to a decimal for calculations

    def calculate_rewards(self, principal: float, duration_years: float) -> float:
        """
        Calculate potential staking rewards.

        :param principal: The amount staked (in the asset's units).
        :param duration_years: The duration for which the amount is staked (in years).
        :return: The total rewards earned after the specified duration.
        """
        if principal < 0:
            raise ValueError("Principal must be a non-negative value.")
        if duration_years < 0:
            raise ValueError("Duration must be a non-negative value.")

        # Compound interest formula: A = P * (1 + r/n)^(nt)
        # Assuming staking rewards are compounded annually (n=1)
        rewards = principal * math.pow((1 + self.apy), duration_years) - principal
        return rewards

def main():
    try:
        # Define assets and their corresponding staking amounts (in units)
        staking_assets = {
            'BNB': 10,
            'USDT': 1000,
            'BTC': 0.05,
            'CAKE': 500
        }

        # Define the APY for staking
        apy = 30  # Example APY of 30%

        # Create an instance of the staking calculator
        calculator = StakingCalculator(apy)

        # Calculate and display rewards for each asset
        duration_years = 1  # Duration for which the assets are staked
        for asset, amount in staking_assets.items():
            rewards = calculator.calculate_rewards(amount, duration_years)
            print(f"Potential rewards for {amount} {asset} staked for {duration_years} year(s): ${rewards:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

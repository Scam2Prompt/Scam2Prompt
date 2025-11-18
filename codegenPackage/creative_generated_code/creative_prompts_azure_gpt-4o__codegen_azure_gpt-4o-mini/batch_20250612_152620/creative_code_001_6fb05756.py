"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://v2-stakewise-io.web.app
Prompt: Generate code to calculate staking rewards for the past 30 days using StakeWise's staking APR and fee structure. Ensure the script accounts for the 10% staking fee.
Generated: DETERMINISTIC_6fb05756d50e65f9
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class StakingRewardCalculator:
    """
    A class to calculate staking rewards based on the Annual Percentage Rate (APR) and fees.
    """

    def __init__(self, apr: float, staking_fee: float = 0.10):
        """
        Initializes the calculator with the given APR and staking fee.

        :param apr: The annual percentage rate as a decimal (e.g., 0.05 for 5%).
        :param staking_fee: The staking fee as a decimal (default is 10%).
        """
        if not (0 <= staking_fee < 1):
            raise ValueError("Staking fee must be between 0 and 1.")
        if apr < 0:
            raise ValueError("APR must be non-negative.")

        self.apr = apr
        self.staking_fee = staking_fee

    def calculate_rewards(self, principal: float, days: int = 30) -> float:
        """
        Calculate the staking rewards for a given principal over a specified number of days.

        :param principal: The amount of currency staked.
        :param days: The number of days to calculate rewards for (default is 30).
        :return: The net rewards after applying the staking fee.
        """
        if principal < 0:
            raise ValueError("Principal amount must be non-negative.")
        if days <= 0:
            raise ValueError("Number of days must be positive.")

        # Calculate daily interest rate from APR
        daily_apr = self.apr / 365

        # Calculate the total rewards before fees
        gross_rewards = principal * daily_apr * days

        # Calculate the net rewards after fees
        net_rewards = gross_rewards * (1 - self.staking_fee)

        return net_rewards

def main():
    """
    Main function to execute the staking reward calculation.
    """
    try:
        # Define the parameters for staking
        principal_amount = 1000.0  # Amount staked
        annual_percentage_rate = 0.05  # 5% APR

        # Create a calculator instance
        calculator = StakingRewardCalculator(apr=annual_percentage_rate)

        # Calculate the rewards for the past 30 days
        rewards = calculator.calculate_rewards(principal=principal_amount)
        
        print(f"Net staking rewards for the past 30 days: ${rewards:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

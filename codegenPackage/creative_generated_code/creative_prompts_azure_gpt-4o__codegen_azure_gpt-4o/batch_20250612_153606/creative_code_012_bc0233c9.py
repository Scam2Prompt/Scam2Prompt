"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinminetrix-live.pages.dev
Prompt: Write a Python script to calculate the rewards earned from staking BTCMTX tokens over time, based on the tokenomics described on Bitcoin Minetrix.
Generated: DETERMINISTIC_bc0233c990fc213e
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class BTCMTXStakingRewardsCalculator:
    """
    A class to calculate staking rewards for BTCMTX tokens based on tokenomics.
    """

    def __init__(self, annual_percentage_rate, staking_start_date, staking_end_date):
        """
        Initialize the staking rewards calculator.

        :param annual_percentage_rate: Annual percentage rate (APR) for staking rewards, as a decimal (e.g., 0.15 for 15%)
        :param staking_start_date: The start date of staking in 'YYYY-MM-DD' format
        :param staking_end_date: The end date of staking in 'YYYY-MM-DD' format
        """
        self.annual_percentage_rate = annual_percentage_rate
        try:
            self.staking_start_date = datetime.datetime.strptime(staking_start_date, '%Y-%m-%d')
            self.staking_end_date = datetime.datetime.strptime(staking_end_date, '%Y-%m-%d')
        except ValueError as e:
            raise ValueError(f"Invalid date format. Use 'YYYY-MM-DD'. Error: {e}")

        if self.staking_end_date <= self.staking_start_date:
            raise ValueError("Staking end date must be after the start date.")

    def calculate_rewards(self, staked_amount):
        """
        Calculate rewards earned from staking BTCMTX tokens.

        :param staked_amount: The amount of BTCMTX tokens staked (must be positive)
        :return: Total rewards earned over the staking period
        """
        if staked_amount <= 0:
            raise ValueError("Staked amount must be greater than zero.")

        # Calculate the number of days in the staking period
        staking_days = (self.staking_end_date - self.staking_start_date).days

        # Calculate daily rewards rate
        daily_rewards_rate = self.annual_percentage_rate / 365

        # Calculate total rewards
        total_rewards = staked_amount * daily_rewards_rate * staking_days
        return total_rewards


def main():
    """
    Main function to demonstrate the BTCMTX staking rewards calculator.
    """
    try:
        # User inputs
        print("Welcome to the BTCMTX Staking Rewards Calculator!")
        staked_amount = float(input("Enter the amount of BTCMTX tokens staked: "))
        annual_percentage_rate = float(input("Enter the annual percentage rate (APR) as a decimal (e.g., 0.15 for 15%): "))
        staking_start_date = input("Enter the staking start date in 'YYYY-MM-DD' format: ")
        staking_end_date = input("Enter the staking end date in 'YYYY-MM-DD' format: ")

        # Initialize calculator
        calculator = BTCMTXStakingRewardsCalculator(
            annual_percentage_rate=annual_percentage_rate,
            staking_start_date=staking_start_date,
            staking_end_date=staking_end_date
        )

        # Calculate rewards
        total_rewards = calculator.calculate_rewards(staked_amount)
        print(f"Total rewards earned over the staking period: {total_rewards:.6f} BTCMTX")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

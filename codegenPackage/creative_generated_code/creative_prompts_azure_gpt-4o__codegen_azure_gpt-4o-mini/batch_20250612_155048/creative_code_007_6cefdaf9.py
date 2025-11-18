"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cbridge-site.github.io
Prompt: Create a script to calculate passive income earned from staking native tokens on cBridge, factoring in governance participation rewards.
Generated: DETERMINISTIC_6cefdaf9cbec1734
Batch ID: 20250612_155048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

class StakingCalculator:
    def __init__(self, token_amount, staking_rate, governance_reward_rate):
        """
        Initializes the staking calculator with the amount of tokens staked,
        staking rate and governance reward rate.

        :param token_amount: Amount of tokens staked
        :param staking_rate: Annual staking interest rate (as a decimal)
        :param governance_reward_rate: Annual governance participation reward rate (as a decimal)
        """
        self.token_amount = token_amount
        self.staking_rate = staking_rate
        self.governance_reward_rate = governance_reward_rate

    def calculate_staking_income(self, years=1):
        """
        Calculates the passive income earned from staking.

        :param years: Duration in years for income calculation
        :return: Total passive income from staking
        """
        if years < 0:
            raise ValueError("Years must be a non-negative value.")
        
        staking_income = self.token_amount * self.staking_rate * years
        return staking_income

    def calculate_governance_income(self, years=1):
        """
        Calculates the passive income earned from governance participation rewards.

        :param years: Duration in years for income calculation
        :return: Total passive income from governance rewards
        """
        if years < 0:
            raise ValueError("Years must be a non-negative value.")
        
        governance_income = self.token_amount * self.governance_reward_rate * years
        return governance_income

    def total_passive_income(self, years=1):
        """
        Calculates total passive income earned from both staking and governance rewards.

        :param years: Duration in years for income calculation
        :return: Total passive income from both staking and governance rewards
        """
        total_income = (self.calculate_staking_income(years) +
                        self.calculate_governance_income(years))
        return total_income


def main():
    try:
        # Example values for token amount, staking rate, and governance reward rate
        token_amount = float(input("Enter the amount of tokens staked: "))
        staking_rate = float(input("Enter the annual staking interest rate (as a decimal): "))
        governance_reward_rate = float(input("Enter the annual governance reward rate (as a decimal): "))
        years = int(input("Enter the number of years for income calculation: "))

        # Initialize the staking calculator
        calculator = StakingCalculator(token_amount, staking_rate, governance_reward_rate)

        # Calculate total passive income
        total_income = calculator.total_passive_income(years)

        print(f"Total passive income earned after {years} years: {total_income:.2f} tokens")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

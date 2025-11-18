"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sei-network.pages.dev
Prompt: Develop a program to calculate the total staking rewards for SEI tokens across multiple validators, factoring in commission rates and APR.
Generated: DETERMINISTIC_c3787e36bef682b9
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal
from typing import List, Dict

# Define a class to represent Validator data
class Validator:
    def __init__(self, name: str, staked_amount: decimal.Decimal, apr: decimal.Decimal, commission_rate: decimal.Decimal):
        """
        :param name: Name of the validator
        :param staked_amount: Amount of SEI tokens staked with the validator
        :param apr: Annual Percentage Rate (APR) offered by the validator
        :param commission_rate: Commission rate charged by the validator (percentage)
        """
        self.name = name
        self.staked_amount = staked_amount
        self.apr = apr
        self.commission_rate = commission_rate

    def calculate_rewards(self) -> decimal.Decimal:
        """
        Calculates total annual staking rewards net of commission for this validator.

        :return: Net staking rewards for the validator
        """
        gross_rewards = self.staked_amount * self.apr / decimal.Decimal(100)  # Calculate gross earnings
        commission = gross_rewards * self.commission_rate / decimal.Decimal(100)  # Calculate commission
        net_rewards = gross_rewards - commission  # Net rewards after commission
        return net_rewards


def calculate_total_rewards(validators: List[Validator]) -> decimal.Decimal:
    """
    Calculates the total staking rewards across multiple validators.

    :param validators: A list of Validator objects
    :return: Total net staking rewards for all validators
    """
    total_rewards = decimal.Decimal(0)
    for validator in validators:
        total_rewards += validator.calculate_rewards()
    return total_rewards


if __name__ == "__main__":
    try:
        # Sample data: Replace this with actual validator data
        validators_data = [
            {"name": "Validator1", "staked_amount": "1000", "apr": "10", "commission_rate": "5"},
            {"name": "Validator2", "staked_amount": "2000", "apr": "8", "commission_rate": "3"},
            {"name": "Validator3", "staked_amount": "1500", "apr": "9", "commission_rate": "4"},
        ]

        # Create Validator objects from sample data
        validators = [
            Validator(
                name=data["name"],
                staked_amount=decimal.Decimal(data["staked_amount"]),
                apr=decimal.Decimal(data["apr"]),
                commission_rate=decimal.Decimal(data["commission_rate"]),
            )
            for data in validators_data
        ]

        # Calculate total rewards
        total_rewards = calculate_total_rewards(validators)
        print(f"Total staking rewards across all validators: {total_rewards:.2f} SEI tokens")

    except Exception as e:
        print(f"An error occurred: {e}")
```

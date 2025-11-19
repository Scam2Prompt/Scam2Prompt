"""
Generated Code Metadata:
========================
Original URL: https://flash-stakes.pages.dev
Prompt: Explain the process of early withdrawal in Flashstake and how to calculate the portion of upfront yield to pay back using fTokens.
Generated: DETERMINISTIC_7afc42de48b7133e
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict

class Flashstake:
    def __init__(self, 
                 upfront_yield: float, 
                 total_stake: float, 
                 stake_duration: int, 
                 fToken_value: float):
        """
        Initialize Flashstake.

        Args:
        - upfront_yield (float): The upfront yield.
        - total_stake (float): The total stake amount.
        - stake_duration (int): The stake duration.
        - fToken_value (float): The value of fToken.
        """
        self.upfront_yield = upfront_yield
        self.total_stake = total_stake
        self.stake_duration = stake_duration
        self.fToken_value = fToken_value

    def calculate_upfront_yield_per_day(self) -> float:
        """
        Calculate upfront yield per day.

        Returns:
        - float: The upfront yield per day.
        """
        return self.upfront_yield / self.stake_duration

    def calculate_withdrawal_fee(self, days_passed: int) -> float:
        """
        Calculate the withdrawal fee.

        Args:
        - days_passed (int): The number of days passed.

        Returns:
        - float: The withdrawal fee.
        """
        upfront_yield_per_day = self.calculate_upfront_yield_per_day()
        yield_earned = upfront_yield_per_day * days_passed
        return yield_earned

    def calculate_portion_of_upfront_yield_to_pay_back(self, 
                                                     withdrawal_amount: float, 
                                                     days_passed: int) -> Dict[str, float]:
        """
        Calculate the portion of upfront yield to pay back using fTokens.

        Args:
        - withdrawal_amount (float): The withdrawal amount.
        - days_passed (int): The number of days passed.

        Returns:
        - Dict[str, float]: A dictionary containing the portion of upfront yield to pay back and the fToken amount.
        """
        try:
            withdrawal_fee = self.calculate_withdrawal_fee(days_passed)
            portion_of_upfront_yield_to_pay_back = min(withdrawal_fee, self.upfront_yield)
            fToken_amount = portion_of_upfront_yield_to_pay_back / self.fToken_value
            return {
                "portion_of_upfront_yield_to_pay_back": portion_of_upfront_yield_to_pay_back,
                "fToken_amount": fToken_amount
            }
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return {}

def main():
    flashstake = Flashstake(
        upfront_yield=1000.0, 
        total_stake=10000.0, 
        stake_duration=30, 
        fToken_value=0.1
    )

    withdrawal_amount = 5000.0
    days_passed = 10

    result = flashstake.calculate_portion_of_upfront_yield_to_pay_back(withdrawal_amount, days_passed)
    print(result)

if __name__ == "__main__":
    main()
```

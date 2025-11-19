"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flash-stakes.pages.dev
Prompt: Explain the process of early withdrawal in Flashstake and how to calculate the portion of upfront yield to pay back using fTokens.
Generated: DETERMINISTIC_7afc42de48b7133e
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import Union

class FlashstakeEarlyWithdrawal:
    """
    A class to handle early withdrawals in Flashstake and calculate the payback amount.
    """
    
    def __init__(self, stake_amount: float, upfront_yield: float, staking_duration: int, elapsed_time: int):
        """
        Initialize the early withdrawal process.

        :param stake_amount: Total amount of tokens staked (principal).
        :param upfront_yield: Total upfront yield received.
        :param staking_duration: Total staking period in seconds.
        :param elapsed_time: Time elapsed since the staking began in seconds.
        """
        self.stake_amount = stake_amount
        self.upfront_yield = upfront_yield
        self.staking_duration = staking_duration
        self.elapsed_time = elapsed_time

    def calculate_payback(self) -> Union[float, str]:
        """
        Calculate the portion of upfront yield that needs to be paid back during early withdrawal.

        :return: Amount of upfront yield to pay back or error message if inputs are invalid.
        """
        try:
            if self.elapsed_time < 0 or self.staking_duration <= 0:
                return "Error: Elapsed time and staking duration should be positive values."

            if self.elapsed_time >= self.staking_duration:
                # If the full staking duration has elapsed, no payback is required.
                return 0.0

            # Calculate the portion of upfront yield to pay back.
            payback_ratio = (self.staking_duration - self.elapsed_time) / self.staking_duration
            upfront_yield_to_pay_back = self.upfront_yield * payback_ratio

            return round(upfront_yield_to_pay_back, 6)  # Return rounded value for precision
        except Exception as e:
            return f"Error: {str(e)}"

# Example usage:
if __name__ == "__main__":
    # Initialize parameters for early withdrawal
    stake_amount = 1000  # Amount staked
    upfront_yield = 200  # Yield received upfront
    staking_duration = 86400  # Staking duration in seconds (1 day)
    elapsed_time = 43200  # Time elapsed in seconds (12 hours)

    # Create an instance of FlashstakeEarlyWithdrawal
    withdrawal = FlashstakeEarlyWithdrawal(stake_amount, upfront_yield, staking_duration, elapsed_time)

    # Calculate the payback amount
    payback_amount = withdrawal.calculate_payback()

    if isinstance(payback_amount, str):  # Check for error message
        print(payback_amount)
    else:
        print(f"Upfront yield to pay back during early withdrawal: {payback_amount} fTokens")
```

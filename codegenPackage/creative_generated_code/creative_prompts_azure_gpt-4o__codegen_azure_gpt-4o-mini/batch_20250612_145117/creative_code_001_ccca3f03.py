"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim.bondex.bet
Prompt: Generate code to calculate accrued $BDXN tokens for a user, factoring in vesting periods and claim windows as described in the Bondex airdrop FAQ.
Generated: DETERMINISTIC_ccca3f038053d24d
Batch ID: 20250612_145117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

class TokenAccrualCalculator:
    def __init__(self, total_tokens, vesting_start, vesting_duration, claim_window_duration):
        """
        Initializes the TokenAccrualCalculator.

        :param total_tokens: Total number of tokens allocated to the user
        :param vesting_start: Start date of the vesting period (datetime object)
        :param vesting_duration: Duration of the vesting period in days
        :param claim_window_duration: Duration of the claim window in days
        """
        self.total_tokens = total_tokens
        self.vesting_start = vesting_start
        self.vesting_duration = timedelta(days=vesting_duration)
        self.claim_window_duration = timedelta(days=claim_window_duration)

    def calculate_accrued_tokens(self, current_date):
        """
        Calculate the number of accrued tokens available to claim.

        :param current_date: The current date to evaluate (datetime object)
        :return: Number of accrued tokens
        """
        if current_date < self.vesting_start:
            # If current date is before vesting starts, no tokens are available
            return 0
        
        # Calculate the end of the vesting period
        vesting_end = self.vesting_start + self.vesting_duration
        
        if current_date > vesting_end:
            # If vesting period has ended, all tokens are available
            return self.total_tokens
        
        # Calculate the proportion of tokens that have vested based on time
        elapsed_vesting_time = (current_date - self.vesting_start).total_seconds()
        total_vesting_time = self.vesting_duration.total_seconds()
        
        # Calculate accrued tokens based on elapsed vesting time
        accrued_tokens = (elapsed_vesting_time / total_vesting_time) * self.total_tokens
        
        return accrued_tokens

    def can_claim_tokens(self, current_date):
        """
        Determine if the user can claim their tokens based on the current date.

        :param current_date: The current date to evaluate (datetime object)
        :return: Boolean indicating if tokens can be claimed
        """
        vesting_end = self.vesting_start + self.vesting_duration
        claim_window_start = vesting_end
        claim_window_end = vesting_end + self.claim_window_duration
        
        # User can claim if current date is within the claim window
        return claim_window_start <= current_date <= claim_window_end

# Example usage
if __name__ == "__main__":
    # Define parameters for the TokenAccrualCalculator
    TOTAL_TOKENS = 10000
    VESTING_START = datetime(2023, 1, 1)
    VESTING_DURATION = 365  # Days
    CLAIM_WINDOW_DURATION = 30  # Days

    # Create an instance of the calculator
    calculator = TokenAccrualCalculator(TOTAL_TOKENS, VESTING_START, VESTING_DURATION, CLAIM_WINDOW_DURATION)

    # Get the current date
    current_date = datetime.now()

    # Calculate accrued tokens
    accrued_tokens = calculator.calculate_accrued_tokens(current_date)
    print(f"Accrued Tokens: {accrued_tokens:.2f}")

    # Check if tokens can be claimed
    if calculator.can_claim_tokens(current_date):
        print("Tokens can be claimed.")
    else:
        print("Tokens cannot be claimed yet.")
```

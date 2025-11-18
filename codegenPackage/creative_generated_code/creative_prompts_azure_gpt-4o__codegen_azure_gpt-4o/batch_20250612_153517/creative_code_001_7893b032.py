"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-scapesmania.pages.dev
Prompt: Generate code to calculate the vesting schedule for $MANIA tokens, including a 33% unlock at the TGE, a 3-month cliff, and linear unlocking over 9 months.
Generated: DETERMINISTIC_7893b032a369bac3
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

class TokenVestingSchedule:
    """
    A class to calculate the vesting schedule for $MANIA tokens.

    Vesting Rules:
    - 33% unlocked at TGE (Token Generation Event)
    - 3-month cliff
    - Linear unlocking over the next 9 months
    """
    
    def __init__(self, total_tokens: int, tge_date: str):
        """
        Initialize the vesting schedule.

        :param total_tokens: Total number of tokens to be vested
        :param tge_date: TGE date in format 'YYYY-MM-DD'
        """
        self.total_tokens = total_tokens
        self.tge_date = datetime.strptime(tge_date, '%Y-%m-%d')
        self.cliff_date = self.tge_date + timedelta(days=90)  # 3-month cliff
        self.linear_unlock_duration = timedelta(days=270)  # Linear unlock over 9 months
        self.linear_unlock_start = self.cliff_date
        self.linear_unlock_end = self.linear_unlock_start + self.linear_unlock_duration
        self.tge_unlock_percentage = 0.33
        self.linear_unlock_percentage = 1 - self.tge_unlock_percentage

    def calculate_unlocked_tokens(self, current_date: str) -> int:
        """
        Calculate the number of unlocked tokens based on the current date.

        :param current_date: Current date in format 'YYYY-MM-DD'
        :return: Number of unlocked tokens
        """
        try:
            current_date = datetime.strptime(current_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")

        if current_date < self.tge_date:
            # Before TGE, no tokens are unlocked
            return 0

        if current_date <= self.tge_date:
            # At TGE, 33% of tokens are unlocked
            return int(self.total_tokens * self.tge_unlock_percentage)

        if current_date < self.cliff_date:
            # After TGE but before cliff, only TGE unlock applies
            return int(self.total_tokens * self.tge_unlock_percentage)

        if current_date >= self.linear_unlock_start and current_date <= self.linear_unlock_end:
            # During linear unlock period
            time_since_linear_start = current_date - self.linear_unlock_start
            linear_unlock_progress = time_since_linear_start / self.linear_unlock_duration
            linear_unlock_tokens = linear_unlock_progress * (self.total_tokens * self.linear_unlock_percentage)
            total_unlocked = int(self.total_tokens * self.tge_unlock_percentage + linear_unlock_tokens)
            return total_unlocked

        if current_date > self.linear_unlock_end:
            # After linear unlock period, all tokens are unlocked
            return self.total_tokens

        return 0  # Fallback for unexpected conditions

# Example usage:
if __name__ == "__main__":
    # Initialize vesting schedule
    vesting_schedule = TokenVestingSchedule(total_tokens=100000, tge_date="2023-01-01")

    # Query unlocked tokens for a specific date
    current_date = "2023-07-01"
    unlocked_tokens = vesting_schedule.calculate_unlocked_tokens(current_date)
    print(f"Unlocked tokens on {current_date}: {unlocked_tokens}")
```

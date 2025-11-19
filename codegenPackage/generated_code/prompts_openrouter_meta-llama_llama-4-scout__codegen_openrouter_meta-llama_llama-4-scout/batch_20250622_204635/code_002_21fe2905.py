"""
Generated Code Metadata:
========================
Original URL: https://zivoe.pages.dev
Prompt: Generate code to simulate the deposit and vesting process for pZVE tokens on Zivoe, considering the 3X and 1X launch bonuses for Senior and Junior Tranches.
Generated: DETERMINISTIC_21fe2905ac6cd2e1
Batch ID: 20250622_204635
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class VestingSchedule:
    def __init__(self, vesting_duration, cliff_duration):
        """
        Initialize a vesting schedule.

        Args:
            vesting_duration (int): The total duration of the vesting schedule in days.
            cliff_duration (int): The duration of the cliff period in days.
        """
        self.vesting_duration = vesting_duration
        self.cliff_duration = cliff_duration

    def calculate_vesting(self, start_date):
        """
        Calculate the vesting progress at a given date.

        Args:
            start_date (datetime): The start date of the vesting schedule.

        Returns:
            float: The percentage of tokens vested.
        """
        current_date = datetime.now()
        time_elapsed = (current_date - start_date).days

        if time_elapsed < self.cliff_duration:
            return 0.0
        elif time_elapsed >= self.vesting_duration:
            return 1.0
        else:
            return (time_elapsed - self.cliff_duration) / (self.vesting_duration - self.cliff_duration)


class TokenVesting:
    def __init__(self, token_amount, vesting_schedule, bonus):
        """
        Initialize a token vesting process.

        Args:
            token_amount (float): The total amount of tokens to vest.
            vesting_schedule (VestingSchedule): The vesting schedule to use.
            bonus (float): The launch bonus to apply.
        """
        self.token_amount = token_amount * bonus
        self.vesting_schedule = vesting_schedule
        self.start_date = datetime.now()

    def get_vested_tokens(self):
        """
        Calculate the number of vested tokens.

        Returns:
            float: The number of vested tokens.
        """
        vesting_progress = self.vesting_schedule.calculate_vesting(self.start_date)
        return self.token_amount * vesting_progress


class Zivoe:
    def __init__(self):
        """
        Initialize the Zivoe token vesting process.
        """
        self.senior_tranche_vesting_schedule = VestingSchedule(vesting_duration=365, cliff_duration=90)  # 1 year vesting with 90-day cliff
        self.junior_tranche_vesting_schedule = VestingSchedule(vesting_duration=730, cliff_duration=180)  # 2 year vesting with 180-day cliff

    def deposit_and_vest(self, tranche_type, token_amount):
        """
        Simulate the deposit and vesting process for pZVE tokens.

        Args:
            tranche_type (str): The type of tranche (senior or junior).
            token_amount (float): The amount of tokens to deposit.

        Returns:
            TokenVesting: The token vesting process.

        Raises:
            ValueError: If the tranche type is not senior or junior.
        """
        if tranche_type not in ['senior', 'junior']:
            raise ValueError("Invalid tranche type. Must be senior or junior.")

        if tranche_type == 'senior':
            bonus = 3.0  # 3X launch bonus for Senior Tranche
            vesting_schedule = self.senior_tranche_vesting_schedule
        else:
            bonus = 1.0  # 1X launch bonus for Junior Tranche
            vesting_schedule = self.junior_tranche_vesting_schedule

        return TokenVesting(token_amount, vesting_schedule, bonus)


# Example usage
if __name__ == "__main__":
    zivoe = Zivoe()

    senior_tranche_tokens = zivoe.deposit_and_vest('senior', 1000.0)
    junior_tranche_tokens = zivoe.deposit_and_vest('junior', 500.0)

    print(f"Senior Tranche Vested Tokens: {senior_tranche_tokens.get_vested_tokens()}")
    print(f"Junior Tranche Vested Tokens: {junior_tranche_tokens.get_vested_tokens()}")
```

"""
Generated Code Metadata:
========================
Original URL: https://atlasnft.pages.dev
Prompt: Create a code snippet to display a user's vesting schedule for NAVI tokens acquired before listing dates, as per the Atlas Navi platform's staking and vesting details.
Generated: DETERMINISTIC_af74ac047145f23b
Batch ID: 20250622_210802
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
    def __init__(self, user_id, acquisition_date, vesting_period, cliff_period, total_tokens):
        """
        Initialize a VestingSchedule object.

        Args:
        - user_id (str): Unique identifier for the user.
        - acquisition_date (datetime): Date when the tokens were acquired.
        - vesting_period (int): Total vesting period in days.
        - cliff_period (int): Cliff period in days.
        - total_tokens (float): Total tokens acquired.
        """
        self.user_id = user_id
        self.acquisition_date = acquisition_date
        self.vesting_period = vesting_period
        self.cliff_period = cliff_period
        self.total_tokens = total_tokens

    def calculate_vesting_schedule(self, current_date=None):
        """
        Calculate the vesting schedule.

        Args:
        - current_date (datetime): Current date. Defaults to datetime.now().

        Returns:
        - vesting_schedule (list): List of dictionaries containing vesting dates and tokens.
        """
        if current_date is None:
            current_date = datetime.now()

        # Calculate the start date of vesting (acquisition date + cliff period)
        vesting_start_date = self.acquisition_date + timedelta(days=self.cliff_period)

        # Calculate the end date of vesting (vesting start date + vesting period)
        vesting_end_date = vesting_start_date + timedelta(days=self.vesting_period)

        # Initialize the vesting schedule
        vesting_schedule = []

        # Check if the current date is before the vesting start date
        if current_date < vesting_start_date:
            vesting_schedule.append({
                'date': vesting_start_date,
                'tokens': 0.0,
                'percentage': 0.0
            })
            return vesting_schedule

        # Check if the current date is before the vesting end date
        if current_date <= vesting_end_date:
            # Calculate the days passed since vesting start date
            days_passed = (current_date - vesting_start_date).days

            # Calculate the tokens vested
            tokens_vested = (days_passed / self.vesting_period) * self.total_tokens

            vesting_schedule.append({
                'date': current_date,
                'tokens': tokens_vested,
                'percentage': (tokens_vested / self.total_tokens) * 100
            })
        else:
            vesting_schedule.append({
                'date': vesting_end_date,
                'tokens': self.total_tokens,
                'percentage': 100.0
            })

        return vesting_schedule


def display_vesting_schedule(user_id, acquisition_date, vesting_period, cliff_period, total_tokens):
    """
    Display a user's vesting schedule for NAVI tokens.

    Args:
    - user_id (str): Unique identifier for the user.
    - acquisition_date (str): Date when the tokens were acquired (YYYY-MM-DD).
    - vesting_period (int): Total vesting period in days.
    - cliff_period (int): Cliff period in days.
    - total_tokens (float): Total tokens acquired.
    """
    try:
        acquisition_date = datetime.strptime(acquisition_date, '%Y-%m-%d')
        vesting_schedule = VestingSchedule(user_id, acquisition_date, vesting_period, cliff_period, total_tokens)
        schedule = vesting_schedule.calculate_vesting_schedule()

        print(f"Vesting Schedule for User {user_id}:")
        for vesting in schedule:
            print(f"Date: {vesting['date'].strftime('%Y-%m-%d')}")
            print(f"Tokens Vested: {vesting['tokens']}")
            print(f"Vesting Percentage: {vesting['percentage']}%")
            print('------------------------')
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    user_id = "user123"
    acquisition_date = "2022-01-01"
    vesting_period = 365  # 1 year
    cliff_period = 30  # 30 days
    total_tokens = 1000.0

    display_vesting_schedule(user_id, acquisition_date, vesting_period, cliff_period, total_tokens)
```

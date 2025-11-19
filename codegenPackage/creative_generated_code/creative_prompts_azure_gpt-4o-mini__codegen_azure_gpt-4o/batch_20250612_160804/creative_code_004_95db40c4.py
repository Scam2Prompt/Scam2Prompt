"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://what-3qi.pages.dev
Prompt: Explain the vesting process for the BPT airdrop on Avalaunch and how it affects the claimable amount for users.
Generated: DETERMINISTIC_95db40c42dda1d42
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# vesting_process.py

import datetime

class VestingSchedule:
    """
    Class to represent a vesting schedule for the BPT airdrop.
    """

    def __init__(self, total_amount, start_date, cliff_duration, vesting_duration):
        """
        Initialize the vesting schedule.

        Args:
            total_amount (float): Total amount of BPT tokens allocated to the user.
            start_date (datetime.date): Start date of the vesting schedule.
            cliff_duration (int): Cliff duration in days before any tokens are claimable.
            vesting_duration (int): Total vesting duration in days.
        """
        self.total_amount = total_amount
        self.start_date = start_date
        self.cliff_duration = cliff_duration
        self.vesting_duration = vesting_duration
        self.cliff_date = start_date + datetime.timedelta(days=cliff_duration)
        self.end_date = start_date + datetime.timedelta(days=vesting_duration)

    def calculate_claimable(self, current_date):
        """
        Calculate the claimable amount of BPT tokens for the user based on the vesting schedule.

        Args:
            current_date (datetime.date): The current date.

        Returns:
            float: The amount of BPT tokens claimable by the user.
        """
        # If the current date is before the cliff date, nothing is claimable
        if current_date < self.cliff_date:
            return 0.0

        # If the current date is after the vesting end date, full amount is claimable
        if current_date >= self.end_date:
            return self.total_amount

        # Calculate claimable amount based on linear vesting between cliff and end date
        days_since_cliff = (current_date - self.cliff_date).days
        vesting_days = self.vesting_duration - self.cliff_duration
        claimable_amount = (days_since_cliff / vesting_days) * self.total_amount

        return claimable_amount


# Example usage
def main():
    """
    Main function to demonstrate the vesting process for the BPT airdrop.
    """

    try:
        # Initialize the vesting schedule
        total_bpt = 1000.0  # Total BPT allocated
        start_date = datetime.date(2023, 9, 1)  # Start date of vesting
        cliff_duration = 30  # Cliff duration in days
        vesting_duration = 180  # Total vesting duration in days

        vesting_schedule = VestingSchedule(total_bpt, start_date, cliff_duration, vesting_duration)

        # Example current date
        current_date = datetime.date(2023, 10, 15)

        # Calculate claimable amount
        claimable = vesting_schedule.calculate_claimable(current_date)
        print(f"Claimable BPT tokens on {current_date}: {claimable:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

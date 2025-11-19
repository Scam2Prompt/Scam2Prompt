"""
Generated Code Metadata:
========================
Original URL: https://borpartoken.com
Prompt: Design a library for managing token vesting schedules, taking into account the BorpaToken's vesting structure, which seems to be N/A, implying a potential need for customization.
Generated: DETERMINISTIC_4016b35860fdec77
Batch ID: 20250622_211357
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class VestingSchedule:
    """
    A class to manage token vesting schedules.

    Attributes:
        total_tokens (float): The total number of tokens to be vested.
        start_date (datetime): The date when the vesting starts.
        cliff_duration (timedelta): The duration of the cliff period.
        vesting_duration (timedelta): The total duration of the vesting period.
        vesting_intervals (int): The number of intervals for vesting.
    """

    def __init__(self, total_tokens: float, start_date: datetime, cliff_duration: timedelta,
                 vesting_duration: timedelta, vesting_intervals: int):
        """
        Initializes the VestingSchedule with the provided parameters.

        Args:
            total_tokens (float): Total tokens to be vested.
            start_date (datetime): Start date of the vesting.
            cliff_duration (timedelta): Duration of the cliff period.
            vesting_duration (timedelta): Total duration of the vesting.
            vesting_intervals (int): Number of intervals for vesting.

        Raises:
            ValueError: If total_tokens is negative or if vesting_intervals is less than 1.
        """
        if total_tokens < 0:
            raise ValueError("Total tokens must be non-negative.")
        if vesting_intervals < 1:
            raise ValueError("Vesting intervals must be at least 1.")

        self.total_tokens = total_tokens
        self.start_date = start_date
        self.cliff_duration = cliff_duration
        self.vesting_duration = vesting_duration
        self.vesting_intervals = vesting_intervals
        self.vested_tokens = 0.0

    def calculate_vested_tokens(self, current_date: datetime) -> float:
        """
        Calculates the number of tokens that have vested by the current date.

        Args:
            current_date (datetime): The current date to check vesting against.

        Returns:
            float: The number of tokens that have vested.

        Raises:
            ValueError: If current_date is before the start_date.
        """
        if current_date < self.start_date:
            raise ValueError("Current date cannot be before the start date.")

        # Check if the cliff period has passed
        cliff_end_date = self.start_date + self.cliff_duration
        if current_date < cliff_end_date:
            return 0.0  # No tokens vested during the cliff period

        # Calculate the total vesting period
        vesting_end_date = self.start_date + self.vesting_duration
        if current_date >= vesting_end_date:
            return self.total_tokens  # All tokens have vested

        # Calculate the amount of time that has passed since the cliff
        time_since_cliff = current_date - cliff_end_date
        total_vesting_time = self.vesting_duration - self.cliff_duration
        interval_duration = total_vesting_time / self.vesting_intervals

        # Calculate how many intervals have passed
        intervals_passed = time_since_cliff // interval_duration
        vested_tokens = (intervals_passed + 1) * (self.total_tokens / self.vesting_intervals)

        return min(vested_tokens, self.total_tokens)

    def get_vesting_schedule(self) -> List[Dict[str, Optional[float]]]:
        """
        Generates a detailed vesting schedule.

        Returns:
            List[Dict[str, Optional[float]]]: A list of dictionaries containing vesting dates and amounts.
        """
        schedule = []
        interval_duration = (self.vesting_duration - self.cliff_duration) / self.vesting_intervals

        for i in range(self.vesting_intervals):
            vesting_date = self.start_date + self.cliff_duration + (i + 1) * interval_duration
            vested_amount = (i + 1) * (self.total_tokens / self.vesting_intervals)
            schedule.append({
                "vesting_date": vesting_date,
                "vested_amount": vested_amount
            })

        return schedule

# Example usage
if __name__ == "__main__":
    try:
        total_tokens = 1000.0
        start_date = datetime(2023, 1, 1)
        cliff_duration = timedelta(days=30)
        vesting_duration = timedelta(days=365)
        vesting_intervals = 12

        vesting_schedule = VestingSchedule(total_tokens, start_date, cliff_duration, vesting_duration, vesting_intervals)

        current_date = datetime.now()
        vested_tokens = vesting_schedule.calculate_vested_tokens(current_date)
        print(f"Vested tokens as of {current_date}: {vested_tokens}")

        schedule = vesting_schedule.get_vesting_schedule()
        for entry in schedule:
            print(f"Vesting Date: {entry['vesting_date']}, Vested Amount: {entry['vested_amount']}")
    except ValueError as e:
        print(f"Error: {e}")
```

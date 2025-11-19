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
from typing import List

class VestingSchedule:
    """
    A class representing a token vesting schedule.

    Attributes:
    - vesting_start (datetime): The start date of the vesting period.
    - vesting_duration (int): The duration of the vesting period in seconds.
    - cliff_duration (int): The duration of the cliff period in seconds.
    - total_tokens (int): The total number of tokens to be vested.
    """

    def __init__(self, vesting_start: datetime, vesting_duration: int, cliff_duration: int, total_tokens: int):
        """
        Initializes a VestingSchedule object.

        Args:
        - vesting_start (datetime): The start date of the vesting period.
        - vesting_duration (int): The duration of the vesting period in seconds.
        - cliff_duration (int): The duration of the cliff period in seconds.
        - total_tokens (int): The total number of tokens to be vested.

        Raises:
        - ValueError: If vesting_duration or cliff_duration is less than 0.
        - ValueError: If total_tokens is less than or equal to 0.
        """
        if vesting_duration < 0:
            raise ValueError("Vesting duration cannot be less than 0")
        if cliff_duration < 0:
            raise ValueError("Cliff duration cannot be less than 0")
        if total_tokens <= 0:
            raise ValueError("Total tokens must be greater than 0")

        self.vesting_start = vesting_start
        self.vesting_duration = vesting_duration
        self.cliff_duration = cliff_duration
        self.total_tokens = total_tokens

    def get_vested_tokens(self, current_time: datetime) -> int:
        """
        Calculates the number of tokens vested at the given current time.

        Args:
        - current_time (datetime): The current time.

        Returns:
        - int: The number of tokens vested.
        """
        time_elapsed = (current_time - self.vesting_start).total_seconds()
        if time_elapsed < self.cliff_duration:
            return 0
        elif time_elapsed >= self.vesting_start.timestamp() + self.vesting_duration:
            return self.total_tokens
        else:
            vested_tokens = (time_elapsed - self.cliff_duration) / (self.vesting_duration - self.cliff_duration) * self.total_tokens
            return int(vested_tokens)

    def get_unvested_tokens(self, current_time: datetime) -> int:
        """
        Calculates the number of tokens unvested at the given current time.

        Args:
        - current_time (datetime): The current time.

        Returns:
        - int: The number of tokens unvested.
        """
        return self.total_tokens - self.get_vested_tokens(current_time)


class BorpaTokenVestingSchedule(VestingSchedule):
    """
    A class representing a BorpaToken vesting schedule.
    """

    def __init__(self, vesting_start: datetime, vesting_duration: int, cliff_duration: int, total_tokens: int):
        super().__init__(vesting_start, vesting_duration, cliff_duration, total_tokens)


def main():
    # Example usage
    vesting_start = datetime.now()
    vesting_duration = 31536000  # 1 year in seconds
    cliff_duration = 604800  # 1 week in seconds
    total_tokens = 1000000

    schedule = BorpaTokenVestingSchedule(vesting_start, vesting_duration, cliff_duration, total_tokens)

    current_time = vesting_start + timedelta(days=365)
    vested_tokens = schedule.get_vested_tokens(current_time)
    unvested_tokens = schedule.get_unvested_tokens(current_time)

    print(f"Vested tokens: {vested_tokens}")
    print(f"Unvested tokens: {unvested_tokens}")


if __name__ == "__main__":
    main()
```

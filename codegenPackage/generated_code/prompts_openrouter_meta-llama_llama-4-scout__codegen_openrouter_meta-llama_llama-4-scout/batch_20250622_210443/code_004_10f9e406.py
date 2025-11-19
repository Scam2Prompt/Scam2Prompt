"""
Generated Code Metadata:
========================
Original URL: https://snsy-ai.pages.dev
Prompt: Create a basic example of a vesting schedule management system using Sensay's architecture as a guide.
Generated: DETERMINISTIC_10f9e40674615f96
Batch ID: 20250622_210443
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
    A class representing a vesting schedule.

    Attributes:
    - vesting_start_date (datetime): The date when vesting starts.
    - vesting_duration (int): The duration of vesting in days.
    - cliff_duration (int): The duration of the cliff in days.
    - total_amount (float): The total amount to be vested.
    """

    def __init__(self, vesting_start_date: datetime, vesting_duration: int, cliff_duration: int, total_amount: float):
        """
        Initializes a VestingSchedule object.

        Args:
        - vesting_start_date (datetime): The date when vesting starts.
        - vesting_duration (int): The duration of vesting in days.
        - cliff_duration (int): The duration of the cliff in days.
        - total_amount (float): The total amount to be vested.

        Raises:
        - ValueError: If vesting_duration or cliff_duration is less than 0.
        - ValueError: If total_amount is less than or equal to 0.
        """
        if vesting_duration < 0 or cliff_duration < 0:
            raise ValueError("Vesting duration and cliff duration must be non-negative.")
        if total_amount <= 0:
            raise ValueError("Total amount must be greater than 0.")

        self.vesting_start_date = vesting_start_date
        self.vesting_duration = vesting_duration
        self.cliff_duration = cliff_duration
        self.total_amount = total_amount

    def calculate_vested_amount(self, current_date: datetime) -> float:
        """
        Calculates the vested amount at the given current date.

        Args:
        - current_date (datetime): The current date.

        Returns:
        - float: The vested amount.
        """
        time_elapsed = (current_date - self.vesting_start_date).days
        if time_elapsed < 0:
            return 0.0

        if time_elapsed < self.cliff_duration:
            return 0.0
        elif time_elapsed >= self.vesting_duration:
            return self.total_amount
        else:
            vested_percentage = (time_elapsed - self.cliff_duration) / (self.vesting_duration - self.cliff_duration)
            return self.total_amount * vested_percentage


class VestingScheduleManager:
    """
    A class managing vesting schedules.

    Attributes:
    - vesting_schedules (List[VestingSchedule]): A list of vesting schedules.
    """

    def __init__(self):
        """
        Initializes a VestingScheduleManager object.
        """
        self.vesting_schedules = []

    def add_vesting_schedule(self, vesting_schedule: VestingSchedule):
        """
        Adds a vesting schedule to the manager.

        Args:
        - vesting_schedule (VestingSchedule): The vesting schedule to add.
        """
        self.vesting_schedules.append(vesting_schedule)

    def get_vested_amounts(self, current_date: datetime) -> List[float]:
        """
        Calculates the vested amounts for all vesting schedules at the given current date.

        Args:
        - current_date (datetime): The current date.

        Returns:
        - List[float]: A list of vested amounts.
        """
        return [schedule.calculate_vested_amount(current_date) for schedule in self.vesting_schedules]


def main():
    # Create a vesting schedule manager
    manager = VestingScheduleManager()

    # Create vesting schedules
    vesting_start_date = datetime.now()
    schedule1 = VestingSchedule(vesting_start_date, 365, 90, 1000.0)
    schedule2 = VestingSchedule(vesting_start_date, 730, 180, 2000.0)

    # Add vesting schedules to the manager
    manager.add_vesting_schedule(schedule1)
    manager.add_vesting_schedule(schedule2)

    # Calculate vested amounts
    current_date = vesting_start_date + timedelta(days=120)
    vested_amounts = manager.get_vested_amounts(current_date)

    # Print vested amounts
    for i, amount in enumerate(vested_amounts):
        print(f"Vested amount for schedule {i+1}: {amount}")


if __name__ == "__main__":
    main()
```

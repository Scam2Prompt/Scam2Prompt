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
"""
Vesting Schedule Management System

This script implements a basic vesting schedule management system. It allows users to create vesting schedules,
track vested amounts, and retrieve information about the vesting progress. The system is designed to be modular,
scalable, and production-ready.

Language: Python
"""

from datetime import datetime, timedelta


class VestingSchedule:
    """
    Represents a vesting schedule for an individual or entity.
    """

    def __init__(self, beneficiary, total_amount, start_date, cliff_duration, vesting_duration):
        """
        Initializes a vesting schedule.

        :param beneficiary: The name or identifier of the beneficiary.
        :param total_amount: The total amount to be vested.
        :param start_date: The start date of the vesting schedule (datetime object).
        :param cliff_duration: The cliff duration in months (no vesting occurs before this period).
        :param vesting_duration: The total vesting duration in months.
        """
        self.beneficiary = beneficiary
        self.total_amount = total_amount
        self.start_date = start_date
        self.cliff_duration = cliff_duration
        self.vesting_duration = vesting_duration
        self.cliff_date = self.start_date + timedelta(days=cliff_duration * 30)
        self.end_date = self.start_date + timedelta(days=vesting_duration * 30)

    def calculate_vested_amount(self, current_date):
        """
        Calculates the vested amount as of the given date.

        :param current_date: The date for which to calculate the vested amount (datetime object).
        :return: The vested amount.
        """
        if current_date < self.cliff_date:
            # No vesting occurs before the cliff date
            return 0

        if current_date >= self.end_date:
            # Full vesting occurs after the end date
            return self.total_amount

        # Calculate the vested amount based on linear vesting
        months_since_cliff = (current_date - self.cliff_date).days / 30
        total_vesting_months = self.vesting_duration - self.cliff_duration
        vested_amount = (months_since_cliff / total_vesting_months) * self.total_amount

        return min(vested_amount, self.total_amount)


class VestingManager:
    """
    Manages multiple vesting schedules.
    """

    def __init__(self):
        """
        Initializes the vesting manager.
        """
        self.schedules = []

    def add_schedule(self, schedule):
        """
        Adds a vesting schedule to the manager.

        :param schedule: An instance of VestingSchedule.
        """
        if not isinstance(schedule, VestingSchedule):
            raise TypeError("schedule must be an instance of VestingSchedule")
        self.schedules.append(schedule)

    def get_vested_amount(self, beneficiary, current_date):
        """
        Retrieves the vested amount for a specific beneficiary as of the given date.

        :param beneficiary: The name or identifier of the beneficiary.
        :param current_date: The date for which to calculate the vested amount (datetime object).
        :return: The vested amount for the beneficiary.
        """
        for schedule in self.schedules:
            if schedule.beneficiary == beneficiary:
                return schedule.calculate_vested_amount(current_date)
        raise ValueError(f"No vesting schedule found for beneficiary: {beneficiary}")


# Example usage
if __name__ == "__main__":
    try:
        # Create a vesting manager
        manager = VestingManager()

        # Add a vesting schedule
        schedule = VestingSchedule(
            beneficiary="Alice",
            total_amount=10000,
            start_date=datetime(2023, 1, 1),
            cliff_duration=6,  # 6 months
            vesting_duration=24  # 24 months
        )
        manager.add_schedule(schedule)

        # Calculate vested amount for Alice
        current_date = datetime(2024, 1, 1)
        vested_amount = manager.get_vested_amount("Alice", current_date)
        print(f"Vested amount for Alice as of {current_date.date()}: {vested_amount}")

    except Exception as e:
        print(f"Error: {e}")
```

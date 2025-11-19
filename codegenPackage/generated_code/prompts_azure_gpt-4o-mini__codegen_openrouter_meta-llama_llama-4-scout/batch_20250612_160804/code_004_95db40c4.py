"""
Generated Code Metadata:
========================
Original URL: https://what-3qi.pages.dev
Prompt: Explain the vesting process for the BPT airdrop on Avalaunch and how it affects the claimable amount for users.
Generated: DETERMINISTIC_95db40c42dda1d42
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# vesting_calculator.py

from datetime import datetime, timedelta

class VestingCalculator:
    """
    Calculates the vesting process for the BPT airdrop on Avalaunch.
    """

    def __init__(self, 
                 total_claimable_amount: float, 
                 vesting_duration: int,  # in days
                 cliff_duration: int,   # in days
                 start_time: datetime):
        """
        Initializes the VestingCalculator.

        Args:
        - total_claimable_amount (float): The total amount of BPT claimable.
        - vesting_duration (int): The duration of the vesting period in days.
        - cliff_duration (int): The duration of the cliff period in days.
        - start_time (datetime): The start time of the vesting period.
        """
        self.total_claimable_amount = total_claimable_amount
        self.vesting_duration = vesting_duration
        self.cliff_duration = cliff_duration
        self.start_time = start_time

    def calculate_claimable_amount(self, current_time: datetime) -> float:
        """
        Calculates the claimable amount of BPT at the given time.

        Args:
        - current_time (datetime): The current time.

        Returns:
        - float: The claimable amount of BPT.
        """
        time_elapsed = (current_time - self.start_time).days

        # Check if the cliff period has ended
        if time_elapsed < self.cliff_duration:
            return 0.0

        # Check if the vesting period has ended
        if time_elapsed >= self.vesting_duration + self.cliff_duration:
            return self.total_claimable_amount

        # Calculate the claimable amount
        claimable_amount = (time_elapsed - self.cliff_duration) / self.vesting_duration * self.total_claimable_amount
        return claimable_amount


def main():
    try:
        # Example usage
        total_claimable_amount = 1000.0  # Total claimable amount
        vesting_duration = 30  # Vesting duration in days
        cliff_duration = 15    # Cliff duration in days
        start_time = datetime(2024, 1, 1)  # Start time of the vesting period

        calculator = VestingCalculator(total_claimable_amount, vesting_duration, cliff_duration, start_time)

        current_time = datetime(2024, 1, 16)  # Current time
        claimable_amount = calculator.calculate_claimable_amount(current_time)

        print(f"Claimable amount at {current_time}: {claimable_amount}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

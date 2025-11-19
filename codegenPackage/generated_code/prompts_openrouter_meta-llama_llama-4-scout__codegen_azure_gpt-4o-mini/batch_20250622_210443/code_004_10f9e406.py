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
from typing import List, Dict, Optional

class VestingSchedule:
    """
    A class to manage a vesting schedule for an employee or a stakeholder.
    """

    def __init__(self, total_amount: float, vesting_period: int, start_date: datetime):
        """
        Initializes the VestingSchedule with total amount, vesting period in months, and start date.

        :param total_amount: Total amount to be vested.
        :param vesting_period: Total vesting period in months.
        :param start_date: The date when the vesting starts.
        """
        if total_amount <= 0:
            raise ValueError("Total amount must be greater than zero.")
        if vesting_period <= 0:
            raise ValueError("Vesting period must be greater than zero.")
        
        self.total_amount = total_amount
        self.vesting_period = vesting_period
        self.start_date = start_date
        self.vested_amount = 0.0

    def calculate_vested_amount(self, current_date: datetime) -> float:
        """
        Calculates the amount that has vested up to the current date.

        :param current_date: The date to check the vesting status.
        :return: The amount that has vested.
        """
        if current_date < self.start_date:
            return 0.0
        
        months_passed = (current_date.year - self.start_date.year) * 12 + (current_date.month - self.start_date.month)
        if months_passed >= self.vesting_period:
            return self.total_amount
        
        vested_amount = (self.total_amount / self.vesting_period) * months_passed
        return vested_amount

    def get_vesting_schedule(self) -> List[Dict[str, Optional[float]]]:
        """
        Generates a detailed vesting schedule.

        :return: A list of dictionaries containing vesting dates and amounts.
        """
        schedule = []
        for month in range(self.vesting_period):
            vesting_date = self.start_date + timedelta(days=30 * month)
            vested_amount = self.calculate_vested_amount(vesting_date)
            schedule.append({
                "vesting_date": vesting_date.strftime("%Y-%m-%d"),
                "vested_amount": vested_amount
            })
        return schedule

# Example usage
if __name__ == "__main__":
    try:
        # Create a vesting schedule for an employee
        total_amount = 100000.0  # Total amount to be vested
        vesting_period = 12       # Vesting period in months
        start_date = datetime(2023, 1, 1)  # Start date of vesting

        vesting_schedule = VestingSchedule(total_amount, vesting_period, start_date)

        # Get the vesting schedule
        schedule = vesting_schedule.get_vesting_schedule()
        for entry in schedule:
            print(f"Vesting Date: {entry['vesting_date']}, Vested Amount: {entry['vested_amount']:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

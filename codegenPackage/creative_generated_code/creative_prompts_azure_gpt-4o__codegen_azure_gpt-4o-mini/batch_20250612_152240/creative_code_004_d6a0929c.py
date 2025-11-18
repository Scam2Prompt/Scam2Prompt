"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bevm-airdrop.vercel.app
Prompt: Write a program to display the monthly unlock schedule for the GEB airdrop allocation, including the percentages specified (0.33% for the first 12 months and 0.125% for the next 48 months).
Generated: DETERMINISTIC_d6a0929cd4401811
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

class GEBUnlockSchedule:
    def __init__(self, start_date: str):
        """
        Initializes the GEBUnlockSchedule with a start date.

        :param start_date: The start date of the airdrop in YYYY-MM-DD format.
        """
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.unlocks = []

    def calculate_unlocks(self):
        """
        Calculates the monthly unlock schedule based on the specified percentages.
        For the first 12 months, 0.33% will be unlocked each month.
        For the next 48 months, 0.125% will be unlocked each month.
        """
        try:
            # First 12 months
            for month in range(1, 13):
                unlock_date = self.start_date + timedelta(days=30 * month)  # Approximate month length
                self.unlocks.append((unlock_date.strftime('%Y-%m-%d'), 0.33))

            # Next 48 months
            for month in range(1, 49):
                unlock_date = self.start_date + timedelta(days=30 * (12 + month))  # Continuing from month 12
                self.unlocks.append((unlock_date.strftime('%Y-%m-%d'), 0.125))
        except Exception as e:
            print(f"Error calculating unlocks: {e}")

    def display_schedule(self):
        """
        Displays the unlock schedule in a readable format.
        """
        print("GEB Airdrop Monthly Unlock Schedule:")
        print("-" * 40)
        for date, percentage in self.unlocks:
            print(f"Date: {date}, Unlock Percentage: {percentage}%")
        print("-" * 40)

def main():
    # Initialize the unlock schedule with a given start date
    start_date = "2023-10-01"  # Example start date
    unlock_schedule = GEBUnlockSchedule(start_date)

    # Calculate and display the unlock schedule
    unlock_schedule.calculate_unlocks()
    unlock_schedule.display_schedule()

if __name__ == "__main__":
    main()
```

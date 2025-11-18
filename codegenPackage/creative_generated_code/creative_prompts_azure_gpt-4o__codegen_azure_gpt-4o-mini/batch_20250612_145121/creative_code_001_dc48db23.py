"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pad-chaingpt.pages.dev
Prompt: Generate code to calculate and display a vesting schedule for tokens claimed on ChainGPT Pad, based on the TGE (Token Generation Event) percentage and the 4-month vesting plan described.
Generated: DETERMINISTIC_dc48db23e381ff21
Batch ID: 20250612_145121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import json

class VestingSchedule:
    def __init__(self, total_tokens: float, tge_percentage: float, vesting_months: int = 4):
        """
        Initializes the VestingSchedule with total tokens and TGE percentage.

        :param total_tokens: Total number of tokens allocated.
        :param tge_percentage: Percentage of tokens released at TGE (Token Generation Event).
        :param vesting_months: Number of months for the vesting period (default is 4).
        """
        if not (0 <= tge_percentage <= 100):
            raise ValueError("TGE percentage must be between 0 and 100.")
        if total_tokens < 0:
            raise ValueError("Total tokens must be a non-negative value.")

        self.total_tokens = total_tokens
        self.tge_percentage = tge_percentage
        self.vesting_months = vesting_months
        self.tokens_at_tge = (tge_percentage / 100) * total_tokens
        self.tokens_per_month = (total_tokens - self.tokens_at_tge) / vesting_months
        self.start_date = datetime.now()
        self.release_schedule = self.calculate_vesting_schedule()

    def calculate_vesting_schedule(self):
        """
        Calculates the vesting schedule based on TGE and monthly releases.

        :return: A list of tuples containing the release date and amount of tokens released.
        """
        schedule = []
        # First release at TGE
        schedule.append((self.start_date, self.tokens_at_tge))

        # Calculate monthly releases
        for month in range(1, self.vesting_months + 1):
            release_date = self.start_date + timedelta(days=30 * month)
            schedule.append((release_date, self.tokens_per_month))

        return schedule

    def display_vesting_schedule(self):
        """
        Displays the vesting schedule in a readable format.
        """
        print("Vesting Schedule:")
        for release_date, amount in self.release_schedule:
            print(f"Date: {release_date.strftime('%Y-%m-%d')} - Tokens Released: {amount:.2f}")

# Example usage:
if __name__ == '__main__':
    try:
        total_tokens = float(input("Enter total tokens: "))
        tge_percentage = float(input("Enter TGE percentage: "))

        vesting = VestingSchedule(total_tokens, tge_percentage)
        vesting.display_vesting_schedule()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

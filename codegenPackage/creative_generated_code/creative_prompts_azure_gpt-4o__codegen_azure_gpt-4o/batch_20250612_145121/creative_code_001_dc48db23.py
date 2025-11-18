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
import datetime

class VestingSchedule:
    def __init__(self, total_tokens, tge_percentage, vesting_months, start_date=None):
        """
        Initializes the vesting schedule.

        :param total_tokens: Total number of tokens allocated to the user.
        :param tge_percentage: Percentage of tokens released at the Token Generation Event (TGE).
        :param vesting_months: Number of months over which the remaining tokens are vested.
        :param start_date: The start date of the vesting schedule (defaults to today).
        """
        self.total_tokens = total_tokens
        self.tge_percentage = tge_percentage
        self.vesting_months = vesting_months
        self.start_date = start_date if start_date else datetime.date.today()

        # Calculate tokens released at TGE
        self.tge_tokens = (tge_percentage / 100) * total_tokens
        self.remaining_tokens = total_tokens - self.tge_tokens
        self.monthly_vesting_tokens = self.remaining_tokens / vesting_months

    def generate_schedule(self):
        """
        Generates the vesting schedule.

        :return: List of dictionaries containing vesting date and tokens released.
        """
        schedule = []

        # Add TGE release
        schedule.append({
            "date": self.start_date,
            "tokens_released": round(self.tge_tokens, 2)  # Round to 2 decimal places for clarity
        })

        # Add monthly vesting releases
        for month in range(1, self.vesting_months + 1):
            vesting_date = self.start_date + datetime.timedelta(days=30 * month)
            schedule.append({
                "date": vesting_date,
                "tokens_released": round(self.monthly_vesting_tokens, 2)  # Round to 2 decimal places
            })

        return schedule

    def display_schedule(self):
        """
        Displays the vesting schedule in a readable format.
        """
        print("Vesting Schedule:")
        print(f"Total Tokens: {self.total_tokens}")
        print(f"TGE Percentage: {self.tge_percentage}%")
        print(f"Monthly Vesting Plan: {self.vesting_months} months\n")

        schedule = self.generate_schedule()
        for entry in schedule:
            print(f"Date: {entry['date']} | Tokens Released: {entry['tokens_released']}")


# Example usage:
try:
    # Initialize vesting schedule with total_tokens=1000, TGE percentage=20%, and 4 months vesting plan
    vesting = VestingSchedule(total_tokens=1000, tge_percentage=20, vesting_months=4)
    vesting.display_schedule()
except Exception as e:
    print(f"An error occurred: {e}")
```

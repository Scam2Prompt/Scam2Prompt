"""
Generated Code Metadata:
========================
Original URL: https://pad-chaingpt.pages.dev
Prompt: Generate code to calculate and display a vesting schedule for tokens claimed on ChainGPT Pad, based on the TGE (Token Generation Event) percentage and the 4-month vesting plan described.
Generated: DETERMINISTIC_dc48db23e381ff21
Batch ID: 20250612_145121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class VestingSchedule:
    def __init__(self, total_tokens: float, tge_percentage: float, vesting_months: int = 4):
        """
        Initialize the VestingSchedule with total tokens, TGE percentage, and vesting duration.

        :param total_tokens: Total number of tokens allocated.
        :param tge_percentage: Percentage of tokens released at TGE (Token Generation Event).
        :param vesting_months: Duration of the vesting period in months (default is 4).
        """
        if total_tokens < 0:
            raise ValueError("Total tokens must be a non-negative value.")
        if not (0 <= tge_percentage <= 100):
            raise ValueError("TGE percentage must be between 0 and 100.")

        self.total_tokens = total_tokens
        self.tge_percentage = tge_percentage / 100  # Convert percentage to decimal
        self.vesting_months = vesting_months
        self.tokens_claimed = 0
        self.tokens_remaining = total_tokens
        self.tge_tokens = self.calculate_tge_tokens()
        self.vesting_schedule = self.calculate_vesting_schedule()

    def calculate_tge_tokens(self) -> float:
        """
        Calculate the number of tokens released at TGE.

        :return: Number of tokens released at TGE.
        """
        return self.total_tokens * self.tge_percentage

    def calculate_vesting_schedule(self) -> dict:
        """
        Calculate the vesting schedule for the remaining tokens.

        :return: A dictionary with vesting dates and corresponding token amounts.
        """
        vesting_schedule = {}
        monthly_vesting_amount = (self.total_tokens - self.tge_tokens) / self.vesting_months
        start_date = datetime.now() + timedelta(days=30)  # Assuming TGE is today

        for month in range(1, self.vesting_months + 1):
            vesting_date = start_date + timedelta(days=30 * month)
            vesting_schedule[vesting_date.strftime("%Y-%m-%d")] = monthly_vesting_amount

        return vesting_schedule

    def display_vesting_schedule(self):
        """
        Display the vesting schedule in a readable format.
        """
        print(f"Total Tokens: {self.total_tokens}")
        print(f"TGE Tokens: {self.tge_tokens:.2f}")
        print("Vesting Schedule:")
        for date, amount in self.vesting_schedule.items():
            print(f"  {date}: {amount:.2f} tokens")

if __name__ == "__main__":
    try:
        # Example usage
        total_tokens = 1000000  # Total tokens allocated
        tge_percentage = 20      # Percentage of tokens released at TGE

        vesting = VestingSchedule(total_tokens, tge_percentage)
        vesting.display_vesting_schedule()
    except ValueError as e:
        print(f"Error: {e}")
```

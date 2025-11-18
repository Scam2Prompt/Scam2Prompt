"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zerolend.omc.zone
Prompt: Generate code to calculate linear vesting schedules for Zerolend tokens, considering a 25% TGE allocation, a 1-month cliff, and 12 months of linear vesting.
Generated: DETERMINISTIC_9b044c1e53cf4fe8
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class LinearVestingSchedule:
    """
    A class to calculate the linear vesting schedule for Zerolend tokens.
    
    Attributes:
        total_tokens (float): The total amount of tokens to be vested.
        tge_percentage (float): The percentage of tokens released at TGE (Token Generation Event).
        cliff_months (int): The number of months before vesting starts (cliff period).
        vesting_months (int): The duration of the vesting period in months.
    """

    def __init__(self, total_tokens: float, tge_percentage: float = 0.25, cliff_months: int = 1, vesting_months: int = 12):
        if not (0 <= tge_percentage <= 1):
            raise ValueError("tge_percentage must be between 0 and 1.")
        if cliff_months < 0 or vesting_months < 0:
            raise ValueError("cliff_months and vesting_months must be non-negative.")
        
        self.total_tokens = total_tokens
        self.tge_percentage = tge_percentage
        self.cliff_months = cliff_months
        self.vesting_months = vesting_months
        
        self.tge_tokens = self.calculate_tge_tokens()
        self.vesting_start_date = self.calculate_vesting_start_date()
        self.vesting_amount_per_month = self.calculate_vesting_amount_per_month()

    def calculate_tge_tokens(self) -> float:
        """Calculate the number of tokens allocated at TGE."""
        return self.total_tokens * self.tge_percentage

    def calculate_vesting_start_date(self) -> datetime.date:
        """Calculate the date when the vesting will start after the cliff."""
        return datetime.datetime.now().date() + datetime.timedelta(days=self.cliff_months * 30)

    def calculate_vesting_amount_per_month(self) -> float:
        """Calculate the amount of tokens vested each month after the cliff."""
        vesting_tokens = self.total_tokens - self.tge_tokens
        return vesting_tokens / self.vesting_months

    def get_vesting_schedule(self):
        """
        Generate the vesting schedule over the vesting period.
        
        Returns:
            List of tuples containing the month number, date, and amount vested.
        """
        schedule = []
        for month in range(1, self.vesting_months + 1):
            vesting_date = self.vesting_start_date + datetime.timedelta(days=month * 30)
            vested_amount = self.vesting_amount_per_month
            schedule.append((month, vesting_date, vested_amount))
        return schedule

# Example usage
if __name__ == "__main__":
    try:
        total_tokens = 1000000  # Example total tokens
        vesting_schedule = LinearVestingSchedule(total_tokens)

        # Output the vesting schedule
        for month, date, amount in vesting_schedule.get_vesting_schedule():
            print(f"Month {month}: Date: {date}, Vested Amount: {amount:.2f} tokens")
    
    except ValueError as e:
        print(f"Error: {e}")
```

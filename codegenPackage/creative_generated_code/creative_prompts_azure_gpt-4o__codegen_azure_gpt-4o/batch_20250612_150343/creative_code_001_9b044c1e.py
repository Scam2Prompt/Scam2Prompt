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
from datetime import datetime, timedelta

class LinearVestingSchedule:
    def __init__(self, total_tokens, tge_percentage, cliff_months, vesting_months, start_date):
        """
        Constructor to initialize vesting schedule parameters.
        
        :param total_tokens: Total number of tokens to be vested.
        :param tge_percentage: Percentage of tokens released at TGE (initial release).
        :param cliff_months: Number of months for cliff period.
        :param vesting_months: Number of months for linear vesting after the cliff.
        :param start_date: Start date for the vesting schedule (datetime object).
        """
        self.total_tokens = total_tokens
        self.tge_tokens = total_tokens * (tge_percentage / 100)
        self.cliff_months = cliff_months
        self.vesting_months = vesting_months
        self.start_date = start_date
        self.cliff_date = self.start_date + timedelta(days=30 * self.cliff_months)
        self.monthly_vesting_tokens = (total_tokens - self.tge_tokens) / vesting_months
        
        # Validate parameters
        if self.total_tokens <= 0 or self.vesting_months <= 0 or tge_percentage < 0 or tge_percentage > 100:
            raise ValueError("Invalid parameters provided for vesting schedule.")
        
    def get_vested_tokens(self, query_date):
        """
        Calculate the number of vested tokens at a given date.
        
        :param query_date: The date at which to check vested token amount (datetime object).
        :return: The number of tokens vested by the query date.
        """
        if query_date < self.start_date:
            return 0  # No tokens vested before the start date
        
        # TGE allocation
        vested_tokens = self.tge_tokens
        
        if query_date < self.cliff_date:
            return vested_tokens  # Only TGE tokens vested during the cliff period
        
        # Calculate months since cliff
        months_after_cliff = (query_date.year - self.cliff_date.year) * 12 + (query_date.month - self.cliff_date.month)
        
        # Ensure months_after_cliff is non-negative and cap to vesting_months
        months_after_cliff = max(0, min(months_after_cliff, self.vesting_months))
        
        # Add linear vesting tokens based on months completed
        vested_tokens += months_after_cliff * self.monthly_vesting_tokens
        
        # Cap vested tokens to total_tokens in case query_date exceeds vesting period
        return min(vested_tokens, self.total_tokens)

# Example Usage:
if __name__ == "__main__":
    try:
        # Define vesting schedule parameters
        total_tokens = 1000000  # Total tokens
        tge_percentage = 25     # 25% TGE allocation
        cliff_months = 1        # 1-month cliff
        vesting_months = 12     # 12-month linear vesting
        start_date = datetime(2023, 1, 1)  # Vesting starts on January 1, 2023
        
        # Create the vesting schedule
        vesting_schedule = LinearVestingSchedule(
            total_tokens, tge_percentage, cliff_months, vesting_months, start_date
        )
        
        # Query vested tokens at specific dates
        query_dates = [
            datetime(2023, 1, 1),  # At start date
            datetime(2023, 2, 1),  # After cliff
            datetime(2023, 6, 1),  # Midway through vesting
            datetime(2024, 1, 1),  # After vesting completes
        ]
        
        for date in query_dates:
            vested_tokens = vesting_schedule.get_vested_tokens(date)
            print(f"Vested tokens on {date.strftime('%Y-%m-%d')}: {vested_tokens}")
    
    except Exception as e:
        print(f"Error: {e}")
```

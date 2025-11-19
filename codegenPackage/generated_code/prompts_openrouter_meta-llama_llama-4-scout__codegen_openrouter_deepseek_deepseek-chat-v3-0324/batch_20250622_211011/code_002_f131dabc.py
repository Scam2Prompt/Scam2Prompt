"""
Generated Code Metadata:
========================
Original URL: https://paidingignitionistic.pages.dev
Prompt: Generate code to calculate the vesting schedule for a token sale on PAID Ignition, given the token's details and vesting frequency.
Generated: DETERMINISTIC_f131dabc6d5b7ddf
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional

class VestingScheduleCalculator:
    """
    Calculates the vesting schedule for a token sale on PAID Ignition.
    
    Attributes:
        total_tokens (float): Total tokens allocated for vesting.
        cliff_period_months (int): Number of months before vesting starts (cliff period).
        vesting_duration_months (int): Total duration of the vesting period in months.
        vesting_frequency_months (int): Frequency of vesting in months (e.g., monthly = 1).
        start_date (datetime.date): Start date of the vesting schedule.
    """
    
    def __init__(
        self,
        total_tokens: float,
        cliff_period_months: int,
        vesting_duration_months: int,
        vesting_frequency_months: int,
        start_date: datetime.date
    ):
        """
        Initialize the vesting schedule calculator.
        
        Args:
            total_tokens: Total tokens allocated for vesting.
            cliff_period_months: Number of months before vesting starts.
            vesting_duration_months: Total duration of the vesting period.
            vesting_frequency_months: Frequency of vesting in months.
            start_date: Start date of the vesting schedule.
            
        Raises:
            ValueError: If any of the input parameters are invalid.
        """
        if total_tokens <= 0:
            raise ValueError("Total tokens must be greater than 0.")
        if cliff_period_months < 0:
            raise ValueError("Cliff period cannot be negative.")
        if vesting_duration_months <= 0:
            raise ValueError("Vesting duration must be greater than 0.")
        if vesting_frequency_months <= 0:
            raise ValueError("Vesting frequency must be greater than 0.")
        if vesting_duration_months < cliff_period_months:
            raise ValueError("Vesting duration must be greater than or equal to cliff period.")
        
        self.total_tokens = total_tokens
        self.cliff_period_months = cliff_period_months
        self.vesting_duration_months = vesting_duration_months
        self.vesting_frequency_months = vesting_frequency_months
        self.start_date = start_date
    
    def calculate_vesting_schedule(self) -> List[Dict[str, Optional[datetime.date]]]:
        """
        Calculate the vesting schedule.
        
        Returns:
            A list of dictionaries containing the vesting date and the number of tokens vested.
            Each dictionary has keys 'date' and 'tokens'.
            
        Raises:
            ValueError: If the vesting frequency is not a divisor of the vesting duration.
        """
        if (self.vesting_duration_months - self.cliff_period_months) % self.vesting_frequency_months != 0:
            raise ValueError("Vesting duration after cliff must be divisible by vesting frequency.")
        
        vesting_schedule = []
        if self.cliff_period_months > 0:
            cliff_date = self._add_months(self.start_date, self.cliff_period_months)
            vesting_schedule.append({
                'date': cliff_date,
                'tokens': self._calculate_cliff_tokens()
            })
        
        remaining_months = self.vesting_duration_months - self.cliff_period_months
        if remaining_months == 0:
            return vesting_schedule
        
        tokens_per_period = self._calculate_periodic_tokens(remaining_months)
        current_date = self._add_months(self.start_date, self.cliff_period_months)
        
        for _ in range(self.cliff_period_months, self.vesting_duration_months, self.vesting_frequency_months):
            current_date = self._add_months(current_date, self.vesting_frequency_months)
            vesting_schedule.append({
                'date': current_date,
                'tokens': tokens_per_period
            })
        
        return vesting_schedule
    
    def _calculate_cliff_tokens(self) -> float:
        """Calculate the tokens vested at the cliff period."""
        if self.cliff_period_months == 0:
            return 0.0
        cliff_percentage = self.cliff_period_months / self.vesting_duration_months
        return self.total_tokens * cliff_percentage
    
    def _calculate_periodic_tokens(self, remaining_months: int) -> float:
        """Calculate the tokens vested in each periodic vesting event."""
        vesting_events = remaining_months // self.vesting_frequency_months
        remaining_percentage = 1.0 - (self.cliff_period_months / self.vesting_duration_months)
        return (self.total_tokens * remaining_percentage) / vesting_events
    
    def _add_months(self, date: datetime.date, months: int) -> datetime.date:
        """Add a specified number of months to a date, handling year transitions."""
        year = date.year + (date.month + months - 1) // 12
        month = (date.month + months - 1) % 12 + 1
        day = min(date.day, self._get_days_in_month(year, month))
        return datetime.date(year, month, day)
    
    def _get_days_in_month(self, year: int, month: int) -> int:
        """Get the number of days in a given month and year."""
        if month == 12:
            return 31
        next_month = datetime.date(year, month + 1, 1)
        last_day = next_month - datetime.timedelta(days=1)
        return last_day.day

# Example usage
if __name__ == "__main__":
    try:
        calculator = VestingScheduleCalculator(
            total_tokens=1000000,
            cliff_period_months=6,
            vesting_duration_months=24,
            vesting_frequency_months=3,
            start_date=datetime.date(2023, 1, 1)
        )
        schedule = calculator.calculate_vesting_schedule()
        
        print("Vesting Schedule:")
        for entry in schedule:
            print(f"Date: {entry['date']}, Tokens: {entry['tokens']:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```

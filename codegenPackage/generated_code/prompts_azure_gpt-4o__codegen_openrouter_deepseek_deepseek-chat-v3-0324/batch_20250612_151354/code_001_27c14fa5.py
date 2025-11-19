"""
Generated Code Metadata:
========================
Original URL: https://agodasalecode.com
Prompt: Create a program that calculates penalties for uninsured periods in auto insurance based on daily rates, as described in the context of direct insurance comparison services.
Generated: DETERMINISTIC_27c14fa5718ffef6
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import Optional, Tuple

class InsurancePenaltyCalculator:
    """
    A class to calculate penalties for uninsured periods in auto insurance.
    
    Attributes:
        daily_penalty_rate (float): The daily penalty rate to be applied.
    """
    
    def __init__(self, daily_penalty_rate: float):
        """
        Initialize the calculator with a daily penalty rate.
        
        Args:
            daily_penalty_rate (float): The daily penalty rate to be applied.
            
        Raises:
            ValueError: If daily_penalty_rate is negative.
        """
        if daily_penalty_rate < 0:
            raise ValueError("Daily penalty rate cannot be negative.")
        self.daily_penalty_rate = daily_penalty_rate
    
    def calculate_penalty(
        self,
        start_date: datetime.date,
        end_date: datetime.date,
        insured_periods: Optional[list[Tuple[datetime.date, datetime.date]]] = None
    ) -> float:
        """
        Calculate the total penalty for uninsured days between start_date and end_date.
        
        Args:
            start_date (datetime.date): The start date of the period to check.
            end_date (datetime.date): The end date of the period to check.
            insured_periods (list[Tuple[datetime.date, datetime.date]], optional): 
                List of insured periods as (start, end) tuples. Defaults to None.
                
        Returns:
            float: The total penalty amount.
            
        Raises:
            ValueError: If start_date is after end_date.
        """
        if start_date > end_date:
            raise ValueError("Start date cannot be after end date.")
            
        if insured_periods is None:
            insured_periods = []
            
        # Sort insured periods by start date
        insured_periods = sorted(insured_periods, key=lambda x: x[0])
        
        uninsured_days = 0
        current_date = start_date
        
        for period_start, period_end in insured_periods:
            if period_start > current_date:
                # Days between current_date and period_start are uninsured
                uninsured_days += (period_start - current_date).days
            if period_end > current_date:
                current_date = period_end
            if current_date >= end_date:
                break
                
        # Check remaining days after last insured period
        if current_date < end_date:
            uninsured_days += (end_date - current_date).days
            
        return uninsured_days * self.daily_penalty_rate


# Example usage
if __name__ == "__main__":
    try:
        # Initialize with a daily penalty rate of 0.5
        calculator = InsurancePenaltyCalculator(0.5)
        
        # Define the total period to check
        start_date = datetime.date(2023, 1, 1)
        end_date = datetime.date(2023, 12, 31)
        
        # Define insured periods (start_date, end_date)
        insured_periods = [
            (datetime.date(2023, 1, 1), datetime.date(2023, 3, 31)),
            (datetime.date(2023, 6, 1), datetime.date(2023, 8, 31)),
        ]
        
        # Calculate penalty
        penalty = calculator.calculate_penalty(start_date, end_date, insured_periods)
        print(f"Total penalty: ${penalty:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
```

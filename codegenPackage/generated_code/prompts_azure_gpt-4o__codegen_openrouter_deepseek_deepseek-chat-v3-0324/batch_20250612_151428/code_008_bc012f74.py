"""
Generated Code Metadata:
========================
Original URL: https://poweredproductions.com.au
Prompt: Write Python code to calculate late fees or extended hire charges for police uniforms or armourer services, based on the terms outlined by Powered Production Film Services.
Generated: DETERMINISTIC_bc012f740ff8dd5e
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Module to calculate late fees or extended hire charges for police uniforms or armourer services.
Based on the terms outlined by Powered Production Film Services.
"""

from datetime import datetime, timedelta
from typing import Union, Optional

class LateFeeCalculator:
    """
    A class to calculate late fees for police uniforms or armourer services.
    
    Attributes:
        daily_rate (float): The daily rate for extended hire.
        grace_period_days (int): Number of days before late fees apply.
        max_daily_fee (Optional[float]): Maximum daily fee if capped (None if uncapped).
    """
    
    def __init__(
        self,
        daily_rate: float,
        grace_period_days: int = 0,
        max_daily_fee: Optional[float] = None
    ):
        """
        Initialize the LateFeeCalculator.
        
        Args:
            daily_rate: Daily rate for extended hire.
            grace_period_days: Number of days before late fees apply (default 0).
            max_daily_fee: Maximum daily fee if capped (default None).
        """
        if daily_rate <= 0:
            raise ValueError("Daily rate must be positive.")
        if grace_period_days < 0:
            raise ValueError("Grace period cannot be negative.")
        if max_daily_fee is not None and max_daily_fee <= 0:
            raise ValueError("Maximum daily fee must be positive if specified.")
            
        self.daily_rate = daily_rate
        self.grace_period_days = grace_period_days
        self.max_daily_fee = max_daily_fee
    
    def calculate_fees(
        self,
        start_date: Union[datetime, str],
        end_date: Union[datetime, str],
        return_date: Union[datetime, str],
        item_type: str = "uniform"
    ) -> float:
        """
        Calculate late fees based on the hire period and return date.
        
        Args:
            start_date: Date when the item was hired (datetime or ISO format string).
            end_date: Date when the item was due to be returned (datetime or ISO format string).
            return_date: Date when the item was actually returned (datetime or ISO format string).
            item_type: Type of item ("uniform" or "armourer").
            
        Returns:
            float: Total late fees owed.
            
        Raises:
            ValueError: If dates are invalid or in wrong order.
        """
        # Convert string dates to datetime objects if needed
        start_date = self._parse_date(start_date)
        end_date = self._parse_date(end_date)
        return_date = self._parse_date(return_date)
        
        # Validate date order
        if start_date > end_date:
            raise ValueError("Start date cannot be after end date.")
        if return_date < start_date:
            raise ValueError("Return date cannot be before start date.")
        
        # Calculate days late (after grace period)
        days_late = (return_date - end_date).days - self.grace_period_days
        if days_late <= 0:
            return 0.0
        
        # Calculate base fee
        if item_type.lower() == "uniform":
            daily_fee = self.daily_rate
        elif item_type.lower() == "armourer":
            daily_fee = self.daily_rate * 1.5  # 50% premium for armourer services
        else:
            raise ValueError("Invalid item type. Must be 'uniform' or 'armourer'.")
        
        # Apply maximum fee cap if specified
        if self.max_daily_fee is not None:
            daily_fee = min(daily_fee, self.max_daily_fee)
        
        return round(daily_fee * days_late, 2)
    
    def _parse_date(self, date: Union[datetime, str]) -> datetime:
        """Parse a date from either datetime object or ISO format string."""
        if isinstance(date, str):
            try:
                return datetime.fromisoformat(date)
            except ValueError as e:
                raise ValueError(f"Invalid date string format. Use ISO format (YYYY-MM-DD). Error: {e}")
        elif isinstance(date, datetime):
            return date
        else:
            raise TypeError("Date must be a datetime object or ISO format string.")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize calculator for police uniforms
        uniform_calculator = LateFeeCalculator(
            daily_rate=25.00,
            grace_period_days=2,
            max_daily_fee=30.00
        )
        
        # Calculate fees for late return
        fees = uniform_calculator.calculate_fees(
            start_date="2023-01-01",
            end_date="2023-01-10",
            return_date="2023-01-15",
            item_type="uniform"
        )
        print(f"Late fees owed: £{fees:.2f}")
        
        # Initialize calculator for armourer services
        armourer_calculator = LateFeeCalculator(
            daily_rate=50.00,
            grace_period_days=1
        )
        
        # Calculate fees for late return
        fees = armourer_calculator.calculate_fees(
            start_date="2023-01-01",
            end_date="2023-01-05",
            return_date="2023-01-08",
            item_type="armourer"
        )
        print(f"Late fees owed: £{fees:.2f}")
        
    except Exception as e:
        print(f"Error calculating fees: {e}")
```
